# Tana Paste Format - Complete Reference

## Official Documentation
- **Tana Paste Docs**: https://tana.inc/docs/tana-paste
- **Examples Repository**: https://github.com/tanainc/tana-paste-examples
- **FAQ**: https://tana.inc/faq

## Format Overview

Tana Paste is a plain text format that represents hierarchical node structures for import into Tana. It uses indentation to represent hierarchy and special syntax for metadata.

## Basic Syntax

### Header
Every Tana Paste content must start with:
```
%%tana%%
```

### Nodes
Nodes are created with bullet points (`-`) and indentation:
```
%%tana%%
- Parent node
  - Child node
    - Grandchild node
  - Another child
```

**Indentation rules:**
- Use 2 spaces per indentation level
- Consistent indentation is critical
- Do NOT use tabs

### Supertags

Supertags classify nodes and provide structure.

**Simple supertags** (no spaces/special chars):
```
- My task #task
- Person: John Doe #person
```

**Supertags with spaces or special chars**:
```
- Project meeting #[[Meeting Notes]]
- Research topic #[[Academic Research]]
```

### Fields

Fields add metadata to nodes using `Field Name::` syntax:

**Simple field values:**
```
- Task title #task
  - Status:: Todo
  - Priority:: High
  - Estimate:: 3h
```

**Field with date:**
```
- Meeting #meeting
  - Date:: [[2026-01-28]]
  - Scheduled for:: [[2026-02-05]]
```

**Field with multiple values:**
```
- Project #project
  - Tags:: #backend, #api, #python
  - Team:: [[Alice]], [[Bob]], [[Charlie]]
```

**Field with paragraph content:**
```
- Task #task
  - Description::
    - This is a multi-line description
    - It can span several lines
    - Each line is indented under the field
```

### References

Create links between nodes using double brackets `[[...]]`:

**Reference to another node:**
```
- Task A #task
  - Depends on:: [[Task B]]
  - Assigned to:: [[John Doe]]
```

**Inline references:**
```
- Meeting notes
  - Discussed [[Project Alpha]] with [[Jane Smith]]
```

### Date References

Dates use the same `[[...]]` syntax:
```
- Task #task
  - Due date:: [[2026-01-30]]
  - Created:: [[2026-01-28]]
```

**Date format:** `YYYY-MM-DD` inside `[[...]]`

### URLs

URLs are automatically recognized:
```
- Research topic
  - Source:: https://example.com/article
  - Documentation:: https://docs.example.com
```

### Code Blocks

Use triple backticks for code:
```
- Solution #tech-note
  - Code::
    - ```python
      def hello():
          return "Hello, world!"
      ```
```

## Advanced Features

### Search Nodes

