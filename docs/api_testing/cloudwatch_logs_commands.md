# CloudWatch Logs Commands for Bodybuilding API

This document provides AWS CLI commands to view and analyze CloudWatch logs for the Bodybuilding API, with a focus on the create plan endpoint.

## Prerequisites

1. AWS CLI installed and configured with appropriate credentials
2. Permissions to access CloudWatch logs

## Finding Log Groups

### 1. List all available log groups for the bodybuildr application:

```powershell
# This command lists all log groups containing "bodybuildr" in their name
aws logs describe-log-groups --query "logGroups[*].logGroupName" | Select-String bodybuildr
```

This will show all log groups related to the bodybuildr application, including:
- `/aws/lambda/bodybuildr-backend-infrastructure-dev-createPlan`
- `/aws/lambda/bodybuildr-backend-infrastructure-dev-savePlan`
- `/aws/lambda/bodybuildr-backend-infrastructure-dev-chatWithCoach`
- And many others

### 2. For better formatting, you can use:

```powershell
# This command provides better formatting for the log group names
aws logs describe-log-groups --query "logGroups[*].logGroupName" --output json
```

### 3. For a more targeted search of specific log groups:

```powershell
# This command finds log groups containing "createPlan" in their name
aws logs describe-log-groups --query "logGroups[?contains(logGroupName, 'createPlan')].logGroupName" --output text
```

## Viewing Logs for Create Plan Lambda

### 4. To view the log streams for the create plan Lambda function:

```powershell
# This command shows the 5 most recent log streams for the createPlan Lambda
$logGroup = "/aws/lambda/bodybuildr-backend-infrastructure-dev-createPlan"
aws logs describe-log-streams --log-group-name $logGroup --order-by LastEventTime --descending --limit 5
```

This will show the 5 most recent log streams, including their names, creation times, and other metadata.

### 5. To view the logs from a specific stream:

```powershell
# First, get the most recent log stream name
$logGroup = "/aws/lambda/bodybuildr-backend-infrastructure-dev-createPlan"
$logStream = $(aws logs describe-log-streams --log-group-name $logGroup --order-by LastEventTime --descending --limit 1 --query "logStreams[0].logStreamName" --output text)

# Then, view the logs from that stream
aws logs get-log-events --log-group-name $logGroup --log-stream-name $logStream --output json
```

This approach automatically captures the most recent log stream and displays its events.

## Filtering Logs for Recent Errors

### 6. To find recent errors in the create plan Lambda function:

```powershell
# This command finds log events containing "ERROR" in the createPlan Lambda
$logGroup = "/aws/lambda/bodybuildr-backend-infrastructure-dev-createPlan"
aws logs filter-log-events --log-group-name $logGroup --filter-pattern "ERROR" --limit 5
```

### 7. To filter logs with a timestamp (last hour):

```powershell
# This command finds ERROR logs from the last hour
$startTime = [long][double]::Parse(((Get-Date).AddHours(-1) - (Get-Date "1/1/1970")).TotalMilliseconds)
$logGroup = "/aws/lambda/bodybuildr-backend-infrastructure-dev-createPlan"
aws logs filter-log-events --log-group-name $logGroup --filter-pattern "ERROR" --start-time $startTime --limit 5
```

Note: We use `[long]` instead of `[int]` to handle the larger timestamp values.

## API Gateway Logs

### 8. Checking API Gateway logs:

```powershell
# Replace API_ID with your actual API Gateway ID
$apiId = "YOUR_API_GATEWAY_ID"
aws logs describe-log-streams --log-group-name "API-Gateway-Execution-Logs_${apiId}/dev" --order-by LastEventTime --descending --limit 5
```

Note: This command will return a "ResourceNotFoundException" error if API Gateway logging is not enabled or if the log group name is incorrect.

To enable API Gateway logging, you need to:
1. Go to the API Gateway console
2. Select your API
3. Go to Settings
4. Enable CloudWatch Logs
5. Set the log level (ERROR or INFO)

## Checking Other Lambda Functions

### 9. Save Plan Logs:

