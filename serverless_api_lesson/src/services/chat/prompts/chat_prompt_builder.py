# serverless-api/src/services/chat/prompts/chat_prompt_builder.py
from typing import Dict, Any, Optional, List
import json

try:
    from services.shared.base_prompt_manager import BasePromptManager
    from util.importhelper import ImportHelper
    from util.loggers.applogger import AppLogger
except ImportError:
    from src.services.shared.base_prompt_manager import BasePromptManager
    from src.util.importhelper import ImportHelper
    from src.util.loggers.applogger import AppLogger

class ChatPromptBuilder(BasePromptManager):
    def __init__(self, logger: Optional[AppLogger] = None):
        super().__init__(logger)
        self.schema = ImportHelper.get_json("schema/json/lessons/lesson.json")
        self.chat_templates = ImportHelper.get_json("schema/json/prompts/chat.json")
        
    def build_component_prompt(self, component: str, context: Dict[str, Any]) -> str:
        """Implementation of abstract method from BasePromptManager"""
        # Get appropriate template and build prompt
        template = self._get_component_template(component)
        prompt = self._apply_template(template, context)
        schema = self._get_component_schema(component)
        
        return f"""{prompt}

        Required JSON Schema:
        {json.dumps(schema, indent=2)}

        Ensure RFC8259 compliance and exact schema match."""
        
    def build_analysis_prompt(self, message: str, context: Dict[str, Any]) -> str:
        """Build prompt for analyzing chat message intent"""
        return f"""Analyze this feedback for a {context.get('grade')} {context.get('subject')} lesson:

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
            'markupProblemSetsBelowGradeLevel': self._get_problem_sets_template(),
            'markupProblemSetsAboveGradeLevel': self._get_problem_sets_template(),
            'standardsAddressed': self._get_standards_template(),
            'pedagogicalContext': self._get_pedagogical_template(),
            'objectives': self._get_objectives_template(),
            'lessonFlow': self._get_lesson_flow_template(),
            'markupProblemSets': self._get_problem_sets_template(),
            'assessments': self._get_assessments_template(),
            'accessibility': self._get_accessibility_template()
        }
        
        if component not in templates:
            self.logger.error(f"No specific template found for component: {component}. Using default template.")
            # Could also raise an exception here if you want to fail fast:
            # raise ValueError(f"No template defined for component: {component}")
        
        return templates.get(component, self._get_default_template())
        
    def _get_standards_template(self) -> str:
        """Template for standards updates"""
        return """Review and update standards for {grade} {subject} ensuring:
            1. Core Standards:
            - Main topic coverage
            - Grade-level alignment
            - Mathematical practices
            
            2. Supporting Standards:
            - Prerequisite skills
            - Related concepts
            - Cross-cutting connections
            
            Current Standards:
            {current_content}

            User Feedback:
            {message}

            Maintain standards format and provide rationale for changes."""
        
    def _get_pedagogical_template(self) -> str:
        """Template for pedagogical context updates"""
        return """Update pedagogical framework for {grade} {subject} considering:
        1. Big Ideas:
        - Core concepts
        - Essential questions
        - Mathematical connections
        
        2. Prerequisites:
        - Required knowledge
        - Foundational skills
        - Prior learning
        
        3. Misconceptions:
        - Common errors
        - Student challenges
        - Addressing strategies
        
        Current Framework:
        {current_content}

        User Feedback:
        {message}

        Ensure coherence with existing lesson structure."""
        
    def _get_objectives_template(self) -> str:
        """Template for objectives updates"""
        return """Revise learning objectives for {grade} {subject} addressing:
        1. Content Objectives:
        - Mathematical understanding
        - Skill development
        - Problem-solving
        
        2. Language Objectives:
        - Mathematical vocabulary
        - Communication skills
        - Discourse practices
        
        3. Success Criteria:
        - Observable outcomes
        - Assessment alignment
        - Progress indicators
        
        Current Objectives:
        {current_content}

        User Feedback:
        {message}

        Maintain clear, measurable objectives."""
        
    def _get_lesson_flow_template(self) -> str:
        """Template for lesson flow updates"""
        return """Update lesson flow for {grade} {subject} focusing on:
        1. Launch Phase:
        - Engagement strategies
        - Prior knowledge
        - Purpose setting
        
        2. Explore Phase:
        - Student activities
        - Differentiation
        - Grouping strategies
        
        3. Discussion Phase:
        - Key questions
        - Student discourse
        - Mathematical reasoning
        
        4. Closure Phase:
        - Summary strategies
        - Assessment connection
        - Next steps
        
        Current Flow:
        {current_content}

        User Feedback:
        {message}

        Maintain instructional coherence."""
        
    def _get_problem_sets_template(self) -> str:
        """Template for problem sets updates"""
        return """Revise mathematics problems for {grade} {subject} ensuring:
        1. Problem Structure:
        - Clear statements
        - Appropriate context
        - Multiple approaches
        
        2. Solution Support:
        - Detailed solutions
        - Step-by-step work
        - Visual supports
        
        3. Scaffolding:
        - Entry points
        - Hint progression
        - Extension options
        
        Current Problems:
        {current_content}

        User Feedback:
        {message}

Use proper LaTeX notation and maintain difficulty progression."""
        
    def _get_assessments_template(self) -> str:
        """Template for assessment updates"""
        return """Update assessment components for {grade} {subject} addressing:
        1. Formative Assessment:
        - Check points
        - Progress monitoring
        - Feedback loops
        
        2. Summative Tasks:
        - Performance measures
        - Understanding checks
        - Application tasks
        
        3. Success Criteria:
        - Clear expectations
        - Scoring guides
        - Feedback methods
        
        Current Assessments:
        {current_content}

        User Feedback:
        {message}

        Align with objectives and standards."""
        
    def _get_accessibility_template(self) -> str:
        """Template for accessibility updates"""
        return """Enhance accessibility features for {grade} {subject} considering:
        1. Language Support:
        - Vocabulary scaffolds
        - Sentence frames
        - Comprehension aids

        2. Visual Support:
        - Representations
        - Models
        - Organizational aids

        3. Learning Support:
        - Differentiation
        - Modifications
        - Accommodations

        Current Supports:
        {current_content}

        User Feedback:
        {message}

        Address diverse learning needs."""
        
    def _get_default_template(self) -> str:
        """Default template for other components"""
        return """Update {component} for {grade} {subject} based on:
        1. Current Content:
        {current_content}

        2. User Feedback:
        {message}

        3. Context:
        - Grade Level: {grade}
        - Subject Area: {subject}
        - Student Needs: {profile}

        Maintain component structure and pedagogical alignment."""
        
    def _get_update_template(self, component: str, tier: int) -> str:
        """Get update template based on component and tier"""
        base_template = self._get_component_template(component)
        
        tier_guidance = {
            1: "Make minimal, focused changes while preserving core structure.",
            2: "Update content while maintaining overall approach.",
            3: "Significantly revise while ensuring pedagogical coherence."
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
            # Fall back to basic prompt if template fails
            return f"Update {context.get('component', 'component')} based on: {context.get('message', '')}"