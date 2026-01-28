# Tana Paste Generator - Claude Code Skill

> Multi-purpose Claude Code skill for converting content to valid [Tana Paste](https://tana.inc/docs/tana-paste) format

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](./VERSION)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-purple.svg)](https://code.claude.com)

## Overview

**Tana Paste Generator** is a specialized skill for [Claude Code](https://code.claude.com) that converts various types of content (tasks, meetings, projects, notes, BIM validation results) into properly formatted Tana Paste for seamless import into [Tana.inc](https://tana.inc).

The skill is customized to use **your personal Tana workspace schema** with real supertags and fields, ensuring generated content integrates perfectly with your existing knowledge management system.

## Features

✅ **Multi-format Support**
- Tasks (`#task`, `#quickTask`) with timesheet tracking
- Projects (`#project`) with goals and stakeholders
- Meetings (`#meeting`) with attendees and action items
- Meeting notes (`#meetingNote`) with detailed discussions
- General notes (`#note`) with CODE status
- BIM/IFC validation results with structured error reporting

✅ **Personal Schema Integration**
- Uses your actual Tana supertags and field definitions
- Respects inheritance structure (e.g., `#task` inherits from `#todo`, `#timed-task`)
- Includes proper field values (e.g., `Task State:: [[📅 Not started]]`)

✅ **Smart Content Analysis**
- Automatically identifies content type
- Generates optimal structure for Tana
- Creates proper references and relationships

✅ **Production Ready**
- Comprehensive format validation
- Detailed examples for common use cases
- Full Tana Paste specification reference

## Installation

### For Claude Code

1. **Copy skill to your Claude skills directory:**

```bash
# Linux/macOS
cp -r tana-paste ~/.claude/skills/

# Windows
xcopy tana-paste %USERPROFILE%\.claude\skills\tana-paste\ /E /I
```

2. **Restart Claude Code** to load the skill

3. **Verify installation:**

```
/tana-paste Test task
```

### For claude.ai (Web UI)

1. **Build the .skill file:**

```bash
python scripts/build_skill.py
```

2. **Upload to claude.ai:**
   - Go to [claude.ai](https://claude.ai) > Settings > Capabilities
   - Upload `dist/tana-paste-v1.0.0.skill`

## Usage

### Basic Invocation

```
/tana-paste [content-to-convert]
```

### Examples

#### Create a Task

```
/tana-paste Implementar validació IDS. Context: Treball BIM. Tipus: Desenvolupament. Programat: 1 febrer. Temps: 5h.
```

**Output:**
```tana-paste
%%tana%%
- Implementar validació IDS #task
  - Context:: [[Treball BIM]]
  - Topic:: [[BIM Validation]]
  - Task State:: [[📅 Not started]]
  - Energy Demand:: High
  - Type:: Desenvolupament
  - Time Sector:: [[⚪ Available]]
  - Due Date:: [[2026-02-01]]
  - Scheduled on:: [[2026-02-01]]
  - TT - Start Time:: 09:00
  - TT - Total Time:: 5h
```

#### Create a Meeting

```
/tana-paste Reunió coordinació bSSp dimarts 30 gener 10h. Assistents: Sergio, Victor, David. Agenda: openBIMathon, IDS review. Online Teams.
```

**Output:**
```tana-paste
%%tana%%
- Reunió coordinació bSSp #meeting
  - Scheduled on:: [[2026-01-30]]
  - Attendees:: [[Sergio Muñoz Gómez]], [[Victor Manuel Ruiz Calderón]], [[David Delgado Vendrell]]
  - Owner:: [[David Delgado Vendrell]]
  - Context:: [[Work]]
  - Organization:: [[buildingSMART Spain]]
  - Topic:: [[BIM Standards]]
  - Event Format:: Online
  - Agenda::
    - Planificació openBIMathon
    - Revisió IDS
```

#### Create a Project

```
/tana-paste Nou projecte BIM DIBA. Client: Diputació Barcelona. Inici: 1 febrer. Tipus: Consultoria. Objectiu: Plec licitació BIM.
```

**Output:**
```tana-paste
%%tana%%
- Consultoria BIM DIBA #project
  - Project Code:: Pr DB3
  - Project Title:: Redacció Plec Licitació BIM DIBA
  - Project Client:: [[Diputació de Barcelona]]
  - Area:: [[A Business]]
  - Project Start:: [[2026-02-01]]
  - Project Type:: BIM Consultancy
  - Project Goal(s)::
    - Redactar plec de licitació amb requisits BIM
  - Stakeholders:: [[Montserrat Jiménez Sapés]], [[David Delgado Vendrell]]
```

## Supported Supertags

Based on your personal Tana workspace:

| Supertag | Description | Use Case |
|----------|-------------|----------|
| `#task` | Full tasks with timesheet tracking | Complex tasks requiring time tracking |
| `#quickTask` | Brief, straightforward tasks | Simple, fast tasks |
| `#project` | Projects with goals and stakeholders | Multi-task initiatives |
| `#meeting` | Meetings/events with attendees | Scheduled meetings |
| `#meetingNote` | Meeting notes | Detailed discussion notes |
| `#note` | General notes | Knowledge capture |
| `#person` | People | Contacts and stakeholders |
| `#client` | Clients | Customer relationships |
| `#organization` | Organizations | Companies and institutions |

## File Structure

```
tana-paste/
├── SKILL.md              # Main skill instructions with your schema
├── README.md             # Usage documentation
├── CHANGELOG.md          # Version history
├── VERSION               # Current version (1.0.0)
├── reference.md          # Complete Tana Paste specification
├── examples/             # Example patterns
│   ├── meeting-notes.md
│   ├── task-list.md
│   ├── bim-validation.md
│   └── research-notes.md
└── scripts/
    └── build_skill.py    # Build script for .skill generation
```

## Building for Distribution

### Generate .skill file for claude.ai

```bash
cd scripts
python build_skill.py
```

Output: `dist/tana-paste-v1.0.0.skill`

### Version Management

Update version in `VERSION` file:
```bash
echo "1.1.0" > VERSION
```

Update `CHANGELOG.md` with changes, then rebuild.

## Configuration

The skill uses your personal Tana schema defined in `SKILL.md`. Key configurations:

- **Supertags**: `#task`, `#quickTask`, `#project`, `#meeting`, etc.
- **Fields**: Context, Topic, Task State, Energy Demand, etc.
- **Values**: `[[📅 Not started]]`, `[[✅ Done]]`, `[[⚪ Available]]`, etc.

To customize for different Tana workspaces, update the "User's Personal Tana Schema" section in `SKILL.md`.

## Documentation

- **[SKILL.md](./SKILL.md)** - Complete skill instructions with schema
- **[reference.md](./reference.md)** - Tana Paste format specification
- **[examples/](./examples/)** - Common use case patterns
- **[CHANGELOG.md](./CHANGELOG.md)** - Version history and updates

## External Resources

- **Tana Paste Documentation**: https://tana.inc/docs/tana-paste
- **Tana Paste Examples**: https://github.com/tanainc/tana-paste-examples
- **Tana FAQ**: https://tana.inc/faq
- **Claude Code Documentation**: https://code.claude.com/docs

## Requirements

- **Claude Code** (CLI or VSCode extension)
- **OR** **claude.ai** Pro/Max/Team/Enterprise plan
- **Tana.inc** account (for paste import)

## Version History

### v1.0.0 (2026-01-28)
- Initial release with personal Tana schema
- Support for tasks, projects, meetings, notes
- BIM/IFC validation result formatting
- Complete Tana Paste specification
- 4 example templates
- Build script for distribution

See [CHANGELOG.md](./CHANGELOG.md) for detailed version history.

## Contributing

This is a personal skill customized for a specific Tana workspace. To adapt for your workspace:

1. Fork this repository
2. Update the "User's Personal Tana Schema" section in `SKILL.md`
3. Modify examples to match your supertags and fields
4. Test with your Tana workspace
5. Rebuild with `build_skill.py`

## License

MIT License - See [LICENSE](./LICENSE) for details.

## Author

**David Delgado Vendrell**
- BIM Consultant & Knowledge Management Specialist
- buildingSMART Spain Technical Coordinator
- Tana Navigator

## Acknowledgments

- **Tana Inc.** for the Tana Paste format
- **Anthropic** for Claude Code
- **buildingSMART** community for BIM workflows

---

**Keywords**: Claude Code, Tana, Tana Paste, Knowledge Management, PKM, BIM, IFC, Task Management, Meeting Notes, Skill Development
