import json
import asyncio
from typing import Optional

try:
    from services.parallellessonservice import ParallelLessonService
    from services.messageanalysis import MessageAnalyzer
    from services.componentmanager import ComponentManager
    from aws.dynamomanager import DynamoManager
    from aws.bedrockmanager import BedrockManager
    from util.loggers.applogger import AppLogger
except ImportError:
    from src.services.parallellessonservice import ParallelLessonService
    from src.services.messageanalysis import MessageAnalyzer
    from src.services.componentmanager import ComponentManager
    from src.aws.dynamomanager import DynamoManager
    from src.aws.bedrockmanager import BedrockManager
    from src.util.loggers.applogger import AppLogger



class ChatService:
    """Service for chat-based refinements to lesson plans"""
    
    def __init__(self, logger: Optional[AppLogger] = None):
        self.logger = logger or AppLogger(__name__)
        self.dynamo = DynamoManager(self.logger)
        self.bedrock = BedrockManager(self.logger)
        self.parallel_service = ParallelLessonService(self.logger, self.bedrock)
        self.message_analyzer = MessageAnalyzer(self.bedrock)
        self.component_manager = ComponentManager(self.bedrock, self.logger)

    async def analyze_message(self, message, current_plan):
        try:
            # Parse existing plan
            self.logger.info("Parsing existing plan")
            current_plan = json.loads(current_plan)
            
            # Get current metadata
            self.logger.info("Getting metadata")
            metadata = current_plan.get('metadata', {})
            self.logger.info("Metadata: %s", json.dumps(metadata))

            # Extract core context
            self.logger.info("Extracting core context")
            initial_context = {
                "grade": metadata.get('grade', "default"),
                "subject": metadata.get('subject', "Mathematics"),
                "topic": metadata.get('topic', ""),
                "profile": current_plan.get('studentProfile', {}),
                "user_feedback": message
            }

            # Analyze message intent
            self.logger.info("Analyzing message intent")
            analysis = await self.message_analyzer.analyze_intent(
                message=message,
                current_plan=current_plan,
                context=initial_context
            )
            self.logger.info("Message analysis: %s", json.dumps(analysis))
            return analysis
        except Exception as e:
            self.logger.error(f"Error analyzing message: {str(e)}")


    async def regenerate_component(self, current_plan, component, analysis):
        ###this recieved a component and an analysis
        ###it will regenerate the component based on the analysis's intent statment
        try:
            # Parse existing plan
            current_plan = json.loads(current_plan)
            self.logger.info("current_plan: %s", json.dumps(current_plan))
            # Get current metadata
            self.logger.info("Getting metadata")
            metadata = current_plan.get('metadata', {})
            self.logger.info("Metadata: %s", json.dumps(metadata))

            self.logger.info("Regenerating component: %s", component)
            self.logger.info("analysis type: %s", type(analysis))
            if isinstance(analysis, str):
                analysis = json.loads(analysis)
            self.logger.info("parsed analysis type: %s", type(analysis))
            self.logger.info("parsed analysis content: %s", json.dumps(analysis))


            # Extract core context
            self.logger.info("Extracting core context")
            initial_context = {
                "grade": metadata.get('grade', "default"),
                "subject": metadata.get('subject', "Mathematics"),  
                "topic": metadata.get('topic', ""),
                "profile": current_plan.get('studentProfile', {}),
                "user_feedback": analysis['intent']
            }


            #i need to update the component with the new intent
            #but only an individual component at a time
            
            response = await self.component_manager.update_components(
                ###components is suposed to be a list of components
                components=[component],
                current_plan=current_plan,
                user_feedback=analysis['intent'],
                tier=0,
                context=initial_context
            )

            print(f"response from regenerate_component service: {str(response)}")


            return {
                "updatedPlan": response,  # Return the single object instead of array
                "chatResponse": "dingus",
                "updatedComponents": [component]
            }

        except Exception as err:
            self.logger.error(f"Error regenerating component: {str(err)}")
            raise ValueError(f"Failed to regenerate component: {str(err)}")
        
    ################################################
    ################################################
            
    async def process_chat(self, email, message, existing_plan, lessonId, analysis):
            try:
                # Parse existing plan
                self.logger.info("Parsing existing plan")
                current_plan = json.loads(existing_plan)
                
                # Get current metadata
                self.logger.info("Getting metadata")
                metadata = current_plan.get('metadata', {})
                self.logger.info("Metadata: %s", json.dumps(metadata))

                # Extract core context
                self.logger.info("Extracting core context")
                initial_context = {
                    "grade": metadata.get('grade', "default"),
                    "subject": metadata.get('subject', "Mathematics"),
                    "topic": metadata.get('topic', ""),
                    "profile": current_plan.get('studentProfile', {}),
                    "user_feedback": message
                }

                # Analyze message intent
                self.logger.info("Message analysis: %s", json.dumps(analysis))
                
                # Check foundation updates
                self.logger.info("Checking foundational components")
                foundational_components = {'pedagogicalContext', 'standardsAddressed'}
                needs_foundation_update = any(comp in analysis['components'] 
                                        for comp in foundational_components)
                self.logger.info("Needs foundation update: %s", needs_foundation_update)

                if needs_foundation_update:
                    # PART 1: Regenerate Foundation Components
                    initial_components = list(foundational_components)
                    initial_tasks = [
                        self.component_manager._regenerate_component(
                            component=component,
                            current_plan=current_plan,
                            user_feedback=message
                        )
                        for component in initial_components
                    ]
                    
                    # Execute parallel generation
                    self.logger.info("Executing parallel generation")
                    initial_results = await asyncio.gather(*initial_tasks, return_exceptions=True)
                    
                    # Build enriched context
                    self.logger.info("Building enriched context")
                    generation_context = {**initial_context}
                    
                    # Debug: Log initial state
                    self.logger.debug(f"Initial components to process: {initial_components}")
                    self.logger.debug(f"Initial results received: {initial_results}")
                    
                    for component, result in zip(initial_components, initial_results):
                        # Debug: Log current component processing
                        self.logger.debug(f"Processing component: {component}")
                        self.logger.debug(f"Result type: {type(result)}")
                        self.logger.debug(f"Result value: {result}")
                        
                        if isinstance(result, Exception):
                            # If regeneration failed, fall back to existing component
                            self.logger.error(f"Error regenerating {component}: {str(result)}")
                            fallback_value = current_plan.get(component, {})
                            self.logger.debug(f"Using fallback value for {component}: {fallback_value}")
                            generation_context[component] = fallback_value
                        else:
                            # Debug: Log successful component update
                            self.logger.debug(f"Successful result structure for {component}: {result.keys() if isinstance(result, dict) else 'not a dict'}")
                            try:
                                # Attempt to access the component key
                                generation_context[component] = result[component]
                                current_plan[component] = result[component]
                                self.logger.debug(f"Successfully updated {component} in context and plan")
                            except (KeyError, TypeError) as e:
                                # Handle case where result doesn't have expected structure
                                self.logger.error(f"Invalid result structure for {component}: {str(e)}")
                                self.logger.debug(f"Raw result: {result}")
                                generation_context[component] = current_plan.get(component, {})
                    
                    # Update remaining components using enriched context
                    remaining_components = [c for c in analysis['components'] 
                                        if c not in foundational_components]

                    self.logger.info("Remaining components: %s", remaining_components)
                    if remaining_components:
                        # Update other components with new context
                        updated_components = await self.component_manager.update_components(
                            components=remaining_components,
                            current_plan=current_plan,
                            user_feedback=message,
                            tier=analysis['tier'],
                            context=generation_context  # Pass enriched context
                        )
                        # Update current plan with new components
                        current_plan.update(updated_components)
                else:
                    # Standard update flow for non-foundational changes
                    updated_components = await self.component_manager.update_components(
                        components=analysis['components'],
                        current_plan=current_plan,
                        user_feedback=message,
                        tier=analysis['tier'],
                        context=initial_context
                    )
                    # Update current plan with new components
                    current_plan.update(updated_components)
                return {
                    "updatedPlan": current_plan,  # Return the single object instead of array
                    "chatResponse": "dingus",
                    "updatedComponents": analysis['components']
                }
            except Exception as e:
                self.logger.error(f"Error processing chat: {str(e)}")
                raise ValueError(f"Chat processing error: {str(e)}")