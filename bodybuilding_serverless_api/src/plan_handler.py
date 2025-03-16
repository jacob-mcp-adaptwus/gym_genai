import json
import asyncio
import os
import sys
from typing import Dict, Any

# Add the current directory to the Python path to enable imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)  # Get the parent directory (src)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

try:
    from services.service_factory import ServiceFactory
    from utils.response_builder import build_response
    from utils.request_validator import validate_request
except ImportError:
    print("plan handler import error")
    try:
        # Try with src prefix
        from src.services.service_factory import ServiceFactory
        from src.utils.response_builder import build_response
        from src.utils.request_validator import validate_request
    except ImportError:
        # Last resort - direct relative imports
        from .services.service_factory import ServiceFactory
        from .utils.response_builder import build_response
        from .utils.request_validator import validate_request


# Get the PlanService instance from the ServiceFactory
service_factory = ServiceFactory.get_instance()
plan_service = service_factory.plan_service

async def create_plan(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for creating a new bodybuilding plan
    """
    print(event)
    try:
        # Validate request body
        body = json.loads(event.get('body', '{}'))
        validate_request(body, 'create_plan')
        
        # Extract user information from request context
        user_id = event['requestContext']['authorizer']['claims']['sub']
        
        # Delegate to service layer
        result = await plan_service.create_plan(user_id=user_id, plan_data=body)
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)})

async def save_plan(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for updating an existing bodybuilding plan
    """
    try:
        body = json.loads(event.get('body', '{}'))
        validate_request(body, 'update_plan')
        
        user_id = event['requestContext']['authorizer']['claims']['sub']
        plan_id = body.get('planId')
        
        result = await plan_service.update_plan(
            user_id=user_id,
            plan_id=plan_id,
            plan_data=body
        )
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)})

async def get(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for retrieving a bodybuilding plan
    """
    try:
        plan_id = event['pathParameters']['planId']
        user_id = event['requestContext']['authorizer']['claims']['sub']
        
        result = await plan_service.get_plan(user_id=user_id, plan_id=plan_id)
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)})

async def list_plans(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for listing all plans for a user
    """
    try:
        user_id = event['requestContext']['authorizer']['claims']['sub']
        
        result = await plan_service.list_plans(user_id=user_id)
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)})

async def delete(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for deleting a plan and all its versions
    """
    try:
        plan_id = event['pathParameters']['planId']
        user_id = event['requestContext']['authorizer']['claims']['sub']
        
        # Delete the plan and all its versions
        result = await plan_service.delete_plan(user_id=user_id, plan_id=plan_id)
        
        return build_response(200, {
            "message": f"Plan '{plan_id}' and all its versions deleted successfully"
        })
    except Exception as e:
        return build_response(500, {'error': str(e)})

async def get_plan_versions(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for retrieving all versions of a specific plan
    """
    try:
        plan_id = event['pathParameters']['planId']
        user_id = event['requestContext']['authorizer']['claims']['sub']
        
        result = await plan_service.get_plan_versions(user_id=user_id, plan_id=plan_id)
        
        return build_response(200, {
            "versions": result,
            "totalVersions": len(result)
        })
    except Exception as e:
        return build_response(500, {'error': str(e)})

# Lambda handler wrappers to run async functions
def lambda_handler_wrapper(handler_func):
    def wrapper(event, context):
        return asyncio.run(handler_func(event, context))
    return wrapper

# Apply the wrapper to all handlers
create_plan_handler = lambda_handler_wrapper(create_plan)
save_plan_handler = lambda_handler_wrapper(save_plan)
get_plan_handler = lambda_handler_wrapper(get)
list_plans_handler = lambda_handler_wrapper(list_plans)
delete_plan_handler = lambda_handler_wrapper(delete)
get_plan_versions_handler = lambda_handler_wrapper(get_plan_versions)