# Tana Paste Generator Skill

## Overview

Multi-purpose skill for converting any content (text, tasks, BIM data, meeting notes, research) to valid Tana Paste format for import into Tana.inc.

## Installation

This skill is installed at: `~/.claude/skills/tana-paste/`

Once installed, Claude Code automatically recognizes it for invocation.

## Usage

### Direct Invocation

```bash
/tana-paste [content-to-convert]
```

**Examples:**

```bash
# Convert inline text
/tana-paste Convert this meeting discussion to Tana format: Team agreed on Q1 roadmap, Alice to review architecture, Bob to update docs

# Convert from file
/tana-paste Convert validation-results.txt to Tana Paste

# Convert from selection
# Select text in editor, then:
/tana-paste
```

### What Gets Converted

- **Plain text/notes** → Hierarchical Tana nodes
- **Task lists** → Tana tasks with status, priority, assignees
- **Meeting notes** → Structured meetings with attendees, agenda, actions
- **BIM/IFC validation results** → Validation reports with errors, warnings, affected elements
- **Project documentation** → Searchable knowledge nodes
- **Research notes** → Linked concepts with references
- **Any structured data** → Automatically parsed and formatted

## Output Format

The skill generates valid Tana Paste that you can:
1. **Copy** the code block output
2. **Open Tana.inc**
3. **Paste** anywhere in your workspace
4. Content appears as properly structured nodes

## File Structure

```
tana-paste/
├── SKILL.md              Main skill instructions
├── reference.md          Complete Tana Paste format specification
├── README.md             This file
└── examples/
    ├── meeting-notes.md      Meeting structure patterns
    ├── task-list.md          Task management examples
    ├── bim-validation.md     BIM validation report format
    └── research-notes.md     Knowledge capture patterns
```

## Examples

### Example 1: Quick Task List

**Input:**
```
/tana-paste Fix authentication bug, Update API documentation, Deploy to staging
```

**Output:**
```tana-paste
%%tana%%
- Fix authentication bug #task
  - Status:: Todo
  - Priority:: High
- Update API documentation #task
  - Status:: Todo
  - Priority:: Normal
- Deploy to staging #task
  - Status:: Todo
  - Priority:: Normal
```

### Example 2: Meeting Notes

**Input:**
```
/tana-paste Team sync January 28: Alice, Bob, Charlie discussed roadmap. Action: Alice review proposal by Feb 1
```

**Output:**
```tana-paste
%%tana%%
- Team Sync #meeting
  - Date:: [[2026-01-28]]
  - Attendees:: [[Alice]], [[Bob]], [[Charlie]]
  - Discussion::
    - Roadmap planning
  - Action Items::
    - Review proposal #task
      - Assigned to:: [[Alice]]
      - Due date:: [[2026-02-01]]
      - Status:: Todo
```

### Example 3: BIM Validation Results

**Input:**
```
/tana-paste IDS validation failed: 8 walls missing FireRating property, 4 walls have invalid LoadBearing values
```

**Output:**
```tana-paste
%%tana%%
- IDS Validation Report #validation
  - Date:: [[2026-01-28]]
  - Status:: Failed
  - Errors::
    - Missing FireRating property #error
      - Count:: 8 elements
      - Entity type:: IFCWALL
      - Severity:: Critical
    - Invalid LoadBearing values #error
      - Count:: 4 elements
      - Entity type:: IFCWALL
      - Severity:: High
```

## Advanced Features

### Supertags
Automatically applies appropriate supertags:
- `#task` for tasks
- `#meeting` for meetings
- `#validation` for BIM validation results
- `#research` for research notes
- `#project` for project documentation

### Fields
Generates structured fields:
- `Status::` for task status
- `Date::` for dates
- `Assigned to::` for assignees
- `Priority::` for priorities
- Custom fields based on content

### References
Creates bidirectional links:
- `[[Person Name]]` for people
- `[[Project Name]]` for projects
- `[[IFCWALL-123]]` for IFC elements
- `[[Related Topic]]` for concepts

### Dates
Formats dates properly:
- `[[2026-01-28]]` for ISO date format
- Automatically detects dates in text

## Configuration

The skill uses these settings:
- `disable-model-invocation: true` - Manual invocation only (controlled by you)
- `user-invocable: true` - Available via `/tana-paste` command
- `allowed-tools: Read, WebFetch` - Can read files and fetch web content
- `model: sonnet` - Uses Claude Sonnet for optimal performance

## Integration with Your Workflow

### BIM/IFC Projects
Convert validation results from IDS checkers, clash detection reports, or model audit logs directly to Tana for project documentation.

### Task Management
Capture todos from various sources (comments, tickets, discussions) and structure them consistently in Tana.

### Meeting Documentation
Quick capture meeting notes and automatically create action item tasks linked to attendees.

### Knowledge Management
Convert research findings, technical documentation, or study notes into linked knowledge graphs in Tana.

## Tips

1. **Be specific**: The more context you provide, the better the structure
2. **Include dates**: Mention dates for automatic date field creation
3. **Name people**: Reference people by name for automatic person links
4. **Mention projects**: Reference projects for automatic linking
5. **Review output**: Always review generated Tana Paste before pasting

## Troubleshooting

**Skill not found?**
- Verify installation: `ls ~/.claude/skills/tana-paste/SKILL.md`
- Restart Claude Code to reload skills

**Invalid Tana Paste output?**
- Check reference.md for format specification
- Report issues with specific examples

**Need custom structure?**
- Specify desired structure in your request
- Ask for specific supertags or fields
- Reference example files for patterns

## Resources

- **Tana Paste Documentation**: https://tana.inc/docs/tana-paste
- **Examples Repository**: https://github.com/tanainc/tana-paste-examples
- **Tana FAQ**: https://tana.inc/faq
- **Local Reference**: [reference.md](reference.md)
- **Local Examples**: [examples/](examples/)

## Version

- **Version**: 1.0.0
- **Created**: 2026-01-28
- **Compatibility**: Claude Code, Tana.inc
- **Format**: Tana Paste (v1.0)

## License

This skill is for personal use. Tana Paste format is property of Tana Inc.
