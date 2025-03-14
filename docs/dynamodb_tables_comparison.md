# DynamoDB Tables Comparison: Bodybuilding vs Lesson Implementation

## Overview

This document provides a detailed comparison of the DynamoDB tables between the Bodybuilding implementation and the original Lesson implementation, highlighting their structure, purpose, and key differences.

## Table Mapping

| Lesson Implementation | Bodybuilding Implementation | Purpose |
|----------------------|----------------------------|---------|
| mathtilda-lesson-table-${stage} | bodybuildr-plans-table-${stage} | Stores the main resources (lessons/workout plans) |
| mathtilda-lessonversions-${stage} | bodybuildr-planversions-${stage} | Tracks versions of the main resources |
| mathtilda-profiles-table-${stage} | bodybuildr-users-table-${stage} | Manages user profiles/information |
| mathtilda-chat-history-${stage} | bodybuildr-chat-history-${stage} | Stores chat interactions |
| mathtilda-files-table-${stage} | bodybuildr-files-table-${stage} | Tracks file metadata |
| N/A | bodybuildr-progress-${stage} | New table for tracking fitness progress |

## Detailed Table Comparison

### Main Resource Tables

#### Lesson Table (mathtilda-lesson-table-${stage})
- **Primary Key**: Composite key of email (HASH) and lessonId (RANGE)
- **Attributes**:
  - email (String) - User's email
  - lessonId (String) - Unique identifier for the lesson
  - Additional attributes likely include: title, subject, grade, content, createdAt, updatedAt

#### Plans Table (bodybuildr-plans-table-${stage})
- **Primary Key**: Composite key of userId (HASH) and planId (RANGE)
- **Attributes**:
  - userId (String) - User's ID
  - planId (String) - Unique identifier for the workout plan
  - Additional attributes likely include: title, goals, experience level, available days, createdAt, updatedAt
- **Key Differences**:
  - Uses userId instead of email as the partition key
  - Simplified schema compared to the lesson table
  - Domain-specific attributes focused on fitness rather than education

### Version Tracking Tables

#### Lesson Versions Table (mathtilda-lessonversions-${stage})
- **Primary Key**: Composite key of lessonId (HASH) and profileId (RANGE)
- **Global Secondary Indexes**:
  - EmailIndex: email (HASH) and timestamp (RANGE)
  - VersionIndex: lessonId (HASH) and version (RANGE)
- **Attributes**:
  - lessonId (String) - Lesson identifier
  - profileId (String) - Profile identifier
  - version (Number) - Version number
  - email (String) - User's email
  - timestamp (String) - When the version was created
  - Additional attributes projected in GSIs: content, title, grade, subject, etc.
- **Access Patterns**:
  - Retrieve all versions of a lesson
  - Retrieve all lessons for a specific email
  - Retrieve specific version of a lesson

#### Plan Versions Table (bodybuildr-planversions-${stage})
- **Primary Key**: Composite key of planId (HASH) and version (RANGE)
- **Attributes**:
  - planId (String) - Plan identifier
  - version (Number) - Version number
  - Likely includes: content, title, goals, createdAt
- **Key Differences**:
  - Simplified schema with fewer attributes
  - No secondary indexes, suggesting more direct access patterns
  - Uses only planId and version for the primary key, removing the profile association
  - Optimized for retrieving version history of a specific plan
- **Access Patterns**:
  - Retrieve all versions of a specific plan
  - Retrieve a specific version of a plan

### User Management Tables

#### Profiles Table (mathtilda-profiles-table-${stage})
- **Primary Key**: Composite key of email (HASH) and profilename (RANGE)
- **Attributes**:
  - email (String) - User's email
  - profilename (String) - Name of the profile
  - Likely includes: grade, subject preferences, learning style, createdAt, updatedAt
- **Access Patterns**:
  - Retrieve all profiles for a user
  - Retrieve a specific profile by name

#### Users Table (bodybuildr-users-table-${stage})
- **Primary Key**: Simple key of userId (HASH)
- **Attributes**:
  - userId (String) - User's ID
  - Likely includes: name, age, height, weight, fitness level, goals, createdAt, updatedAt
