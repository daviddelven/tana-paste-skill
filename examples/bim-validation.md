# BIM Validation Results Example

## Input
```
IDS Validation Report
Project: Hospital Wing Extension
Model: Architecture-LOD300.ifc
Specification: Design_Requirements_v2.1.ids
Date: 2026-01-28

Results: FAILED
- 8 errors found
- 5 warnings found
- 142 elements checked

Errors:
1. Missing property "FireRating" on 8 IFCWALL elements
   - Required by: Fire Safety Requirements
   - Affected: Walls in fire compartments

2. Invalid value for "LoadBearing" property on 4 IFCWALL elements
   - Found: "maybe", "unknown"
   - Expected: Boolean (True/False)

Warnings:
1. Recommended property "ThermalTransmittance" missing on 12 exterior walls
2. Material classification not aligned with buildingSMART standards
```

## Output (Tana Paste)

```tana-paste
%%tana%%
- IDS Validation: Hospital Wing Extension #validation
  - Date:: [[2026-01-28]]
  - Project:: [[Hospital Wing Extension]]
  - Model:: [[Architecture-LOD300.ifc]]
  - Specification:: [[Design_Requirements_v2.1.ids]]
  - Status:: Failed
  - Summary::
    - Total elements checked: 142
    - Errors: 8
    - Warnings: 5
    - Pass rate: 91%
  - Errors::
    - Missing FireRating property #error
      - Severity:: Critical
      - Requirement:: [[Fire Safety Requirements]]
      - Count:: 8 elements
      - Entity type:: IFCWALL
      - Description::
        - Property "FireRating" is mandatory for walls in fire compartments
        - Standard: EN 13501-1 classification required
      - Affected elements::
        - [[IFCWALL-2vH8P0000000000001]]
        - [[IFCWALL-2vH8P0000000000002]]
        - [[IFCWALL-2vH8P0000000000008]]
        - [[IFCWALL-2vH8P0000000000015]]
        - [[IFCWALL-2vH8P0000000000023]]
        - [[IFCWALL-2vH8P0000000000034]]
        - [[IFCWALL-2vH8P0000000000041]]
        - [[IFCWALL-2vH8P0000000000055]]
      - Remediation::
        - Add "FireRating" property to all fire-rated walls
        - Use Pset_WallCommon property set
        - Values: REI 60, REI 90, REI 120, etc.
      - Responsible:: [[Architecture Team]]
    - Invalid LoadBearing value #error
      - Severity:: High
      - Count:: 4 elements
      - Entity type:: IFCWALL
      - Description::
        - Property "LoadBearing" contains invalid values
        - Found values: "maybe", "unknown"
        - Expected: Boolean (True or False)
      - Affected elements::
        - [[IFCWALL-2vH8P0000000000067]]
        - [[IFCWALL-2vH8P0000000000073]]
        - [[IFCWALL-2vH8P0000000000089]]
        - [[IFCWALL-2vH8P0000000000091]]
      - Remediation::
        - Review structural drawings
        - Update LoadBearing property to True or False
        - Coordinate with structural engineer
      - Responsible:: [[Architecture Team]], [[Structure Team]]
  - Warnings::
    - Missing ThermalTransmittance #warning
      - Severity:: Medium
      - Count:: 12 elements
      - Entity type:: IFCWALL
      - Description::
        - Recommended property "ThermalTransmittance" missing on exterior walls
        - Needed for energy analysis
      - Remediation::
        - Add U-values from energy calculations
        - Property: ThermalTransmittance (W/m²K)
      - Responsible:: [[Architecture Team]]
    - Material classification mismatch #warning
      - Severity:: Low
      - Description::
        - Materials not aligned with buildingSMART bSDD
        - May affect material quantity takeoffs
      - Remediation::
        - Map materials to bSDD classifications
        - Use standard material library
      - Responsible:: [[BIM Manager]]
  - Next Steps::
    - [[Task: Fix FireRating errors]] - Priority: Critical
    - [[Task: Correct LoadBearing values]] - Priority: High
    - [[Task: Add ThermalTransmittance]] - Priority: Medium
    - [[Task: Revalidate model]] - After fixes complete
  - Related::
    - [[BCF Issue #234: Fire rating compliance]]
    - [[Coordination Meeting: 2026-02-01]]
    - [[Previous validation: 2026-01-15]]
```

## Variations

### Compact format (summary only)
```tana-paste
%%tana%%
- Validation: Hospital Wing Extension #validation
  - Date:: [[2026-01-28]]
  - Status:: Failed (8 errors, 5 warnings)
  - Model:: [[Architecture-LOD300.ifc]]
  - Critical issues::
    - Missing FireRating: 8 walls
    - Invalid LoadBearing values: 4 walls
  - Assigned to:: [[Architecture Team]]
```

### With BCF issue integration
```tana-paste
%%tana%%
- IDS Validation: Hospital Wing #validation
  - Date:: [[2026-01-28]]
  - Status:: Failed
  - BCF Issues Created::
    - [[BCF-001: FireRating missing]] - Priority: Critical
    - [[BCF-002: LoadBearing invalid]] - Priority: High
    - [[BCF-003: ThermalTransmittance recommended]] - Priority: Low
  - Issue Tracker:: https://bimcollab.example.com/project/hospital
```

### Timeline view (multiple validations)
```tana-paste
%%tana%%
- Hospital Wing Extension: Validation History #project
  - Validations::
    - [[2026-01-15 Validation]] - Status: Failed (15 errors)
    - [[2026-01-22 Validation]] - Status: Failed (10 errors)
    - [[2026-01-28 Validation]] - Status: Failed (8 errors)
  - Trend::
    - Error count decreasing
    - FireRating issues persist
    - Need focused fix session
```

## Advanced: Multi-model coordination check

```tana-paste
%%tana%%
- Coordination Check: Hospital Wing #coordination
  - Date:: [[2026-01-28]]
  - Models checked::
    - [[Architecture-LOD300.ifc]] - v2.3
    - [[Structure-LOD300.ifc]] - v1.8
    - [[MEP-LOD300.ifc]] - v2.1
  - Clash Detection::
    - Total clashes: 47
    - Critical: 12
    - Medium: 23
    - Low: 12
  - Issues::
    - Structural beam conflicts with MEP ducts #clash
      - Location:: Grid C-D / Level 2
      - Count:: 8 clashes
      - Models:: [[Structure-LOD300.ifc]], [[MEP-LOD300.ifc]]
      - Resolution:: MEP to reroute ducts below beam
      - Responsible:: [[MEP Team]]
    - Architectural wall intersects column #clash
      - Location:: Grid F3 / Level 1
      - Count:: 4 clashes
      - Models:: [[Architecture-LOD300.ifc]], [[Structure-LOD300.ifc]]
      - Resolution:: Architecture to adjust wall position
      - Responsible:: [[Architecture Team]]
  - Property Validation::
    - [[IDS Validation: Architecture]] - 8 errors
    - [[IDS Validation: Structure]] - 2 errors
    - [[IDS Validation: MEP]] - 5 errors
  - Action Items::
    - [[Task: Resolve structural-MEP clashes]] - Due: [[2026-02-05]]
    - [[Task: Fix IDS errors]] - Due: [[2026-02-08]]
    - [[Task: Update model versions]] - After fixes
    - [[Task: Re-run coordination check]] - Due: [[2026-02-10]]
```
