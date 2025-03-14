# Bodybuilding AI Coach - Implementation Plan

## Overview
This document outlines the implementation strategy for converting the lesson planner template into a bodybuilding coach AI system. The original template (`serverless_api_lesson/`) serves as a reference only and will never be modified.

## Project Structure
```bash
bodybuilding_serverless_api/
├── src/
│   ├── models/
│   │   ├── plan.py           # Data models for bodybuilding plan
│   │   ├── profile.py        # Athlete profile models
│   │   └── workout.py        # Workout specific models
│   ├── services/
│   │   ├── chat/
│   │   │   ├── orchestration/
│   │   │   │   └── plan_orchestrator.py
│   │   │   └── prompts/
│   │   │       ├── workout_prompts.py
│   │   │       ├── nutrition_prompts.py
│   │   │       └── system_prompts.py
│   │   └── core/
│   │       ├── plan_service.py
│   │       ├── workout_service.py
│   │       └── nutrition_service.py
│   └── aws/
│       └── bedrock_manager.py
├── schema/
│   └── json/
│       ├── plan_schema.json
│       └── validation/
└── tests/
```

## Implementation Phases

### Phase 1: Foundation (Week 1)
- [ ] Project structure setup
- [ ] Basic AWS infrastructure
- [ ] Core models implementation
- [ ] Database schema setup

### Phase 2: Core Services (Week 2)
- [ ] Plan service implementation
- [ ] Basic chat functionality
- [ ] Profile management
- [ ] Progress tracking

### Phase 3: AI Integration (Week 3)
- [ ] Bedrock integration
- [ ] Prompt engineering
- [ ] Plan generation
- [ ] Chat intelligence

### Phase 4: Enhancement (Week 4)
- [ ] Advanced features
- [ ] Testing & optimization
- [ ] Documentation
- [ ] Deployment pipeline

## Core Components

### Data Models
1. **Plan Model**
   - Full plan structure matching bodybuilding.json
   - Versioning support
   - State management (draft, active, completed)

2. **Profile Model**
   - Current stats tracking
   - Goals management
   - Progress history

3. **Workout Model**
   - Exercise definitions
   - Split structures
   - Progression schemes

### AWS Infrastructure
```yaml
# serverless.yml key components
service: bodybuildr

provider:
  name: aws
  runtime: python3.11
  
functions:
  createPlan:
    handler: src/handlers/plan_handler.create
  updatePlan:
    handler: src/handlers/plan_handler.update
  chatWithCoach:
    handler: src/handlers/chat_handler.process
```

### Database Schema
```typescript
// DynamoDB Tables
PlansTable {
  PK: userId
  SK: planId
  planData: Object
  version: Number
  status: String
}

ChatHistoryTable {
  PK: userId_planId
  SK: timestamp
  message: String
  role: String
  changes: Object
}

ProgressTable {
  PK: userId_planId
  SK: date
  metrics: Object
  notes: String
}
```

## API Endpoints

```typescript
// Core Endpoints
POST /plan/create
PUT /plan/{planId}
GET /plan/{planId}
POST /plan/{planId}/chat
PUT /plan/{planId}/progress

// Supporting Endpoints
GET /exercises
GET /nutrition/templates
GET /progress/{userId}
```

## Key Differences from Template

1. **Domain Specific**
   - All educational concepts replaced with bodybuilding terminology
   - Workout-focused component structure
   - Progress tracking emphasis

2. **Data Structure**
   - Complex nested JSON for workouts
   - Detailed progress metrics
   - Supplement and nutrition tracking

3. **AI Interaction**
   - Workout-specific prompts
   - Form check capabilities
   - Progress-based adjustments 