# Changelog - Tana Paste Generator Skill

All notable changes to this skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-01-28

### Added
- Initial release of Tana Paste Generator skill
- Multi-purpose content conversion to Tana Paste format
- Support for multiple content types:
  - Plain text and notes
  - Task lists with metadata
  - Meeting notes with attendees and actions
  - BIM/IFC validation results
  - Project documentation
  - Research and knowledge notes
- Comprehensive reference documentation (`reference.md`)
- Four example templates:
  - `meeting-notes.md` - Meeting structure patterns
  - `task-list.md` - Task management examples
  - `bim-validation.md` - BIM validation report format
  - `research-notes.md` - Knowledge capture patterns
- README with usage instructions and troubleshooting
- Frontmatter configuration:
  - `disable-model-invocation: true` - Manual invocation only
  - `user-invocable: true` - Available via `/tana-paste` command
  - `allowed-tools: Read, WebFetch` - Tool restrictions
  - `model: sonnet` - Performance optimization

### Documentation
- Complete Tana Paste format specification with syntax rules
- Validation checklist for output quality
- Common patterns and use cases
- Integration workflows (BIM, tasks, meetings, research)
- Error prevention guidelines
- Troubleshooting guide

### Features
- Automatic supertag assignment based on content type
- Structured field generation (Status, Priority, Date, etc.)
- Bidirectional reference creation for people, projects, concepts
- ISO date formatting (`[[YYYY-MM-DD]]`)
- Hierarchical node structure with proper indentation
- Support for special characters and escaping
- Multi-line field content support

---

## Future Enhancements

### Planned for v1.1.0
- [ ] Template system for common patterns
- [ ] Interactive mode for custom structure definition
- [ ] Validation script for Tana Paste syntax
- [ ] Support for Tana search nodes
- [ ] Batch conversion from multiple files
- [ ] Integration with IDS validation output files

### Planned for v1.2.0
- [ ] Direct integration with BCF-XML format
- [ ] Export to Tana Paste from IFC element queries
- [ ] Custom supertag mapping configuration
- [ ] Field template library
- [ ] Multi-language support (Catalan, Spanish, English)

### Planned for v2.0.0
- [ ] GUI for structure preview before conversion
- [ ] Real-time Tana Paste validation
- [ ] Integration with bSDD for property definitions
- [ ] Advanced relationship mapping
- [ ] Custom plugin development for specific BIM workflows

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2026-01-28 | Initial release with core functionality |

---

## Migration Notes

### Upgrading from Pre-release
This is the first stable release. No migration needed.

### Breaking Changes
None.

---

## Credits

**Author:** David (DDV Solutions)
**Created:** 2026-01-28
**License:** Personal use
**Tana Paste Format:** © Tana Inc.

## Resources
- Tana Paste Documentation: https://tana.inc/docs/tana-paste
- Examples Repository: https://github.com/tanainc/tana-paste-examples
- Tana FAQ: https://tana.inc/faq
