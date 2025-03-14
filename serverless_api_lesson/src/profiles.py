"""Profile management Lambda functions with educational profile support"""
# pylint: disable=C0301,W0613
import json
import os
from typing import Dict, Any

try:
    from util.lambdahelper import LambdaHelper
    from util.loggers.applogger import AppLogger
    from aws.dynamomanager import DynamoManager
except ImportError:
    from src.util.lambdahelper import LambdaHelper
    from src.util.loggers.applogger import AppLogger
    from src.aws.dynamomanager import DynamoManager

LOGGER = AppLogger(__name__)
LAMBDAHELPER = LambdaHelper(LOGGER)
DYNAMO_MANAGER = DynamoManager(LOGGER)

def create_profile(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda handler for creating a new educational profile"""
    LOGGER.info("create_profile event payload: %s", json.dumps(event))
    
    try:
        email = event["requestContext"]["authorizer"]["principalId"]
        body = json.loads(event.get('body', '{}'))
        profile_name = body.get('profileName')
        general_background = body.get('generalBackground')
        demographics = body.get('demographics')
        math_ability = body.get('mathAbility')
        engagement = body.get('engagement')
        special_considerations = body.get('specialConsiderations')
        if not all([profile_name, general_background, demographics, math_ability, engagement, special_considerations]):
            return LAMBDAHELPER.format_response(400, {
                "error": "Missing required fields. All profile fields are required: profileName, generalBackground, demographics, mathAbility, engagement, specialConsiderations"
            })
        profile_item = {
            'email': email,
            'profilename': profile_name,
            'demographics': demographics,
            'general_background': general_background,
            'math_ability': math_ability,
            'engagement': engagement,
            'special_considerations': special_considerations,
            'active': True
        }
        DYNAMO_MANAGER.put_dynamo_item(
            table_name=os.environ['PROFILES_TABLE'],
            payload=profile_item
        )
        return LAMBDAHELPER.format_response(200, {
            "message": "Profile created successfully",
            "profile": profile_item
        })
    except Exception as err:
        LOGGER.error("Error creating profile: %s", str(err))
        return LAMBDAHELPER.format_response(500, {
            "error": f"An error occurred while creating the profile: {str(err)}"
        })
def list_profiles(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda handler for listing user's profiles"""
    LOGGER.info("list_profiles event payload: %s", json.dumps(event))
    try:
        email = event["requestContext"]["authorizer"]["principalId"]
        profiles = DYNAMO_MANAGER.query_table(
            table_name=os.environ['PROFILES_TABLE'],
            filter_key='email',
            filter_value=email
        )
        if not profiles:
            profiles = load_profiles(email)
        formatted_profiles = []
        for profile in profiles:
            formatted_profile = {
                'profileName': profile.get('profilename'),
                'demographics': profile.get('demographics'),
                'generalBackground': profile.get('general_background'),
                'mathAbility': profile.get('math_ability'),
                'engagement': profile.get('engagement'),
                'specialConsiderations': profile.get('special_considerations'),
                'active': profile.get('active', True)
            }
            formatted_profiles.append(formatted_profile)
        return LAMBDAHELPER.format_response(200, {
            "profiles": formatted_profiles
        })
    except Exception as err:
        LOGGER.error("Error listing profiles: %s", str(err))
        return LAMBDAHELPER.format_response(500, {
            "error": f"An error occurred while listing profiles: {str(err)}"
        })

def update_profile(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda handler for updating an existing profile"""
    LOGGER.info("update_profile event payload: %s", json.dumps(event))
    
    try:
        email = event["requestContext"]["authorizer"]["principalId"]
        profile_name = event["pathParameters"]["profileName"]
        body = json.loads(event.get('body', '{}'))
        general_background = body.get('generalBackground')
        demographics = body.get('demographics')
        math_ability = body.get('mathAbility')
        engagement = body.get('engagement')
        special_considerations = body.get('specialConsiderations')
        active = body.get('active')
        existing_profile = DYNAMO_MANAGER.get_dynamo_item_multi_key(
            table_name=os.environ['PROFILES_TABLE'],
            lookup_keys={'email': email, 'profilename': profile_name}
        )
        if not existing_profile:
            return LAMBDAHELPER.format_response(404, {
                "error": f"Profile '{profile_name}' not found"
            })
        updated_profile = {
            'email': email,
            'profilename': profile_name,
            'demographics': demographics or existing_profile.get('demographics'),
            'general_background': general_background or existing_profile.get('general_background'),
            'math_ability': math_ability or existing_profile.get('math_ability'),
            'engagement': engagement or existing_profile.get('engagement'),
            'special_considerations': special_considerations or existing_profile.get('special_considerations'),
            'active': active if active is not None else existing_profile.get('active', True)
        }
        DYNAMO_MANAGER.put_dynamo_item(
            table_name=os.environ['PROFILES_TABLE'],
            payload=updated_profile
        )
        return LAMBDAHELPER.format_response(200, {
            "message": "Profile updated successfully",
            "profile": updated_profile
        })
    except Exception as err:
        LOGGER.error("Error updating profile: %s", str(err))
        return LAMBDAHELPER.format_response(500, {
            "error": f"An error occurred while updating the profile: {str(err)}"
        })

def delete_profile(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda handler for deleting a profile"""
    LOGGER.info("delete_profile event payload: %s", json.dumps(event))
    try:
        email = event["requestContext"]["authorizer"]["principalId"]
        profile_name = event["pathParameters"]["profileName"]
        existing_profile = DYNAMO_MANAGER.get_dynamo_item_multi_key(
            table_name=os.environ['PROFILES_TABLE'],
            lookup_keys={'email': email, 'profilename': profile_name}
        )
        if not existing_profile:
            return LAMBDAHELPER.format_response(404, {
                "error": f"Profile '{profile_name}' not found"
            })
        DYNAMO_MANAGER.delete_item(
            key_dict={'email': email, 'profilename': profile_name},
            table_name=os.environ['PROFILES_TABLE']
        )
        return LAMBDAHELPER.format_response(200, {
            "message": f"Profile '{profile_name}' deleted successfully"
        })
    except Exception as err:
        LOGGER.error("Error deleting profile: %s", str(err))
        return LAMBDAHELPER.format_response(500, {
            "error": f"An error occurred while deleting the profile: {str(err)}"
        })
    
def load_profiles(user_email):
    """Load predefined profiles into DynamoDB"""    
    # Predefined profiles exactly matching the PDF document structure
    profiles = [
        {
            'email': user_email,
            'profilename': 'creative_visual_learner',  # More descriptive than "Profile A"
            'demographics': 'Hispanic, from a lower-middle-class family',
            'general_background': 'Shows a keen interest in arts and crafts, using colors and shapes creatively but struggles with abstract numerical concepts',
            'math_ability': 'Finds basic arithmetic challenging but has a good grasp of patterns and sequences through visual representations',
            'engagement': 'Engages more with math when it is integrated with art or storytelling',
            'special_considerations': 'No current IEP or 504 plan, but visual learning strategies are recommended',
            'active': True
        },
        {
            'email': user_email,
            'profilename': 'bilingual_narrative_learner',
            'demographics': 'African American, from a bilingual household',
            'general_background': 'Enjoys storytelling and has a strong memory for details. Often shares culturally rich family stories',
            'math_ability': 'Excels in verbal explanations of problem-solving but struggles with written computation',
            'engagement': 'Shows enthusiasm when math problems involve storytelling or real-life scenarios',
            'special_considerations': 'Benefits from verbal and visual cues; may require support for translating mathematical concepts to paper',
            'active': True
        },
        {
            'email': user_email,
            'profilename': 'technological_logical_learner',
            'demographics': 'Asian American, lives in a multigenerational household',
            'general_background': 'Enthusiastic about technology and creates simple coding projects',
            'math_ability': 'Demonstrates strong logical reasoning and pattern recognition, capable in algorithmic thinking',
            'engagement': 'Highly engaged when able to use technology as a tool for learning math',
            'special_considerations': 'Encouragement to collaborate with peers can enhance social learning and application of math skills',
            'active': True
        }
    ]
    
    # Load each profile into DynamoDB
    for profile in profiles:
        try:
            DYNAMO_MANAGER.put_dynamo_item(
                table_name=os.environ['PROFILES_TABLE'],
                payload=profile
            )
            print(f"Successfully loaded profile: {profile['profilename']}")
        except Exception as e:
            print(f"Error loading profile {profile['profilename']}: {str(e)}")
    return profiles