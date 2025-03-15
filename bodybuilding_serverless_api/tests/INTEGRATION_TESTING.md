# Integration Testing for Bodybuilding API

This document explains the integration testing approach for the Bodybuilding API.

## Overview

The integration tests are designed to test the actual functionality of the API handlers with minimal mocking. Unlike the unit tests, which mock most dependencies, the integration tests use:

1. Real service implementations
2. In-memory database for DynamoDB
3. Real request validation and response building
4. Actual handler logic

Only external AWS services like boto3, Cognito, and Secrets Manager are still mocked to avoid requiring real AWS credentials.

## Benefits of Integration Testing

- Tests the actual code paths that will run in production
- Verifies that components work together correctly
- Catches integration issues that unit tests might miss
- Provides more confidence in the functionality

## Running the Tests

To run the integration tests on Windows:

```bash
cd bodybuilding_serverless_api
tests\run_integration.bat
```

On Linux/Mac:

```bash
cd bodybuilding_serverless_api
python -m tests.run_integration_tests
```

## Test Structure

The integration tests follow a flow-based approach:

1. `test_create_and_get_plan`: Creates a plan and then retrieves it
2. `test_create_update_and_get_versions`: Creates a plan, updates it, and gets versions
3. `test_list_and_delete_plans`: Lists plans and then deletes one
4. `test_error_handling`: Tests error handling in the plan handler

Each test builds on the previous one to create a realistic flow of operations.

## In-Memory Database

The tests use an in-memory implementation of DynamoDB to avoid requiring a real database. This allows the tests to run quickly and without external dependencies while still testing the actual database access patterns.

## Adding More Tests

To add more integration tests:

1. Create a new test file in the `tests` directory
2. Import the handlers you want to test
3. Create test methods that call the handlers directly
4. Add your test class to the `run_integration_tests.py` file

## Limitations

- External AWS services are still mocked
- Some complex interactions might not be fully tested
- Performance characteristics will differ from production

## Future Improvements

- Add more test coverage for other handlers
- Add tests for edge cases and error conditions
- Consider using localstack for more realistic AWS service testing 