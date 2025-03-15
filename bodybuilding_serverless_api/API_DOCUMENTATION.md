# Bodybuilding API Documentation

## Base URL
```
https://jpn7bdhehi.execute-api.us-east-1.amazonaws.com/dev
```

## API Endpoints

### Workout Plan Management

#### Create Plan
- **Endpoint**: `POST /plans/create`
- **Full URL**: `https://jpn7bdhehi.execute-api.us-east-1.amazonaws.com/dev/plans/create`
- **Description**: Creates a new workout plan for a user

#### Save Plan
- **Endpoint**: `POST /plans/save`
- **Full URL**: `https://jpn7bdhehi.execute-api.us-east-1.amazonaws.com/dev/plans/save`
- **Description**: Saves changes to an existing workout plan

#### List Plans
- **Endpoint**: `GET /plans/list`
- **Full URL**: `https://jpn7bdhehi.execute-api.us-east-1.amazonaws.com/dev/plans/list`
- **Description**: Lists all workout plans for a user

#### Get Plan Versions
- **Endpoint**: `GET /plans/versions/{planId}`
- **Full URL**: `https://jpn7bdhehi.execute-api.us-east-1.amazonaws.com/dev/plans/versions/{planId}`
- **Description**: Retrieves all versions of a specific workout plan

### User Profile Management

#### Create User
- **Endpoint**: `POST /users/create`
- **Full URL**: `https://jpn7bdhehi.execute-api.us-east-1.amazonaws.com/dev/users/create`
- **Description**: Creates a new user profile

#### Update User
- **Endpoint**: `PUT /users/{userId}`
- **Full URL**: `https://jpn7bdhehi.execute-api.us-east-1.amazonaws.com/dev/users/{userId}`
- **Description**: Updates an existing user profile

#### Get User
- **Endpoint**: `GET /users/{userId}`
- **Full URL**: `https://jpn7bdhehi.execute-api.us-east-1.amazonaws.com/dev/users/{userId}`
- **Description**: Retrieves a user profile

### Progress Tracking

#### Update Progress
- **Endpoint**: `POST /progress/{userId}`
- **Full URL**: `https://jpn7bdhehi.execute-api.us-east-1.amazonaws.com/dev/progress/{userId}`
- **Description**: Updates progress for a specific user

#### Get Progress
- **Endpoint**: `GET /progress/{userId}`
- **Full URL**: `https://jpn7bdhehi.execute-api.us-east-1.amazonaws.com/dev/progress/{userId}`
- **Description**: Retrieves progress history for a specific user

### Chat Functionality

#### Chat with Coach
- **Endpoint**: `POST /plans/chat`
- **Full URL**: `https://jpn7bdhehi.execute-api.us-east-1.amazonaws.com/dev/plans/chat`
- **Description**: Sends a message to the AI coach and receives a response

#### Get Chat History
- **Endpoint**: `GET /plans/{planId}/chat-history`
- **Full URL**: `https://jpn7bdhehi.execute-api.us-east-1.amazonaws.com/dev/plans/{planId}/chat-history`
- **Description**: Retrieves chat history for a specific workout plan

## Authentication

All endpoints require authentication. The API uses AWS Cognito for authentication and authorization.

## Deployment Information

- **Service**: bodybuildr-backend-infrastructure
- **Stage**: dev
- **Region**: us-east-1
- **Stack**: bodybuildr-backend-infrastructure-dev 