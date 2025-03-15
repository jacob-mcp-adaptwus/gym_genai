# Bodybuilding API Unit Tests

This directory contains unit tests and integration tests for the Bodybuilding API handlers.

## Test Structure

The tests are organized by handler:

- `test_plan_handler.py` - Tests for plan creation, retrieval, updating, and deletion
- `test_chat_handler.py` - Tests for chat functionality with the AI coach
- `test_user_handler.py` - Tests for user profile management
- `test_progress_handler.py` - Tests for tracking workout progress
- `test_auth_handler.py` - Tests for authentication and authorization
- `test_plan_integration.py` - Integration tests for plan functionality

## Test Cases

### Plan Handler Tests
- `test_create_plan_success`: Tests creating a new workout plan
- `test_save_plan_success`: Tests updating an existing plan
- `test_get_plan_success`: Tests retrieving a plan by ID
- `test_list_plans_success`: Tests listing all plans for a user
- `test_delete_plan_success`: Tests deleting a plan
- `test_get_plan_versions_success`: Tests retrieving plan versions
- `test_error_handling`: Tests error handling in plan operations

### Chat Handler Tests
- `test_chat_with_coach_success`: Tests processing chat messages with the AI coach
- `test_get_chat_history_success`: Tests retrieving chat history
- `test_chat_with_coach_error`: Tests error handling in chat message processing
- `test_get_chat_history_error`: Tests error handling in chat history retrieval

### User Handler Tests
- `test_create_user_profile_success`: Tests creating a user profile
- `test_update_user_profile_success`: Tests updating a user profile
- `test_get_user_profile_success`: Tests retrieving a user profile
- `test_user_handler_error`: Tests error handling in user operations

### Progress Handler Tests
- `test_log_progress_success`: Tests logging workout progress
- `test_get_progress_success`: Tests retrieving progress history
- `test_get_progress_summary_success`: Tests getting progress summaries
- `test_progress_handler_error`: Tests error handling in progress operations

### Auth Handler Tests
- `test_token_validation`: Tests token validation
- `test_policy_generation`: Tests policy generation
- `test_auth_handler_error`: Tests error handling in authentication

## Running the Tests

### Unit Tests

To run the unit tests, use the following command from the project root directory:

```bash
python -m tests.run_tests
```

This will run the tests for the plan handler and chat handler, which are currently working.

### Integration Tests

To run the integration tests, use the following command from the project root directory:

```bash
tests\run_integration.bat  # On Windows
```

Or:

```bash
python -m tests.run_integration_tests  # On any platform
```

The integration tests use fewer mocks and test more of the actual functionality.

## Mocking Strategy

The unit tests use a comprehensive mocking strategy to isolate the handler logic from external dependencies:

### Mock Classes
- `MockRequestValidator`: Mocks request validation
- `MockResponseBuilder`: Mocks response building
- `MockPlanService`: Mocks the plan service with predefined responses
- `MockPlanOrchestrator`: Mocks the plan orchestrator for chat functionality
- `MockDynamoManager`: Mocks DynamoDB operations
- `MockProgressService`: Mocks the progress service
- `MockSecretsManager`: Mocks AWS Secrets Manager
- `MockAppLogger`: Mocks application logging

### Patched Modules
The test runner (`run_tests.py`) patches several modules to prevent actual AWS calls:
- `boto3`: AWS SDK
- `boto3.dynamodb.conditions`: DynamoDB conditions
- `jwt`: JSON Web Token library
- `requests`: HTTP requests library
- `jsonschema`: JSON Schema validation

### Test Fixtures
Each test class includes a `setUp` method that creates common test fixtures:
- User ID and plan ID for testing
- Base event structure with authorization context
- Mock request and response data

## Test Coverage

The tests cover the following functionality:

### Plan Handler Tests
- Creating a new workout plan
- Updating an existing plan
- Retrieving a plan by ID
- Listing all plans for a user
- Deleting a plan
- Retrieving plan versions
- Error handling

### Chat Handler Tests
- Processing chat messages with the AI coach
- Retrieving chat history
- Error handling

### User Handler Tests (In Progress)
- Creating a user profile
- Updating a user profile
- Retrieving a user profile
- Error handling

### Progress Handler Tests (In Progress)
- Logging workout progress
- Retrieving progress history
- Getting progress summaries
- Error handling

### Auth Handler Tests (In Progress)
- Token validation
- Policy generation
- Error handling

## Future Improvements

- Complete the user handler, progress handler, and auth handler tests
- Add integration tests for end-to-end API testing
- Add tests for the service layer components
- Implement test coverage reporting 