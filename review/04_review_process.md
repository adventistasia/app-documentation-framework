# Review Process

## Purpose

This process defines how automated review agents and verifier agents should assess documentation artifacts.

## Roles

| Role | Responsibility |
|---|---|
| Producer agent | Drafts or updates documentation artifacts. |
| Review agent | Applies rubrics and produces AIDOS-style audit results. |
| Verifier/control agent | Applies deterministic pass/fail rules to accept, conditionally accept, reject, or require revision. |
| Business owner | Confirms business accuracy and acceptance. |
| Support owner | Confirms support readiness. |
| Technical/application owner | Confirms technical/application support assumptions and dependencies. |

## Three-pass review model

### Pass 1 - Structural and rubric review

Goal:

- Verify required sections, tables, owners, and references.
- Identify missing content early.
- Review whether the rubric itself has blind spots for the artifact.

Output:

- Pass/Partial/Fail for each criterion.
- Bugs, Risks, Ideas.
- Required fixes.

### Pass 2 - Coherence review

Goal:

- Compare artifact against related artifacts.
- Verify roles, workflows, capabilities, statuses, dependencies, risks, limitations, and support paths.

Output:

- Traceability findings.
- Cross-document inconsistencies.
- Updated acceptance recommendation.

### Pass 3 - Final acceptance review

Goal:

- Confirm all blocking issues are resolved or accepted as conditions.
- Confirm owner sign-off readiness.

Output:

- Final recommendation: Accept, Accept with Conditions, Revise and Resubmit, or Reject.

## Finding classifications

| Type | Meaning | Example |
|---|---|---|
| Bug | Something incorrect, inconsistent, missing, or unusable. | Workflow references role not defined in access matrix. |
| Risk | Something that may cause operational, governance, support, or acceptance failure. | Critical dependency has no owner or workaround. |
| Idea | Non-blocking improvement. | Add criticality column to capability register. |

## Evidence requirement

Every Bug or Risk should include evidence from the artifact or the absence of required evidence.

Examples:

- Evidence: Capability C04 has no workflow mapping.
- Evidence: No access removal process found.
- Evidence: Dependency D02 is marked High but has no support path.

## Recommended review sequence

1. Application Overview
2. Capabilities Register
3. Workflow Register
4. Roles and Access Matrix
5. Business Rules and Status Lifecycle
6. Data, Reports, and Notifications Register
7. Application Dependencies Register
8. Support and Operations Guide
9. Risk and Controls Register
10. User and Admin Guide
11. Acceptance and Handover Record
12. Package-level acceptance review
