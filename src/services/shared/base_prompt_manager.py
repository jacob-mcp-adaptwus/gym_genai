from typing import Dict, Any, Optional

class BasePromptManager:
    def __init__(self):
        self.prompts: Dict[str, str] = {}
        self.context: Dict[str, Any] = {}

    def add_prompt(self, key: str, prompt: str) -> None:
        """Add a prompt template to the manager."""
        self.prompts[key] = prompt

    def get_prompt(self, key: str) -> Optional[str]:
        """Get a prompt template by key."""
        return self.prompts.get(key)

    def set_context(self, key: str, value: Any) -> None:
        """Set context value for prompt formatting."""
        self.context[key] = value

    def format_prompt(self, key: str, **kwargs) -> Optional[str]:
        """Format a prompt template with given kwargs and stored context."""
        prompt = self.get_prompt(key)
        if prompt is None:
            return None
        
        # Combine stored context with provided kwargs
        format_args = {**self.context, **kwargs}
        try:
            return prompt.format(**format_args)
        except KeyError as e:
            raise KeyError(f"Missing required prompt variable: {e}")
        except Exception as e:
            raise Exception(f"Error formatting prompt: {e}")

    def clear_context(self) -> None:
        """Clear all stored context values."""
        self.context.clear() 