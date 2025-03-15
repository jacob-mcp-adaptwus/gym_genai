import json
import unittest
from unittest.mock import patch, MagicMock

from src.handlers.user_handler import create_user, update_user, get_user


class TestUserHandler(unittest.TestCase):
    """Test cases for the user handler functions"""

    def setUp(self):
        """Set up test fixtures"""
        self.user_id = "test-user-123"
        
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

    @patch('src.handlers.user_handler.DYNAMO_MANAGER')
    def test_create_user_success(self, mock_dynamo):
        """Test successful user creation"""
        # Arrange
        user_data = {
            "name": "John Doe",
            "age": 30,
            "height": 180,
            "weight": 85,
            "fitnessGoals": ["Muscle gain", "Weight loss"],
            "experienceLevel": "Intermediate",
            "preferredWorkoutDays": ["Monday", "Wednesday", "Friday"]
        }
        
        event = {
            **self.event_base,
            "body": json.dumps(user_data)
        }
        
        expected_result = {
            "userId": self.user_id,
            "name": user_data["name"],
            "age": user_data["age"],
            "height": user_data["height"],
            "weight": user_data["weight"],
            "fitnessGoals": user_data["fitnessGoals"],
            "experienceLevel": user_data["experienceLevel"],
            "preferredWorkoutDays": user_data["preferredWorkoutDays"],
            "createdAt": "2023-01-01T00:00:00Z"
        }
        
        mock_dynamo.put_item.return_value = expected_result
        
        # Act
        response = create_user(event, {})
        
        # Assert
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(json.loads(response['body']), expected_result)
        
        # Verify DynamoDB interaction
        mock_dynamo.put_item.assert_called_once()
        # We can't check the exact arguments since they include timestamps
        # but we can verify the table name and key fields
        call_args = mock_dynamo.put_item.call_args[0][0]
        self.assertIn('users', call_args.lower())  # Table name should contain 'users'
        
        item = mock_dynamo.put_item.call_args[0][1]
        self.assertEqual(item['userId'], self.user_id)
        self.assertEqual(item['name'], user_data['name'])
        self.assertEqual(item['age'], user_data['age'])

    @patch('src.handlers.user_handler.DYNAMO_MANAGER')
    def test_update_user_success(self, mock_dynamo):
        """Test successful user update"""
        # Arrange
        user_data = {
            "name": "John Doe Updated",
            "weight": 82,
            "fitnessGoals": ["Muscle gain", "Endurance"],
            "injuries": ["Mild shoulder pain"]
        }
        
        event = {
            **self.event_base,
            "body": json.dumps(user_data)
        }
        
        # Mock the get_item to return existing user
        existing_user = {
            "userId": self.user_id,
            "name": "John Doe",
            "age": 30,
            "height": 180,
            "weight": 85,
            "fitnessGoals": ["Muscle gain", "Weight loss"],
            "experienceLevel": "Intermediate",
            "preferredWorkoutDays": ["Monday", "Wednesday", "Friday"],
            "createdAt": "2023-01-01T00:00:00Z"
        }
        
        expected_result = {
            **existing_user,
            "name": user_data["name"],
            "weight": user_data["weight"],
            "fitnessGoals": user_data["fitnessGoals"],
            "injuries": user_data["injuries"],
            "updatedAt": "2023-01-02T00:00:00Z"
        }
        
        mock_dynamo.get_item.return_value = existing_user
        mock_dynamo.update_item.return_value = expected_result
        
        # Act
        response = update_user(event, {})
        
        # Assert
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(json.loads(response['body']), expected_result)
        
        # Verify DynamoDB interactions
        mock_dynamo.get_item.assert_called_once()
        mock_dynamo.update_item.assert_called_once()

    @patch('src.handlers.user_handler.DYNAMO_MANAGER')
    def test_get_user_success(self, mock_dynamo):
        """Test successful user retrieval"""
        # Arrange
        event = self.event_base
        
        expected_result = {
            "userId": self.user_id,
            "name": "John Doe",
            "age": 30,
            "height": 180,
            "weight": 85,
            "fitnessGoals": ["Muscle gain", "Weight loss"],
            "experienceLevel": "Intermediate",
            "preferredWorkoutDays": ["Monday", "Wednesday", "Friday"],
            "createdAt": "2023-01-01T00:00:00Z"
        }
        
        mock_dynamo.get_item.return_value = expected_result
        
        # Act
        response = get_user(event, {})
        
        # Assert
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(json.loads(response['body']), expected_result)
        
        # Verify DynamoDB interaction
        mock_dynamo.get_item.assert_called_once()
        call_args = mock_dynamo.get_item.call_args
        self.assertIn('users', call_args[0][0].lower())  # Table name should contain 'users'
        self.assertEqual(call_args[0][1], {'userId': self.user_id})

    @patch('src.handlers.user_handler.DYNAMO_MANAGER')
    def test_get_user_not_found(self, mock_dynamo):
        """Test user not found scenario"""
        # Arrange
        event = self.event_base
        
        # Mock DynamoDB returning None (user not found)
        mock_dynamo.get_item.return_value = None
        
        # Act
        response = get_user(event, {})
        
        # Assert
        self.assertEqual(response['statusCode'], 404)
        self.assertEqual(json.loads(response['body'])['error'], "User not found")

    @patch('src.handlers.user_handler.DYNAMO_MANAGER')
    def test_create_user_missing_required_fields(self, mock_dynamo):
        """Test user creation with missing required fields"""
        # Arrange
        # Missing required fields (name and age)
        user_data = {
            "height": 180,
            "weight": 85,
            "fitnessGoals": ["Muscle gain"]
        }
        
        event = {
            **self.event_base,
            "body": json.dumps(user_data)
        }
        
        # Act
        response = create_user(event, {})
        
        # Assert
        self.assertEqual(response['statusCode'], 400)
        response_body = json.loads(response['body'])
        self.assertIn('error', response_body)
        # The error should mention the missing fields
        self.assertTrue('name' in response_body['error'].lower() or 
                       'age' in response_body['error'].lower())

    @patch('src.handlers.user_handler.DYNAMO_MANAGER')
    def test_error_handling(self, mock_dynamo):
        """Test error handling in handlers"""
        # Arrange
        event = self.event_base
        error_message = "Database connection error"
        mock_dynamo.get_item.side_effect = Exception(error_message)
        
        # Act
        response = get_user(event, {})
        
        # Assert
        self.assertEqual(response['statusCode'], 500)
        self.assertEqual(json.loads(response['body'])['error'], error_message)


if __name__ == '__main__':
    unittest.main() 