# serverless-api/src/services/shared/base_prompt_manager.py
from typing import Dict, Any, Optional, List
from abc import ABC, abstractmethod

try:
    from util.loggers.applogger import AppLogger
except ImportError:
    from src.util.loggers.applogger import AppLogger

class BasePromptManager(ABC):
    def __init__(self, logger: Optional[AppLogger] = None):
        self.logger = logger or AppLogger(__name__)
        
    def format_prompt(self, template: str, context: Dict[str, Any]) -> str:
        try:
            # Replace placeholders with context values
            formatted = template
            for key, value in context.items():
                placeholder = f"{{{key}}}"
                if placeholder in formatted:
                    formatted = formatted.replace(placeholder, str(value))
                    
            # Clean up any remaining placeholders
            formatted = self._clean_unmatched_placeholders(formatted)
            
            return formatted.strip()
            
        except Exception as e:
            self.logger.error(f"Error formatting prompt: {str(e)}")
            return template
            
    def build_list_section(self, items: List[str], prefix: str = "- ") -> str:
        if not items:
            return ""
            
        return "\n".join(f"{prefix}{item}" for item in items)
        
    def format_json_example(self, example: Dict[str, Any], indent: int = 2) -> str:
        try:
            import json
            return json.dumps(example, indent=indent)
        except Exception as e:
            self.logger.error(f"Error formatting JSON example: {str(e)}")
            return str(example)
            
    def format_constraints(self, constraints: List[str]) -> str:
        if not constraints:
            return ""
            
        return "Requirements:\n" + self.build_list_section(constraints)
        
    def format_examples(self, examples: List[Dict[str, Any]]) -> str:
        if not examples:
            return ""
            
        formatted_examples = []
        for i, example in enumerate(examples, 1):
            formatted = f"Example {i}:"
            if "input" in example:
                formatted += f"\nInput: {example['input']}"
            if "output" in example:
                formatted += f"\nOutput: {self.format_json_example(example['output'])}"
            if "explanation" in example:
                formatted += f"\nExplanation: {example['explanation']}"
            formatted_examples.append(formatted)
            
        return "\n\n".join(formatted_examples)
        
    def clean_text(self, text: str) -> str:
        # Remove extra whitespace
        cleaned = " ".join(text.split())
        # Normalize newlines
        cleaned = cleaned.replace("\r\n", "\n").replace("\r", "\n")
        # Remove duplicate newlines
        while "\n\n\n" in cleaned:
            cleaned = cleaned.replace("\n\n\n", "\n\n")
        return cleaned.strip()
        
    def format_error_message(self, error: Exception) -> str:
        return f"Error ({type(error).__name__}): {str(error)}"
        
    def _clean_unmatched_placeholders(self, text: str) -> str:
        import re
        # Find all remaining {placeholder} patterns
        placeholders = re.findall(r'{[^}]+}', text)
        
        # Replace each unmatched placeholder
        for placeholder in placeholders:
            # Convert placeholder like {someVar} to someVar
            var_name = placeholder[1:-1]
            text = text.replace(placeholder, f"[{var_name}]")
            
        return text
        
    @abstractmethod
    def build_component_prompt(self, component: str, context: Dict[str, Any]) -> str:
        raise NotImplementedError("Subclasses must implement build_component_prompt")