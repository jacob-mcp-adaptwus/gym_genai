from typing import Optional
import boto3
import os
import sys
import inspect

# Add the parent directory to the Python path to enable imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)  # services dir -> src dir
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# Directory of this lambda function: /var/task/src/services
try:
    # First try relative imports (for local development)
    from .plan_service import PlanService
    from .chat_service import ChatService
    from .progress_service import ProgressService
    from ..aws.bedrockmanager import BedrockManager
except ImportError:
    try:
        print("service factory import error, trying absolute imports")
        from src.services.plan_service import PlanService
        from src.services.chat_service import ChatService
        from src.services.progress_service import ProgressService
        from src.aws.bedrockmanager import BedrockManager
    except ImportError:
        # Fallback to direct imports (for when imported from handlers)
        print("service factory import error, using fallback imports")
        from services.plan_service import PlanService
        from services.chat_service import ChatService
        from services.progress_service import ProgressService
        from aws.bedrockmanager import BedrockManager





class ServiceFactory:
    _instance: Optional['ServiceFactory'] = None
    
    def __init__(self):
        # Initialize AWS clients
        self.dynamodb = boto3.client('dynamodb')
        self.bedrock_manager = BedrockManager()
        
        # Initialize services
        self._plan_service = None
        self._chat_service = None
        self._progress_service = None

    @classmethod
    def get_instance(cls) -> 'ServiceFactory':
        """
        Get or create the singleton instance of ServiceFactory.
        """
        if cls._instance is None:
            cls._instance = ServiceFactory()
        return cls._instance

    @property
    def plan_service(self) -> PlanService:
        """
        Get the PlanService instance.
        """
        if self._plan_service is None:
            self._plan_service = PlanService(
                dynamodb_client=self.dynamodb,
                bedrock_manager=self.bedrock_manager
            )
        return self._plan_service

    @property
    def chat_service(self) -> ChatService:
        """
        Get the ChatService instance.
        """
        if self._chat_service is None:
            self._chat_service = ChatService(
                bedrock_manager=self.bedrock_manager,
                plan_service=self.plan_service,
                dynamodb_client=self.dynamodb
            )
        return self._chat_service

    @property
    def progress_service(self) -> ProgressService:
        """
        Get the ProgressService instance.
        """
        if self._progress_service is None:
            self._progress_service = ProgressService(
                dynamodb_client=self.dynamodb,
                plan_service=self.plan_service
            )
        return self._progress_service

    def reset(self) -> None:
        """
        Reset all service instances.
        Useful for testing or when needing to recreate services with new configurations.
        """
        self._plan_service = None
        self._chat_service = None
        self._progress_service = None 