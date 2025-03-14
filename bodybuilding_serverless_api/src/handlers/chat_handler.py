import json
from typing import Dict, Any
from ..services.chat.orchestration.plan_orchestrator import PlanOrchestrator
from ..utils.response_builder import build_response
from ..utils.request_validator import validate_request

plan_orchestrator = PlanOrchestrator()

def chat_with_coach(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for processing chat messages with the AI coach
    """
    try:
        # Validate request body
        body = json.loads(event.get('body', '{}'))
        validate_request(body, 'chat_message')
        
        plan_id = body.get('planId')
        user_id = event['requestContext']['authorizer']['claims']['sub']
        
        # Extract message and any additional context
        message = body.get('message')
        context_data = body.get('context', {})
        
        # Delegate to orchestrator for processing
        result = plan_orchestrator.process_message(
            user_id=user_id,
            plan_id=plan_id,
            message=message,
            context=context_data
        )
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)})

def get_chat_history(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for retrieving chat history for a plan
    """
    try:
        plan_id = event['pathParameters']['planId']
        user_id = event['requestContext']['authorizer']['claims']['sub']
        
        result = plan_orchestrator.get_chat_history(
            user_id=user_id,
            plan_id=plan_id
        )
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)}) 