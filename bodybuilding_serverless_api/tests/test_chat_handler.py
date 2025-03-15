import json
import unittest
from unittest.mock import patch, MagicMock

from src.handlers.chat_handler import chat_with_coach, get_chat_history


class TestChatHandler(unittest.TestCase):
    """Test cases for the chat handler functions"""

    def setUp(self):
        """Set up test fixtures"""
        self.user_id = "test-user-123"
        self.plan_id = "test-plan-456"
        
        # Mock event with authorization context
        self.event_base = {
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": self.user_id
                    }
                }
            }
        }

    @patch('src.handlers.chat_handler.plan_orchestrator')
    @patch('src.handlers.chat_handler.validate_request')
    def test_chat_with_coach_success(self, mock_validate, mock_orchestrator):
        """Test successful chat message processing"""
        # Arrange
        message = "How should I adjust my workout for a shoulder injury?"
        chat_data = {
            "planId": self.plan_id,
            "message": message,
            "context": {
                "injury": "shoulder",
                "severity": "mild"
            }
        }
        
        event = {
            **self.event_base,
            "body": json.dumps(chat_data)
        }
        
        expected_result = {
            "messageId": "msg-123",
            "planId": self.plan_id,
            "userId": self.user_id,
            "message": message,
            "response": "I recommend avoiding overhead presses and focusing on...",
            "timestamp": "2023-01-01T00:00:00Z",
            "planUpdates": {
                "workoutRoutines": {
                    "modified": True
                }
            }
        }
        
        mock_orchestrator.process_message.return_value = expected_result
        
        # Act
        response = chat_with_coach(event, {})
        
        # Assert
        mock_validate.assert_called_once_with(chat_data, 'chat_message')
        mock_orchestrator.process_message.assert_called_once_with(
            user_id=self.user_id,
            plan_id=self.plan_id,
            message=message,
            context=chat_data.get('context', {})
        )
        
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(json.loads(response['body']), expected_result)

    @patch('src.handlers.chat_handler.plan_orchestrator')
    def test_get_chat_history_success(self, mock_orchestrator):
        """Test successful retrieval of chat history"""
        # Arrange
        event = {
            **self.event_base,
            "pathParameters": {
                "planId": self.plan_id
            }
        }
        
        expected_result = {
            "messages": [
                {
                    "messageId": "msg-123",
                    "planId": self.plan_id,
                    "userId": self.user_id,
                    "message": "How should I adjust my workout for a shoulder injury?",
                    "response": "I recommend avoiding overhead presses and focusing on...",
                    "timestamp": "2023-01-01T00:00:00Z"
                },
                {
                    "messageId": "msg-124",
                    "planId": self.plan_id,
                    "userId": self.user_id,
                    "message": "What about cardio options?",
                    "response": "For cardio with a shoulder injury, I suggest...",
                    "timestamp": "2023-01-01T00:05:00Z"
                }
            ],
            "totalMessages": 2
        }
        
        mock_orchestrator.get_chat_history.return_value = expected_result
        
        # Act
        response = get_chat_history(event, {})
        
        # Assert
        mock_orchestrator.get_chat_history.assert_called_once_with(
            user_id=self.user_id,
            plan_id=self.plan_id
        )
        
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(json.loads(response['body']), expected_result)

    @patch('src.handlers.chat_handler.plan_orchestrator')
    @patch('src.handlers.chat_handler.validate_request')
    def test_chat_with_coach_error(self, mock_validate, mock_orchestrator):
        """Test error handling in chat handler"""
        # Arrange
        message = "How should I adjust my workout for a shoulder injury?"
        chat_data = {
            "planId": self.plan_id,
            "message": message
        }
        
        event = {
            **self.event_base,
            "body": json.dumps(chat_data)
        }
        
        error_message = "Failed to process message"
        mock_orchestrator.process_message.side_effect = Exception(error_message)
        
        # Act
        response = chat_with_coach(event, {})
        
        # Assert
        self.assertEqual(response['statusCode'], 500)
        self.assertEqual(json.loads(response['body'])['error'], error_message)

    @patch('src.handlers.chat_handler.plan_orchestrator')
    def test_get_chat_history_error(self, mock_orchestrator):
        """Test error handling in get chat history handler"""
        # Arrange
        event = {
            **self.event_base,
            "pathParameters": {
                "planId": self.plan_id
            }
        }
        
        error_message = "Failed to retrieve chat history"
        mock_orchestrator.get_chat_history.side_effect = Exception(error_message)
        
        # Act
        response = get_chat_history(event, {})
        
        # Assert
        self.assertEqual(response['statusCode'], 500)
        self.assertEqual(json.loads(response['body'])['error'], error_message)


if __name__ == '__main__':
    unittest.main() 