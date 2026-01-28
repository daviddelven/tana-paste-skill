# Research Notes Example

## Input
```
Research topic: ISO 19650 BIM Information Management
Date: January 28, 2026

Key findings:
- ISO 19650 is the international standard for BIM information management
- Part 1 covers concepts and principles
- Part 2 covers delivery phase of assets
- Defines Common Data Environment (CDE) workflow
- Information containers have states: WIP, Shared, Published, Archived

Related concepts:
- Level of Information Need (LOIN)
- Appointment documents (BEP, EIR)
- Information delivery milestones

Sources:
- ISO 19650-1:2018
- ISO 19650-2:2018
- buildingSMART documentation
- https://www.iso.org/standard/68078.html
```

## Output (Tana Paste)

```tana-paste
%%tana%%
- ISO 19650: BIM Information Management #research
  - Date:: [[2026-01-28]]
  - Topic:: Building Information Modeling
  - Category:: Standards & Regulations
  - Summary::
    - International standard for managing information throughout asset lifecycle
    - Defines processes, procedures, and terminology for BIM projects
    - Focus on information management using Common Data Environment
  - Key Concepts::
    - Common Data Environment (CDE) #concept
      - Description::
        - Digital environment for collecting, managing, and sharing information
        - Single source of truth for project information
      - States::
        - WIP (Work in Progress) - Information being developed
        - Shared - Information shared for review/coordination
        - Published - Authorized information for construction/operation
        - Archived - Historical information for reference
      - Related to:: [[ISO 19650-2]], [[Information Management]]
    - Level of Information Need (LOIN) #concept
      - Description::
        - Framework for defining required detail of information
        - Specifies geometric, alphanumeric, and documentation requirements
        - Prevents over-modeling and under-modeling
      - Components::
        - Geometric information (detail, dimensionality, location)
        - Alphanumeric information (properties, parameters)
        - Documentation (drawings, specifications, reports)
      - Related to:: [[ISO 19650-1]], [[Information Delivery]]
    - BIM Execution Plan (BEP) #concept
      - Description::
        - Plan explaining how information will be managed
        - Pre-appointment BEP vs Post-appointment BEP
        - Details roles, processes, standards, procedures
      - Contents::
        - Project information requirements
        - Information delivery strategy
        - Federated model structure
        - Quality assurance procedures
      - Related to:: [[Exchange Information Requirements]], [[Appointment Documents]]
    - Exchange Information Requirements (EIR) #concept
      - Description::
        - Client's requirements for information delivery
        - Technical, management, and commercial requirements
        - Used for appointing parties and procurement
      - Related to:: [[BIM Execution Plan]], [[Client Requirements]]
  - Standards Structure::
    - ISO 19650-1:2018 #standard
      - Title:: Concepts and principles
      - Scope:: Fundamental concepts for information management
      - Key topics::
        - Information management principles
        - High-level process framework
        - Roles and responsibilities
        - Terminology and definitions
      - Status:: Published
      - URL:: https://www.iso.org/standard/68078.html
    - ISO 19650-2:2018 #standard
      - Title:: Delivery phase of assets
      - Scope:: Information management during design and construction
      - Key topics::
        - CDE workflow and information states
        - Information delivery cycles
        - Collaborative production of information
        - Change management processes
      - Status:: Published
      - URL:: https://www.iso.org/standard/68080.html
    - ISO 19650-3:2020 #standard
      - Title:: Operational phase of assets
      - Scope:: Information management during building operation
      - Status:: Published
    - ISO 19650-5:2020 #standard
      - Title:: Security-minded approach
      - Scope:: Information security considerations
      - Status:: Published
  - Implementation Workflow::
    - Assessment and need
      - Define organizational information requirements (OIR)
      - Establish asset information requirements (AIR)
      - Create project information requirements (PIR)
    - Invitation to tender
      - Prepare Exchange Information Requirements (EIR)
      - Define information delivery milestones
      - Specify standards and methods
    - Tender response
      - Develop pre-appointment BEP
      - Demonstrate capability and capacity
      - Propose information delivery approach
    - Appointment
      - Finalize post-appointment BEP
      - Establish CDE and workflows
      - Confirm roles and responsibilities
    - Mobilization
      - Set up project team and systems
      - Configure CDE environments
      - Conduct project launch meeting
    - Collaborative production
      - Create information containers in WIP
      - Progress through CDE workflow states
      - Regular coordination and review
    - Information delivery
      - Submit information at milestones
      - Client review and authorization
      - Move to Published state
    - Project close-out
      - Archive project information
      - Deliver Asset Information Model (AIM)
      - Lessons learned and feedback
  - Practical Applications::
    - CDE state management in project workflows
    - Defining information requirements in tenders
    - Structuring information delivery milestones
    - Quality control checkpoints for information
    - Handover procedures for facility management
  - Related Topics::
    - [[IFC (Industry Foundation Classes)]]
    - [[IDS (Information Delivery Specification)]]
    - [[BCF (BIM Collaboration Format)]]
    - [[COBie (Construction Operations Building Information Exchange)]]
    - [[buildingSMART International]]
    - [[Digital Twin]]
    - [[Asset Information Model (AIM)]]
  - Sources::
    - ISO 19650-1:2018 standard document
    - ISO 19650-2:2018 standard document
    - buildingSMART International
      - URL:: https://www.buildingsmart.org
    - UK BIM Framework
      - URL:: https://www.ukbimframework.org
    - ISO Standards Catalog
      - URL:: https://www.iso.org/standard/68078.html
  - Personal Notes::
    - Critical for large infrastructure projects
    - Adoption varies by country and sector
    - UK mandate drove initial adoption
    - Now becoming global standard
    - Integration with IDS for requirements specification
    - CDE workflow maps well to document states (S0-S5, AF, AR)
  - Next Steps::
    - [[Research: ISO 19650-3 operational phase details]]
    - [[Experiment: Map DDV nomenclature to ISO 19650 states]]
    - [[Document: ISO 19650 implementation checklist]]
    - [[Compare: ISO 19650 vs PAS 1192 differences]]
```

