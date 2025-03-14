from typing import Dict, Any
import json

try:
    from utils.importhelper import ImportHelper
except ImportError:
    from src.utils.importhelper import ImportHelper


class SystemPromptBuilder():
    """Builds system prompts for different components in chat interactions"""
    
    def __init__(self, logger=None):
        self.logger = logger
        self.schema = ImportHelper.get_json("schema/json/plans/plan.json")
    
    def format_system_prompt(self, role: str, instructions: str, schema: Dict[str, Any]) -> Dict[str, str]:
        """Format a system prompt with role, instructions and schema"""
        return {
            "text": f"""You are {role}.

            {instructions}

            Required JSON Schema:
            {json.dumps(schema, indent=2)}

            Return only the updated component matching the exact schema structure.
            Ensure RFC8259 compliance."""
        }

    def get_training_context_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """System prompt for updating training context"""
        return self.format_system_prompt(
            role="an expert strength and conditioning coach",
            instructions="""
            Update training context while maintaining:
            1. Experience level assessment
            2. Equipment requirements
            3. Time constraints
            4. Physical limitations
            
            Ensure updates consider:
            - Current fitness level
            - Training history
            - Recovery capacity
            - Available resources""",
            schema={component:self.schema.get(component, {})}
        )
        
    def get_fitness_goals_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """System prompt for updating fitness goals"""
        return self.format_system_prompt(
            role="a professional bodybuilding coach",
            instructions="""
            Update fitness goals while maintaining:
            1. Specific targets
            2. Measurable metrics
            3. Achievable timelines
            4. Progressive milestones
            
            Consider:
            - Current capabilities
            - Realistic progression
            - Individual limitations
            - Long-term vision""",
            schema={component:self.schema.get(component, {})}
        )
        
    def get_workout_routines_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """System prompt for updating workout routines"""
        return self.format_system_prompt(
            role="an expert exercise programmer",
            instructions="""
            Update workout routines while:
            1. Following proper exercise selection
            2. Managing volume and intensity
            3. Structuring training splits
            4. Planning progression
            
            Ensure:
            - Movement pattern balance
            - Recovery management
            - Progressive overload
            - Exercise technique focus""",
            schema={component:self.schema.get(component, {})}
        )
        
    def get_nutrition_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """System prompt for updating nutrition plans"""
        return self.format_system_prompt(
            role="a sports nutrition specialist",
            instructions="""
            Update nutrition plan while maintaining:
            1. Macronutrient ratios
            2. Meal timing
            3. Food quality
            4. Supplement integration
            
            Consider:
            - Training demands
            - Recovery needs
            - Individual preferences
            - Practical implementation""",
            schema={component:self.schema.get(component, {})}
        )
        
    def get_progress_metrics_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """System prompt for updating progress metrics"""
        return self.format_system_prompt(
            role="a performance tracking specialist",
            instructions="""
            Update progress metrics while maintaining:
            1. Performance measurements
            2. Body composition tracking
            3. Recovery monitoring
            4. Progress evaluation
            
            Ensure:
            - Objective measures
            - Consistent tracking
            - Meaningful metrics
            - Actionable insights""",
            schema={component:self.schema.get(component, {})}
        )
        
    def get_supplementation_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """System prompt for updating supplementation protocols"""
        return self.format_system_prompt(
            role="a sports supplementation expert",
            instructions="""
            Update supplementation protocol while:
            1. Following safety guidelines
            2. Optimizing timing
            3. Managing dosages
            4. Integrating with nutrition
            
            Consider:
            - Essential needs
            - Performance goals
            - Individual response
            - Cost effectiveness""",
            schema={component:self.schema.get(component, {})}
        )
        
    def get_recovery_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """System prompt for updating recovery protocols"""
        return self.format_system_prompt(
            role="a recovery and regeneration specialist",
            instructions="""
            Update recovery protocol while focusing on:
            1. Rest optimization
            2. Recovery techniques
            3. Stress management
            4. Adaptation monitoring
            
            Ensure:
            - Sleep quality
            - Active recovery
            - Injury prevention
            - Mental recovery""",
            schema={component:self.schema.get(component, {})}
        )
        
    def get_adaptations_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """System prompt for updating program adaptations"""
        return self.format_system_prompt(
            role="a program optimization specialist",
            instructions="""
            Update program adaptations while:
            1. Managing progression
            2. Adjusting volume
            3. Modifying intensity
            4. Optimizing frequency
            
            Consider:
            - Individual response
            - Recovery capacity
            - Performance trends
            - Goal alignment""",
            schema={component:self.schema.get(component, {})}
        )
        
    def get_default_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """Default system prompt for other components"""
        return self.format_system_prompt(
            role=f"a fitness programming specialist",
            instructions=f"""
            Update the {component} while maintaining:
            1. Program coherence
            2. Individual focus
            3. Goal alignment
            4. Safety considerations
            
            Consider:
            - Experience level
            - Available resources
            - Time constraints
            - Personal limitations""",
            schema={component:self.schema.get(component, {})}
        )

    def get_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """Get appropriate system prompt based on component type"""
        component_prompts = {
            'trainingContext': self.get_training_context_system_prompt,
            'fitnessGoals': self.get_fitness_goals_system_prompt,
            'workoutRoutines': self.get_workout_routines_system_prompt,
            'nutritionPlan': self.get_nutrition_system_prompt,
            'progressMetrics': self.get_progress_metrics_system_prompt,
            'supplementation': self.get_supplementation_system_prompt,
            'recoveryProtocol': self.get_recovery_system_prompt,
            'adaptations': self.get_adaptations_system_prompt
        }
        
        prompt_function = component_prompts.get(component, self.get_default_system_prompt)
        return prompt_function(component, context) 