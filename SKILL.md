---
name: tana-paste
description: Convert any content (text, tasks, BIM data, notes) to valid Tana Paste format for import into Tana.inc
disable-model-invocation: true
user-invocable: true
argument-hint: [content-to-convert]
allowed-tools: Read, WebFetch
model: sonnet
---

# Tana Paste Generator

Convert content directly to valid Tana Paste format for import into Tana.inc.

## Overview

Tana Paste is a structured text format that Tana.inc uses to import nodes, tags, and relationships. This skill converts various types of content into properly formatted Tana Paste.

## Supported Content Types

1. **Plain text/notes** - Convert to hierarchical nodes
2. **Task lists** - Convert to Tana tasks with status
3. **Meeting notes** - Structure with attendees, agenda, actions
4. **BIM/IFC validation results** - Format validation reports with proper structure
5. **Project documentation** - Convert docs to searchable Tana nodes
6. **Research notes** - Create linked knowledge nodes
7. **Any structured data** - Parse and format automatically

## Instructions

When invoked:

1. **Analyze the input content** provided by the user (from $ARGUMENTS, selected text, or file path)
2. **Identify the content type** and optimal structure for Tana
3. **Generate valid Tana Paste** following the specification in [reference.md](reference.md)
4. **Output the result** as a code block that the user can copy directly

## User's Personal Tana Schema

**IMPORTANT:** Use the user's actual supertags and fields defined in their Tana workspace:

