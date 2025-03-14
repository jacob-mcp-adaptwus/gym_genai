import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, Any, Optional
import json
from datetime import datetime
try:
    from src.util.importhelper import ImportHelper
except ImportError:
    from util.importhelper import ImportHelper

class ParallelLessonService:
    MODEL_ID = "us.amazon.nova-pro-v1:0" 
    SCHEMA = ImportHelper.get_json("schema/json/lessons/lesson.json")

    def __init__(self, logger, bedrock_client):
        self.logger = logger
        self.bedrock = bedrock_client
        self.executor = ThreadPoolExecutor(max_workers=5)

    def _get_component_schema(self, component: str) -> Dict:
        """Get schema for a specific component"""
        return self.SCHEMA[component]
    
    def _get_problem_set_system_prompt(self, grade: str = None, subject: str = None, component: str = None) -> Dict[str, str]:
        problem_sets_schema = self.SCHEMA[component]
        # Define the example JSON separately with proper escaping
        example_json = '''{
            "type": "practice",
            "difficulty": 3,
            "problem": {
                "stem": "Solve the equation: $\\\\frac{x^2 + 1}{x - 2} = 4$ for $x \\\\neq 2$",
                "context": "This rational equation appears when analyzing the limit: $\\\\lim_{x \\\\to 2} \\\\frac{x^2 + 1}{x - 2}$"
            },
            "solution": {
                "answer": "$x = 3$ or $x = -1$",
                "workingOut": [
                    "1. Multiply both sides by $(x-2)$: $x^2 + 1 = 4(x-2)$",
                    "2. Expand: $x^2 + 1 = 4x - 8$",
                    "3. Rearrange: $x^2 - 4x + 9 = 0$",
                    "4. Solve quadratic: $x = \\\\frac{4 \\\\pm \\\\sqrt{16-36}}{2}$"
                ]
            },
            "hints": [
                {
                    "text": "First clear the fraction by multiplying both sides by $(x-2)$",
                    "scaffold": "Remember: $\\\\frac{a}{b} \\\\cdot b = a$"
                }
            ]
        }'''

        return {
            "text": f"""
            You are an expert mathematics education content creator specializing in {grade or 'default'} {subject or 'Mathematics'}.
            Create clear, engaging problems using LaTeX math notation between single $ delimiters for inline math and double $$ for display math.

            LaTeX Formatting Rules:
            - Use single $ for inline math: "Find $x$ when $2x + 3 = 11$"
            - Use double $$ for displayed equations: "$$\\\\frac{{dy}}{{dx}} = 2x + 1$$"
            - Use proper LaTeX commands: \\\\sqrt{{}}, \\\\frac{{}}{{}}, \\\\pi, etc.
            - Escape special characters: Use {{}} for grouping

            Example Problem:
            ```json
            {example_json}
            ```
            
            Expected JSON response Structure:
            {json.dumps(problem_sets_schema, indent=2)}
            """
        }

    def _get_pedagogical_system_prompt(self, grade: str = None, subject: str = None, component_schema: Dict = None) -> Dict[str, str]:
        """Get system prompt for pedagogical framework with grade and subject alignment"""
        return {
            "text": f"""
            You are an PHD with 24 years of experience and educational agent specializing in differentiated instruction who only reponds in RFC8259 compliant JSON.
            Follow these principles:
            1. All content must align with grade-level standards while providing multiple entry points
            2. Include specific supports for diverse learners (ELL, gifted, struggling, spectrum)
            3. Ensure cognitive and linguistic scaffolding in all components
            4. Maintain coherence between objectives, activities, and assessments
            5. Include formative assessment opportunities throughout

            You must ensure all content is developmentally appropriate for grade level {grade or 'default'} 
            and aligns with typical {subject or 'Mathematics'} standards and practices.

            6. respond with  a  RFC8259 compliant JSON follwing this format without deviation :
            {json.dumps(component_schema )}
            """
        }
    
    def _get_educational_standards_system_prompt(self, grade: str = None, subject: str = None, component_schema: Dict = None) -> Dict[str, str]:
        """Get system prompt for educational standards generation."""
        return {
            "text": f"""You are an educational standards specialist focusing on grade {grade} {subject or 'Mathematics'}.
            IMPORTANT: You are mathtilda who focuses on  inclusive and equitable educational standards, must ONLY output a pure RFC8259 compliant JSON object with no additional text, preamble, or explanation.
            
            DO NOT include phrases like:
            - "Here is the JSON..."
            - "Certainly!"
            - "Below is..."
            
            ONLY output the raw JSON object following this exact schema:
            {json.dumps(component_schema, indent=2)}

            Guidelines:
            - Primary standards: Core learning objectives based on  the topic, grade never let bias or personal feelings influence the standards
            - Secondary standards: Supporting concepts
            - Generate inclusive and equitable educational standards

            Example response from grade 2 fractions:
            {{
                "standardsAddressed": {{
                    "focalStandard": [
                        "2.NF.1: Partition circles and rectangles into equal shares",
                        "2.NF.2:  comparing fractions with different numerators and denominators"
                    ],
                    "supportingStandards": [
                        "2.G.3: Partition shapes into equal parts"
                    ]
                }}
            }}

            Required schema:
            {json.dumps(component_schema, indent=2)}
            """
        }

    async def _generate_component(self, component: str, topic: str, context: Dict, profile: Optional[Dict]) -> Dict[str, Any]:
        """Generate a specific lesson plan component with appropriate system prompt"""
        
        if component == 'standardsAddressed':
            request_params = {
                "modelId": self.MODEL_ID,
                "messages": [{
                    "role": "user",
                    "content": [{
                        "text": f"""Please mathtilda we need your help, Generate  inclusive and equitable educational standards for:
                        Topic: {topic}
                        Grade: {context.get('grade')}
                        Subject: {context.get('subject')}
                        
                        Return ONLY a JSON object with this exact structure:
                        {{
                            "standardsAddressed": {{
                                "focalStandard": ["string"],
                                "supportingStandards": ["string"]
                            }}
                        }}"""
                    }]
                }],
                "system": [self._get_educational_standards_system_prompt(
                    grade=context.get('grade'),
                    subject=context.get('subject'),
                    component_schema=self._get_component_schema(component)
                )],
                "inferenceConfig": {
                    "maxTokens": 1000,
                    "temperature": 0.1
                }
            }
            result = await self._make_bedrock_call(request_params)
            
            # Validate and restructure response if needed
            if 'standardsAddressed' not in result:
                if 'focalStandard' in result and 'supportingStandards' in result:
                    result = {'standardsAddressed': result}
                else:
                    raise ValueError("Invalid standards response structure")
            
            return result
        else:
            # Select appropriate system prompt based on component
            if component in ['markupProblemSets', 'markupProblemSetsAboveGradeLevel', 'markupProblemSetsBelowGradeLevel']:
                system_prompt = self._get_problem_set_system_prompt(
                    grade=context.get('grade'),
                    subject=context.get('subject'),
                    component=component
                )
            else:
                system_prompt = self._get_pedagogical_system_prompt(
                    grade=context.get('grade'),
                    subject=context.get('subject'),
                    component_schema=self._get_component_schema(component)
                )

            # Configure the API request for Bedrock model inference
            request_params = {
                # Specify which Anthropic Claude model to use
                "modelId": self.MODEL_ID,
                
                # Structure the conversation with a clear user prompt
                "messages": [{
                    "role": "user",
                    "content": [{
                        # Format a detailed prompt that:
                        # 1. Clearly states what component needs to be generated
                        # 2. Provides essential context (topic, grade, subject)
                        # 3. Includes full context and profile data for personalization
                        # 4. Explicitly requests RFC8259 compliant JSON
                        # 5. Provides the exact schema to follow
                        "text": f"""
                        Create {component} for:
                        Topic: {topic}
                        Grade Level: {context.get('grade', 'default')}
                        Subject: {context.get('subject', 'Mathematics')}
                        Context: {json.dumps(context)}
                        Profile: {json.dumps(profile) if profile and component != 'standardsAddressed' else 'default'}
                        Use this RFC8259 compliant JSON as a response
                        {json.dumps({component: self._get_component_schema(component)}, indent=2)}
                        """
                    }]

                }],
                
                # Include the component-specific system prompt that defines:
                # - The AI's role and expertise
                # - Content generation guidelines
                # - Required format and structure
                "system": [system_prompt],
                
                # Configure generation parameters:
                # - maxTokens: Allow for detailed, comprehensive responses
                # - temperature: Balance creativity with consistency (0.7 is moderately creative)
                "inferenceConfig": {
                    "maxTokens": 4000,
                    "temperature": 0.7
                }
            }
            
            result = await self._make_bedrock_call(request_params)
            # Validate response has expected component
            if component not in result:
                raise ValueError(f"Generated content missing '{component}' key")
            return result

    async def generate_lesson_plan(self, topic: str, profile: Optional[Dict] = None,
                                grade: Optional[str] = None, 
                                subject: Optional[str] = None,
                                user_chat: Optional[str] = None) -> Dict[str, Any]:
            """
            Generates a complete lesson plan by orchestrating parallel generation of components.
            Uses a three-part workflow to ensure pedagogical coherence and standards alignment.
            """
            try:
                #############################################################
                # PART 1: Initial Setup and Context Creation
                # This section establishes the foundational context needed for generation.
                # We create a base context that will be enriched with standards and 
                # pedagogical insights in parallel processing.
                #############################################################
                
                initial_context = {
                    "grade": grade or "default",
                    "subject": subject or "Mathematics",
                    "topic": topic,
                    "profile": profile,
                    "user_feedback": user_chat  # Add user feedback to context
                }
                
                #############################################################
                # PART 2: Parallel Generation of Foundation Components
                # Here we generate pedagogicalContext and standardsAddressed in parallel
                # because:
                # 1. These components are independent of each other
                # 2. They form the foundation for other components
                # 3. Running them in parallel improves performance
                # 4. Both need the same initial context but don't depend on each other
                #############################################################
                
                # Define components for parallel generation
                initial_components = ['pedagogicalContext', 'standardsAddressed']
                initial_tasks = [
                    self._generate_component(component, topic, initial_context, profile)
                    for component in initial_components
                ]
                
                # Execute parallel generation
                initial_results = await asyncio.gather(*initial_tasks, return_exceptions=True)
                
                # Process results and build enriched context
                generation_context = {**initial_context}
                for component, result in zip(initial_components, initial_results):
                    if isinstance(result, Exception):
                        self.logger.error(f"Error generating {component}: {str(result)}")
                        generation_context[component] = self._get_component_schema(component)
                    else:
                        generation_context[component] = result[component]
                
                
                #############################################################
                # PART 3: Parallel Generation of Lesson Components
                # Now that we have the foundational context established, we can
                # generate the rest of the components in parallel because:
                # 1. Each component uses the same enriched context
                # 2. Components are independent but aligned through the context
                # 3. Parallel generation significantly reduces total generation time
                #############################################################
                
                # Define main components for parallel generation
                components = ['objectives', 'lessonFlow', 'markupProblemSets', 'markupProblemSetsAboveGradeLevel', 'markupProblemSetsBelowGradeLevel', 'assessments', 'accessibility']
                tasks = [
                    self._generate_component(
                        component, 
                        topic, 
                        {**generation_context, "user_feedback": user_chat}, 
                        profile
                    )
                    for component in components
                ]
                
                # Execute parallel generation of main components
                results = await asyncio.gather(*tasks, return_exceptions=True)
                
                # Assemble the final plan with metadata
                assembled_plan = {
                    "metadata": {
                        "topic": topic,
                        "grade": grade or "default",
                        "subject": subject or "Mathematics",
                        "lastModified": datetime.utcnow().isoformat(),
                        "profileId": profile.get("profileId") if profile else "default",
                        "standardsAddressed": generation_context.get('standardsAddressed', {
                            "focal": [],
                            "supporting": []
                        })
                    },
                    # Include foundation components
                    "pedagogicalContext": generation_context.get('pedagogicalContext', {})
                }
                
                # Add generated components to final plan
                for component, result in zip(components, results):
                    if isinstance(result, Exception):
                        self.logger.error(f"Error generating {component}: {str(result)}")
                        assembled_plan[component] = self._get_component_schema(component)
                    else:
                        assembled_plan[component] = result[component]
                
                return assembled_plan
                
            except Exception as e:
                self.logger.error(f"Error in lesson generation: {str(e)}")
                raise

    async def _make_bedrock_call(self, request_params: Dict) -> Dict[str, Any]:
        """Make async call to Bedrock"""
        try:
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                self.executor,
                lambda: self.bedrock.converse(**request_params)
            )
            content = response["output"]["message"]["content"][0]["text"]
            cleaned_content = self._clean_json_string(content)
            return json.loads(cleaned_content)
                
        except Exception as e:
            self.logger.error(f"Bedrock API error: {str(e)}")
            self.logger.error(f"Failed to parse response into JSON. Raw content: {content}")
            self.logger.error(f"Request params: {str(request_params)}")

    def _clean_json_string(self, content: str) -> str:
        """Remove markdown JSON code block markers if present."""
        # Remove ```json from start and ``` from end if they exist
        content = content.strip()
        if content.startswith('```json'):
            content = content[7:]  # Remove ```json
        elif content.startswith('```'):
            content = content[3:]  # Remove ```
        if content.endswith('```'):
            content = content[:-3]  # Remove trailing ```
        return content