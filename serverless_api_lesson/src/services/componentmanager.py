import json
from typing import Dict, Any, Optional
import asyncio
try:
    from services.parallellessonservice import ParallelLessonService
    from util.loggers.applogger import AppLogger
except ImportError:
    from src.services.parallellessonservice import ParallelLessonService
    from src.util.loggers.applogger import AppLogger

class ComponentManager:
    """Manages updates to lesson plan components"""
    
    def __init__(self, bedrock_client, logger: Optional[AppLogger] = None):
        self.bedrock = bedrock_client
        self.logger = logger or AppLogger(__name__)

    def _get_regenerate_system_prompt(self, component: str, current_plan: Dict, context: Dict) -> Dict[str, str]:
        return {
            "text": f"""You are an PHD expert lesson component generator who responds only in RFC8259 compliant JSON.

                DO NOT include phrases like:
                - "Here is the JSON..."
                - "Certainly!"
                - "Below is..."


                Only respond with the JSON object, nothing else.

                Task: Regenerate the {component} section based on user feedback while maintaining schema compliance.

                Current Component:
                {json.dumps(current_plan[component], indent=2)}

                Context:
                {json.dumps(context if context else {}, indent=2)}

                Requirements:
                1. Maintain exact schema structure
                2. Incorporate user feedback
                3. Ensure pedagogical soundness
                4. Return only the {component} object"""
        }

    def _get_update_system_prompt(self, component: str, current_plan: Dict, context: Dict) -> Dict[str, str]:
        return {
            "text": f"""
                You are an PHD expert machine lesson component generator who responds only in RFC8259 compliant JSON.
                respond only is json format, nothing else.
                DO NOT include phrases like:
                - "Here is the JSON..."
                - "Certainly!"
                - "Below is...

                becasue you only repsond in Json format, nothing else.

                Profile of the student json:
                {json.dumps(context if context else {})}

                this is the users plan that need to be considered for update: 
                {json.dumps(current_plan[component])}

                Requirements:
                4. Schema of the component that need to be considered for update: 
                  {json.dumps(ParallelLessonService.SCHEMA[component])} 

                return the modified object in RFC8259 compliant JSON besed on feedback,profile and schema:"""
        }

    async def update_components(self, components, current_plan, user_feedback, tier, context):
        """Update components in parallel"""
        updated_plan = current_plan.copy()
        update_tasks = []
        for component in components:
            task = self._update_component(component, current_plan, user_feedback, context)
            update_tasks.append(task)
        results = await asyncio.gather(*update_tasks, return_exceptions=True)

        print(f"results from update_components 196 service: {str(results)}")
        for component, result in zip(components, results):
            if isinstance(result, Exception):
                self.logger.error(f"Error updating {component}: {str(result)}")
                continue
            updated_plan[component] = result
        return updated_plan
    
    async def _regenerate_component(self, component, current_plan, user_feedback, context=None):
        request_params = {
            "modelId": ParallelLessonService.MODEL_ID,
            "messages": [{
                "role": "user",
                "content": [{
                    "text": (
                        f"This is the= User's Feedback: {user_feedback}"
                        "Respond with a RFC8259 compliant JSON following this format without deviation:"
                        f"{json.dumps(ParallelLessonService.SCHEMA[component])}"
                    )
                }]
            }],
            "system": [self._get_regenerate_system_prompt(component, current_plan, context)],
            "inferenceConfig": {
                "maxTokens": 4000,
                "temperature": 0.6
            }
        }
        self.logger.info(f"regenerating entire component with this bedrock request: {str(request_params)}")
        return await self._make_bedrock_call(request_params)

    async def _update_component(self, component, current_plan, user_feedback, context=None):
        request_params = {
            "modelId": ParallelLessonService.MODEL_ID,
            "messages": [{
                "role": "user",
                "content": [{
                    "text": (
                        f"User Feedback: {user_feedback}\n\n"
                        f"Update {component} section while preserving structure. "
                        "Respond with a RFC8259 compliant JSON following this format without deviation:\n"
                        f"{json.dumps(ParallelLessonService.SCHEMA[component], indent=2)}"
                    )
                }]
            }],
            "system": [self._get_update_system_prompt(component, current_plan, context)],
            "inferenceConfig": {
                "maxTokens": 4000,
                "temperature": 0.7
            }
        }
        self.logger.info(f"updating component with this bedrock request: {str(request_params)}")
        return await self._make_bedrock_call(request_params)

    async def _make_bedrock_call(self, request_params: Dict) -> Dict[str, Any]:
        """Make async call to Bedrock with error handling"""
        try:
            return await self.bedrock.make_async_call(request_params)
        except Exception as e:
            self.logger.error(f"Bedrock API error: {str(e)}")
            raise ValueError(f"Error in Bedrock API call: {str(e)}")