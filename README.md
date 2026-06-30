# Application Documentation and Audit Framework

This framework defines a practical documentation set and audit model for a software application from an application ownership, operations, support, and governance perspective. It is designed for application owners, project teams, support teams, and automated review agents.

The package covers the full cycle:

1. Produce the documentation artifacts.
2. Review each artifact using structured rubrics.
3. Verify whether submitted artifacts pass or fail acceptance gates.
4. Produce AIDOS-style audit results using Bug, Risk, and Idea findings.

The model is intentionally plain-language and operations-oriented. It documents what the application does, who uses it, how work flows through it, what data and rules matter, what it depends on, and how it is supported after launch.

## Recommended file use

Start here:

- `01_documentation_model.md` - concept model and document relationships
- `02_document_set_register.md` - full document set, purpose, production method, and questions answered
- `templates/` - markdown templates for each document
- `rubrics/` - universal and artifact-specific acceptance criteria
- `review/` - audit output template, verifier rules, and package gates
- `examples/lhc_booking_system_example.md` - sample capabilities and workflows for the LHC Booking System
- `agent_prompts/` - prompts for producing and auditing artifacts

## Core principle

A documentation package is acceptable only when it allows an application owner, process owner, or support owner to answer:

1. What does the application do?
2. Who uses and owns it?
3. What workflows does it support?
4. What rules, data, reports, dependencies, and risks matter?
5. How is it supported after launch?
6. What has been accepted, deferred, or handed over?

## Recommended acceptance posture

Do not accept a package only because all files exist. Accept it only when the artifacts are complete, coherent, traceable, operationally usable, and reviewed by the right owners.
