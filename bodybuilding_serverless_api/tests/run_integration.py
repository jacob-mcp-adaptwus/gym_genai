#!/usr/bin/env python
"""
Simple script to run the integration tests
"""
import os
import sys

# Add the parent directory to the path so we can import the tests module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the run_tests function from run_integration_tests
from tests.run_integration_tests import run_tests

if __name__ == '__main__':
    print("Running integration tests with minimal mocking...")
    sys.exit(run_tests()) 