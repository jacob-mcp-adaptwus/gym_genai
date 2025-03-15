from typing import Dict, Any, Optional, List
import json

try:
    from services.shared.base_prompt_manager import BasePromptManager
    from utils.importhelper import ImportHelper
    from utils.loggers.applogger import AppLogger
except ImportError:
    from src.services.shared.base_prompt_manager import BasePromptManager
    from src.utils.importhelper import ImportHelper
    from src.utils.loggers.applogger import AppLogger

class ChatPromptBuilder(BasePromptManager):
    def __init__(self, logger: Optional[AppLogger] = None):
        super().__init__(logger)
        self.schema = ImportHelper.get_json("schema/json/plans/plan.json")
        self.chat_templates = ImportHelper.get_json("schema/json/prompts/chat.json")
        
    def build_component_prompt(self, component: str, context: Dict[str, Any]) -> str:
        """Implementation of abstract method from BasePromptManager"""
        template = self._get_component_template(component)
        prompt = self._apply_template(template, context)
        schema = self._get_component_schema(component)
        
        return f"""{prompt}

        Required JSON Schema:
        {json.dumps(schema, indent=2)}

        Ensure RFC8259 compliance and exact schema match."""
        
    def build_analysis_prompt(self, message: str, context: Dict[str, Any]) -> str:
        """Build prompt for analyzing chat message intent"""
        return f"""Analyze this feedback for a {context.get('experience_level')} {context.get('goal')} training plan:

        User Message: {message}

        Consider:
        1. Components affected
        2. Update priority (tier 1-3)
        3. Required changes
        4. Dependencies

        Return JSON with:
        {{
            "components": ["affected components"],
            "tier": "numeric 1-3",
            "intent": "clear action description",
            "requires_foundation_update": boolean
        }}"""
        
    def build_update_prompt(self, 
                          message: str,
                          component: str,
                          current_content: Dict[str, Any],
                          tier: int) -> str:
        """Build prompt for updating a specific component"""
        template = self._get_update_template(component, tier)
        context = {
            "message": message,
            "component": component,
            "current_content": json.dumps(current_content, indent=2),
            "tier": tier
        }
        
        return self._apply_template(template, context)
        
    def _get_component_template(self, component: str) -> str:
        """Get appropriate template for component type"""
        templates = {
            'trainingContext': self._get_training_context_template(),
            'fitnessGoals': self._get_fitness_goals_template(),
            'workoutRoutines': self._get_workout_routines_template(),
            'nutritionPlan': self._get_nutrition_template(),
            'progressMetrics': self._get_progress_metrics_template(),
            'supplementation': self._get_supplementation_template(),
            'recoveryProtocol': self._get_recovery_template(),
            'adaptations': self._get_adaptations_template()
        }
        
        if component not in templates:
            self.logger.error(f"No specific template found for component: {component}. Using default template.")
        
        return templates.get(component, self._get_default_template())
        
    def _get_training_context_template(self) -> str:
        """Template for training context updates"""
        return """Review and update training context ensuring:
            1. Core Training Factors:
            - Experience level assessment
            - Available equipment
            - Time constraints
            
            2. Physical Considerations:
            - Current fitness level
            - Injury history
            - Movement limitations
            
            Current Context:
            {current_content}

            User Feedback:
            {message}

            Maintain format and provide rationale for changes."""
        
    def _get_fitness_goals_template(self) -> str:
        """Template for fitness goals updates"""
        return """Update fitness goals framework considering:
        1. Primary Goals:
        - Strength targets
        - Physique objectives
        - Performance metrics
        
        2. Timeline:
        - Short-term milestones
        - Long-term vision
        - Progress checkpoints
        
        3. Constraints:
        - Recovery capacity
        - Time availability
        - Equipment access
        
        Current Goals:
        {current_content}

        User Feedback:
        {message}

        Ensure goals are specific, measurable, and achievable."""
        
    def _get_workout_routines_template(self) -> str:
        """Template for workout routines updates"""
        return """Revise workout routines addressing:
        1. Exercise Selection:
        - Movement patterns
        - Equipment requirements
        - Progressive overload
        
        2. Volume and Intensity:
        - Sets and reps
        - Rest periods
        - Load progression
        
        3. Training Split:
        - Frequency
        - Exercise order
        - Recovery windows
        
        Current Routines:
        {current_content}

        User Feedback:
        {message}

        Maintain clear, executable workout structure."""
        
    def _get_nutrition_template(self) -> str:
        """Template for nutrition plan updates"""
        return """Update nutrition plan focusing on:
        1. Macronutrient Distribution:
        - Protein requirements
        - Carbohydrate timing
        - Fat sources
        
        2. Meal Timing:
        - Pre-workout nutrition
        - Post-workout recovery
        - Daily meal structure
        
        3. Food Selection:
        - Quality sources
        - Portion control
        - Supplement integration
        
        Current Plan:
        {current_content}

        User Feedback:
        {message}

        Maintain nutritional coherence."""
        
    def _get_progress_metrics_template(self) -> str:
        """Template for progress metrics updates"""
        return """Revise progress tracking metrics ensuring:
        1. Performance Metrics:
        - Strength progression
        - Volume tracking
        - Work capacity
        
        2. Body Composition:
        - Weight trends
        - Measurements
        - Visual progress
        
        3. Recovery Markers:
        - Sleep quality
        - Fatigue levels
        - Injury prevention
        
        Current Metrics:
        {current_content}

        User Feedback:
        {message}

        Use proper measurement standards and maintain tracking consistency."""
        
    def _get_supplementation_template(self) -> str:
        """Template for supplementation updates"""
        return """Update supplementation protocol addressing:
        1. Core Supplements:
        - Essential nutrients
        - Performance aids
        - Recovery support
        
        2. Timing Protocol:
        - Pre-workout timing
        - Post-workout window
        - Daily scheduling
        
        3. Dosage Guidelines:
        - Recommended amounts
        - Cycling protocols
        - Safety considerations
        
        Current Protocol:
        {current_content}

        User Feedback:
        {message}

        Align with goals and ensure safety."""
        
    def _get_recovery_template(self) -> str:
        """Template for recovery protocol updates"""
        return """Enhance recovery protocol considering:
        1. Rest Strategies:
        - Sleep optimization
        - Active recovery
        - Deload planning

        2. Recovery Techniques:
        - Mobility work
        - Stress management
        - Therapeutic methods

        3. Monitoring:
        - Recovery markers
        - Fatigue management
        - Adaptation signs

        Current Protocol:
        {current_content}

        User Feedback:
        {message}

        Address recovery needs comprehensively."""
        
    def _get_adaptations_template(self) -> str:
        """Template for adaptations updates"""
        return """Update program adaptations considering:
        1. Progress Adjustments:
        - Load progression
        - Volume manipulation
        - Exercise variation
        
        2. Recovery Modifications:
        - Deload timing
        - Volume reduction
        - Intensity management
        
        3. Individual Response:
        - Fatigue management
        - Injury prevention
        - Performance optimization
        
        Current Adaptations:
        {current_content}

        User Feedback:
        {message}

        Maintain program effectiveness."""
        
    def _get_default_template(self) -> str:
        """Default template for other components"""
        return """Update {component} for {experience_level} trainee with {goal} goals based on:
        1. Current Content:
        {current_content}

        2. User Feedback:
        {message}

        3. Context:
        - Experience Level: {experience_level}
        - Primary Goal: {goal}
        - Individual Needs: {profile}

        Maintain component structure and training alignment."""
        
    def _get_update_template(self, component: str, tier: int) -> str:
        """Get update template based on component and tier"""
        base_template = self._get_component_template(component)
        
        tier_guidance = {
            1: "Make minimal, focused changes while preserving core structure.",
            2: "Update content while maintaining overall approach.",
            3: "Significantly revise while ensuring training coherence."
        }
        
        return f"""{base_template} Update Tier {tier}: {tier_guidance.get(tier)}"""
        
    def _get_component_schema(self, component: str) -> Dict[str, Any]:
        """Get schema for specific component"""
        if component in self.schema:
            return {component: self.schema[component]}
        else:
            self.logger.warning(f"Schema not found for component: {component}")
            return {component: {}}
        
    def _apply_template(self, template: str, context: Dict[str, Any]) -> str:
        """Apply context to template with error handling"""
        try:
            # Format template with context
            formatted = self.format_prompt(template, context)
            
            # Clean up and validate
            cleaned = self.clean_text(formatted)
            
            return cleaned
            
        except Exception as e:
            self.logger.error(f"Error applying template: {str(e)}")
            return f"Update {context.get('component', 'component')} based on: {context.get('message', '')}" 