#!/usr/bin/env pwsh
# debug_logs.ps1 - Automated CloudWatch Log Retrieval for Lambda Functions
# Usage: ./debug_logs.ps1 -FunctionName "createPlan" -Stage "dev" -Service "bodybuildr-backend-infrastructure" -Hours 1

param(
    [Parameter(Mandatory=$true)]
    [string]$FunctionName,
    
    [Parameter(Mandatory=$false)]
    [string]$Stage = "dev",
    
    [Parameter(Mandatory=$false)]
    [string]$Service = "bodybuildr-backend-infrastructure",
    
    [Parameter(Mandatory=$false)]
    [int]$Hours = 1,
    
    [Parameter(Mandatory=$false)]
    [string]$OutputFile = "",
    
    [Parameter(Mandatory=$false)]
    [switch]$ErrorsOnly = $false
)

# Set error action preference
$ErrorActionPreference = "Stop"

# Construct log group name
$logGroupName = "/aws/lambda/$Service-$Stage-$FunctionName"
Write-Host "Target Log Group: $logGroupName" -ForegroundColor Cyan

# Calculate start time (last N hours)
$startTime = [long][double]::Parse(((Get-Date).AddHours(-$Hours) - (Get-Date "1/1/1970")).TotalMilliseconds)

# Get the most recent log stream
try {
    Write-Host "Retrieving most recent log streams..." -ForegroundColor Cyan
    $logStreams = aws logs describe-log-streams `
        --log-group-name $logGroupName `
        --order-by LastEventTime `
        --descending `
        --limit 5 `
        --query "logStreams[*].logStreamName" `
        --output json | ConvertFrom-Json
    
    if ($null -eq $logStreams -or $logStreams.Count -eq 0) {
        Write-Host "No log streams found for $logGroupName" -ForegroundColor Red
        exit 1
    }
    
    $mostRecentStream = $logStreams[0]
    Write-Host "Most recent log stream: $mostRecentStream" -ForegroundColor Green
} 
catch {
    Write-Host "Error retrieving log streams: $_" -ForegroundColor Red
    exit 1
}

# Build filter pattern if errors only
$filterPattern = if ($ErrorsOnly) { "--filter-pattern 'ERROR'" } else { "" }

# Get log events
try {
    Write-Host "Retrieving log events..." -ForegroundColor Cyan
    
    # Build the command
    $command = "aws logs get-log-events --log-group-name `"$logGroupName`" --log-stream-name `"$mostRecentStream`" --start-time $startTime --output json"
    
    # Execute the command
    $logEvents = Invoke-Expression $command | ConvertFrom-Json
    
    if ($null -eq $logEvents -or $null -eq $logEvents.events -or $logEvents.events.Count -eq 0) {
        Write-Host "No log events found in the specified time range" -ForegroundColor Yellow
        exit 0
    }
    
    # Process and display logs
    Write-Host "Found $($logEvents.events.Count) log events" -ForegroundColor Green
    
    # Format and output logs
    $formattedLogs = $logEvents.events | ForEach-Object {
        $timestamp = [DateTimeOffset]::FromUnixTimeMilliseconds($_.timestamp).LocalDateTime.ToString("yyyy-MM-dd HH:mm:ss")
        "$timestamp - $($_.message)"
    }
    
    # Output to file if specified
    if ($OutputFile -ne "") {
        $formattedLogs | Out-File -FilePath $OutputFile
        Write-Host "Logs saved to $OutputFile" -ForegroundColor Green
    } else {
        # Display logs to console
        $formattedLogs | ForEach-Object { Write-Host $_ }
    }
}
catch {
    Write-Host "Error retrieving log events: $_" -ForegroundColor Red
    exit 1
}

# Provide helpful next steps
Write-Host "`nDebugging Tips:" -ForegroundColor Cyan
Write-Host "- Look for ERROR or Exception messages in the logs" -ForegroundColor Cyan
Write-Host "- Check for missing environment variables or permissions" -ForegroundColor Cyan
Write-Host "- Verify request payload format matches schema requirements" -ForegroundColor Cyan
Write-Host "- Examine DynamoDB or other service interactions" -ForegroundColor Cyan 