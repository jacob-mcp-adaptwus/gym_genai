# serverless-api/src/services/chat/orchestration/component_orchestrator.py
from typing import Dict, Any, Optional, List
import asyncio
import json

try:
    from services.chat.generators.chat_generator import ChatGenerator
    from services.chat.prompts.chat_prompt_builder import ChatPromptBuilder
    from util.loggers.applogger import AppLogger
    from aws.bedrockmanager import BedrockManager
except ImportError:
    from src.services.chat.generators.chat_generator import ChatGenerator
    from src.services.chat.prompts.chat_prompt_builder import ChatPromptBuilder
    from src.util.loggers.applogger import AppLogger
    from src.aws.bedrockmanager import BedrockManager

class ComponentOrchestrator:
    def __init__(self, logger: Optional[AppLogger] = None):
        """Initialize orchestrator with required dependencies"""
        self.logger = logger or AppLogger(__name__)
        self.bedrock = BedrockManager(self.logger)
        self.chat_generator = ChatGenerator(self.bedrock, self.logger)
        self.prompt_builder = ChatPromptBuilder()
        
    async def process_chat_update(self, message: str, components: List[str], current_plan: Dict[str, Any], tier: int, context: Dict[str, Any]) -> Dict[str, Any]:
        try:
            # Phase 1: Validate and prepare
            self._validate_components(components, current_plan)
            enriched_context = self._enrich_context(context, current_plan)
            
            # Phase 2: Handle foundation components
            if self._needs_foundation_update(components):
                updated_plan = await self._handle_foundation_update(message=message, current_plan=current_plan, context=enriched_context)
            else:
                updated_plan = current_plan.copy()
            
            # Phase 3: Update remaining components
            remaining = self._get_remaining_components(components)
            if remaining:
                component_updates = await self._update_components(message=message, components=remaining, current_plan=updated_plan, tier=tier, context=enriched_context)
                updated_plan.update(component_updates)
            
            return updated_plan
            
        except Exception as e:
            self.logger.error(f"Error in chat update orchestration: {str(e)}")
            raise
            
    def _validate_components(self, components: List[str], current_plan: Dict[str, Any]):
        """Validate that requested components exist in current plan"""
        for component in components:
            if component not in current_plan:
                raise ValueError(f"Component not found in lesson plan: {component}")
                
    def _enrich_context(self, context: Dict[str, Any], current_plan: Dict[str, Any]) -> Dict[str, Any]:
        """Enrich context with relevant information from current plan"""
        enriched = context.copy()
        
        # Add standards if available
        if 'standardsAddressed' in current_plan:
            enriched['standards'] = current_plan['standardsAddressed']
            
        # Add pedagogical context if available
        if 'pedagogicalContext' in current_plan:
            enriched['pedagogical'] = current_plan['pedagogicalContext']
            
        # Add objectives if available
        if 'objectives' in current_plan:
            enriched['objectives'] = current_plan['objectives']
            
        return enriched
        
    def _needs_foundation_update(self, components: List[str]) -> bool:
        """Check if foundation components need update"""
        foundation_components = {'pedagogicalContext', 'standardsAddressed'}
        return any(comp in foundation_components for comp in components)
        
    async def _handle_foundation_update(self, message: str, current_plan: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle updates to foundation components"""
        foundation_components = ['pedagogicalContext', 'standardsAddressed']
        tasks = []
        
        for component in foundation_components:
            if component in current_plan:
                task = self.chat_generator.update_component(message=message, component=component, current_content=current_plan[component], context=context)
                tasks.append((component, task))
        
        # Execute updates in parallel
        updated_plan = current_plan.copy()
        results = await asyncio.gather(*[task for _, task in tasks], return_exceptions=True)
        
        for (component, _), result in zip(tasks, results):
            if isinstance(result, Exception):
                self.logger.error(f"Error updating {component}: {str(result)}")
            else:
                updated_plan[component] = result[component]
        
        return updated_plan
        
    def _get_remaining_components(self, components: List[str]) -> List[str]:
        """Get non-foundation components that need update"""
        foundation_components = {'pedagogicalContext', 'standardsAddressed'}
        return [comp for comp in components if comp not in foundation_components]
        
    async def _update_components(self, message: str, components: List[str], current_plan: Dict[str, Any], tier: int, context: Dict[str, Any]) -> Dict[str, Any]:
        """Update specified components in parallel"""
        tasks = []
        
        for component in components:
            if component in current_plan:
                task = self.chat_generator.update_component(message=message, component=component, current_content=current_plan[component], context=context, tier=tier)
                tasks.append((component, task))
        
        # Execute updates in parallel
        updates = {}
        results = await asyncio.gather(*[task for _, task in tasks], return_exceptions=True)
        
        for (component, _), result in zip(tasks, results):
            if isinstance(result, Exception):
                self.logger.error(f"Error updating {component}: {str(result)}")
            else:
                updates[component] = result[component]
        
        return updates
        
    async def process_single_component(self, message: str, component: str, current_plan: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        try:
            self._validate_components([component], current_plan)
            enriched_context = self._enrich_context(context, current_plan)
            result = await self.chat_generator.update_component(message=message, component=component, current_content=current_plan[component], context=enriched_context)
            return result
        except Exception as e:
            self.logger.error(f"Error updating single component: {str(e)}")
            raise

    def generate_chat_response(self, updated_components: List[str]) -> str:
        try:
            component_list = ", ".join(updated_components)
            return f"I've updated the following components: {component_list}. How else can I help improve the lesson plan?"
        except Exception as e:
            self.logger.error(f"Error generating chat response: {str(e)}")
            return "I've made the requested updates. Is there anything specific you'd like me to explain or modify further?"