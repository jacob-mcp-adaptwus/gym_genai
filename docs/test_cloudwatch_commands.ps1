# Test CloudWatch Commands

Write-Host "Command 1: List all available log groups for the bodybuildr application"
aws logs describe-log-groups --query "logGroups[*].logGroupName" | Select-String bodybuildr

Write-Host "`nCommand 2: For better formatting"
aws logs describe-log-groups --query "logGroups[*].logGroupName" | Select-String bodybuildr | Out-String -Width 4096

Write-Host "`nCommand 3: For a more targeted search of specific log groups"
aws logs describe-log-groups --query "logGroups[?contains(logGroupName, 'createPlan')].logGroupName" --output text

Write-Host "`nCommand 4: To view the log streams for the create plan Lambda function"
$logGroup = "/aws/lambda/bodybuildr-backend-infrastructure-dev-createPlan"
aws logs describe-log-streams --log-group-name $logGroup --order-by LastEventTime --descending --limit 5 | Out-String -Width 4096

Write-Host "`nCommand 5: To view the logs from a specific stream"
# Get the most recent log stream automatically
$logStream = $(aws logs describe-log-streams --log-group-name $logGroup --order-by LastEventTime --descending --limit 1 --query "logStreams[0].logStreamName" --output text)
Write-Host "Using log stream: $logStream"
aws logs get-log-events --log-group-name $logGroup --log-stream-name $logStream --output json | Out-String -Width 4096

Write-Host "`nCommand 6: To find recent errors in the create plan Lambda function"
aws logs filter-log-events --log-group-name $logGroup --filter-pattern "ERROR" --limit 5 | Out-String -Width 4096

Write-Host "`nCommand 7: To filter logs with a timestamp (last hour)"
$startTime = [long][double]::Parse(((Get-Date).AddHours(-1) - (Get-Date "1/1/1970")).TotalMilliseconds)
aws logs filter-log-events --log-group-name $logGroup --filter-pattern "ERROR" --start-time $startTime --limit 5 | Out-String -Width 4096

Write-Host "`nCommand 8: Checking API Gateway logs"
# This may return ResourceNotFoundException if the log group doesn't exist
aws logs describe-log-streams --log-group-name "API-Gateway-Execution-Logs_jpn7bdhehi/dev" --order-by LastEventTime --descending --limit 5 | Out-String -Width 4096

Write-Host "`nCommand 9: Checking another API Gateway log group"
# This may return ResourceNotFoundException if the log group doesn't exist
aws logs describe-log-streams --log-group-name "API-Gateway-Execution-Logs_zo34ythx94/dev" --order-by LastEventTime --descending --limit 5 | Out-String -Width 4096

Write-Host "`nCommand 10: Save Plan Logs"
aws logs describe-log-streams --log-group-name "/aws/lambda/bodybuildr-backend-infrastructure-dev-savePlan" --order-by LastEventTime --descending --limit 5 | Out-String -Width 4096

Write-Host "`nCommand 11: List Plans Logs"
aws logs describe-log-streams --log-group-name "/aws/lambda/bodybuildr-backend-infrastructure-dev-listPlans" --order-by LastEventTime --descending --limit 5 | Out-String -Width 4096

Write-Host "`nCommand 12: Chat with Coach Logs"
aws logs describe-log-streams --log-group-name "/aws/lambda/bodybuildr-backend-infrastructure-dev-chatWithCoach" --order-by LastEventTime --descending --limit 5 | Out-String -Width 4096

Write-Host "`nCommand 15: To export logs to a file for further analysis"
# Using the same log stream from command 5
Write-Host "Using log stream: $logStream"
aws logs get-log-events --log-group-name $logGroup --log-stream-name $logStream | ConvertTo-Json > createplan_logs.json
Write-Host "Logs exported to createplan_logs.json" 