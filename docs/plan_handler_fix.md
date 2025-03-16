# Proposed Fixes for plan_handler.py

Based on the analysis of the code and potential issues, here are the proposed fixes for the `plan_handler.py` file:

## 1. Fix Service Initialization

The `PlanService` class requires two parameters in its constructor, but it's being initialized without any parameters in the handler file.

```python
# Original code (problematic)
plan_service = PlanService()

# Fixed code
from ..aws.dynamomanager import get_dynamodb_client
from ..aws.bedrockmanager import BedrockManager

dynamodb_client = get_dynamodb_client()
bedrock_manager = BedrockManager()
plan_service = PlanService(dynamodb_client, bedrock_manager)
```

## 2. Fix Async/Sync Mismatch

The handler function is synchronous, but it's calling an asynchronous method without awaiting it.

### Option 1: Make the handler asynchronous (if your framework supports it)

```python
import asyncio

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
        
        # Delegate to service layer (with await)
        result = await plan_service.create_plan(user_id=user_id, plan_data=body)
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)})
```

### Option 2: Use a synchronous wrapper (more compatible with AWS Lambda)

```python
def create_plan(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
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
        
        # Use a synchronous wrapper to call the async method
        result = asyncio.run(plan_service.create_plan(user_id=user_id, plan_data=body))
        
        return build_response(200, result)
    except Exception as e:
        return build_response(500, {'error': str(e)})
```

### Option 3: Modify the service method to be synchronous (simplest approach)

This would require changing the `create_plan` method in `plan_service.py` to be synchronous.

## 3. Fix Response Serialization

Ensure the response body is properly JSON serialized:

```python
# In utils/response_builder.py
import json

def build_response(status_code: int, body: Any) -> Dict[str, Any]:
    """
    Builds a standardized API response
    
    Args:
        status_code (int): HTTP status code
        body (Any): Response body
        
    Returns:
        Dict[str, Any]: Formatted API Gateway response
    """
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        'body': json.dumps(body)
    }
```

## 4. Improve Error Handling

Add more specific error handling to better identify issues:

```python
def create_plan(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for creating a new bodybuilding plan
    """
    print(f"Received event: {event}")
    try:
        # Validate request body
        try:
            body = json.loads(event.get('body', '{}'))
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return build_response(400, {'error': f"Invalid JSON in request body: {str(e)}"})
            
        try:
            validate_request(body, 'create_plan')
        except Exception as e:
            print(f"Validation error: {e}")
            return build_response(400, {'error': f"Request validation failed: {str(e)}"})
        
        # Extract user information from request context
        try:
            user_id = event['requestContext']['authorizer']['claims']['sub']
        except KeyError as e:
            print(f"Authorization error: {e}")
            return build_response(401, {'error': "Missing or invalid authorization"})
        
        # Delegate to service layer
        try:
            result = plan_service.create_plan(user_id=user_id, plan_data=body)
            return build_response(200, result)
        except Exception as e:
            print(f"Service error: {e}")
            return build_response(500, {'error': f"Error creating plan: {str(e)}"})
            
    except Exception as e:
        print(f"Unexpected error: {e}")
        return build_response(500, {'error': str(e)})
```

## Complete Fixed Handler

Here's the complete fixed version of the `create_plan` handler:

```python
import json
import asyncio
from typing import Dict, Any
from ..services.plan_service import PlanService
from ..utils.response_builder import build_response
from ..utils.request_validator import validate_request
from ..aws.dynamomanager import get_dynamodb_client
from ..aws.bedrockmanager import BedrockManager

# Properly initialize service with dependencies
dynamodb_client = get_dynamodb_client()
bedrock_manager = BedrockManager()
plan_service = PlanService(dynamodb_client, bedrock_manager)

def create_plan(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handler for creating a new bodybuilding plan
    """
    print(f"Received event: {event}")
    try:
        # Validate request body
        try:
            body = json.loads(event.get('body', '{}'))
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return build_response(400, {'error': f"Invalid JSON in request body: {str(e)}"})
            
        try:
            validate_request(body, 'create_plan')
        except Exception as e:
            print(f"Validation error: {e}")
            return build_response(400, {'error': f"Request validation failed: {str(e)}"})
        
        # Extract user information from request context
        try:
            user_id = event['requestContext']['authorizer']['claims']['sub']
        except KeyError as e:
            print(f"Authorization error: {e}")
            return build_response(401, {'error': "Missing or invalid authorization"})
        
        # Delegate to service layer (using asyncio.run if the method is async)
        try:
            # Option 1: If keeping the service method as async
            result = asyncio.run(plan_service.create_plan(user_id=user_id, plan_data=body))
            
            # Option 2: If the service method is made synchronous
            # result = plan_service.create_plan(user_id=user_id, plan_data=body)
            
            return build_response(200, result)
        except Exception as e:
            print(f"Service error: {e}")
            return build_response(500, {'error': f"Error creating plan: {str(e)}"})
            
    except Exception as e:
        print(f"Unexpected error: {e}")
        return build_response(500, {'error': str(e)})
```

Apply these changes to fix the issues with the `create_plan` function. 