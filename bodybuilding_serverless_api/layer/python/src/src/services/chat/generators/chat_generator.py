from typing import Dict, Any, Optional
import json

try:
    from services.shared.base_generator import BaseGenerator
    from services.chat.prompts.chat_prompt_builder import ChatPromptBuilder
    from utils.loggers.applogger import AppLogger
    from aws.bedrockmanager import BedrockManager
    from services.chat.prompts.system_prompt_builder import SystemPromptBuilder
except ImportError:
    print("chat generator import error")
    from src.services.shared.base_generator import BaseGenerator
    from src.services.chat.prompts.chat_prompt_builder import ChatPromptBuilder
    from src.utils.loggers.applogger import AppLogger
    from src.aws.bedrockmanager import BedrockManager
    from src.services.chat.prompts.system_prompt_builder import SystemPromptBuilder

class ChatGenerator(BaseGenerator):
    def __init__(self, bedrock_client: BedrockManager, logger: Optional[AppLogger] = None):
        """Initialize with Bedrock client and logger"""
        super().__init__(bedrock_client, logger)
        self.prompt_builder = ChatPromptBuilder()
        self.system_prompt_builder = SystemPromptBuilder(logger)
        
    async def update_component(self, message: str, component: str, current_content: Dict[str, Any], context: Dict[str, Any], tier: int = 2) -> Dict[str, Any]:
        try:
            # Get appropriate system prompt based on component type
            system_prompt = self._get_system_prompt(component, context)
            
            # Build user message
            user_message = self._build_user_message(
                message=message,
                component=component,
                current_content=current_content,
                tier=tier
            )
            
            # Prepare request parameters
            request_params = self.prepare_request_params(
                messages=[user_message],
                system_prompt=system_prompt,
                **self._get_component_config(component, tier)
            )
            
            # Generate update with retry
            result = await self.generate_with_retry(request_params)
            
            # Validate and clean response
            if not self.validate_response(result, [component]):
                raise ValueError(f"Invalid response format for {component}")
                
            return self.clean_response(result)
            
        except Exception as e:
            return self.handle_generation_error(e, component, context)
            
    def _get_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """Get appropriate system prompt based on component type"""
        return self.system_prompt_builder.get_system_prompt(component, context)
        
    def _build_user_message(self, message: str, component: str, current_content: Dict[str, Any], tier: int) -> Dict[str, Any]:
        """Build the user message for the API request"""
        return {
            "role": "user",
            "content": [{
                "text": f"""
                Component to Update: {component}
                User Feedback: {message}
                Update Tier: {tier}
                
                Current Content:
                {json.dumps(current_content, indent=2)}
                
                Provide the updated component maintaining exact schema structure.
                Return only the {component} object.
                """
            }]
        }
        
    def _get_component_config(self, component: str, tier: int) -> Dict[str, Any]:
        """Get component-specific configuration"""
        # Base configurations for different tiers
        tier_configs = {
            1: {"temperature": 0.3, "max_tokens": 2000},  # More precise
            2: {"temperature": 0.5, "max_tokens": 3000},  # Balanced
            3: {"temperature": 0.7, "max_tokens": 4000}   # More creative
        }
        
        # Component-specific adjustments
        component_adjustments = {
            'trainingContext': {"temperature": -0.2},  # More precise
            'workoutRoutines': {"temperature": 0.1, "max_tokens": 4000},  # More detailed
            'nutritionPlan': {"max_tokens": 3500},  # Detailed meal plans
            'supplementation': {"temperature": -0.1},  # More conservative
            'fitnessGoals': {"temperature": -0.1},  # More precise
            'progressMetrics': {"temperature": -0.2},  # Very precise
            'recoveryProtocol': {"max_tokens": 2500},  # Standard length
            'adaptations': {"temperature": 0.1}  # More creative
        }
        
        # Get base config for tier
        config = tier_configs.get(tier, tier_configs[2])
        
        # Apply component-specific adjustments
        if component in component_adjustments:
            for key, adjustment in component_adjustments[component].items():
                if key == "temperature":
                    config[key] = max(0.1, min(1.0, config[key] + adjustment))
                else:
                    config[key] += adjustment
                    
        return config
        
    async def generate_component(self, component: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Implementation of abstract method from BaseGenerator"""
        # This method is required by BaseGenerator but not used in chat context
        raise NotImplementedError("Use update_component for chat-based generation") 