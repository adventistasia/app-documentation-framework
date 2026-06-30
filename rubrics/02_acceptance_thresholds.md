# Acceptance Thresholds

## Artifact review decisions

| Decision | Meaning |
|---|---|
| Accept | Document is complete, clear, traceable, operationally usable, and ready for use. |
| Accept with Conditions | Minor gaps exist but do not block handover; fixes are tracked. |
| Revise and Resubmit | Important gaps prevent reliable use. |
| Reject | Document is missing, inaccurate, contradictory, or unusable. |

## Artifact-level acceptance gates

An artifact can be marked Accept only when:

- All critical universal criteria pass.
- All critical artifact-specific criteria pass.
- No high-severity Bug remains open.
- No high-severity Risk remains unmitigated or unaccepted.
- Required cross-document references are consistent.
- Known gaps are either fixed or recorded as accepted limitations.

An artifact can be marked Accept with Conditions only when:

- Remaining issues are low or medium severity.
- No issue prevents operation, support, governance, or handover.
- Conditions are clearly listed with owners and target dates.
- The accepting owner agrees to the conditions.

An artifact should be Revise and Resubmit when:

- Required fields or sections are missing.
- Traceability to related documents is incomplete.
- Ownership is unclear.
- Content is too vague for operational use.
- Contradictions exist but are fixable.

An artifact should be Rejected when:

- It is the wrong document.
- It cannot be used by the target audience.
- It contradicts accepted scope or other accepted artifacts.
- It falsely claims readiness despite missing critical content.
- It omits ownership, support path, or known limitations in a way that creates acceptance risk.

## Critical universal criteria

These must pass for core acceptance:

- U-01 Identity
- U-02 Purpose
- U-04 Required structure
- U-07 Traceability
- U-08 Operational usability
- U-10 Ownership and accountability
- U-12 Acceptance readiness

## Required artifacts for package acceptance

The package should not be accepted unless these artifacts are Accept or Accept with Conditions:

- DOC-01 Application Overview
- DOC-02 Capabilities Register
- DOC-03 Workflow Register
- DOC-04 Roles and Access Matrix
- DOC-05 Business Rules and Status Lifecycle
- DOC-06 Data, Reports, and Notifications Register
- DOC-07 Application Dependencies Register
- DOC-08 Support and Operations Guide
- DOC-11 Acceptance and Handover Record

DOC-09 Risk and Controls Register and DOC-10 User and Admin Guide may be Accept with Conditions for limited internal pilot use, but should be accepted before full operational launch.
