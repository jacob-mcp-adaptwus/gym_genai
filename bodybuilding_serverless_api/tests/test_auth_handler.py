import json
import unittest
from unittest.mock import patch, MagicMock, PropertyMock

from src.handlers.auth_handler import authorizer, generate_policy, CognitoJwtValidator


class TestAuthHandler(unittest.TestCase):
    """Test cases for the auth handler functions"""

    def setUp(self):
        """Set up test fixtures"""
        self.method_arn = "arn:aws:execute-api:us-east-1:123456789012:api123/dev/GET/plans"
        self.token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0LXVzZXItMTIzIiwiZW1haWwiOiJ0ZXN0QGV4YW1wbGUuY29tIiwiaXNzIjoiaHR0cHM6Ly9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbS91cy1lYXN0LTFfdGVzdHBvb2wiLCJjbGllbnRfaWQiOiJ0ZXN0Y2xpZW50aWQiLCJleHAiOjE2MTY1MjM2MDB9.signature"
        
        # Mock event with authorization token
        self.event = {
            "type": "TOKEN",
            "authorizationToken": f"Bearer {self.token}",
            "methodArn": self.method_arn
        }

    def test_generate_policy(self):
        """Test policy generation"""
        # Arrange
        principal_id = "test-user-123"
        effect = "Allow"
        claims = {
            "sub": principal_id,
            "email": "test@example.com"
        }
        
        # Act
        policy = generate_policy(principal_id, effect, self.method_arn, claims)
        
        # Assert
        self.assertEqual(policy["principalId"], principal_id)
        self.assertEqual(policy["policyDocument"]["Statement"][0]["Effect"], effect)
        self.assertEqual(policy["policyDocument"]["Statement"][0]["Resource"], self.method_arn)
        self.assertEqual(policy["context"]["sub"], claims["sub"])
        self.assertEqual(policy["context"]["email"], claims["email"])

    @patch('src.handlers.auth_handler.CognitoJwtValidator')
    def test_authorizer_valid_token(self, mock_validator_class):
        """Test authorizer with valid token"""
        # Arrange
        mock_validator = MagicMock()
        mock_validator_class.return_value = mock_validator
        
        user_claims = {
            "sub": "test-user-123",
            "email": "test@example.com",
            "token_use": "id"
        }
        mock_validator.validate_token.return_value = user_claims
        
        # Act
        result = authorizer(self.event, {})
        
        # Assert
        mock_validator.validate_token.assert_called_once_with(self.token)
        self.assertEqual(result["principalId"], user_claims["sub"])
        self.assertEqual(result["policyDocument"]["Statement"][0]["Effect"], "Allow")
        self.assertEqual(result["context"]["sub"], user_claims["sub"])
        self.assertEqual(result["context"]["email"], user_claims["email"])

    @patch('src.handlers.auth_handler.CognitoJwtValidator')
    def test_authorizer_invalid_token(self, mock_validator_class):
        """Test authorizer with invalid token"""
        # Arrange
        mock_validator = MagicMock()
        mock_validator_class.return_value = mock_validator
        
        mock_validator.validate_token.side_effect = Exception("Invalid token")
        
        # Act
        result = authorizer(self.event, {})
        
        # Assert
        mock_validator.validate_token.assert_called_once_with(self.token)
        self.assertEqual(result["principalId"], "unauthorized")
        self.assertEqual(result["policyDocument"]["Statement"][0]["Effect"], "Deny")

    @patch('src.handlers.auth_handler.CognitoJwtValidator')
    def test_authorizer_missing_token(self, mock_validator_class):
        """Test authorizer with missing token"""
        # Arrange
        event_without_token = {
            "type": "TOKEN",
            "methodArn": self.method_arn
        }
        
        # Act
        result = authorizer(event_without_token, {})
        
        # Assert
        self.assertEqual(result["principalId"], "unauthorized")
        self.assertEqual(result["policyDocument"]["Statement"][0]["Effect"], "Deny")

    @patch('src.handlers.auth_handler.CognitoJwtValidator')
    def test_authorizer_malformed_token(self, mock_validator_class):
        """Test authorizer with malformed token"""
        # Arrange
        event_with_malformed_token = {
            "type": "TOKEN",
            "authorizationToken": "NotBearer token",
            "methodArn": self.method_arn
        }
        
        # Act
        result = authorizer(event_with_malformed_token, {})
        
        # Assert
        self.assertEqual(result["principalId"], "unauthorized")
        self.assertEqual(result["policyDocument"]["Statement"][0]["Effect"], "Deny")

    @patch('src.handlers.auth_handler.SecretsManager')
    @patch('src.handlers.auth_handler.requests.get')
    def test_cognito_jwt_validator_init(self, mock_get, mock_secrets_manager):
        """Test CognitoJwtValidator initialization"""
        # Arrange
        mock_secrets = MagicMock()
        mock_secrets_manager.return_value.get_secret.return_value = {
            'COGNITO_CLIENT_ID': 'test-client-id',
            'COGNITO_USER_POOL': 'test-user-pool',
            'COGNITO_REGION': 'us-east-1'
        }
        
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'keys': [
                {
                    'kid': 'test-key-id',
                    'kty': 'RSA',
                    'n': 'test-modulus',
                    'e': 'test-exponent'
                }
            ]
        }
        mock_get.return_value = mock_response
        
        # Act
        with patch.dict('os.environ', {'COGNITO': 'test-secret-name'}):
            validator = CognitoJwtValidator()
        
        # Assert
        mock_secrets_manager.return_value.get_secret.assert_called_once_with('test-secret-name')
        self.assertEqual(validator.app_client_id, 'test-client-id')
        self.assertEqual(validator.user_pool_id, 'test-user-pool')
        self.assertEqual(validator.region, 'us-east-1')
        self.assertEqual(validator.keys_url, 'https://cognito-idp.us-east-1.amazonaws.com/test-user-pool/.well-known/jwks.json')
        mock_get.assert_called_once_with(validator.keys_url)
        self.assertEqual(validator.jwks, mock_response.json.return_value)


if __name__ == '__main__':
    unittest.main() 