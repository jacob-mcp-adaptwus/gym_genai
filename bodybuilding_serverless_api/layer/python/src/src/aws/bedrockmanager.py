"""Class to handle all Amazon Bedrock operations for the bodybuilding app"""
import json
import asyncio
from typing import Dict, Any, Optional, List
import boto3
from botocore.config import Config

class BedrockManager:
    """Bedrock manager for handling AI operations in the bodybuilding app"""

    def __init__(self, logger):
        """Initialize Bedrock manager with logger and client"""
        self.logger = logger
        self.bedrock = self._initialize_bedrock()
        self.executor = None
        self.model_id = "anthropic.claude-3-sonnet-20240229-v1:0"  # Updated to Claude 3 Sonnet

    def _initialize_bedrock(self):
        """Initialize Bedrock client with optimized configuration"""
        config = Config(
            retries={'max_attempts': 3},
            read_timeout=30,
            connect_timeout=30,
            max_pool_connections=50
        )
        return boto3.client('bedrock-runtime', config=config)

    def set_model(self, model_id: str):
        """Set the model ID to use for inference"""
        self.model_id = model_id
        self.logger.info(f"Set Bedrock model to: {model_id}")

    async def generate_workout_plan(self, user_profile: Dict, prompt: str) -> Dict[str, Any]:
        """Generate a workout plan based on user profile and prompt"""
        request_params = self._build_request_params(
            prompt=prompt,
            context={"user_profile": user_profile},
            temperature=0.7
        )
        return await self.make_async_call(request_params)

    async def analyze_progress(self, workout_history: Dict, metrics: Dict) -> Dict[str, Any]:
        """Analyze user's workout progress and provide recommendations"""
        request_params = self._build_request_params(
            prompt="Analyze workout progress and provide recommendations",
            context={
                "workout_history": workout_history,
                "metrics": metrics
            },
            temperature=0.3
        )
        return await self.make_async_call(request_params)

    async def make_async_call(self, request_params: Dict) -> Dict[str, Any]:
        """Make asynchronous call to Bedrock"""
        try:
            loop = asyncio.get_event_loop()
            
            if 'messages' in request_params:
                # Use converse API for chat-based interactions
                response = await loop.run_in_executor(
                    self.executor,
                    lambda: self.bedrock.converse(**request_params)
                )
                content = response["output"]["message"]["content"][0]["text"]
            else:
                # Use invoke_model for traditional completions
                response = await loop.run_in_executor(
                    self.executor,
                    lambda: self.bedrock.invoke_model(**request_params)
                )
                response_body = json.loads(response['body'].read())
                content = response_body.get('completion') or response_body.get('text')
            
            if not content:
                raise ValueError("No content in response")
                
            cleaned_content = self._clean_json_string(content)
            return json.loads(cleaned_content)
                
        except Exception as e:
            self.logger.error(f"Bedrock API error: {str(e)}")
            self.logger.error(f"Request params: {json.dumps({k: v for k, v in request_params.items() if k != 'body'}, indent=2)}")
            raise

    def make_sync_call(self, request_params: Dict) -> Dict[str, Any]:
        """Make synchronous call to Bedrock"""
        try:
            if 'messages' in request_params:
                # Use converse API for chat-based interactions
                response = self.bedrock.converse(**request_params)
                content = response["output"]["message"]["content"][0]["text"]
            else:
                # Use invoke_model for traditional completions
                response = self.bedrock.invoke_model(**request_params)
                response_body = json.loads(response['body'].read())
                content = response_body.get('completion') or response_body.get('text')
            
            if not content:
                raise ValueError("No content in response")
                
            cleaned_content = self._clean_json_string(content)
            return json.loads(cleaned_content)
                
        except Exception as e:
            self.logger.error(f"Bedrock API error: {str(e)}")
            self.logger.error(f"Request params: {json.dumps({k: v for k, v in request_params.items() if k != 'body'}, indent=2)}")
            raise

    def prepare_request_params(self, messages: List[Dict], system_prompt: Dict, temperature: float = 0.7, max_tokens: int = 4096) -> Dict:
        """Prepare request parameters for converse API"""
        return {
            "modelId": self.model_id,
            "messages": messages,
            "system": system_prompt,
            "anthropicVersion": "bedrock-2023-05-31",
            "maxTokens": max_tokens,
            "temperature": temperature,
            "topP": 0.9
        }

    def _build_request_params(
        self, 
        prompt: str, 
        context: Optional[Dict] = None, 
        temperature: float = 0.7
    ) -> Dict:
        """Build request parameters for Bedrock API call"""
        body = {
            "prompt": prompt,
            "max_tokens_to_sample": 4096,
            "temperature": temperature,
            "top_p": 0.9,
        }

        if context:
            body["context"] = context

        return {
            "modelId": self.model_id,
            "body": json.dumps(body),
            "contentType": "application/json",
            "accept": "application/json",
        }

    def _clean_json_string(self, content: str) -> str:
        """Clean and validate JSON string from response"""
        content = content.strip()
        
        # Remove markdown code block markers if present
        if content.startswith('```json'):
            content = content[7:]
        elif content.startswith('```'):
            content = content[3:]
        if content.endswith('```'):
            content = content[:-3]
            
        content = content.strip()
        
        # Validate JSON structure
        try:
            json.loads(content)
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in response: {str(e)}")
            self.logger.error(f"Content: {content}")
            raise
            
        return content 