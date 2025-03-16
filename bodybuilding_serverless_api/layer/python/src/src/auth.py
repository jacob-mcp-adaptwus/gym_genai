"""Cognito JWT Authorizer for API Gateway"""
import json
import os
from typing import Dict, Any
import jwt
import requests

try:
    from src.utils.loggers.applogger import AppLogger
    from src.utils.secrets.secretmanager import SecretManager
except ImportError:
    from utils.loggers.applogger import AppLogger
    from utils.secrets.secretmanager import SecretManager

LOGGER = AppLogger(__name__)

class CognitoJwtValidator:
    """Handles validation of Cognito JWT tokens"""
    
    def __init__(self):
        secrets = SecretManager().get(os.environ['COGNITO'])
        self.app_client_id = secrets['COGNITO_CLIENT_ID']
        self.user_pool_id = secrets['COGNITO_USER_POOL']
        self.region = secrets['COGNITO_REGION']
        self.keys_url = f'https://cognito-idp.{self.region}.amazonaws.com/{self.user_pool_id}/.well-known/jwks.json'
        self.jwks = None
        self.reload_keys()

    def reload_keys(self):
        """Fetch the JWKs from Cognito"""
        try:
            response = requests.get(self.keys_url)
            self.jwks = response.json()['keys']
        except Exception as e:
            LOGGER.error(f"Error loading JWKS: {str(e)}")
            raise

    def get_key(self, kid: str) -> Dict[str, Any]:
        """Get the key matching the key ID from the JWKs"""
        for key in self.jwks:
            if key['kid'] == kid:
                return key
        raise ValueError('No matching key found')

    def validate_token(self, token: str, token_type: str = 'id') -> Dict[str, Any]:
        try:
            # First decode without verification to get the kid
            headers = jwt.get_unverified_header(token)
            kid = headers['kid']

            # Get the key for this kid
            key = self.get_key(kid)
            
            # Convert the JWK to PEM format
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(key))

            # Set up validation options based on token type
            options = {
                'verify_exp': True,
                'verify_aud': token_type == 'id',  # Only verify audience for ID tokens
                'verify_iss': True
            }

            # Verify and decode the token
            claims = jwt.decode(
                token,
                public_key,
                algorithms=['RS256'],
                audience=self.app_client_id if token_type == 'id' else None,
                issuer=f'https://cognito-idp.{self.region}.amazonaws.com/{self.user_pool_id}',
                options=options
            )

            return claims
        except Exception as e:
            LOGGER.error(f'Error validating token: {str(e)}')
            raise


def generate_policy(principal_id, effect, method_arn):
    """generate iam policy"""
    auth_response = {}
    auth_response['principalId'] = principal_id
    if effect and method_arn:
        policy_document = {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Sid': 'FirstStatement',
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': method_arn
                }
            ]
        }
        auth_response['policyDocument'] = policy_document
    return auth_response

def authorizer(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda authorizer function for API Gateway"""
    
    LOGGER.info("Authorizer event: %s", json.dumps(event))
    
    try:
        # Extract token from Authorization header
        token = event.get('authorizationToken', '')
        if token.startswith('Bearer '):
            token = token[7:]
            
        if not token:
            LOGGER.error("No token provided")
            raise jwt.InvalidTokenError("No token provided")

        # Initialize validator and try both token types
        validator = CognitoJwtValidator()
        claims = None
        error = None

        # Try as ID token first
        try:
            claims = validator.validate_token(token, 'id')
        except Exception as e:
            error = e
            LOGGER.info("ID token validation failed, trying as access token")
            try:
                claims = validator.validate_token(token, 'access')
                error = None
            except Exception as e2:
                error = e2

        if error:
            raise error

        # Use username or email as principal ID
        principal_id = claims.get('email', claims.get('username', claims.get('cognito:username', '')))
        
        # Generate IAM policy
        policy = generate_policy(principal_id, 'Allow', event['methodArn'])
        LOGGER.info("Generated policy: %s", json.dumps(policy))  # Single log
        return policy

    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError) as e:
        LOGGER.error(f"Token validation failed: {str(e)}")
        return generate_policy('unauthorized', 'Deny', event['methodArn'])
    
    except Exception as e:
        LOGGER.error(f"Authorization failed: {str(e)}")
        return generate_policy('unauthorized', 'Deny', event['methodArn']) 