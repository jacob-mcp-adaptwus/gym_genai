import asyncio
import os
import json
from typing import Dict, Any

try:
    from util.lambdahelper import LambdaHelper
    from util.loggers.applogger import AppLogger
    from services.lessonservice import LessonService
    from aws.dynamomanager import DynamoManager
except ImportError:
    from src.util.lambdahelper import LambdaHelper
    from src.util.loggers.applogger import AppLogger
    from src.services.lessonservice import LessonService
    from src.aws.dynamomanager import DynamoManager

LOGGER = AppLogger(__name__)
LAMBDAHELPER = LambdaHelper(LOGGER)
LESSON_SERVICE = LessonService(LOGGER)
DYNAMO_MANAGER = DynamoManager(LOGGER)

def create_lesson(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda handler for generating lesson plans"""
    LOGGER.info("create_lesson event payload: %s", json.dumps(event))
    
    try:
        body = json.loads(event.get('body', '{}'))
        
        if not body.get('topic'):
            return LAMBDAHELPER.format_response(400, {
                "error": "Lesson topic is required"
            })
        
        # Create event loop and run the async function
        loop = asyncio.get_event_loop()
        lesson_plan = loop.run_until_complete(
            LESSON_SERVICE.create_lesson(
                topic=body.get('topic'),
                profile=body.get('profile'),
                existing_plan=body.get('existing_plan'),
                grade=body.get('grade'),
                subject=body.get('subject'),
                user_chat=body.get('user_chat')  # Add user_chat paramete
            )
        )
        
        return LAMBDAHELPER.format_response(200, {
            "lesson_plan": lesson_plan
        })
        
    except json.JSONDecodeError as err:
        LOGGER.error("Error parsing JSON: %s", str(err))
        return LAMBDAHELPER.format_response(400, {
            "error": "Invalid JSON in request body"
        })
    except Exception as err:
        LOGGER.error("Error in create_lesson: %s", str(err))
        return LAMBDAHELPER.format_response(500, {
            "error": f"An error occurred: {str(err)}"
        })

def save_lesson(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda handler for saving lesson plans"""
    LOGGER.info("save_lesson event payload: %s", json.dumps(event))
    
    try:
        # Get user email from authorizer
        email = event["requestContext"]["authorizer"]["principalId"]
        
        # Parse request
        body = json.loads(event.get('body', '{}'))
        
        # Validate required fields
        required_fields = ['title', 'content', 'grade', 'subject']
        if not all(field in body for field in required_fields):
            return LAMBDAHELPER.format_response(400, {
                "error": f"Missing required fields: {', '.join(required_fields)}"
            })
        
        # Save lesson
        saved_lesson = LESSON_SERVICE.save_lesson(email, body)
        
        return LAMBDAHELPER.format_response(200, {
            "message": "Lesson plan saved successfully",
            "lesson": saved_lesson
        })
        
    except Exception as err:
        LOGGER.error("Error in save_lesson: %s", str(err))
        return LAMBDAHELPER.format_response(500, {
            "error": f"An error occurred: {str(err)}"
        })

def list_lessons(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda handler for listing user's lesson plans"""
    LOGGER.info("list_lessons event payload: %s", json.dumps(event))
    
    try:
        # Get user email from authorizer
        email = event["requestContext"]["authorizer"]["principalId"]
        
        # Retrieve lessons
        lessons = LESSON_SERVICE.get_user_lessons(email)
        
        return LAMBDAHELPER.format_response(200, {
            "lessons": lessons
        })
        
    except Exception as err:
        LOGGER.error("Error in list_lessons: %s", str(err))
        return LAMBDAHELPER.format_response(500, {
            "error": f"An error occurred: {str(err)}"
        })
    

def delete_lesson(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda handler for deleting a lesson and all its versions"""
    LOGGER.info("delete_lesson event payload: %s", json.dumps(event))
    
    try:
        # Get user email from authorizer
        email = event["requestContext"]["authorizer"]["principalId"]
        
        # Get lesson ID from path parameters
        lesson_id = event["pathParameters"]["lessonId"]
        
        # First verify the lesson exists and user has access
        existing_lesson = LESSON_SERVICE._get_lesson_by_id(email, lesson_id)
        if not existing_lesson:
            return LAMBDAHELPER.format_response(404, {
                "error": f"Lesson '{lesson_id}' not found"
            })

        # Delete all versions from versions table
        versions_table = DYNAMO_MANAGER.dynamo_client.Table(os.environ['LESSON_VERSIONS_TABLE'])
        versions = LESSON_SERVICE.get_lesson_versions(email, lesson_id)
        
        # Batch delete all versions
        for version in versions:
            DYNAMO_MANAGER.delete_item(
                key_dict={
                    'lessonId': lesson_id,
                    'profileId': version['profileId']
                },
                table_name=os.environ['LESSON_VERSIONS_TABLE']
            )

        # Delete main lesson record
        DYNAMO_MANAGER.delete_item(
            key_dict={
                'email': email,
                'lessonId': lesson_id
            },
            table_name=os.environ['LESSONS_TABLE']
        )

        return LAMBDAHELPER.format_response(200, {
            "message": f"Lesson '{lesson_id}' and all its versions deleted successfully"
        })
        
    except Exception as err:
        LOGGER.error("Error deleting lesson: %s", str(err))
        return LAMBDAHELPER.format_response(500, {
            "error": f"An error occurred while deleting the lesson: {str(err)}"
        })
    
def get_lesson_versions(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    LOGGER.info("get_lesson_versions event payload: %s", json.dumps(event))
    try:
        # Get user email from authorizer for access control
        email = event["requestContext"]["authorizer"]["principalId"]
        
        # Extract lesson ID from request path parameters
        lesson_id = event["pathParameters"]["lessonId"]
        
        # Retrieve all versions using the lesson service
        versions = LESSON_SERVICE.get_lesson_versions(email, lesson_id)
        
        # Format each version while preserving all saved fields
        formatted_versions = []
        for version in versions:
            formatted_version = {
                'lessonId': version.get('lessonId'),
                'profileVersion': version.get('profileVersion'),  # Contains profile#version string
                'content': version.get('content'),
                'title': version.get('title'),
                'grade': version.get('grade'),
                'subject': version.get('subject'),
                'timestamp': version.get('timestamp'),
                'version': version.get('version'),  # Numeric version number
                'profileId': version.get('profileId'),
                'email': version.get('email')
            }
            formatted_versions.append(formatted_version)

        # Sort versions by timestamp for consistent ordering
        formatted_versions.sort(key=lambda x: x['timestamp'], reverse=True)

        return LAMBDAHELPER.format_response(200, {
            "versions": formatted_versions,
            "totalVersions": len(formatted_versions)
        })
        
    except Exception as err:
        LOGGER.error("Error retrieving lesson versions: %s", str(err))
        return LAMBDAHELPER.format_response(500, {
            "error": f"An error occurred while retrieving lesson versions: {str(err)}"
        })