# Bodybuilding API Debugging Guide

This guide provides instructions for debugging issues with the Bodybuilding API, with a focus on Lambda function errors.

## Quick Start: Retrieving Lambda Logs

Use the `debug_logs.ps1` script to quickly retrieve logs for any Lambda function:

```powershell
# Basic usage - get logs for createPlan function from the last hour
./docs/debug_logs.ps1 -FunctionName "createPlan"

# Get only error logs from the last 24 hours and save to a file
./docs/debug_logs.ps1 -FunctionName "createPlan" -Hours 24 -ErrorsOnly -OutputFile "createplan_errors.log"

# Debug a different function in production
./docs/debug_logs.ps1 -FunctionName "savePlan" -Stage "prod"
```

## Common Issues and Solutions

### 1. Create Plan Errors

If you're encountering errors with the `createPlan` function, check for:

- **Request Validation Errors**: Ensure the request body includes all required fields:
  - `goals` (array of strings)
  - `experience_level` (string: "beginner", "intermediate", or "advanced")
  - `available_days` (array of strings)

- **Authorization Issues**: Verify that the request includes proper authorization headers and the user has valid Cognito tokens.

- **DynamoDB Errors**: Check if the DynamoDB tables exist and the Lambda function has proper permissions.

### 2. Authentication Problems

If you're seeing authentication errors:

- Verify Cognito user pool configuration
- Check that the token is not expired
- Ensure the authorization header is properly formatted

### 3. Service Initialization Issues

The PlanService constructor requires:
- dynamodb_client
- bedrock_manager

If these aren't properly initialized, you'll see errors when calling any methods.

## Debugging with CloudWatch Logs Directly

If you need more advanced log analysis, use these AWS CLI commands:

```powershell
# List all log groups for the application
aws logs describe-log-groups --query "logGroups[?contains(logGroupName, 'bodybuildr')].logGroupName" --output json

# Get the most recent log stream for a specific function
$logGroup = "/aws/lambda/bodybuildr-backend-infrastructure-dev-createPlan"
aws logs describe-log-streams --log-group-name $logGroup --order-by LastEventTime --descending --limit 1

# Filter logs for errors in the last hour
$startTime = [long][double]::Parse(((Get-Date).AddHours(-1) - (Get-Date "1/1/1970")).TotalMilliseconds)
aws logs filter-log-events --log-group-name $logGroup --filter-pattern "ERROR" --start-time $startTime
```

## Troubleshooting API Gateway Issues

If the Lambda function is working but API requests fail:

1. Check API Gateway configuration in the AWS Console
2. Verify CORS settings if requests come from a browser
3. Check API Gateway logs (if enabled)
4. Test the endpoint directly with Postman or curl

## Debugging Plan Service Implementation

The `plan_service.py` file contains the core business logic. Common issues include:

- **Async/Await Usage**: The service uses async methods but may not be properly awaited
- **DynamoDB Schema Mismatch**: Ensure the DynamoDB table schema matches what the code expects
- **Bedrock AI Integration**: Check for issues with the Bedrock AI service configuration

## Automating Regular Log Checks

Add this to your CI/CD pipeline or scheduled tasks:

```powershell
# Schedule daily log check for errors
$ErrorLogs = ./docs/debug_logs.ps1 -FunctionName "createPlan" -Hours 24 -ErrorsOnly
if ($ErrorLogs -match "ERROR") {
    Send-MailMessage -To "team@example.com" -Subject "Bodybuilding API Errors Detected" -Body $ErrorLogs
}
```

## Useful AWS CLI Commands for Debugging

```powershell
# Check Lambda function configuration
aws lambda get-function --function-name bodybuildr-backend-infrastructure-dev-createPlan

# View recent invocation metrics
aws cloudwatch get-metric-statistics --namespace AWS/Lambda --metric-name Errors --dimensions Name=FunctionName,Value=bodybuildr-backend-infrastructure-dev-createPlan --start-time (Get-Date).AddDays(-1).ToString('o') --end-time (Get-Date).ToString('o') --period 3600 --statistics Sum

# Test Lambda function directly
aws lambda invoke --function-name bodybuildr-backend-infrastructure-dev-createPlan --payload '{"body": "{\"goals\":[\"muscle gain\"],\"experience_level\":\"beginner\",\"available_days\":[\"Monday\",\"Wednesday\",\"Friday\"]}"}' response.json
``` 