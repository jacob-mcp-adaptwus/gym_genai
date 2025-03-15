from typing import Dict, Any, List
from datetime import datetime
import json
from util.loggers.applogger import AppLogger

# Create a logger instance
logger = AppLogger(__name__)


class ChatService:
    def __init__(self, bedrock_manager, plan_service, dynamodb_client):
        self.bedrock_manager = bedrock_manager
        self.plan_service = plan_service
        self.dynamodb_client = dynamodb_client
        self.chat_history_table = "bodybuilding-chat-history"

    async def process_message(self, user_id: str, plan_id: str, message: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Process a user message and generate an appropriate response.
        """
        # Get the current plan
        plan = await self.plan_service.get_plan(plan_id, user_id)
        if not plan:
            raise ValueError(f"Plan {plan_id} not found")

        # Get chat history
        chat_history = await self._get_chat_history(plan_id)

        # Prepare the context for the AI
        ai_context = {
            "current_plan": plan,
            "chat_history": chat_history,
            "user_context": context or {},
            "message_type": self._analyze_message_type(message)
        }

        # Generate AI response
        response = await self._generate_response(message, ai_context)

        # Save chat history
        await self._save_chat_message(plan_id, user_id, message, response)

        # If the response includes plan updates, apply them
        if response.get("plan_updates"):
            await self.plan_service.update_plan(
                plan_id,
                user_id,
                response["plan_updates"]
            )

        return response

    def _analyze_message_type(self, message: str) -> str:
        """
        Analyze the type of message to determine appropriate response strategy.
        """
        message = message.lower()
        if any(word in message for word in ["modify", "change", "update", "adjust"]):
            return "modification_request"
        elif any(word in message for word in ["explain", "why", "how", "what"]):
            return "explanation_request"
        elif any(word in message for word in ["progress", "track", "log"]):
            return "progress_related"
        return "general_query"

    async def _generate_response(self, message: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate an AI response based on the message and context.
        """
        # Construct the prompt based on message type and context
        prompt = self._build_prompt(message, context)

        # Get response from Bedrock
        ai_response = await self.bedrock_manager.generate_response(prompt)

        # Parse and structure the response
        structured_response = {
            "message": ai_response.get("message", ""),
            "plan_updates": ai_response.get("plan_updates"),
            "suggested_actions": ai_response.get("suggested_actions", [])
        }

        return structured_response

    async def _get_chat_history(self, plan_id: str) -> List[Dict[str, Any]]:
        """
        Retrieve chat history for a specific plan.
        """
        response = await self.dynamodb_client.query(
            TableName=self.chat_history_table,
            KeyConditionExpression="plan_id = :pid",
            ExpressionAttributeValues={":pid": {"S": plan_id}}
        )
        return response.get("Items", [])

    async def _save_chat_message(self, plan_id: str, user_id: str, message: str, response: Dict[str, Any]) -> None:
        """
        Save a chat message and its response to the history.
        """
        timestamp = datetime.utcnow().isoformat()
        chat_entry = {
            "plan_id": plan_id,
            "user_id": user_id,
            "timestamp": timestamp,
            "message": message,
            "response": response,
            "message_id": f"{plan_id}-{timestamp}"
        }
        
        await self.dynamodb_client.put_item(
            TableName=self.chat_history_table,
            Item=chat_entry
        )

    def _build_prompt(self, message: str, context: Dict[str, Any]) -> str:
        """
        Build a prompt for the AI based on the message and context.
        """
        message_type = context["message_type"]
        current_plan = context["current_plan"]
        
        prompt = f"""As a professional fitness and bodybuilding coach, respond to the following message:

User's current plan:
- Goals: {', '.join(current_plan['goals'])}
- Experience Level: {current_plan['experience_level']}
- Available Days: {', '.join(current_plan['available_days'])}

User's message: {message}

Message type: {message_type}

Provide a response that includes:
1. A direct answer to the user's query
2. Any necessary modifications to their workout plan
3. Suggested actions they should take

Format your response as a JSON object with 'message', 'plan_updates', and 'suggested_actions' fields."""

        return prompt 