- **Key Differences**:
  - Uses a simple primary key instead of a composite key
  - No concept of multiple profiles per user (one user = one fitness profile)
  - Uses userId instead of email as the identifier
  - Contains fitness-specific attributes
- **Access Patterns**:
  - Direct lookup of user information by userId

### Chat History Tables

#### Chat History Table (Lesson) (mathtilda-chat-history-${stage})
- **Primary Key**: Composite key of lessonId (HASH) and timestamp (RANGE)
- **Global Secondary Index**:
  - EmailIndex: email (HASH) and timestamp (RANGE)
- **Attributes**:
  - email (String) - User's email
  - lessonId (String) - Lesson identifier
  - timestamp (String) - When the chat message was sent
  - Likely includes: message, role (user/system), component (if applicable)
- **Access Patterns**:
  - Retrieve chat history for a specific lesson
  - Retrieve all chat history for a user across lessons

#### Chat History Table (Bodybuilding) (bodybuildr-chat-history-${stage})
- **Primary Key**: Composite key of userId_planId (HASH) and timestamp (RANGE)
- **Attributes**:
  - userId_planId (String) - Composite string of user ID and plan ID
  - timestamp (Number) - When the chat message was sent (as a number)
  - Likely includes: message, role (user/coach), context (workout, nutrition, etc.)
- **Key Differences**:
  - Uses a composite string key (userId_planId) instead of separate fields
  - Uses numeric timestamp instead of string for better sorting and range queries
  - No secondary indexes, suggesting more focused query patterns
  - May include fitness-specific context markers
- **Access Patterns**:
  - Retrieve chat history for a specific user-plan combination
  - Time-ordered retrieval of messages

### File Management Tables

#### Files Table (Both implementations)
- Both implementations have a files table with similar structure
- Used to track file metadata for files stored in S3
- **Attributes likely include**:
  - File path/name
  - File type
  - Upload timestamp
  - User/owner reference
  - Size
  - Content type
- **Access Patterns**:
  - Retrieve file metadata by path
  - List files for a specific user

### Progress Tracking Table (Bodybuilding-specific)

#### Progress Table (bodybuildr-progress-${stage})
- **Primary Key**: Composite key of userId (HASH) and date (RANGE)
- **Attributes**:
  - userId (String) - User's ID
  - date (String) - Date of the progress entry
  - Likely includes: workouts completed, sets, reps, weights, measurements (weight, body fat %, etc.), nutrition data
- **Purpose**: Tracks fitness progress over time, including workouts completed, measurements, and other fitness metrics
- **Note**: This table has no equivalent in the Lesson implementation as it's specific to the fitness domain
- **Access Patterns**:
  - Retrieve progress entries for a specific date
  - Retrieve progress history for a user within a date range
  - Track changes in specific metrics over time

## Key Architectural Differences

### 1. Authentication and User Identification:
- **Lesson implementation** uses email as the primary user identifier
  - Pros: Easy to understand and relate to real users
  - Cons: Emails can change, potentially requiring complex update operations
- **Bodybuilding implementation** uses userId (likely from Cognito)
  - Pros: Stable identifier that won't change, better security
  - Cons: Less human-readable, requires lookup to associate with user information

### 2. Data Modeling Approach:
- **Lesson implementation** has more complex relationships with profiles and lessons
  - Supports multiple profiles per user (e.g., different student profiles)
  - More normalized data model with separate tables for different entity types
- **Bodybuilding implementation** has a more streamlined approach with direct user-to-plan relationships
  - One user = one fitness profile
  - Denormalized in some areas for performance
  - Domain-specific tables for fitness tracking

### 3. Secondary Indexes:
- **Lesson implementation** makes extensive use of GSIs for querying data in different ways
  - Supports more complex query patterns
  - Higher cost due to index maintenance
  - More flexible access patterns
- **Bodybuilding implementation** has fewer or no GSIs, suggesting simpler query patterns
  - More cost-effective
  - Potentially faster for primary access patterns
  - May require client-side filtering for some queries