## Variations

### Quick reference note
```tana-paste
%%tana%%
- ISO 19650 Overview #reference
  - Type:: Standard
  - Summary:: BIM information management standard
  - Key points::
    - CDE states: WIP, Shared, Published, Archived
    - Requires BEP and EIR documents
    - Defines LOIN framework
  - URL:: https://www.iso.org/standard/68078.html
```

### Literature review format
```tana-paste
%%tana%%
- Literature Review: BIM Standards #research
  - Date:: [[2026-01-28]]
  - Papers reviewed::
    - [[ISO 19650: Information Management]] - 5/5 relevance
    - [[IFC Schema Evolution]] - 4/5 relevance
    - [[Digital Twin Frameworks]] - 3/5 relevance
  - Themes identified::
    - Interoperability is key challenge
    - Standardization reduces friction
    - Information security increasingly important
  - Gaps in literature::
    - Limited research on AI integration with BIM standards
    - Need more case studies on ISO 19650 adoption
```

### Concept map format
```tana-paste
%%tana%%
- BIM Concepts Map #knowledge-graph
  - ISO 19650 #concept
    - Defines:: [[Common Data Environment]], [[LOIN]], [[BEP]]
    - Related to:: [[IFC]], [[BCF]], [[COBie]]
    - Implemented via:: [[CDE Platforms]], [[Model Checkers]]
  - Common Data Environment #concept
    - Part of:: [[ISO 19650]]
    - States:: [[WIP]], [[Shared]], [[Published]], [[Archived]]
    - Examples:: [[BIM 360]], [[Trimble Connect]], [[BIMcollab]]
```

## Advanced: Comparative analysis

```tana-paste
%%tana%%
- Comparison: BIM Information Management Standards #analysis
  - Date:: [[2026-01-28]]
  - Standards compared::
    - [[ISO 19650]] (International)
    - [[PAS 1192]] (UK, predecessor)
    - [[COBIM]] (Finland)
    - [[BIM Guidelines]] (Singapore)
  - Comparison matrix::
    - Scope
      - ISO 19650:: Full lifecycle, international
      - PAS 1192:: Design & construction, UK-specific
      - COBIM:: Prescriptive requirements, Finnish market
      - Singapore BIM:: Government projects, local requirements
    - CDE Workflow
      - ISO 19650:: 4 states (WIP, Shared, Published, Archived)
      - PAS 1192:: Similar structure, slightly different terminology
      - COBIM:: Aligned with ISO 19650
      - Singapore BIM:: Follows ISO 19650 framework
    - Information Requirements
      - ISO 19650:: OIR → AIR → PIR → EIR framework
      - PAS 1192:: EIR and BEP approach
      - COBIM:: Detailed requirement specifications per discipline
      - Singapore BIM:: EGIDS (Employer's Geometric Information Delivery Specification)
  - Convergence trends::
    - Markets aligning to ISO 19650
    - PAS 1192 superseded by ISO 19650
    - Local variations for specific requirements
    - Common terminology emerging
  - Implications::
    - Adopt ISO 19650 as baseline
    - Understand local variations for specific markets
    - IDS can bridge different requirement frameworks
```
