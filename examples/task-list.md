# Task List Example

## Input
```
Project tasks:
1. Set up development environment (high priority)
2. Implement user authentication
3. Create database schema
4. Write API documentation
5. Deploy to staging (blocked by #2 and #3)
```

## Output (Tana Paste)

Using your personal Tana schema with `#task` and `#quickTask` supertags:

```tana-paste
%%tana%%
- Set up development environment #task
  - Context:: [[Work]]
  - Topic:: [[Software Development]]
  - Task State:: [[📅 Not started]]
  - Energy Demand:: High
  - Type:: Setup
  - Time Sector:: [[⚪ Available]]
  - Due Date:: [[2026-02-01]]
  - Scheduled on:: [[2026-02-01]]
  - Annotations::
    - Install Docker and dependencies
    - Configure environment variables
    - Set up local database
    - Verify API endpoints work
    - Priority: High
    - Estimated effort: 2h
  - TT - Start Time:: 09:00
  - TT - Total Time:: 2h

- Implement user authentication #task
  - Context:: [[Work]]
  - Topic:: [[Backend Development]]
  - Task State:: [[🔄 In Progress]]
  - Energy Demand:: High
  - Type:: Development
  - Time Sector:: [[⚪ Available]]
  - Due Date:: [[2026-02-05]]
  - Scheduled on:: [[2026-02-02]]
  - Annotations::
    - Assigned to: Alice
    - Related project: Customer Portal
    - JWT token generation
    - Login/logout endpoints
    - Password hashing with bcrypt
    - Refresh token mechanism
    - Subtasks: Design auth flow, Implement JWT service, Add API endpoints, Write tests
    - Estimated effort: 5h
  - TT - Start Time:: 10:00
  - TT - Total Time:: 5h

- Create database schema #task
  - Context:: [[Work]]
  - Topic:: [[Database Design]]
  - Task State:: [[📅 Not started]]
  - Energy Demand:: Medium
  - Type:: Design
  - Time Sector:: [[⚪ Available]]
  - Due Date:: [[2026-02-03]]
  - Scheduled on:: [[2026-02-03]]
  - Annotations::
    - Assigned to: Bob
    - Related project: Customer Portal
    - Design entity relationships
    - Create migration scripts
    - Add indexes for performance
    - Document schema
    - Depends on: Implement user authentication
    - Estimated effort: 3h

- Write API documentation #quickTask
  - Context:: [[Work]]
  - Topic:: [[Documentation]]
  - Task State:: [[📅 Not started]]
  - Energy Demand:: Low
  - Annotations::
    - Related project: Customer Portal
    - Document all endpoints
    - Add request/response examples
    - Include authentication flow
    - Generate OpenAPI spec
    - Estimated effort: 4h

- Deploy to staging #task
  - Context:: [[Work]]
  - Topic:: [[DevOps]]
  - Task State:: [[⏸ Blocked]]
  - Energy Demand:: Medium
  - Type:: Deployment
  - Time Sector:: [[⚪ Available]]
  - Due Date:: [[2026-02-12]]
  - Scheduled on:: [[2026-02-12]]
  - Annotations::
    - Assigned to: Charlie
    - Related project: Customer Portal
    - Blocked by: Implement user authentication, Create database schema
    - Configure staging environment
    - Run database migrations
    - Deploy application
    - Verify functionality
    - Share staging URL with team
    - Estimated effort: 2h
```

## Variations

### Simple task list (no metadata)
```tana-paste
%%tana%%
- Tasks for Customer Portal #project
  - Set up dev environment #task
  - Implement authentication #task
  - Create database schema #task
  - Write API docs #task
  - Deploy to staging #task
```

### With sprint/iteration
```tana-paste
%%tana%%
- Sprint 5: Authentication & Database #sprint
  - Start date:: [[2026-02-01]]
  - End date:: [[2026-02-14]]
  - Tasks::
    - [[Set up development environment]]
    - [[Implement user authentication]]
    - [[Create database schema]]
  - Goals::
    - Complete auth implementation
    - Database schema finalized
    - All tests passing
```

### Grouped by status
```tana-paste
%%tana%%
- Task Board: Customer Portal #taskboard
  - Todo::
    - [[Set up development environment]]
    - [[Create database schema]]
    - [[Write API documentation]]
  - In Progress::
    - [[Implement user authentication]]
  - Blocked::
    - [[Deploy to staging]]
  - Done::
    - [[Project kickoff meeting]]
    - [[Requirements gathering]]
```

## Advanced: Task with acceptance criteria

```tana-paste
%%tana%%
- Implement user authentication #task
  - Status:: Todo
  - Assigned to:: [[Alice]]
  - Priority:: High
  - Due date:: [[2026-02-05]]
  - Description::
    - Full JWT-based authentication system
  - Acceptance Criteria::
    - Users can register with email and password
    - Users can log in and receive JWT token
    - Token expires after 24 hours
    - Refresh token mechanism works
    - Passwords are securely hashed
    - All endpoints properly secured
    - Unit tests cover edge cases
    - Integration tests verify flow
  - Technical Notes::
    - Use bcrypt for password hashing
    - JWT secret stored in environment variable
    - Refresh tokens stored in Redis
  - Resources::
    - [[Documentation: JWT Best Practices]]
    - https://jwt.io/introduction
```