Create dynamic search nodes (see: https://tana.inc/faq#can-i-create-search-nodes-using-tana-paste):

```
- Search: All open tasks
  - Query:: #task AND Status::Todo
```

### Node Movement Commands

Move nodes to fields automatically (see: https://tana.inc/faq#can-a-command-move-the-current-node-to-a-field-of-a-new-node):

```
- Command: Archive completed tasks
  - Move:: #task WHERE Status::Done TO [[Archive]]
```

## Special Characters

### Escaping

Use backslash `\` to escape special characters:
```
- Text with \# hash but not a tag
- Text with \[\[brackets\]\] but not a reference
```

### Supertags with Special Characters

When supertags contain non-alphanumeric characters, use `#[[...]]`:
```
- Note #[[2024 Q1 Review]]
- Item #[[Priority: High]]
```

**Reference:** https://tana.inc/faq#how-to-use-tana-paste-with-supertags-that-have-non-alphanumeric-characters

## Common Patterns

### Task Management

```
%%tana%%
- Implement authentication #task
  - Status:: In Progress
  - Priority:: High
  - Assigned to:: [[John Doe]]
  - Due date:: [[2026-02-15]]
  - Tags:: #backend, #security
  - Subtasks::
    - [[Design auth flow]]
    - [[Implement JWT tokens]]
    - [[Add tests]]
```

### Meeting Notes

```
%%tana%%
- Weekly Team Sync #meeting
  - Date:: [[2026-01-28]]
  - Attendees:: [[Alice]], [[Bob]], [[Charlie]]
  - Agenda::
    - Project status update
    - Roadmap planning
    - Q&A
  - Action items::
    - [[Task: Review PRs]] - Assigned to:: [[Alice]]
    - [[Task: Update docs]] - Assigned to:: [[Bob]]
  - Next meeting:: [[2026-02-04]]
```

### Project Documentation

```
%%tana%%
- Project: Customer Portal #project
  - Status:: Active
  - Owner:: [[Product Team]]
  - Start date:: [[2026-01-15]]
  - Tech stack:: #react, #typescript, #nodejs
  - Documentation::
    - Architecture overview
    - API endpoints
    - Deployment process
  - Related::
    - [[Backend API Project]]
    - [[Design System]]
```

### Research/Knowledge Notes

```
%%tana%%
- BIM Methodology Research #research
  - Topic:: Building Information Modeling
  - Date:: [[2026-01-28]]
  - Sources::
    - https://buildingsmart.org
    - [[Book: BIM Handbook]]
  - Key findings::
    - IFC is the standard for interoperability
    - ISO 19650 defines BIM workflows
    - COBie for facility management data
  - Related topics::
    - [[IFC Schema]]
    - [[ISO 19650]]
    - [[Digital Twins]]
```

### BIM Validation Results

```
%%tana%%
- IDS Validation: Project XYZ #validation
  - Date:: [[2026-01-28]]
  - Model:: [[Building A - Architecture.ifc]]
  - Specification:: [[Design Requirements IDS v2.0]]
  - Status:: Failed
  - Summary:: 12 errors, 5 warnings
  - Errors::
    - Missing property: FireRating on 8 walls
      - Elements:: [[IFCWALL-001]], [[IFCWALL-002]], [[IFCWALL-008]]
      - Requirement:: All fire walls must have FireRating
    - Invalid value: LoadBearing = "maybe" on 4 walls
      - Elements:: [[IFCWALL-015]], [[IFCWALL-023]]
      - Expected:: Boolean (True/False)
  - Warnings::
    - Recommended property missing: ThermalTransmittance
```

## Validation Checklist

Before outputting Tana Paste, verify:

- [ ] Starts with `%%tana%%` header
- [ ] Uses 2-space indentation consistently
- [ ] Supertags use `#tag` or `#[[Tag Name]]`
- [ ] Fields use `Field Name::` syntax
- [ ] References use `[[...]]` syntax
- [ ] Dates use `[[YYYY-MM-DD]]` format
- [ ] No tabs (only spaces)
- [ ] Special characters escaped when needed
- [ ] Hierarchy is logically structured

## Error Prevention

### Common Mistakes

❌ **Missing header:**
```
- Node without header
```

✅ **Correct:**
```
%%tana%%
- Node with header
```

❌ **Inconsistent indentation:**
```
%%tana%%
- Parent
   - Child (3 spaces)
  - Another child (2 spaces)
```

✅ **Correct:**
```
%%tana%%
- Parent
  - Child (2 spaces)
  - Another child (2 spaces)
```

❌ **Wrong supertag syntax:**
```
- Meeting Notes #Meeting Notes (spaces without brackets)
```

✅ **Correct:**
```
- Meeting Notes #[[Meeting Notes]]
```

❌ **Wrong field syntax:**
```
- Task
  - Status: Todo (using colon instead of double colon)
```

✅ **Correct:**
```
- Task
  - Status:: Todo
```

## Integration Workflows

### From BIM/IFC Validation
1. Parse validation results (errors, warnings, affected elements)
2. Create nodes with `#validation` supertag
3. Add structured fields (Date, Model, Specification, Status)
4. List errors/warnings as child nodes with references to IFC elements
5. Link to related validations or projects

### From Task Management
1. Extract tasks from various sources (comments, tickets, notes)
2. Create nodes with `#task` supertag
3. Add standard fields (Status, Priority, Assigned to, Due date)
4. Create references to related projects or people
5. Nest subtasks as children

### From Meeting Notes
1. Parse meeting content (attendees, agenda, discussions)
2. Create node with `#meeting` supertag
3. Add structured fields (Date, Attendees)
4. Organize content hierarchically (Agenda, Notes, Action items)
5. Create task nodes for action items with references

### From Research/Documentation
1. Analyze content structure and key concepts
2. Create nodes with appropriate supertags (#research, #documentation)
3. Extract and format references (URLs, citations)
4. Create bidirectional links between related concepts
5. Add metadata fields (Date, Topic, Sources)

## Performance Tips

- Keep individual nodes focused (one concept per node)
- Use references instead of duplicating content
- Create consistent supertag taxonomy
- Use fields for filterable metadata
- Leverage search nodes for dynamic collections

## Troubleshooting

**Issue:** Tana doesn't recognize the paste
- Check for `%%tana%%` header
- Verify no tabs are used (only spaces)
- Ensure consistent 2-space indentation

**Issue:** Supertags not applied
- Check syntax: `#tag` or `#[[Tag Name]]`
- Verify supertag exists in Tana or will be created

**Issue:** Fields not recognized
- Ensure double colon syntax: `Field Name::`
- Check field is at correct indentation level
- Verify field name follows Tana conventions

**Issue:** References broken
- Check double bracket syntax: `[[Reference]]`
- Ensure referenced nodes exist or will be created
- Verify no typos in reference names

## Version History

- **v1.0** (2024): Initial Tana Paste specification
- **Current**: Active development with community examples

## Additional Resources

- **Tana Paste Examples**: https://github.com/tanainc/tana-paste-examples
- **Tana Community**: Tana Slack workspace
- **Video Tutorials**: Available on Tana YouTube channel
