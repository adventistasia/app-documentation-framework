# Changelog

## 2.0.0 – 2026-10-07

A rewrite of the 2026-06-30 release, based on two reviews of it: an assessment of the framework against recommended documentation practice, and a resolution report that set out the fix for each finding. The 2026-06-30 release is kept in [releases/](releases/) and in git history.

### What changed, in short

- **Purpose made explicit.** The framework tells teams how to document an application, requires the documentation to define success measures and application acceptance criteria, and supplies documentation review criteria for the documents themselves. The two kinds of criteria are named separately everywhere.
- **Engineering layer added** (ENG-01 to ENG-10): requirements, user journeys, architecture and design, data model, integrations and dependencies, configuration and environments, deployment and release, operations and support runbook, developer and agent guide, decision log.
- **Success spine added:** Scope Record, Glossary, Success Measures (four levels, including output correctness), Acceptance Criteria & Verification (Given/When/Then), and an extended Acceptance & Handover Record.
- **Business layer extended:** business case with benefits, baselines and targets and "What success looks like"; new Resource & Cost Model; data classification, purpose and retention; privacy risk category; a user guide organised by what the reader is trying to do.
- **Scoping instead of a fixed set:** seven scored dimensions give Foundation, Standard or Full; eleven triggers add or drop items; a depth matrix sets each item to not needed, section, document or document with extras; a Scope Record is approved by the owners and becomes what the package is reviewed against. A never-dropped minimum applies at every level.
- **Lifecycle:** documents due by build stage, update triggers tied to pull requests, review cadence by level, change log in every document, docs stored in the application repository.
- **Rules consolidated:** one decision table, defined severity, a Critical flag on every rubric row, cross-document rules tagged Mechanical or Judgment, and eight gates that compute the package decision. Each rule lives in one file.
- **Tooling:** a linter for the mechanical rules, a framework self-check, a generated consolidated guide, and agent prompts that name the files to load.
- **Examples rebuilt:** a Foundation example, a Standard example with its Scope Record, and review-training material with expected findings.

### Document ID mapping

| 2026-06-30 | 2.0.0 | Notes |
|---|---|---|
| DOC-01 Application Overview | BUS-01 Application Overview & Business Case | Extended with business case and "What success looks like" |
| DOC-02 Capabilities Register | BUS-02 Capabilities Register | `Automated` column replaces "System" as a user |
| DOC-03 Workflow Register | BUS-03 Business Process Register | Same content; journeys split out to ENG-02 |
| DOC-04 Roles and Access Matrix | BUS-04 Roles & Access Matrix | Adds periodic access review |
| DOC-05 Business Rules and Status Lifecycle | BUS-05 Business Rules & Status Lifecycle | Statuses and transitions get IDs |
| DOC-06 Data, Reports, and Notifications Register | BUS-06 Data, Reports & Notifications Register | Classification, purpose, retention and disposal replace "Sensitive? Yes/No" |
| DOC-07 Application Dependencies Register | ENG-05 Integrations & Dependencies Register | Adds interface contracts, runbook and cost links |
| DOC-08 Support and Operations Guide | ENG-08 Operations & Support Runbook | Adds service levels, monitoring, incidents, runbook entries, backup and restore, continuity, maintenance, output checks, change management |
| DOC-09 Risk and Controls Register | BUS-08 Risk & Controls Register | Adds privacy and technical categories |
| DOC-10 User and Admin Guide | BUS-09 User & Admin Guide | Restructured: getting started, how-to, concepts, reference, help, what's new, accessibility |
| DOC-11 Acceptance and Handover Record | SP-12 Acceptance & Handover Record | Adds acceptance results, success baselines and dry-run evidence |
| — | SP-00, SP-01, SP-10, SP-11, BUS-07, ENG-01 to ENG-04, ENG-06, ENG-07, ENG-09, ENG-10 | New |

Content ID formats changed from `C01`, `W01`, `D01` to `C-01`, `W-01`, `D-01`; see [conventions §5](02_conventions.md#5-content-ids). Rubric criteria changed from `AO-01`-style IDs to `<DOC-ID>.<n>`; each rubric file ends with its mapping table.

### Files

| 2026-06-30 | 2.0.0 |
|---|---|
| `01_documentation_model.md` | `00_documentation_model.md` |
| `02_document_set_register.md` | `01_document_set_register.md` |
| — | `02_conventions.md`, `03_scoping_guide.md` |
| `templates/01` … `11` | `templates/spine/`, `templates/business/`, `templates/engineering/` |
| `rubrics/01_artifact_specific_rubrics.md` | `rubrics/01_business_rubrics.md`, `02_engineering_rubrics.md`, `03_spine_rubrics.md` |
| `rubrics/02_acceptance_thresholds.md`, `review/02_verifier_control_rules.md` (decision parts) | `rubrics/04_decision_rules.md` |
| `review/02_verifier_control_rules.md` (cross-document rules) | `review/02_cross_document_rules.md` |
| `review/03_package_acceptance_gates.md` | `review/03_package_gates.md` |
| — | `review/05_linter_spec.md`, `tools/doclint.py`, `build/` |
| `agent_prompts/01` … `03` | `agent_prompts/scoping.md`, `producer_forward.md`, `producer_reverse.md`, `reviewer.md`, `verifier.md` |
| `examples/lhc_booking_system_example.md` | `examples/lhc_booking_system/`, `examples/small_tool/`, `examples/review_training/` |
| `consolidated_guide.md` (hand-maintained) | `consolidated_guide.md` (generated) |

### Review findings resolved

Every finding in the assessment, and its fix in the resolution report, is addressed in this release. The traceability from finding to file is in the pull request that introduced 2.0.0.

## Calibration

Record each project scored with the [scoping guide](03_scoping_guide.md): the scores, the level the method gave, and the level the owners agreed. Adjust the thresholds or the dimension wording when they disagree.

| Date | Project | D1–D7 | Total | Method level | Agreed level | Notes |
|---|---|---|---|---|---|---|
| 2026-10-07 | Stock Count Sheets (small_tool example) | 1,1,1,1,1,1,1 | 7 | Foundation | Foundation | Worked example, not a live project; top of the Foundation band |
| 2026-10-07 | Booking system (example) | 3,2,2,1,3,2,1 | 14 | Standard | Standard | Worked example; calibrate on 3–4 live projects next |

## 2026-06-30

First release: business and governance handover standard (DOC-01 to DOC-11), rubrics, verifier rules, gates and an example.
