# Meeting Notes Example

## Input
```
Team sync meeting on January 28, 2026
Attendees: Alice, Bob, Charlie
Topics discussed:
- Q1 roadmap planning
- Technical debt priorities
- New hire onboarding process

Action items:
- Alice to review architecture proposal by Feb 1
- Bob to update deployment documentation
- Charlie to schedule security audit
```

## Output (Tana Paste)

Using your personal Tana schema with `#meeting` supertag and actual fields:

```tana-paste
%%tana%%
- Team Sync: Q1 Planning #meeting
  - Scheduled on:: [[2026-01-28]]
  - Actual (real) Date:: [[2026-01-28]]
  - Attendees:: [[Alice]], [[Bob]], [[Charlie]]
  - Owner:: [[David Delgado Vendrell]]
  - Context:: [[Work]]
  - Organization:: [[DDV Solutions]]
  - Topic:: [[Project Management]]
  - Event Format:: Online
  - Meeting link:: https://meet.google.com/abc-defg-hij
  - Agenda::
    - Q1 roadmap planning
    - Technical debt priorities
    - New hire onboarding process
  - Annotations::
    - Roadmap Discussion::
      - Agreed to focus on customer portal v2.0
      - Backend API refactoring is high priority
      - Timeline: Ship by end of March
    - Technical Debt::
      - Prioritize database optimization
      - Refactor authentication system
      - Update deprecated dependencies
    - Onboarding Process::
      - Create structured onboarding checklist
      - Assign buddy system for new hires
      - Schedule weekly check-ins for first month
  - ▶ Actions::
    - [[Review architecture proposal]] #task
    - [[Update deployment documentation]] #quickTask
    - [[Schedule security audit]] #quickTask
  - Related Notes::
    - [[Meeting notes: Q1 Planning details]] #meetingNote
```

Companion meeting note with detailed discussion:

```tana-paste
%%tana%%
- Meeting notes: Q1 Planning details #meetingNote
  - CODE Status:: [[📷 Captured]]
  - Context:: [[Work]]
  - Topic:: [[Q1 Planning]]
  - Related meeting:: [[Team Sync: Q1 Planning]]
  - Discussion notes::
    - Roadmap planning::
      - Agreed to focus on customer portal v2.0
      - Backend API refactoring is high priority
      - Timeline: Ship by end of March
      - Dependencies: Complete auth system first
    - Technical debt review::
      - Database optimization (priority 1)
      - Authentication system refactor (priority 2)
      - Update deprecated dependencies (priority 3)
      - Estimated time: 3 weeks total
    - Onboarding improvements::
      - Create structured checklist by Feb 15
      - Buddy system assignments by Feb 20
      - Weekly check-ins for 1st month of new hires
  - Action items created::
    - [[Review architecture proposal]] - Alice - Due: [[2026-02-01]]
    - [[Update deployment documentation]] - Bob - Due: [[2026-02-05]]
    - [[Schedule security audit]] - Charlie - Due: [[2026-02-10]]
```

## Variations

### Minimal format (quick capture)
```tana-paste
%%tana%%
- Team Sync #meeting
  - Date:: [[2026-01-28]]
  - Notes::
    - Discussed Q1 roadmap
    - Need to prioritize tech debt
    - [[Alice]] to review proposal
```

### With linked project references
```tana-paste
%%tana%%
- Team Sync #meeting
  - Date:: [[2026-01-28]]
  - Related to:: [[Project: Customer Portal]], [[Initiative: Q1 2026]]
  - Topics::
    - [[Topic: Roadmap Planning]]
    - [[Topic: Technical Debt]]
```
