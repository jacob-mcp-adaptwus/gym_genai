from typing import Dict, Any
import json

try:
    from util.importhelper import ImportHelper
except ImportError:
    from src.util.importhelper import ImportHelper


class SystemPromptBuilder():
    """Builds system prompts for different components in chat interactions"""
    
    def __init__(self, logger=None):
        self.logger = logger  # Simply store the logger, no need for super().__init__
        self.schema = ImportHelper.get_json("schema/json/lessons/lesson.json")
    
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

    def get_standards_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """System prompt for updating educational standards"""
        return self.format_system_prompt(
            role="an educational standards specialist",
            instructions="""
            Update standards while maintaining:
            1. Grade-level alignment
            2. Topic coverage
            3. Mathematical progression
            4. Cross-cutting connections
            
            Ensure updates preserve:
            - Core mathematical concepts
            - Process standards
            - Learning progressions
            - Assessment alignment""",
            schema={component:self.schema.get(component, {})}
        )
        
    def get_pedagogical_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """System prompt for updating pedagogical context"""
        return self.format_system_prompt(
            role="a pedagogical expert",
            instructions="""
            Update pedagogical framework while maintaining:
            1. Conceptual coherence
            2. Learning progressions
            3. Student misconceptions
            4. Instructional strategies
            
            Consider:
            - Prior knowledge
            - Student background
            - Learning objectives
            - Assessment needs""",
            schema={component:self.schema.get(component, {})}
        )
        
    def get_problem_set_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """System prompt for updating problem sets"""
        return self.format_system_prompt(
            role="a mathematics education expert",
            instructions="""
            Update mathematics problems while:
            1. Using proper LaTeX notation
            2. Maintaining difficulty progression
            3. Including worked solutions
            4. Providing scaffolding
            
            Ensure:
            - Clear problem statements
            - Contextual relevance
            - Multiple approaches
            - Appropriate challenge level""",
            schema={component:self.schema.get(component, {})}
        )
        
    def get_default_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """Default system prompt for other components"""
        return self.format_system_prompt(
            role=f"an expert in {component} development",
            instructions=f"""
            Update the {component} while maintaining:
            1. Pedagogical coherence
            2. Student engagement
            3. Learning objectives
            4. Assessment alignment
            
            Consider:
            - Grade level appropriateness
            - Subject area focus
            - Student needs
            - Teaching strategies""",
            schema={component:self.schema.get(component, {})}
        )

    def get_system_prompt(self, component: str, context: Dict[str, Any]) -> Dict[str, str]:
        """Get appropriate system prompt based on component type"""
        print(f"retreiving  system prompt for component: {component}")
        if component == 'standardsAddressed':
            return self.get_standards_system_prompt(component, context)
        elif component == 'pedagogicalContext':
            return self.get_pedagogical_system_prompt(component, context)
        elif 'markupProblemSets' in component:
            return self.get_problem_set_system_prompt(component, context)
        else:
            return self.get_default_system_prompt(component, context)
