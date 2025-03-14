# pylint: disable=C0301
"""Class to handle all calls with Amazon Bedrock"""
import json
import asyncio
from typing import Dict, Any
import boto3
from botocore.config import Config

try:
    from src.util.importhelper import ImportHelper
except ImportError:
    from util.importhelper import ImportHelper

class BedrockManager:
    """Bedrock manager for handling API calls and response processing"""

    def __init__(self, logger):
        """Initialize Bedrock manager with logger and client"""
        self.logger = logger
        self.bedrock = self._initialize_bedrock()
        self.executor = None  # Can be set later if needed for async operations

    def _initialize_bedrock(self):
        """Initialize Bedrock client with retry configuration."""
        config = Config(
            retries={'max_attempts': 3},
            read_timeout=30,
            connect_timeout=30,
            max_pool_connections=50
        )
        return boto3.client('bedrock-runtime', config=config)

    async def make_async_call(self, request_params: Dict) -> Dict[str, Any]:
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
            self.logger.error(f"Failed to parse response. Raw content: {content if 'content' in locals() else 'No content'}")
            self.logger.error(f"Request params: {str(request_params)}")
            raise

    def make_sync_call(self, request_params: Dict) -> Dict[str, Any]:
        """Make synchronous call to Bedrock"""
        try:
            response = self.bedrock.converse(**request_params)
            content = response["output"]["message"]["content"][0]["text"]
            cleaned_content = self._clean_json_string(content)
            return json.loads(cleaned_content)
                
        except Exception as e:
            self.logger.error(f"Bedrock API error: {str(e)}")
            self.logger.error(f"Failed to parse response. Raw content: {content if 'content' in locals() else 'No content'}")
            self.logger.error(f"Request params: {str(request_params)}")
            raise

    def _clean_json_string(self, content: str) -> str:
        """Remove markdown JSON code block markers if present."""
        content = content.strip()
        if content.startswith('```json'):
            content = content[7:]  # Remove ```json
        elif content.startswith('```'):
            content = content[3:]  # Remove ```
        if content.endswith('```'):
            content = content[:-3]  # Remove trailing ```
        return content