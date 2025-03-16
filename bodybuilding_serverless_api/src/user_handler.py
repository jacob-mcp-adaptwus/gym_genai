"""User management Lambda functions with fitness profile support"""
# pylint: disable=C0301,W0613
import json
import os
import sys
from typing import Dict, Any

# Add the current directory to the Python path to enable imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

try:
    from utils.response_builder import build_response
    from utils.loggers.applogger import AppLogger
    from aws.dynamomanager import DynamoManager
except ImportError:
    try:
        # Try with src prefix
        from src.utils.response_builder import build_response
        from src.utils.loggers.applogger import AppLogger
        from src.aws.dynamomanager import DynamoManager
    except ImportError:
        # Last resort - direct relative imports
        from .utils.response_builder import build_response
        from .utils.loggers.applogger import AppLogger
        from .aws.dynamomanager import DynamoManager

LOGGER = AppLogger(__name__)
DYNAMO_MANAGER = DynamoManager(LOGGER)

def create_user(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda handler for creating a new user profile"""
    LOGGER.info("create_user event payload: %s", json.dumps(event))
    
    try:
        # Get user ID from Cognito claims
        user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
        body = json.loads(event.get('body', '{}'))
        
        # Required fields for a fitness profile
        name = body.get('name')
        age = body.get('age')
        height = body.get('height')
        weight = body.get('weight')
        fitness_level = body.get('fitnessLevel')
        fitness_goals = body.get('fitnessGoals')
        available_days = body.get('availableDays')
        
        if not all([name, age, height, weight, fitness_level, fitness_goals, available_days]):
            return build_response(400, {
                "error": "Missing required fields. All user fields are required: name, age, height, weight, fitnessLevel, fitnessGoals, availableDays"
            })
        
        user_item = {
            'userId': user_id,
            'name': name,
            'age': age,
            'height': height,
            'weight': weight,
            'fitnessLevel': fitness_level,
            'fitnessGoals': fitness_goals,
            'availableDays': available_days,
            'active': True
        }
        
        DYNAMO_MANAGER.put_item(
            table_name=os.environ['USERS_TABLE'],
            item=user_item
        )
        
        return build_response(200, {
            "message": "User profile created successfully",
            "user": user_item
        })
    except Exception as err:
        LOGGER.error("Error creating user profile: %s", str(err))
        return build_response(500, {
            "error": f"An error occurred while creating the user profile: {str(err)}"
        })

def update_user(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda handler for updating an existing user profile"""
    LOGGER.info("update_user event payload: %s", json.dumps(event))
    
    try:
        # Get user ID from Cognito claims
        user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
        path_user_id = event["pathParameters"]["userId"]
        
        # Ensure the user can only update their own profile
        if user_id != path_user_id:
            return build_response(403, {
                "error": "You can only update your own profile"
            })
        
        body = json.loads(event.get('body', '{}'))
        
        # Fields that can be updated
        name = body.get('name')
        age = body.get('age')
        height = body.get('height')
        weight = body.get('weight')
        fitness_level = body.get('fitnessLevel')
        fitness_goals = body.get('fitnessGoals')
        available_days = body.get('availableDays')
        
        # Get existing user profile
        existing_user = DYNAMO_MANAGER.get_item(
            table_name=os.environ['USERS_TABLE'],
            key={'userId': user_id}
        )
        
        if not existing_user:
            return build_response(404, {
                "error": "User profile not found"
            })
        
        # Update with new values or keep existing ones
        updated_user = {
            'userId': user_id,
            'name': name or existing_user.get('name'),
            'age': age or existing_user.get('age'),
            'height': height or existing_user.get('height'),
            'weight': weight or existing_user.get('weight'),
            'fitnessLevel': fitness_level or existing_user.get('fitnessLevel'),
            'fitnessGoals': fitness_goals or existing_user.get('fitnessGoals'),
            'availableDays': available_days or existing_user.get('availableDays'),
            'active': body.get('active', existing_user.get('active', True))
        }
        
        DYNAMO_MANAGER.put_item(
            table_name=os.environ['USERS_TABLE'],
            item=updated_user
        )
        
        return build_response(200, {
            "message": "User profile updated successfully",
            "user": updated_user
        })
    except Exception as err:
        LOGGER.error("Error updating user profile: %s", str(err))
        return build_response(500, {
            "error": f"An error occurred while updating the user profile: {str(err)}"
        })

def get_user(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda handler for retrieving a user profile"""
    LOGGER.info("get_user event payload: %s", json.dumps(event))
    
    try:
        # Get user ID from Cognito claims
        user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
        path_user_id = event["pathParameters"]["userId"]
        
        # Ensure the user can only view their own profile
        if user_id != path_user_id:
            return build_response(403, {
                "error": "You can only view your own profile"
            })
        
        # Get user profile
        user = DYNAMO_MANAGER.get_item(
            table_name=os.environ['USERS_TABLE'],
            key={'userId': user_id}
        )
        
        if not user:
            return build_response(404, {
                "error": "User profile not found"
            })
        
        return build_response(200, {
            "user": user
        })
    except Exception as err:
        LOGGER.error("Error retrieving user profile: %s", str(err))
        return build_response(500, {
            "error": f"An error occurred while retrieving the user profile: {str(err)}"
        }) 