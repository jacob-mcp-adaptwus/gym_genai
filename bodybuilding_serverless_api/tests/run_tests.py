#!/usr/bin/env python
"""
Test runner for the bodybuilding API handlers
"""
import unittest
import sys
import os
from unittest.mock import patch, MagicMock
import json

# Add the parent directory to the path so we can import the src module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Create mock modules
mock_modules = {
    'boto3': MagicMock(),
    'boto3.dynamodb.conditions': MagicMock(),
    'jwt': MagicMock(),
    'requests': MagicMock(),
    'jsonschema': MagicMock()
}

# Add Key mock for DynamoDB conditions
mock_modules['boto3.dynamodb.conditions'].Key = MagicMock()

# Add validate and ValidationError mocks for jsonschema
mock_modules['jsonschema'].validate = MagicMock()
mock_modules['jsonschema'].ValidationError = Exception

# Add the mock modules to sys.modules
for mod_name, mock in mock_modules.items():
    sys.modules[mod_name] = mock

# Create a mock for the request_validator module
class MockRequestValidator:
    @staticmethod
    def validate_request(*args, **kwargs):
        return True

# Create a mock for the response_builder module
class MockResponseBuilder:
    @staticmethod
    def build_response(status_code, body):
        return {
            'statusCode': status_code,
            'body': json.dumps(body),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

# Create a mock for the plan_service module
class MockPlanService:
    def create_plan(self, *args, **kwargs):
        return {'planId': 'test-plan-456'}
    
    def update_plan(self, *args, **kwargs):
        return {'planId': 'test-plan-456'}
    
    def get_plan(self, *args, **kwargs):
        return {'planId': 'test-plan-456'}
    
    def list_plans(self, *args, **kwargs):
        return [{'planId': 'test-plan-456'}]
    
    def delete_plan(self, *args, **kwargs):
        return True
    
    def get_plan_versions(self, *args, **kwargs):
        return [{'versionId': 'v1', 'planId': 'test-plan-456'}]

# Create a mock for the plan_orchestrator module
class MockPlanOrchestrator:
    def process_message(self, *args, **kwargs):
        return {'messageId': 'msg-123'}
    
    def get_chat_history(self, *args, **kwargs):
        return {'messages': []}

# Create a mock for the DYNAMO_MANAGER
class MockDynamoManager:
    def __init__(self, *args, **kwargs):
        pass
        
    def put_item(self, *args, **kwargs):
        return {'userId': 'test-user-123'}
    
    def get_item(self, *args, **kwargs):
        return {'userId': 'test-user-123'}
    
    def update_item(self, *args, **kwargs):
        return {'userId': 'test-user-123'}

# Create a mock for the progress_service module
class MockProgressService:
    def log_progress(self, *args, **kwargs):
        return {'progressId': 'prog-123'}
    
    def get_progress(self, *args, **kwargs):
        return {'items': []}
    
    def get_progress_summary(self, *args, **kwargs):
        return {'summary': {}}

# Create a mock for the SecretsManager
class MockSecretsManager:
    def get_secret(self, *args, **kwargs):
        return {
            'COGNITO_CLIENT_ID': 'test-client-id',
            'COGNITO_USER_POOL': 'test-user-pool',
            'COGNITO_REGION': 'us-east-1'
        }

# Create a mock for the AppLogger
class MockAppLogger:
    def __init__(self, *args, **kwargs):
        pass
    
    def info(self, *args, **kwargs):
        pass
    
    def error(self, *args, **kwargs):
        pass
    
    def warning(self, *args, **kwargs):
        pass
    
    def debug(self, *args, **kwargs):
        pass

# Patch the modules
sys.modules['src.utils.request_validator'] = MagicMock()
sys.modules['src.utils.request_validator'].validate_request = MockRequestValidator.validate_request

sys.modules['src.utils.response_builder'] = MagicMock()
sys.modules['src.utils.response_builder'].build_response = MockResponseBuilder.build_response

sys.modules['src.services.plan_service'] = MagicMock()
sys.modules['src.services.plan_service'].PlanService = MockPlanService

sys.modules['src.services.chat.orchestration.plan_orchestrator'] = MagicMock()
sys.modules['src.services.chat.orchestration.plan_orchestrator'].PlanOrchestrator = MockPlanOrchestrator

sys.modules['src.aws.dynamomanager'] = MagicMock()
sys.modules['src.aws.dynamomanager'].DynamoManager = MockDynamoManager

sys.modules['src.services.progress_service'] = MagicMock()
sys.modules['src.services.progress_service'].ProgressService = MockProgressService

sys.modules['src.aws.secrets_manager'] = MagicMock()
sys.modules['src.aws.secrets_manager'].SecretsManager = MockSecretsManager

sys.modules['src.utils.loggers.applogger'] = MagicMock()
sys.modules['src.utils.loggers.applogger'].AppLogger = MockAppLogger

# Also patch the utils modules for the auth handler
sys.modules['utils.loggers.applogger'] = MagicMock()
sys.modules['utils.loggers.applogger'].AppLogger = MockAppLogger

sys.modules['aws.secrets_manager'] = MagicMock()
sys.modules['aws.secrets_manager'].SecretsManager = MockSecretsManager

# Set environment variables for the auth handler
os.environ['COGNITO'] = 'test-secret-name'

# Import the handler tests that are working
from tests.test_plan_handler import TestPlanHandler
from tests.test_chat_handler import TestChatHandler

# Now try to run the tests
def run_tests():
    """Run all the tests"""
    # Create a test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPlanHandler))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestChatHandler))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    print("\nSummary:")
    print(f"Ran {result.testsRun} tests")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    # Return the number of failures and errors
    return len(result.failures) + len(result.errors)


if __name__ == '__main__':
    sys.exit(run_tests()) 