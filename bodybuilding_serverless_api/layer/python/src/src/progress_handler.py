import json
import os
import sys
from typing import Dict, Any

# Add the current directory to the Python path to enable imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

try:
    from services.progress_service import ProgressService
    from utils.response_builder import build_response
    from utils.request_validator import validate_request
except ImportError:
    try:
        # Try with src prefix
        from src.services.progress_service import ProgressService
        from src.utils.response_builder import build_response
        from src.utils.request_validator import validate_request
    except ImportError:
        # Last resort - direct relative imports
        from .services.progress_service import ProgressService
        from .utils.response_builder import build_response
        from .utils.request_validator import validate_request

progress_service = ProgressService()

def update_progress(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for logging progress updates (workouts, measurements, etc.)
    """
    try:
        body = json.loads(event.get('body', '{}'))
        validate_request(body, 'progress_update')
        
        user_id = event['pathParameters']['userId']
        auth_user_id = event['requestContext']['authorizer']['claims']['sub']
        
        # Ensure users can only update their own progress
        if user_id != auth_user_id:
            return build_response(403, {'error': 'You can only update your own progress'})
        
        result = progress_service.log_progress(
            user_id=user_id,
            progress_data=body
        )
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)})

def get_progress(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for retrieving progress history
    """
    try:
        user_id = event['pathParameters']['userId']
        auth_user_id = event['requestContext']['authorizer']['claims']['sub']
        
        # Ensure users can only view their own progress
        if user_id != auth_user_id:
            return build_response(403, {'error': 'You can only view your own progress'})
        
        # Optional query parameters for filtering
        query_params = event.get('queryStringParameters', {}) or {}
        start_date = query_params.get('startDate')
        end_date = query_params.get('endDate')
        metric_type = query_params.get('metricType')
        
        result = progress_service.get_progress_history(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date,
            metric_type=metric_type
        )
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)})

def get_progress_summary(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for getting a summary of progress metrics
    """
    try:
        plan_id = event['pathParameters']['planId']
        user_id = event['requestContext']['authorizer']['claims']['sub']
        
        result = progress_service.get_progress_summary(
            user_id=user_id,
            plan_id=plan_id
        )
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)}) 