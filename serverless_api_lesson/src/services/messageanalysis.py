import json
from typing import Dict, Any

try:
    from services.parallellessonservice import ParallelLessonService
    from util.loggers.applogger import AppLogger
except ImportError:
    from src.services.parallellessonservice import ParallelLessonService
    from src.util.loggers.applogger import AppLogger

class MessageAnalyzer:
    
    def __init__(self, bedrock_client):
        """Initialize with bedrock client."""
        self.bedrock = bedrock_client
        self.logger = AppLogger(__name__)  # Add logger for error handling

    def _get_intent_analysis_system_prompt(self) -> Dict[str, str]:
        """Get system prompt for intent analysis with proper JSON formatting."""
        return {
            "text": """
                You are Tilly, a friendly PHD expert education assistant who responds only in RFC8259 compliant JSON.
                You understand how lesson components work together and help teachers improve their lessons efficiently.

                DO NOT include phrases like:
                - "Here is the JSON..."
                - "Certainly!"
                - "Below is..."
                
                Component Dependencies:
                Foundation Components (changes affect everything):
                * standardsAddressed
                * pedagogicalContext
                
                Dependent Components:
                * objectives
                * lessonFlow
                * assessments
                * markupProblemSets
                * accessibility
                * materials

                Response Format:
                {
                    "components": ["affected components"],
                    "intent": "brief action description this is what gets passed to the component manager to understand  user feedback, make intent specfic to users needs",
                    "tier": "numeric tier (1-3)",
                    "rationale": "brief, friendly explanation will be read by user in chat",
                    "requires_foundation_update": boolean
                }

                Example 1: intent is what get passed to the component manager to understand  user feedback, make intent specfic to users needs
                User: I need to update the lesson plan to address fractional standards better
                {
                    "components": ["standardsAddressed", "objectives", "assessments", "markupProblemSets", "lessonFlow", "materials", "accessibility"],
                    "intent": " align with grade levelfraction standards, to help the student understand fractions better",
                    "tier": 1,
                    "rationale": "Hey ! Since we're updating core standards, we'll need to adjust all related materials to match.",
                    "requires_foundation_update": true
                }

                Example 2:
                User: I need to add some additional problems to the problem set
                {
                    "components": ["markupProblemSets"],
                    "intent": "add more practice problems by adding more problems sets and mixing things up",
                    "tier": 2,
                    "rationale": "I'll help you expand the problems sets, by adding more problems and mixing it up.",
                    "requires_foundation_update": false
                }

                Example 3:
                User: I want to only change objectives to focus on fractions
                {
                    "components": ["objectives"],
                    "intent": "user only want to change objectives to focus on fractions",
                    "tier": 2,
                    "rationale": "I'll help you only change the objectivea, but understand other components should reflect this change",
                    "requires_foundation_update": false
                }



            """
        }

    async def analyze_intent(self, message: str, current_plan: Dict[str, Any], 
                            context: Dict[str, Any]) -> Dict[str, Any]:
        request_params = {
            "modelId": ParallelLessonService.MODEL_ID,
            "messages": [{
                "role": "user",
                "content": [{
                    "text": f"""Analyze this user feedback considering the full context:

                        User Message: {message}

                        Context:
                        Grade: {context.get('grade', 'default')}
                        Subject: {context.get('subject', 'Mathematics')}
                        Topic: {context.get('topic', '')}
                        Profile: {json.dumps(context.get('profile', {}))}

                        Current Plan Structure:
                        {json.dumps(current_plan, indent=2)}"""
                }]
            }],
            "system": [self._get_intent_analysis_system_prompt()],
            "inferenceConfig": {
                "maxTokens": 4000,
                "temperature": 0.2
            }
        }
        response = await self.bedrock.make_async_call(request_params)
        return response
