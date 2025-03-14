from typing import Dict, Any

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
        'body': body
    } 