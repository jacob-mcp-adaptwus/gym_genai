import os
import asyncio
import json
from typing import Dict, Any

try:
    from services.chat.orchestration.component_orchestrator import ComponentOrchestrator
    from services.messageanalysis import MessageAnalyzer
    from aws.dynamomanager import DynamoManager
    from aws.bedrockmanager import BedrockManager
    from util.loggers.applogger import AppLogger
except ImportError:
    from src.services.chat.orchestration.component_orchestrator import ComponentOrchestrator
    from src.services.messageanalysis import MessageAnalyzer
    from src.aws.dynamomanager import DynamoManager
    from src.aws.bedrockmanager import BedrockManager
    from src.util.loggers.applogger import AppLogger

LOGGER = AppLogger(__name__)
BEDROCK = BedrockManager(LOGGER)
DYNAMO_MANAGER = DynamoManager(LOGGER)
MESSAGE_ANALYZER = MessageAnalyzer(BEDROCK)
COMPONENT_ORCHESTRATOR = ComponentOrchestrator(LOGGER)

def analyze_message(event: Dict[str, Any], context: Any):
    """Lambda handler for analyzing chat messages to determine intent and affected components"""
    LOGGER.info("analyze_message event payload: %s", json.dumps(event))

    try:
        body = json.loads(event.get('body', '{}'))
        
        # Create event loop and run the async analysis
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            MESSAGE_ANALYZER.analyze_intent(
                message=body['message'],
                current_plan=json.loads(body.get('existing_plan', '{}')),
                context={
                    'grade': body.get('grade'),
                    'subject': body.get('subject'),
                    'topic': body.get('topic'),
                    'profile': body.get('profile', {})
                }
            )
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(response),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
        
    except json.JSONDecodeError as err:
        LOGGER.error("Error parsing JSON: %s", str(err))
        return {
            'statusCode': 400,
            'body': json.dumps({"error": "Invalid JSON in request body"}),
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as err:
        LOGGER.error("Error in analyze_message: %s", str(err))
        return {
            'statusCode': 500,
            'body': json.dumps({"error": f"An error occurred: {str(err)}"}),
            'headers': {'Content-Type': 'application/json'}
        }

def chat_with_component(event: Dict[str, Any], context: Any):
    """Lambda handler for updating specific components based on chat interaction"""
    LOGGER.info("chat_with_component event payload: %s", json.dumps(event))
    
    try:
        body = json.loads(event.get('body', '{}'))
        
        # Create event loop and run the async component update
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            COMPONENT_ORCHESTRATOR.process_single_component(
                message=body['message'],
                component=body['component'],
                current_plan=json.loads(body.get('existing_plan', '{}')),
                context={
                    'grade': body.get('grade'),
                    'subject': body.get('subject'),
                    'topic': body.get('topic'),
                    'profile': body.get('profile', {})
                }
            )
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(response),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
        
    except json.JSONDecodeError as err:
        LOGGER.error("Error parsing JSON: %s", str(err))
        return {
            'statusCode': 400,
            'body': json.dumps({"error": "Invalid JSON in request body"}),
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as err:
        LOGGER.error("Error in chat_with_component: %s", str(err))
        return {
            'statusCode': 500,
            'body': json.dumps({"error": f"An error occurred: {str(err)}"}),
            'headers': {'Content-Type': 'application/json'}
        }

def chat_with_lesson(event: Dict[str, Any], context: Any):
    """Lambda handler for processing chat interactions and updating lesson plans"""
    LOGGER.info("chat_with_lesson event payload: %s", json.dumps(event))
    
    try:
        # Get user email from authorizer
        email = event["requestContext"]["authorizer"]["principalId"]
        body = json.loads(event.get('body', '{}'))
        
        # Create event loop and run the async chat processing
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            COMPONENT_ORCHESTRATOR.process_chat_update(
                message=body['message'],
                components=body.get('analysis', {}).get('components', []),
                current_plan=json.loads(body.get('existing_plan', '{}')),
                tier=body.get('analysis', {}).get('tier', 2),
                context={
                    'email': email,
                    'grade': body.get('grade'),
                    'subject': body.get('subject'),
                    'topic': body.get('topic'),
                    'profile': body.get('profile', {}),
                    'lessonId': body.get('lessonId')
                }
            )
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(response),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
        
    except json.JSONDecodeError as err:
        LOGGER.error("Error parsing JSON: %s", str(err))
        return {
            'statusCode': 400,
            'body': json.dumps({"error": "Invalid JSON in request body"}),
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as err:
        LOGGER.error("Error in chat_with_lesson: %s", str(err))
        return {
            'statusCode': 500,
            'body': json.dumps({"error": f"An error occurred: {str(err)}"}),
            'headers': {'Content-Type': 'application/json'}
        }

def get_chat_history(event: Dict[str, Any], context: Any):
    """Lambda handler for retrieving chat history for a lesson"""
    LOGGER.info("get_chat_history event payload: %s", json.dumps(event))
    
    try:
        # Get user email from authorizer
        email = event["requestContext"]["authorizer"]["principalId"]
        lesson_id = event["pathParameters"]["lessonId"]
        
        # Query chat history from DynamoDB
        chat_history = DYNAMO_MANAGER.query_table(
            table_name=os.environ['CHAT_HISTORY_TABLE'],
            key_condition_expression='lessonId = :lid AND email = :email',
            expression_attribute_values={
                ':lid': lesson_id,
                ':email': email
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({"chatHistory": chat_history}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
        
    except Exception as err:
        LOGGER.error("Error in get_chat_history: %s", str(err))
        return {
            'statusCode': 500,
            'body': json.dumps({"error": f"An error occurred: {str(err)}"}),
            'headers': {'Content-Type': 'application/json'}
        }