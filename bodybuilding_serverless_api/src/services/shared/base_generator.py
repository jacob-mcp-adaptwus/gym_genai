# serverless-api/src/services/shared/base_generator.py
from typing import Dict, Any, Optional, List
from abc import ABC, abstractmethod
import json
import asyncio
from concurrent.futures import ThreadPoolExecutor


try:
    from aws.bedrockmanager import BedrockManager
    from utils.loggers.applogger import AppLogger
    from bodybuilding_serverless_api.src.utils.importhelper import ImportHelper
except ImportError:
    from src.aws.bedrockmanager import BedrockManager
    from bodybuilding_serverless_api.src.utils.importhelper import ImportHelper
    from src.utils.loggers.applogger import AppLogger

class BaseGenerator(ABC):
    # Default model settings
    DEFAULT_MODEL_ID = "us.amazon.nova-pro-v1:0"
    DEFAULT_MAX_TOKENS = 3000
    DEFAULT_TEMPERATURE = 0.7
    SCHEMA = ImportHelper.get_json("schema/json/bodybuilding/bodybuilding.json")
    
    def __init__(self, bedrock_client: BedrockManager, logger: Optional[AppLogger] = None):
        self.bedrock = bedrock_client
        self.logger = logger or AppLogger(__name__)
        self.executor = ThreadPoolExecutor(max_workers=5)
        
    async def generate_with_retry(self, 
                                request_params: Dict[str, Any],
                                max_retries: int = 3,
                                retry_delay: float = 1.0) -> Dict[str, Any]:
        last_error = None
        
        for attempt in range(max_retries):
            try:
                return await self.bedrock.make_async_call(request_params)
                
            except Exception as e:
                last_error = e
                self.logger.warning(
                    f"Generation attempt {attempt + 1} failed: {str(e)}"
                )
                
                if attempt < max_retries - 1:
                    await asyncio.sleep(retry_delay * (attempt + 1))
                    
        self.logger.error(f"All generation attempts failed: {str(last_error)}")
        raise last_error
        
    def prepare_request_params(self,
                             messages: List[Dict[str, Any]],
                             system_prompt: Dict[str, str],
                             model_id: Optional[str] = None,
                             max_tokens: Optional[int] = None,
                             temperature: Optional[float] = None) -> Dict[str, Any]:
        return {
            "modelId": model_id or self.DEFAULT_MODEL_ID,
            "messages": messages,
            "system": [system_prompt],
            "inferenceConfig": {
                "maxTokens": max_tokens or self.DEFAULT_MAX_TOKENS,
                "temperature": temperature or self.DEFAULT_TEMPERATURE
            }
        }
        
    def validate_response(self, 
                         response: Dict[str, Any], 
                         required_keys: List[str]) -> bool:
        try:
            for key in required_keys:
                if key not in response:
                    self.logger.error(f"Missing required key in response: {key}")
                    return False
            return True
            
        except Exception as e:
            self.logger.error(f"Error validating response: {str(e)}")
            return False
            
    def format_system_prompt(self, 
                           role: str,
                           instructions: str,
                           examples: Optional[List[Dict[str, Any]]] = None,
                           schema: Optional[Dict[str, Any]] = None) -> Dict[str, str]:
        prompt = f"""You are {role} who responds only in RFC8259 compliant JSON.

            DO NOT include phrases like:
            - "Here is the JSON..."
            - "Certainly!"
            - "Below is..."

            {instructions}"""

        if examples:
            prompt += "\n\nExamples:\n"
            for i, example in enumerate(examples, 1):
                prompt += f"\nExample {i}:\n{json.dumps(example, indent=2)}"

        if schema:
            prompt += f"\n\nRequired JSON Schema:\n{json.dumps(schema, indent=2)}"

        return {"text": prompt}
        
    def clean_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        try:
            # Remove any null or empty string values
            cleaned = {}
            for key, value in response.items():
                if value is not None and value != "":
                    if isinstance(value, dict):
                        cleaned[key] = self.clean_response(value)
                    elif isinstance(value, list):
                        cleaned[key] = [
                            self.clean_response(item) if isinstance(item, dict) else item
                            for item in value
                            if item is not None and item != ""
                        ]
                    else:
                        cleaned[key] = value
            return cleaned
            
        except Exception as e:
            self.logger.error(f"Error cleaning response: {str(e)}")
            return response
            
    def handle_generation_error(self, 
                              error: Exception,
                              component: str,
                              context: Dict[str, Any]) -> Dict[str, Any]:
        self.logger.error(
            f"Error generating {component}: {str(error)}\n"
            f"Context: {json.dumps(context)}"
        )
        
        # Return minimal valid structure
        return {
            component: {
                "error": str(error),
                "status": "failed",
                "timestamp": self.get_timestamp()
            }
        }
        
    def get_timestamp(self) -> str:
        """Get current timestamp string"""
        from datetime import datetime
        return datetime.utcnow().isoformat()
        
    @abstractmethod
    async def generate_component(self, 
                               component: str,
                               context: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement generate_component") 