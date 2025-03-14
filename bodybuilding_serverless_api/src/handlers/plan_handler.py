import json
from typing import Dict, Any
from ..services.plan_service import PlanService
from ..utils.response_builder import build_response
from ..utils.request_validator import validate_request

plan_service = PlanService()

def create_plan(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for creating a new bodybuilding plan
    """
    try:
        # Validate request body
        body = json.loads(event.get('body', '{}'))
        validate_request(body, 'create_plan')
        
        # Extract user information from request context
        user_id = event['requestContext']['authorizer']['claims']['sub']
        
        # Delegate to service layer
        result = plan_service.create_plan(user_id=user_id, plan_data=body)
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)})

def save_plan(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for updating an existing bodybuilding plan
    """
    try:
        body = json.loads(event.get('body', '{}'))
        validate_request(body, 'update_plan')
        
        user_id = event['requestContext']['authorizer']['claims']['sub']
        plan_id = body.get('planId')
        
        result = plan_service.update_plan(
            user_id=user_id,
            plan_id=plan_id,
            plan_data=body
        )
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)})

def get(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for retrieving a bodybuilding plan
    """
    try:
        plan_id = event['pathParameters']['planId']
        user_id = event['requestContext']['authorizer']['claims']['sub']
        
        result = plan_service.get_plan(user_id=user_id, plan_id=plan_id)
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)})

def list_plans(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for listing all plans for a user
    """
    try:
        user_id = event['requestContext']['authorizer']['claims']['sub']
        
        result = plan_service.list_plans(user_id=user_id)
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)})

def delete(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for deleting a plan and all its versions
    """
    try:
        plan_id = event['pathParameters']['planId']
        user_id = event['requestContext']['authorizer']['claims']['sub']
        
        # Delete the plan and all its versions
        result = plan_service.delete_plan(user_id=user_id, plan_id=plan_id)
        
        return build_response(200, {
            "message": f"Plan '{plan_id}' and all its versions deleted successfully"
        })
    except Exception as e:
        return build_response(500, {'error': str(e)})

def get_plan_versions(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for retrieving all versions of a specific plan
    """
    try:
        plan_id = event['pathParameters']['planId']
        user_id = event['requestContext']['authorizer']['claims']['sub']
        
        result = plan_service.get_plan_versions(user_id=user_id, plan_id=plan_id)
        
        return build_response(200, {
            "versions": result,
            "totalVersions": len(result)
        })
    except Exception as e:
        return build_response(500, {'error': str(e)})