### Supertags Available
- `#task` - Full tasks with timesheet tracking (inherits from #todo, #[[task (base type)]], #timed-task)
- `#quickTask` - Brief, straightforward tasks (inherits from #todo, #[[task (base type)]])
- `#project` - Projects (inherits from #[[project (base type)]])
- `#meeting` - Meetings/events (inherits from #[[meeting (base type)]])
- `#meetingNote` - Meeting notes
- `#note` - General notes
- `#person` - People
- `#client` - Clients (inherits from #person)
- `#organization` - Organizations
- `#area` - Areas of responsibility
- `#topic` - Topics/concepts

**Note:** `#todo` is only used as a parent tag for inheritance - use `#task` or `#quickTask` directly.

### Task (#task) Fields - For standard tasks
- `Context::` - Context reference
- `Topic::` - Topic reference
- `Task State::` - Use values like `[[📅 Not started]]`, `[[✅ Done]]`
- `Energy Demand::` - Low/Medium/High
- `Annotations::` - Additional notes
- `Type::` - Task type classification
- `Time Sector::` - Time allocation (e.g., `[[⚪ Available]]`)
- `Due Date::` - Due date reference
- `Scheduled on::` - Scheduled date reference
- `Related decisions::` - Decision references
- `Subtask of::` - Parent task reference
- `Done time::` - Completion timestamp
- `TT - Start Time::` - Timesheet start time
- `TT - Total Time::` - Timesheet total duration

### Quick Task (#quickTask) Fields - For simple, fast tasks
- `Context::` - Context reference
- `Topic::` - Topic reference
- `Task State::` - Use values like `[[📅 Not started]]`, `[[✅ Done]]`
- `Energy Demand::` - Low/Medium/High
- `Annotations::` - Additional notes
- `Done time::` - Completion timestamp

### Project (#project) Fields
- `Area::` - Area reference
- `Project Index Number::` - Unique identifier
- `Project Code::` - Short code (e.g., Pr ABC123)
- `Project Title::` - Full title
- `Project Client::` - Client reference
- `Time Sector::` - Time allocation (e.g., `[[⚪ Available]]`)
- `Project Start::` - Start date
- `Project Type::` - Type classification
- `Project Goal(s)::` - Goals list
- `Project Outcomes::` - Expected outcomes
- `Project Requirements::` - Requirements list
- `Stakeholders::` - People references

### Meeting (#meeting) Fields
- `Scheduled on::` - Date/time
- `Actual (real) Date::` - Actual date if different
- `Attendees::` - People references
- `Owner::` - Meeting organizer
- `Context::` - Context reference
- `Organization::` - Organization reference
- `Topic::` - Topic reference
- `Agenda::` - Agenda items
- `▶ Actions::` - Action items (can reference #task or #quickTask nodes)
- `Meeting link::` - URL
- `Event Format::` - Online/In-person
- `Location::` - Physical or virtual location

### Meeting Note (#meetingNote) Fields
- `CODE Status::` - Use `[[📷 Captured]]` or similar
- `Context::` - Context reference
- `Topic::` - Topic reference

### General Note (#note) Fields
- `Context::` - Context reference
- `Resource Category::` - Category reference
- `Topic::` - Topic reference
- `CODE Status::` - Status indicator (e.g., `[[📷 Captured]]`)

### Person Fields
- `Works in/for::` - Organization reference
- `Role::` - Job title
- `Email::` - Email address
- `Phone::` - Phone number

## Format Guidelines

### Task Example (#task for standard tasks with timesheet)
```
%%tana%%
- Fix authentication bug #task
  - Context:: [[Work]]
  - Topic:: [[Backend Development]]
  - Task State:: [[📅 Not started]]
  - Energy Demand:: High
  - Type:: Bug Fix
  - Time Sector:: [[⚪ Available]]
  - Due Date:: [[2026-02-05]]
  - Scheduled on:: [[2026-02-01]]
  - Annotations::
    - Requires database migration
    - Test with staging environment first
  - TT - Start Time:: 09:00
  - TT - Total Time:: 3h
```

### Quick Task Example (#quickTask for simple, fast tasks)
```
%%tana%%
- Update README file #quickTask
  - Context:: [[Work]]
  - Topic:: [[Documentation]]
  - Task State:: [[📅 Not started]]
  - Energy Demand:: Low
  - Annotations::
    - Add installation instructions
    - Update API examples
```

### Project Example
```
%%tana%%
- BIM Validation Tool #project
  - Project Code:: Pr VAL01
  - Project Title:: IDS Validation Tool Development
  - Project Client:: [[Client ABC]]
  - Area:: [[A Digital Systems]]
  - Project Start:: [[2026-01-28]]
  - Project Type:: Software Development
  - Project Goal(s)::
    - Automate IDS validation workflow
    - Integrate with IFC model checker
  - Project Requirements::
    - Support IDS v1.0 specification
    - Generate BCF issues from validation errors
  - Stakeholders:: [[David Delgado Vendrell]], [[Client ABC]]
```

### Meeting Example
```
%%tana%%
- Weekly Project Sync #meeting
  - Scheduled on:: [[2026-01-28]]
  - Attendees:: [[David Delgado Vendrell]], [[Client ABC]], [[Team Member]]
  - Owner:: [[David Delgado Vendrell]]
  - Context:: [[Work]]
  - Organization:: [[DDV Solutions]]
  - Topic:: [[Project Management]]
  - Agenda::
    - Review project progress
    - Discuss blockers
    - Plan next sprint
  - ▶ Actions::
    - [[Fix validation bug]] #task
    - [[Update documentation]] #quickTask
  - Meeting link:: https://meet.google.com/abc-defg-hij
```

### Meeting Note Example
```
%%tana%%
- Notes from kickoff meeting #meetingNote
  - CODE Status:: [[📷 Captured]]
  - Context:: [[Work]]
  - Topic:: [[Project Kickoff]]
  - Key discussion points::
    - Project timeline confirmed
    - Milestones agreed upon
    - Team roles assigned
```

## Special Characters

Handle special characters according to Tana Paste spec:
- Use `#[[Supertag Name]]` for supertags with spaces/special chars
- Use `\` to escape special characters in node content
- Use `%%tana%%` header only once at the beginning

## Output Format

Always output as:

```tana-paste
%%tana%%
[Your generated Tana Paste content here]
```

Include a brief explanation of the structure created before the code block.

## Examples

For common patterns, see [examples/](examples/) directory:
- [meeting-notes.md](examples/meeting-notes.md) - Meeting structure
- [task-list.md](examples/task-list.md) - Task management
- [bim-validation.md](examples/bim-validation.md) - BIM validation reports
- [research-notes.md](examples/research-notes.md) - Knowledge capture

## Error Handling

If content cannot be automatically structured:
1. Ask the user clarifying questions about desired structure
2. Suggest multiple structure options
3. Allow manual refinement

## Reference Documentation

For detailed Tana Paste specification, see:
- [reference.md](reference.md) - Full format specification
- https://tana.inc/docs/tana-paste
- https://github.com/tanainc/tana-paste-examples

## Important Notes

- Always start output with `%%tana%%` header
- Use proper indentation (2 spaces per level)
- Validate field names follow Tana conventions
- Test references are properly formatted with `[[...]]`
- Supertags use `#tag` or `#[[Tag Name]]` format
- Fields use `Field Name::` format
