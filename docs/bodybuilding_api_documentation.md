# Bodybuilding API Documentation

## Core Files
- `bodybuilding.json` - Main data model for workout plans
- `bodybuilding_serverless_api/serverless.yml` - AWS serverless configuration
- `bodybuilding_serverless_api/README.md` - Project documentation
- `bodybuilding_serverless_api/requirements.txt` - Python dependencies

## API Handlers
- `bodybuilding_serverless_api/src/handlers/plan_handler.py` - Endpoints for workout plan CRUD operations
- `bodybuilding_serverless_api/src/handlers/chat_handler.py` - Chat interface for workout plan assistance
- `bodybuilding_serverless_api/src/handlers/user_handler.py` - User management endpoints
- `bodybuilding_serverless_api/src/handlers/progress_handler.py` - Workout progress tracking endpoints

## Core Services
- `bodybuilding_serverless_api/src/services/plan_service.py` - Workout plan business logic
- `bodybuilding_serverless_api/src/services/chat_service.py` - Chat interaction service
- `bodybuilding_serverless_api/src/services/progress_service.py` - Progress tracking service
- `bodybuilding_serverless_api/src/services/service_factory.py` - Service dependency injection

## Chat Components
- `bodybuilding_serverless_api/src/services/chat/prompts` - AI prompt templates
- `bodybuilding_serverless_api/src/services/chat/generators` - Content generation components
- `bodybuilding_serverless_api/src/services/chat/orchestration` - Component orchestration

## AWS Integration
- `bodybuilding_serverless_api/src/aws/bedrockmanager.py` - Amazon Bedrock AI integration
- `bodybuilding_serverless_api/src/aws/dynamomanager.py` - DynamoDB data storage
- `bodybuilding_serverless_api/src/aws/s3manager.py` - S3 file storage
- `bodybuilding_serverless_api/src/aws/emailmanager.py` - Email notification service

## Authentication
- `bodybuilding_serverless_api/src/auth.py` - Authentication and authorization

## Key Transformations from Lesson Planner
- Renamed "lesson" → "plan" throughout the codebase
- Replaced "mathtilda" → "bodybuildr" in service names
- Updated DynamoDB tables: lessonsTable → plansTable, lessonVersionsTable → planVersionsTable
- Transformed educational terminology to fitness terminology:
  - "pedagogicalContext" → "trainingContext"
  - "standardsAddressed" → "fitnessGoals"
  - "markupProblemSets" → "workoutRoutines"
- Updated AI prompts to focus on bodybuilding expertise

## Implementation Status
- ✅ Schema Migration: Converted JSON schemas
- ✅ Resource Renaming: Updated resource names in serverless.yml
- ✅ Lambda Functions: Modified function names and handlers
- ✅ API Structure: Maintained consistent API structure with domain-specific naming
- ✅ Storage: Updated DynamoDB schemas for bodybuilding domain
- ✅ Chat Integration: Adapted chat functionality for workout plan context 