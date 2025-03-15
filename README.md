# Bodybuilding AI Coach API

A serverless API for an AI-powered bodybuilding coach that provides personalized workout plans, progress tracking, and real-time feedback.

## Features

- Personalized workout plan generation
- Progress tracking and metrics
- AI coach chat interface
- User profile management
- Plan versioning and history
- Real-time workout feedback

## Project Structure

```
bodybuilding_serverless_api/
├── src/
│   ├── models/         # Data models
│   ├── services/       # Business logic
│   │   ├── chat/      # AI chat functionality
│   │   └── core/      # Core services
│   └── aws/           # AWS service wrappers
├── schema/            # JSON schemas
├── tests/             # Test suite
└── config files       # Configuration files
```

## Documentation

Detailed documentation is available in the `docs` directory:
- [Bodybuilding API Documentation](../docs/bodybuilding_api_documentation.md) - Complete API structure and components
- [Implementation Plan](../docs/IMPLEMENTATION_PLAN.md) - Project implementation phases
- [DynamoDB Tables Comparison](../docs/dynamodb_tables_comparison.md) - Database schema changes
- [Handler Comparison](../docs/handler_comparison.md) - API handler transformations

## Setup

1. Install dependencies:
```bash
npm install -g serverless
pip install -r requirements.txt
```

2. Configure AWS credentials:
```bash
serverless config credentials --provider aws --key YOUR_KEY --secret YOUR_SECRET
```

3. Deploy:
```bash
serverless deploy --stage dev
```

## Development

- Use `serverless offline` for local development
- Run tests with `pytest`
- Format code with `black`

## API Endpoints

### Plans
- POST /plans/create - Create new workout plan
- POST /plans/save - Save plan changes
- GET /plans/list - List user's plans
- GET /plans/versions/{planId} - Get plan versions

### Users
- POST /users/create - Create user profile
- PUT /users/{userId} - Update user profile

### Progress
- POST /progress/{userId} - Update progress
- GET /progress/{userId} - Get progress history

### Chat
- POST /plans/chat - Chat with AI coach
- GET /plans/{planId}/chat-history - Get chat history

## Environment Variables

Required environment variables:
- `STAGE` - Deployment stage (dev/prod)
- `COGNITO` - Cognito secret name
- Various table names (see serverless.yml)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License 