import json
import unittest
from unittest.mock import patch, MagicMock

from src.handlers.plan_handler import create_plan, save_plan, get, list_plans, delete, get_plan_versions


class TestPlanHandler(unittest.TestCase):
    """Test cases for the plan handler functions"""

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

    @patch('src.handlers.plan_handler.plan_service')
    @patch('src.handlers.plan_handler.validate_request')
    def test_create_plan_success(self, mock_validate, mock_service):
        """Test successful plan creation"""
        # Arrange
        plan_data = {"name": "Test Workout Plan", "goal": "Muscle gain"}
        event = {
            **self.event_base,
            "body": json.dumps(plan_data)
        }
        
        expected_result = {
            "planId": self.plan_id,
            "userId": self.user_id,
            "name": plan_data["name"],
            "createdAt": "2023-01-01T00:00:00Z"
        }
        
        mock_service.create_plan.return_value = expected_result
        
        # Act
        response = create_plan(event, {})
        
        # Assert
        mock_validate.assert_called_once_with(plan_data, 'create_plan')
        mock_service.create_plan.assert_called_once_with(
            user_id=self.user_id,
            plan_data=plan_data
        )
        
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(json.loads(response['body']), expected_result)

    @patch('src.handlers.plan_handler.plan_service')
    @patch('src.handlers.plan_handler.validate_request')
    def test_save_plan_success(self, mock_validate, mock_service):
        """Test successful plan update"""
        # Arrange
        plan_data = {
            "planId": self.plan_id,
            "name": "Updated Workout Plan",
            "goal": "Strength"
        }
        event = {
            **self.event_base,
            "body": json.dumps(plan_data)
        }
        
        expected_result = {
            "planId": self.plan_id,
            "userId": self.user_id,
            "name": plan_data["name"],
            "updatedAt": "2023-01-01T00:00:00Z"
        }
        
        mock_service.update_plan.return_value = expected_result
        
        # Act
        response = save_plan(event, {})
        
        # Assert
        mock_validate.assert_called_once_with(plan_data, 'update_plan')
        mock_service.update_plan.assert_called_once_with(
            user_id=self.user_id,
            plan_id=self.plan_id,
            plan_data=plan_data
        )
        
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(json.loads(response['body']), expected_result)

    @patch('src.handlers.plan_handler.plan_service')
    def test_get_plan_success(self, mock_service):
        """Test successful plan retrieval"""
        # Arrange
        event = {
            **self.event_base,
            "pathParameters": {
                "planId": self.plan_id
            }
        }
        
        expected_result = {
            "planId": self.plan_id,
            "userId": self.user_id,
            "name": "Test Workout Plan",
            "goal": "Muscle gain",
            "createdAt": "2023-01-01T00:00:00Z"
        }
        
        mock_service.get_plan.return_value = expected_result
        
        # Act
        response = get(event, {})
        
        # Assert
        mock_service.get_plan.assert_called_once_with(
            user_id=self.user_id,
            plan_id=self.plan_id
        )
        
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(json.loads(response['body']), expected_result)

    @patch('src.handlers.plan_handler.plan_service')
    def test_list_plans_success(self, mock_service):
        """Test successful plan listing"""
        # Arrange
        event = self.event_base
        
        expected_result = [
            {
                "planId": self.plan_id,
                "userId": self.user_id,
                "name": "Test Workout Plan",
                "createdAt": "2023-01-01T00:00:00Z"
            },
            {
                "planId": "another-plan-789",
                "userId": self.user_id,
                "name": "Another Workout Plan",
                "createdAt": "2023-01-02T00:00:00Z"
            }
        ]
        
        mock_service.list_plans.return_value = expected_result
        
        # Act
        response = list_plans(event, {})
        
        # Assert
        mock_service.list_plans.assert_called_once_with(user_id=self.user_id)
        
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(json.loads(response['body']), expected_result)

    @patch('src.handlers.plan_handler.plan_service')
    def test_delete_plan_success(self, mock_service):
        """Test successful plan deletion"""
        # Arrange
        event = {
            **self.event_base,
            "pathParameters": {
                "planId": self.plan_id
            }
        }
        
        mock_service.delete_plan.return_value = True
        
        # Act
        response = delete(event, {})
        
        # Assert
        mock_service.delete_plan.assert_called_once_with(
            user_id=self.user_id,
            plan_id=self.plan_id
        )
        
        self.assertEqual(response['statusCode'], 200)
        expected_message = f"Plan '{self.plan_id}' and all its versions deleted successfully"
        self.assertEqual(json.loads(response['body'])['message'], expected_message)

    @patch('src.handlers.plan_handler.plan_service')
    def test_get_plan_versions_success(self, mock_service):
        """Test successful retrieval of plan versions"""
        # Arrange
        event = {
            **self.event_base,
            "pathParameters": {
                "planId": self.plan_id
            }
        }
        
        expected_versions = [
            {
                "versionId": "v1",
                "planId": self.plan_id,
                "createdAt": "2023-01-01T00:00:00Z"
            },
            {
                "versionId": "v2",
                "planId": self.plan_id,
                "createdAt": "2023-01-02T00:00:00Z"
            }
        ]
        
        mock_service.get_plan_versions.return_value = expected_versions
        
        # Act
        response = get_plan_versions(event, {})
        
        # Assert
        mock_service.get_plan_versions.assert_called_once_with(
            user_id=self.user_id,
            plan_id=self.plan_id
        )
        
        self.assertEqual(response['statusCode'], 200)
        response_body = json.loads(response['body'])
        self.assertEqual(response_body['versions'], expected_versions)
        self.assertEqual(response_body['totalVersions'], 2)

    @patch('src.handlers.plan_handler.plan_service')
    def test_error_handling(self, mock_service):
        """Test error handling in handlers"""
        # Arrange
        event = self.event_base
        error_message = "Something went wrong"
        mock_service.list_plans.side_effect = Exception(error_message)
        
        # Act
        response = list_plans(event, {})
        
        # Assert
        self.assertEqual(response['statusCode'], 500)
        self.assertEqual(json.loads(response['body'])['error'], error_message)


if __name__ == '__main__':
    unittest.main() 