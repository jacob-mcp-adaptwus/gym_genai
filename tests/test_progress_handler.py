import json
import unittest
from unittest.mock import patch, MagicMock

from src.handlers.progress_handler import update_progress, get_progress, get_progress_summary


class TestProgressHandler(unittest.TestCase):
    """Test cases for the progress handler functions"""

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
            },
            "pathParameters": {
                "userId": self.user_id
            }
        }

    @patch('src.handlers.progress_handler.progress_service')
    @patch('src.handlers.progress_handler.validate_request')
    def test_update_progress_success(self, mock_validate, mock_service):
        """Test successful progress update"""
        # Arrange
        progress_data = {
            "date": "2023-03-15",
            "type": "workout",
            "details": {
                "workout": "Chest and Triceps",
                "exercises": [
                    {
                        "name": "Bench Press",
                        "sets": [
                            {"weight": 80, "reps": 10},
                            {"weight": 85, "reps": 8},
                            {"weight": 90, "reps": 6}
                        ]
                    },
                    {
                        "name": "Tricep Pushdown",
                        "sets": [
                            {"weight": 30, "reps": 12},
                            {"weight": 35, "reps": 10},
                            {"weight": 35, "reps": 10}
                        ]
                    }
                ],
                "duration": 65,
                "notes": "Felt strong today"
            }
        }
        
        event = {
            **self.event_base,
            "body": json.dumps(progress_data)
        }
        
        expected_result = {
            "progressId": "prog-123",
            "userId": self.user_id,
            "date": progress_data["date"],
            "type": progress_data["type"],
            "details": progress_data["details"],
            "createdAt": "2023-03-15T10:30:00Z"
        }
        
        mock_service.log_progress.return_value = expected_result
        
        # Act
        response = update_progress(event, {})
        
        # Assert
        mock_validate.assert_called_once_with(progress_data, 'progress_update')
        mock_service.log_progress.assert_called_once_with(
            user_id=self.user_id,
            progress_data=progress_data
        )
        
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(json.loads(response['body']), expected_result)

    @patch('src.handlers.progress_handler.progress_service')
    def test_get_progress_success(self, mock_service):
        """Test successful progress retrieval"""
        # Arrange
        event = {
            **self.event_base,
            "queryStringParameters": {
                "startDate": "2023-03-01",
                "endDate": "2023-03-31",
                "type": "workout"
            }
        }
        
        expected_result = {
            "items": [
                {
                    "progressId": "prog-123",
                    "userId": self.user_id,
                    "date": "2023-03-15",
                    "type": "workout",
                    "details": {
                        "workout": "Chest and Triceps",
                        "exercises": [
                            {
                                "name": "Bench Press",
                                "sets": [
                                    {"weight": 80, "reps": 10},
                                    {"weight": 85, "reps": 8},
                                    {"weight": 90, "reps": 6}
                                ]
                            }
                        ],
                        "duration": 65,
                        "notes": "Felt strong today"
                    },
                    "createdAt": "2023-03-15T10:30:00Z"
                },
                {
                    "progressId": "prog-124",
                    "userId": self.user_id,
                    "date": "2023-03-18",
                    "type": "workout",
                    "details": {
                        "workout": "Back and Biceps",
                        "exercises": [
                            {
                                "name": "Pull-ups",
                                "sets": [
                                    {"reps": 12},
                                    {"reps": 10},
                                    {"reps": 8}
                                ]
                            }
                        ],
                        "duration": 70,
                        "notes": "Good pump"
                    },
                    "createdAt": "2023-03-18T11:15:00Z"
                }
            ],
            "count": 2
        }
        
        mock_service.get_progress.return_value = expected_result
        
        # Act
        response = get_progress(event, {})
        
        # Assert
        mock_service.get_progress.assert_called_once_with(
            user_id=self.user_id,
            start_date="2023-03-01",
            end_date="2023-03-31",
            progress_type="workout"
        )
        
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(json.loads(response['body']), expected_result)

    @patch('src.handlers.progress_handler.progress_service')
    def test_get_progress_summary_success(self, mock_service):
        """Test successful progress summary retrieval"""
        # Arrange
        event = {
            **self.event_base,
            "queryStringParameters": {
                "period": "month"
            }
        }
        
        expected_result = {
            "summary": {
                "workouts": {
                    "count": 12,
                    "totalDuration": 780,
                    "byType": {
                        "Chest": 3,
                        "Back": 3,
                        "Legs": 3,
                        "Shoulders": 2,
                        "Arms": 1
                    }
                },
                "measurements": {
                    "weight": {
                        "start": 85,
                        "end": 83.5,
                        "change": -1.5
                    },
                    "bodyFat": {
                        "start": 18,
                        "end": 16.5,
                        "change": -1.5
                    }
                },
                "period": {
                    "start": "2023-03-01",
                    "end": "2023-03-31"
                }
            }
        }
        
        mock_service.get_progress_summary.return_value = expected_result
        
        # Act
        response = get_progress_summary(event, {})
        
        # Assert
        mock_service.get_progress_summary.assert_called_once_with(
            user_id=self.user_id,
            period="month"
        )
        
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(json.loads(response['body']), expected_result)

    def test_update_progress_unauthorized(self):
        """Test unauthorized progress update attempt"""
        # Arrange
        different_user_id = "different-user-456"
        event = {
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": self.user_id
                    }
                }
            },
            "pathParameters": {
                "userId": different_user_id  # Different from authenticated user
            },
            "body": json.dumps({"date": "2023-03-15", "type": "workout"})
        }
        
        # Act
        response = update_progress(event, {})
        
        # Assert
        self.assertEqual(response['statusCode'], 403)
        self.assertEqual(json.loads(response['body'])['error'], 'You can only update your own progress')

    @patch('src.handlers.progress_handler.progress_service')
    def test_error_handling(self, mock_service):
        """Test error handling in handlers"""
        # Arrange
        event = self.event_base
        error_message = "Invalid progress data"
        mock_service.get_progress_summary.side_effect = Exception(error_message)
        
        # Act
        response = get_progress_summary(event, {})
        
        # Assert
        self.assertEqual(response['statusCode'], 500)
        self.assertEqual(json.loads(response['body'])['error'], error_message)


if __name__ == '__main__':
    unittest.main() 