@echo off
echo Running integration tests with minimal mocking...
python -m tests.run_integration_tests
exit /b %ERRORLEVEL% 