### 4. Domain-Specific Tables:
- **Bodybuilding implementation** adds the Progress table for fitness tracking
  - Enables time-series tracking of fitness metrics
  - Supports progress visualization and analysis
  - Allows for workout completion tracking
- This reflects the domain-specific requirements of a fitness application
  - Progress tracking is central to fitness applications
  - Time-based analysis is important for fitness goals

### 5. Timestamp Handling:
- **Lesson implementation** uses string timestamps
  - Easier to read and debug
  - May require additional parsing for range queries
- **Bodybuilding implementation** uses numeric timestamps in some tables
  - Better performance for range queries and sorting
  - More compact storage
  - Easier to perform date calculations

### 6. Composite Keys vs. Simple Keys:
- **Lesson implementation** uses more composite keys
  - Enables hierarchical data organization
  - Supports more complex relationships
- **Bodybuilding implementation** simplifies some key structures
  - Uses composite strings (e.g., userId_planId) instead of separate attributes
  - Reduces the need for GSIs in some cases

## Implementation Considerations

### Data Migration
When migrating from the Lesson to Bodybuilding implementation, data transformation would be needed to:
- Convert email-based keys to userId-based keys
  - Requires mapping between emails and user IDs
  - May need temporary lookup tables during migration
- Restructure the version history data
  - Simplify the version tracking schema
  - Ensure version continuity during migration
- Adapt chat history to the new composite key format
  - Transform separate keys to composite string keys
  - Convert string timestamps to numeric format
- Handle domain-specific data transformation
  - Map educational concepts to fitness concepts
  - Preserve user-generated content where applicable

### Query Patterns
The different table structures suggest different query patterns:
- **Lesson implementation** supports more complex queries via GSIs
  - Can query lessons by email, profile, or lesson ID
  - Supports time-based queries across multiple dimensions
- **Bodybuilding implementation** focuses on direct access patterns
  - Optimized for retrieving a user's plans
  - Streamlined for time-series progress data
  - Simplified chat history retrieval

### Scalability
Both implementations use pay-per-request billing mode, but:
- **Bodybuilding implementation's** simpler key structure may provide better partition distribution
  - Less risk of hot partitions
  - More predictable performance under load
- Fewer GSIs in the Bodybuilding implementation may reduce costs
  - Lower write capacity requirements
  - Less index storage overhead
- Progress table designed for time-series data may scale better for fitness tracking
  - Efficient for date-range queries
  - Natural partitioning by user

### Domain Adaptation
The addition of the Progress table demonstrates how the data model was adapted to fit the fitness domain's specific requirements:
- Time-series data is crucial for fitness tracking
  - Regular progress updates
  - Trend analysis over time
- User-centric design reflects individual fitness journeys
  - Personal progress tracking
  - Individual workout plans
- Simplified profile model matches fitness domain expectations
  - One user = one fitness profile
  - Comprehensive user attributes

### Performance Optimizations
- **Bodybuilding implementation** shows several performance-focused changes:
  - Use of numeric timestamps for better range query performance
  - Composite string keys to reduce the need for GSIs
  - Simplified table structures for more direct access patterns
  - Domain-specific denormalization where appropriate

## Conclusion

The DynamoDB table structure transformation from the Lesson to Bodybuilding implementation shows a thoughtful adaptation of the data model to fit the new domain while maintaining the core functionality. The Bodybuilding implementation simplifies some aspects of the data model, adds domain-specific tables, and updates the authentication approach to use user IDs instead of emails.

These changes reflect not just a renaming of resources but a deeper understanding of the different requirements between educational and fitness applications. The streamlined data model in the Bodybuilding implementation suggests a focus on performance, cost-efficiency, and domain-specific functionality, while preserving the core capabilities of the original system.

The migration path between these two implementations would require careful planning, especially around user identity mapping and data transformation, but the architectural similarities provide a solid foundation for such a migration. The domain-specific additions, particularly the Progress table, demonstrate how DynamoDB's flexible schema can be leveraged to support different application domains while maintaining a consistent architectural approach. 