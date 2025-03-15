import json
import unittest
import uuid
from datetime import datetime
from unittest.mock import patch

# Import the handlers
from src.handlers.plan_handler import create_plan, save_plan, get, list_plans, delete, get_plan_versions

class TestPlanIntegration(unittest.TestCase):
    """Integration test cases for the plan handler functions"""

    def setUp(self):
        """Set up test fixtures"""
        self.user_id = "test-user-123"
        self.plan_id = str(uuid.uuid4())
        
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

    def test_create_and_get_plan(self):
        """Test creating a plan and then retrieving it"""
        # Create a plan
        plan_data = {
            "name": "Test Workout Plan",
            "goal": "Muscle gain",
            "workoutFrequency": 4,
            "targetMuscleGroups": ["chest", "back", "legs"],
            "fitnessLevel": "intermediate"
        }
        
        create_event = {
            **self.event_base,
            "body": json.dumps(plan_data)
        }
        
        # Act - Create the plan
        create_response = create_plan(create_event, {})
        response_body = json.loads(create_response["body"])
        
        # Assert - Check the response
        self.assertEqual(create_response["statusCode"], 200)
        self.assertIn("planId", response_body)
        
        # Store the plan ID for the next test
        created_plan_id = response_body["planId"]
        
        # Now get the plan
        get_event = {
            **self.event_base,
            "pathParameters": {
                "planId": created_plan_id
            }
        }
        
        # Act - Get the plan
        get_response = get(get_event, {})
        get_body = json.loads(get_response["body"])
        
        # Assert - Check the response
        self.assertEqual(get_response["statusCode"], 200)
        self.assertEqual(get_body["planId"], created_plan_id)
        self.assertEqual(get_body["name"], plan_data["name"])
        self.assertEqual(get_body["goal"], plan_data["goal"])
        
        return created_plan_id

    def test_create_update_and_get_versions(self):
        """Test creating a plan, updating it, and getting versions"""
        # First create a plan
        plan_id = self.test_create_and_get_plan()
        
        # Now update the plan
        update_data = {
            "name": "Updated Workout Plan",
            "goal": "Strength building",
            "workoutFrequency": 5,
            "targetMuscleGroups": ["shoulders", "arms", "core"],
            "fitnessLevel": "advanced"
        }
        
        update_event = {
            **self.event_base,
            "pathParameters": {
                "planId": plan_id
            },
            "body": json.dumps(update_data)
        }
        
        # Act - Update the plan
        update_response = save_plan(update_event, {})
        update_body = json.loads(update_response["body"])
        
        # Assert - Check the response
        self.assertEqual(update_response["statusCode"], 200)
        self.assertEqual(update_body["planId"], plan_id)
        
        # Now get the plan to verify the update
        get_event = {
            **self.event_base,
            "pathParameters": {
                "planId": plan_id
            }
        }
        
        get_response = get(get_event, {})
        get_body = json.loads(get_response["body"])
        
        # Assert - Check the updated values
        self.assertEqual(get_body["name"], update_data["name"])
        self.assertEqual(get_body["goal"], update_data["goal"])
        
        # Now get the versions
        versions_event = {
            **self.event_base,
            "pathParameters": {
                "planId": plan_id
            }
        }
        
        versions_response = get_plan_versions(versions_event, {})
        versions_body = json.loads(versions_response["body"])
        
        # Assert - Check that we have versions
        self.assertEqual(versions_response["statusCode"], 200)
        self.assertIsInstance(versions_body, list)
        self.assertGreaterEqual(len(versions_body), 1)  # Should have at least one version
        
        return plan_id

    def test_list_and_delete_plans(self):
        """Test listing plans and then deleting one"""
        # First create a plan
        plan_id = self.test_create_and_get_plan()
        
        # Now list all plans
        list_event = {
            **self.event_base
        }
        
        # Act - List the plans
        list_response = list_plans(list_event, {})
        list_body = json.loads(list_response["body"])
        
        # Assert - Check the response
        self.assertEqual(list_response["statusCode"], 200)
        self.assertIsInstance(list_body, list)
        self.assertGreaterEqual(len(list_body), 1)  # Should have at least one plan
        
        # Find our plan in the list
        found_plan = False
        for plan in list_body:
            if plan["planId"] == plan_id:
                found_plan = True
                break
        
        self.assertTrue(found_plan, "Created plan not found in the list")
        
        # Now delete the plan
        delete_event = {
            **self.event_base,
            "pathParameters": {
                "planId": plan_id
            }
        }
        
        # Act - Delete the plan
        delete_response = delete(delete_event, {})
        
        # Assert - Check the response
        self.assertEqual(delete_response["statusCode"], 204)
        
        # Try to get the deleted plan
        get_event = {
            **self.event_base,
            "pathParameters": {
                "planId": plan_id
            }
        }
        
        get_response = get(get_event, {})
        
        # Assert - Check that the plan is gone
        self.assertEqual(get_response["statusCode"], 404)

    def test_error_handling(self):
        """Test error handling in the plan handler"""
        # Create a plan first to ensure we have a valid plan ID
        plan_id = self.test_create_and_get_plan()
        
        # Test missing plan ID
        get_event = {
            **self.event_base,
            "pathParameters": {}  # Missing planId
        }
        
        # Act - Try to get a plan without an ID
        get_response = get(get_event, {})
        
        # Assert - Check the error response
        self.assertEqual(get_response["statusCode"], 500)
        
        # Delete the plan we created
        delete_event = {
            **self.event_base,
            "pathParameters": {
                "planId": plan_id
            }
        }
        delete(delete_event, {})
        
        # Test non-existent plan ID
        get_event = {
            **self.event_base,
            "pathParameters": {
                "planId": plan_id  # This ID no longer exists
            }
        }
        
        # Act - Try to get a non-existent plan
        get_response = get(get_event, {})
        
        # Assert - Check the error response
        self.assertEqual(get_response["statusCode"], 404)
        
        # Test invalid request body
        create_event = {
            **self.event_base,
            "body": "not-valid-json"
        }
        
        # Act - Try to create a plan with invalid JSON
        create_response = create_plan(create_event, {})
        
        # Assert - Check the error response
        self.assertEqual(create_response["statusCode"], 400)

if __name__ == "__main__":
    unittest.main() 