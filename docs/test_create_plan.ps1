#!/usr/bin/env pwsh
# test_create_plan.ps1 - Test the create_plan endpoint with a valid payload
# Usage: ./test_create_plan.ps1 -ApiUrl "https://your-api-endpoint.execute-api.us-east-1.amazonaws.com/dev" -IdToken "your-id-token"

param(
    [Parameter(Mandatory=$true)]
    [string]$ApiUrl,
    
    [Parameter(Mandatory=$true)]
    [string]$IdToken,
    
    [Parameter(Mandatory=$false)]
    [string]$Stage = "dev",
    
    [Parameter(Mandatory=$false)]
    [switch]$Verbose = $false
)

# Set error action preference
$ErrorActionPreference = "Stop"

# Construct the full API URL
$fullApiUrl = "$ApiUrl/$Stage/plans/create"
if ($Verbose) {
    Write-Host "Target API URL: $fullApiUrl" -ForegroundColor Cyan
}

# Create a valid payload
$payload = @{
    goals = @("muscle gain", "weight loss")
    experience_level = "beginner"
    available_days = @("Monday", "Wednesday", "Friday")
    preferences = @{
        workout_duration = 60
        focus_areas = @("chest", "arms")
    }
    limitations = @("lower back pain")
} | ConvertTo-Json

if ($Verbose) {
    Write-Host "Request Payload:" -ForegroundColor Cyan
    Write-Host $payload -ForegroundColor Gray
}

# Set up headers
$headers = @{
    "Content-Type" = "application/json"
    "Authorization" = "Bearer $IdToken"
}

# Make the API request
try {
    Write-Host "Sending request to create plan endpoint..." -ForegroundColor Cyan
    
    $response = Invoke-RestMethod -Uri $fullApiUrl -Method Post -Headers $headers -Body $payload -ErrorVariable restError
    
    Write-Host "Request successful!" -ForegroundColor Green
    Write-Host "Response:" -ForegroundColor Cyan
    $response | ConvertTo-Json -Depth 10
    
    # Save the plan ID for future reference
    if ($response.plan_id) {
        $response.plan_id | Out-File -FilePath "last_created_plan_id.txt"
        Write-Host "Plan ID saved to last_created_plan_id.txt" -ForegroundColor Green
    }
}
catch {
    Write-Host "Error making API request:" -ForegroundColor Red
    
    if ($restError) {
        Write-Host "Status Code: $($restError.StatusCode)" -ForegroundColor Red
        Write-Host "Error Message: $($restError.Message)" -ForegroundColor Red
        
        if ($restError.ErrorRecord.Exception.Response) {
            $reader = New-Object System.IO.StreamReader($restError.ErrorRecord.Exception.Response.GetResponseStream())
            $responseBody = $reader.ReadToEnd()
            $reader.Close()
            
            Write-Host "Response Body:" -ForegroundColor Red
            Write-Host $responseBody -ForegroundColor Gray
        }
    }
    else {
        Write-Host $_.Exception.Message -ForegroundColor Red
    }
    
    # Suggest next steps
    Write-Host "`nTroubleshooting Steps:" -ForegroundColor Yellow
    Write-Host "1. Check your ID token is valid and not expired" -ForegroundColor Yellow
    Write-Host "2. Verify the API URL is correct" -ForegroundColor Yellow
    Write-Host "3. Run the debug_logs.ps1 script to check Lambda logs" -ForegroundColor Yellow
    Write-Host "4. Review the create_plan_troubleshooting.md document" -ForegroundColor Yellow
}

# Provide helpful next steps
Write-Host "`nNext Steps:" -ForegroundColor Cyan
Write-Host "- To view logs for this request: ./docs/debug_logs.ps1 -FunctionName 'createPlan'" -ForegroundColor Cyan
Write-Host "- To list all plans: Invoke-RestMethod -Uri '$ApiUrl/$Stage/plans/list' -Headers @{'Authorization'='Bearer $IdToken'}" -ForegroundColor Cyan 