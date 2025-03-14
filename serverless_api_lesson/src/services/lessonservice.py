import json
import os
import uuid
from datetime import datetime
from typing import Dict, Any, List, Optional
import boto3
from botocore.config import Config
from boto3.dynamodb.conditions import Key 

try:
    from services.parallellessonservice import ParallelLessonService
    from aws.dynamomanager import DynamoManager
    from util.loggers.applogger import AppLogger
except ImportError:
    from src.services.parallellessonservice import ParallelLessonService
    from src.aws.dynamomanager import DynamoManager
    from src.util.loggers.applogger import AppLogger

class LessonService:
    """Service class for managing lesson-related operations with versioning support"""
    MODEL_ID = "us.amazon.nova-pro-v1:0"
    
    def __init__(self, logger: Optional[AppLogger] = None):
        """Initialize the lesson service with dependencies"""
        self.logger = logger or AppLogger(__name__)
        self.dynamo_manager = DynamoManager(self.logger)
        self.bedrock = self._initialize_bedrock()

    def _initialize_bedrock(self):
        """Initialize the Bedrock client with retry configuration"""
        config = Config(
            retries={'max_attempts': 3},
            read_timeout=30,
            connect_timeout=30,
            max_pool_connections=50
        )
        return boto3.client('bedrock-runtime', config=config)

    ##########
    ##########
    ##########
    async def create_lesson(self, 
                            topic: str, 
                            profile: Optional[Dict[str, Any]] = None,
                            existing_plan: Optional[str] = None, 
                            grade: Optional[str] = None,
                            subject: Optional[str] = None,
                            user_chat: Optional[str] = None) -> Dict[str, Any]:
        if not topic:
            raise ValueError("Topic is required to generate a lesson plan")
            
        try:
            parallel_service = ParallelLessonService(self.logger, self.bedrock)
            
            if existing_plan:
                existing_context = json.loads(existing_plan)
                if profile and 'studentProfile' in existing_context:
                    merged_profile = {
                        **existing_context['studentProfile'],
                        **profile
                    }
                else:
                    merged_profile = profile or existing_context.get('studentProfile')
                
                # Pass user_chat to generate_lesson_plan
                lesson_plan = await parallel_service.generate_lesson_plan(
                    topic=topic,
                    profile=merged_profile,
                    grade=grade or existing_context.get('grade'),
                    subject=subject or existing_context.get('subject'),
                    user_chat=user_chat
                )
                # Preserve any existing metadata
                if 'metadata' in existing_context:
                    lesson_plan['metadata'].update(existing_context['metadata'])
                    
            else:
                # Generate completely new lesson plan
                lesson_plan = await parallel_service.generate_lesson_plan(
                    topic=topic,
                    profile=profile,
                    grade=grade,
                    subject=subject
                )
            
            # Update metadata with correct profile information and grade
            if 'metadata' not in lesson_plan:
                lesson_plan['metadata'] = {}
                
            lesson_plan['metadata'].update({
                'profileName': profile.get('profileName') if profile else 'default',
                'grade': grade or lesson_plan['metadata'].get('grade', 'default'),
                'subject': subject or 'Mathematics'  # Use provided subject or default to Mathematics
            })
            
            # Remove deprecated profileId if it exists
            if 'profileId' in lesson_plan['metadata']:
                del lesson_plan['metadata']['profileId']
                
            # Convert student profile format if necessary
            if profile:
                lesson_plan['studentProfile'] = {
                    'profileName': profile.get('profileName', 'Custom'),
                    'adaptations': profile.get('specialConsiderations', '').split(',') if profile.get('specialConsiderations') else [],
                    'teachingStrategies': [
                        f"Math Level: {profile.get('mathAbility', '')}",
                        f"Engagement: {profile.get('engagement', '')}",
                        profile.get('generalBackground', '')
                    ] if all(key in profile for key in ['mathAbility', 'engagement', 'generalBackground']) else []
                }
                
            # Set required grade and subject fields from metadata
            lesson_plan['grade'] = lesson_plan['metadata']['grade']
            lesson_plan['subject'] = lesson_plan['metadata']['subject']
            lesson_plan['total_duration'] = self._calculate_total_duration(lesson_plan)
                
            return lesson_plan
                
        except json.JSONDecodeError as err:
            self.logger.error("Error parsing existing plan JSON: %s", str(err))
            raise ValueError(f"Invalid JSON format in existing plan: {str(err)}")
            
        except KeyError as err:
            self.logger.error("Missing required field: %s", str(err))
            raise ValueError(f"Missing required field in lesson plan: {str(err)}")
            
        except AttributeError as err:
            self.logger.error("Invalid data structure: %s", str(err))
            raise ValueError(f"Invalid data structure in lesson plan: {str(err)}")
            
        except Exception as err:
            self.logger.error("Error generating lesson plan: %s", str(err))
            raise ValueError(f"Failed to generate lesson plan: {str(err)}")

    ###############
    ###############
    ###############
    def _calculate_total_duration(self, lesson_plan: Dict[str, Any]) -> str:
        """Calculate total lesson duration from components"""
        try:
            total_minutes = 0
            lesson_flow = lesson_plan.get('lessonFlow', {})
            
            # Add up durations from each section
            if 'launch' in lesson_flow:
                launch_duration = lesson_flow['launch'].get('duration', '0')
                total_minutes += int(launch_duration.split()[0])  # Assumes format like "10 minutes"
                
            if 'explore' in lesson_flow:
                # Assuming 15 minutes per activity as default if not specified
                total_minutes += len(lesson_flow['explore'].get('activities', [])) * 15
                
            if 'discussion' in lesson_flow:
                # Estimate 5 minutes per key question
                total_minutes += len(lesson_flow['discussion'].get('keyQuestions', [])) * 5
                
            if 'closure' in lesson_flow:
                # Add 10 minutes for closure activities
                total_minutes += 10
                
            return f"{total_minutes} minutes"
        except Exception:
            return "45-60 minutes"  # Default duration if calculation fails



    def save_lesson(self, email: str, lesson_data: Dict[str, Any]) -> Dict[str, Any]:
        """Save a lesson plan with versioning support"""
        try:
            # Generate unique lesson ID if not provided
            lesson_id = lesson_data.get('lessonId', str(uuid.uuid4()))
            profile_id = str(uuid.uuid4())
            
            # Create composite subject key
            subject_key = f"{lesson_data['grade']}-{lesson_data['title']}"
            
            # Prepare item for primary lessons table
            lesson_item = {
                'email': email,
                'subject': subject_key,
                'lessonId': lesson_id,
                'title': lesson_data['title'],
                'content': lesson_data['content'],
                'grade': lesson_data['grade'],
                'original_subject': lesson_data['subject'],
                'status': lesson_data.get('status', 'draft'),
                'last_modified': datetime.utcnow().isoformat()
            }
            
            # Save to primary lessons table
            self.dynamo_manager.put_dynamo_item(
                table_name=os.environ['LESSONS_TABLE'],
                payload=lesson_item
            )
            
            # Save version
            version_item = self._save_lesson_version(
                lesson_id=lesson_id,
                profile_id=profile_id,
                lesson_data={**lesson_item, 'email': email}
            )
            
            return {**lesson_item, 'version': version_item}
            
        except Exception as err:
            self.logger.error("Error saving lesson: %s", str(err))
            raise

    def _save_lesson_version(self, lesson_id: str, profile_id: str, lesson_data: Dict[str, Any]) -> Dict[str, Any]:
        """Save a version of a lesson to the versions table"""
        try:
            # Use DynamoDB's query with both hash and range key
            table = self.dynamo_manager.dynamo_client.Table(os.environ['LESSON_VERSIONS_TABLE'])
            response = table.query(
                KeyConditionExpression=Key('lessonId').eq(lesson_id)
            )

            new_version = len(response.get('Items', [])) + 1

            print(response)
            print("new version: " +str(new_version) )
            
            # Create version item
            version_item = {
                'lessonId': lesson_id,
                'profileId': profile_id,
                'profileVersion': f"{profile_id}#v{new_version}",
                'content': lesson_data['content'],
                'title': lesson_data['title'],
                'grade': lesson_data['grade'],
                'subject': lesson_data.get('original_subject'),
                'timestamp': datetime.utcnow().isoformat(),
                'version': new_version,
                'email': lesson_data['email']
            }
            
            # Save version
            self.dynamo_manager.put_dynamo_item(
                table_name=os.environ['LESSON_VERSIONS_TABLE'],
                payload=version_item
            )
            
            return version_item
            
        except Exception as err:
            self.logger.error("Error saving lesson version: %s", str(err))
            raise

    def get_user_lessons(self, email: str) -> List[Dict[str, Any]]:
        """Retrieve all lessons for a user with their latest versions"""
        ##email field is provided from cognotio for secure access
        try:
            lessons = self.dynamo_manager.query_table(
                table_name=os.environ['LESSONS_TABLE'],
                filter_key='email',
                filter_value=email
            )
            
            # For each lesson, get its latest version
            enriched_lessons = []
            for lesson in lessons:
                latest_version = self.get_latest_version(
                    email=email,
                    lesson_id=lesson['lessonId']
                )
                
                enriched_lesson = {
                    'lessonId': lesson['lessonId'],
                    'title': lesson['title'],
                    'grade': lesson['grade'],
                    'subject': lesson.get('original_subject'),
                    'status': lesson.get('status'),
                    'lastModified': lesson.get('last_modified'),
                    'content': latest_version['content'] if latest_version else lesson['content'],
                    'currentVersion': latest_version['version'] if latest_version else 1
                }
                enriched_lessons.append(enriched_lesson)
            
            return enriched_lessons
            
        except Exception as err:
            self.logger.error("Error retrieving lessons: %s", str(err))
            raise

    def create_differentiated_lessons(self, email: str, lesson_id: str) -> List[Dict[str, Any]]:
        """Create differentiated versions of a lesson for all active profiles"""
        try:
            # Verify user has access to lesson
            lesson = self._get_lesson_by_id(email, lesson_id)
            if not lesson:
                raise ValueError(f"Lesson {lesson_id} not found or access denied")

            # Get all active profiles
            profiles = self.dynamo_manager.query_table(
                table_name=os.environ['PROFILES_TABLE'],
                filter_key='email',
                filter_value=email
            )
            active_profiles = [p for p in profiles if p.get('active', True)]

            differentiated_versions = []
            for profile in active_profiles:
                # Generate differentiated content
                differentiated_content = self.create_lesson(
                    topic=lesson['title'],
                    profile=profile,
                    existing_plan=json.dumps(lesson['content'])
                )

                # Save as new version
                version = self._save_lesson_version(
                    lesson_id=lesson_id,
                    profile_id=profile['profilename'],
                    lesson_data={
                        **lesson,
                        'content': differentiated_content,
                        'email': email
                    }
                )
                
                differentiated_versions.append(version)

            return differentiated_versions
            
        except Exception as err:
            self.logger.error("Error creating differentiated lessons: %s", str(err))
            raise

    def _get_lesson_by_id(self, email: str, lesson_id: str) -> Optional[Dict[str, Any]]:
        try:
            return self.dynamo_manager.get_dynamo_item_multi_key(
                table_name=os.environ['LESSONS_TABLE'],
                lookup_keys={
                    'email': email,
                    'lessonId': lesson_id
                }
            )
        except Exception as err:
            self.logger.error(
                "Database error retrieving lesson %s for user %s: %s",
                lesson_id, email, type(err).__name__
            )
            raise

    def get_lesson_versions(self, email: str, lesson_id: str) -> List[Dict[str, Any]]:
        """Get all versions of a lesson after verifying access"""
        try:
            # Verify access
            lesson = self._get_lesson_by_id(email, lesson_id)
            if not lesson:
                return []

            # Get all versions
            versions = self.dynamo_manager.query_table(
                table_name=os.environ['LESSON_VERSIONS_TABLE'],
                filter_key='lessonId',
                filter_value=lesson_id
            )
            
            # Sort by profile and version number
            return sorted(versions, key=lambda x: (x['profileId'], x['version']))
            
        except Exception as err:
            self.logger.error("Error retrieving lesson versions: %s", str(err))
            raise

    def get_latest_version(self, email: str, lesson_id: str, 
                        profile_id: str = 'base') -> Optional[Dict[str, Any]]:
        """Get latest version of a lesson for a specific profile"""
        try:
            versions = self.get_lesson_versions(email, lesson_id)
            profile_versions = [v for v in versions if v['profileId'] == profile_id]
            return profile_versions[-1] if profile_versions else None
        except Exception as err:
            self.logger.error("Error retrieving latest version: %s", str(err))
            raise

    def _construct_user_message(self, topic: str, profile: Optional[Dict[str, Any]], 
                            existing_plan: Optional[str]) -> Dict[str, Any]:
        """Construct the user message for the API request"""
        profile_context = self._format_profile_context(profile) if profile else ""
        existing_plan_context = f"Here is the current plan to improve: {existing_plan}" if existing_plan else ""
        
        return {
            "role": "user",
            "content": [{
                "text": f"""Create a lesson plan for the topic '{topic}'.
                {profile_context}
                {existing_plan_context}
                Ensure the response is a complete JSON object following the specified structure."""
            }]
        }

    def _format_profile_context(self, profile: Dict[str, Any]) -> str:
        """Format the profile information for the prompt"""
        return f"""
        Student Profile:
        - Demographics: {profile.get('demographics', '')}
        - Background: {profile.get('generalBackground', '')}
        - Math Ability: {profile.get('mathAbility', '')}
        - Engagement Style: {profile.get('engagement', '')}
        - Special Considerations: {profile.get('specialConsiderations', '')}
        """
    
    def get_profile_variations(self, email: str, lesson_id: str) -> List[Dict[str, Any]]:
        try:
            # Verify user has access to the lesson
            lesson = self._get_lesson_by_id(email, lesson_id)
            if not lesson:
                raise ValueError(f"Lesson {lesson_id} not found or access denied")
                
            # Query the versions table using the ProfileIndex
            table = self.dynamo_manager.dynamo_client.Table(os.environ['LESSON_VERSIONS_TABLE'])
            response = table.query(
                IndexName='ProfileIndex',##is this even defined?
                KeyConditionExpression=Key('lessonId').eq(lesson_id),
                ProjectionExpression='lessonId, profileId, version, content, title, grade, subject, timestamp'
            )
            
            if not response.get('Items'):
                return []
                
            # Process versions to get latest for each profile
            profile_versions: Dict[str, Dict[str, Any]] = {}
            for version in response['Items']:
                profile_id = version['profileId']
                current_version = version.get('version', 0)
                
                if profile_id not in profile_versions or \
                current_version > profile_versions[profile_id].get('version', 0):
                    profile_versions[profile_id] = version
            
            # Format the response
            variations = list(profile_versions.values())
            for variation in variations:
                variation['lastModified'] = variation.pop('timestamp', None)
                
            self.logger.info(f"Retrieved {len(variations)} profile variations for lesson {lesson_id}")
            return variations
            
        except ValueError as ve:
            self.logger.warning(f"Access verification failed: {str(ve)}")
            raise
        except Exception as err:
            self.logger.error(f"Error retrieving profile variations: {str(err)}")
            raise

    def get_profile_history(self, email: str, lesson_id: str, profile_id: str) -> List[Dict[str, Any]]:
        try:
            # Verify user has access to the lesson
            lesson = self._get_lesson_by_id(email, lesson_id)
            if not lesson:
                raise ValueError(f"Lesson {lesson_id} not found or access denied")
                
            # Query versions table using the ProfileIndex
            table = self.dynamo_manager.dynamo_client.Table(os.environ['LESSON_VERSIONS_TABLE'])
            response = table.query(
                IndexName='ProfileIndex',
                KeyConditionExpression=
                    Key('lessonId').eq(lesson_id) & Key('profileId').eq(profile_id),
                ProjectionExpression='lessonId, profileId, version, content, title, \
                                grade, subject, timestamp, profileVersion'
            )
            
            if not response.get('Items'):
                return []
                
            # Sort versions chronologically
            versions = sorted(
                response['Items'],
                key=lambda x: (x.get('version', 0), x.get('timestamp', ''))
            )
            
            # Format the response
            for version in versions:
                version['lastModified'] = version.pop('timestamp', None)
                # Extract version number from profileVersion if needed
                if 'profileVersion' in version:
                    version['versionLabel'] = version['profileVersion'].split('#')[1]
                
            self.logger.info(
                f"Retrieved {len(versions)} versions for profile {profile_id} \
                in lesson {lesson_id}"
            )
            return versions
            
        except ValueError as ve:
            self.logger.warning(f"Access verification failed: {str(ve)}")
            raise
        except Exception as err:
            self.logger.error(
                f"Error retrieving profile history for {profile_id}: {str(err)}"
            )
            raise