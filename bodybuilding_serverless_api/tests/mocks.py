"""
Mock modules for testing
"""
import sys
from unittest.mock import MagicMock

# Create mock modules for AWS dependencies
mock_modules = {
    'boto3': MagicMock(),
    'boto3.dynamodb.conditions': MagicMock(),
    'jwt': MagicMock(),
    'requests': MagicMock()
}

# Add Key mock for DynamoDB conditions
mock_modules['boto3.dynamodb.conditions'].Key = MagicMock()

# Add the mock modules to sys.modules
for mod_name, mock in mock_modules.items():
    sys.modules[mod_name] = mock 