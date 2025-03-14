# Template Usage Rules

## Core Principle
The `serverless_api_lesson/` directory serves as a READ-ONLY template and reference implementation. It should NEVER be modified, copied into, or deleted.

## Template Directory Rules

### ❌ NEVER:
1. Add files to `serverless_api_lesson/`
2. Modify files in `serverless_api_lesson/`
3. Delete files from `serverless_api_lesson/`
4. Create symbolic links into `serverless_api_lesson/`
5. Copy partial implementations from template without proper adaptation

### ✅ ALLOWED:
1. Read files from `serverless_api_lesson/` for reference
2. Use as architectural guidance
3. Copy and adapt code patterns with proper domain translation
4. Reference implementation approaches

## Template Reference Files

### Key Reference Files
1. `serverless.yml` - Base serverless configuration
2. `lesson.json` - Data structure template (to be adapted to bodybuilding.json)
3. `lesson_chat.py` - Chat interface reference
4. `component_orchestrator.py` - Component update patterns
5. `bedrockmanager.py` - AWS Bedrock integration

### Usage Pattern
When referencing these files:
1. Understand the core pattern
2. Translate to bodybuilding domain
3. Implement in new project structure
4. Document adaptations made

## Implementation Guidelines

### Code Migration
- Create equivalent files in new project
- Adapt naming conventions to bodybuilding domain
- Maintain similar architectural patterns
- Update all domain-specific logic

### Testing
- Create new tests for bodybuilding domain
- Don't copy test cases directly
- Maintain similar test structure
- Add domain-specific test cases

### Documentation
- Reference template patterns in comments
- Document major architectural decisions
- Explain deviations from template
- Maintain clear separation in docs

## Version Control

### Repository Structure
- Keep template in separate branch
- Never merge template changes
- Document template version used
- Track adaptations in commit messages 