```powershell
# This command shows log streams for the savePlan Lambda
aws logs describe-log-streams --log-group-name "/aws/lambda/bodybuildr-backend-infrastructure-dev-savePlan" --order-by LastEventTime --descending --limit 5
```

### 10. List Plans Logs:

```powershell
# This command shows log streams for the listPlans Lambda
aws logs describe-log-streams --log-group-name "/aws/lambda/bodybuildr-backend-infrastructure-dev-listPlans" --order-by LastEventTime --descending --limit 5
```

### 11. Chat with Coach Logs:

```powershell
# This command shows log streams for the chatWithCoach Lambda
aws logs describe-log-streams --log-group-name "/aws/lambda/bodybuildr-backend-infrastructure-dev-chatWithCoach" --order-by LastEventTime --descending --limit 5
```

Note: These commands may return empty lists if the functions haven't been invoked yet.

## Real-time Log Monitoring

### 12. To watch logs in real-time (not recommended for automation):

```powershell
# This command watches logs in real-time - press Ctrl+C to exit
$logGroup = "/aws/lambda/bodybuildr-backend-infrastructure-dev-createPlan"
aws logs tail $logGroup --follow
```

Warning: This command will run indefinitely until manually stopped with Ctrl+C. Not suitable for automation.

## Exporting Logs for Analysis

### 13. To export logs to a file for further analysis:

```powershell
# First, get the most recent log stream name
$logGroup = "/aws/lambda/bodybuildr-backend-infrastructure-dev-createPlan"
$logStream = $(aws logs describe-log-streams --log-group-name $logGroup --order-by LastEventTime --descending --limit 1 --query "logStreams[0].logStreamName" --output text)

# Then, export the logs to a JSON file
aws logs get-log-events --log-group-name $logGroup --log-stream-name $logStream | ConvertTo-Json > createplan_logs.json
```

This approach automatically captures the most recent log stream and exports its events to a JSON file.

## Troubleshooting Common Issues

### No Log Streams Found
If you don't see any log streams, it might mean:
- The Lambda function hasn't been invoked yet
- You don't have the correct permissions
- You're looking at the wrong log group

### Logs Not Showing Expected Information
If logs don't contain the information you're looking for:
- Check if the logging level is set correctly in your Lambda function
- Verify that your code is actually logging the information you need
- Make sure you're looking at the correct log stream (most recent invocation)

### API Gateway Logs Not Available
If API Gateway logs aren't available:
- Verify that logging is enabled for your API Gateway
- Check the execution logs settings in the API Gateway console
- Confirm you're using the correct API Gateway ID in the log group name

### Error with Start Time in Filter Command
If you get an error about the start time value being too large for an Int32:
- Use `[long]` instead of `[int]` when converting the timestamp
- The correct command is:
```powershell
$startTime = [long][double]::Parse(((Get-Date).AddHours(-1) - (Get-Date "1/1/1970")).TotalMilliseconds)
```

### PowerShell Pagination Issues
Many AWS CLI commands in PowerShell will trigger pagination for large outputs:
- Press space to see more results
- Press q to exit pagination
- Press Ctrl+C to cancel the command entirely
- For better formatting, consider using `--output json` instead of trying to format the output with PowerShell commands

### Log Stream Not Found
If you get "The specified log stream does not exist" error:
- Double-check the log stream name for typos
- Verify the log stream exists in the log group
- Use the exact log stream name from the describe-log-streams command
- Try using filter-log-events instead, which doesn't require a specific stream name

## Summary of Commands That May Hang in Automation

1. Commands that trigger PowerShell pagination:
   - All `describe-log-streams` commands with large outputs
   - All `filter-log-events` commands with large outputs
   - All `get-log-events` commands with large outputs
   - Fix: Use `--output json` for better formatting

2. Commands that run indefinitely (require alternative approaches):
   - `aws logs tail ... --follow` command (command #12)
   - Replace with time-bounded `filter-log-events` commands for automation

3. Commands requiring manual input:
   - Commands requiring specific log stream names
   - Fix: Use automatic capture of the most recent stream as shown in commands #5 and #13
