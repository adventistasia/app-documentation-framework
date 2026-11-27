# Example: a Standard package (LHC Booking System)

This folder is a complete, illustrative Standard-level documentation package for the LHC Booking System: a public booking form for a guest house, with staff review, room assignment, check-in and reporting. It was rebuilt from the old single-file example and keeps its business content (its 16 capabilities, 8 workflows and 10 dependencies), corrected and filled out; two capabilities were added for check-in and the automated expiry into the full set of documents. Names, people, numbers, costs, hosts, technology choices, commands, test results and sign-offs are all illustrative. They show the shape of a good package, not a real system.

## Why it is Standard

The Scope Record ([SP-00](docs/SP-00-scope-record.md)) scores it D1 3 (public users), D2 2, D3 2 (guest personal data), D4 1, D5 3 (five roles, ten statuses, eleven rules), D6 2 and D7 1. That totals 14, inside the Standard band. Floor rule F3 applies because D6 is 2, which sets ENG-09 to depth D. All eleven triggers are Yes. T7 is the nightly job that sends reminders for Returned requests after 7 days and expires them after 14. T11 is the public form, which brings in the accessibility statement, the rate limit and the threat model.

## How to read it

Start with [BUS-01](docs/BUS-01-overview-and-business-case.md), which covers the problem, the benefits, what success looks like and who owns the system, and use its package map to find everything else. Then pick the route that fits your role:

- **Business owner or manager:** BUS-01, SP-10, BUS-07, BUS-08, SP-12.
- **Front office or support:** BUS-03, BUS-05, BUS-09, ENG-08.
- **Engineer or agent:** [AGENTS.md](AGENTS.md), ENG-09, ENG-01, ENG-03, ENG-04, ENG-10.
- **Tester or acceptor:** ENG-01, SP-11, SP-12.

Things to look for:

- **One lifecycle.** The statuses ST-01 to ST-10 and the transitions TR-01 to TR-10 are defined once, in BUS-05. Every other document uses those exact names. Room assignment is an action, not a status (ADR-004).
- **Links that agree in both directions.** Each capability's `Processes` matches the process's `Capabilities`, each process's `Journeys` matches the journey's `Processes`, and each dependency's `Capabilities affected` matches the capabilities that list it.
- **No "System" as a role.** Work the application does on its own appears under `Automated`, for example C-12, C-18 and TR-07.
- **Measures linked to evidence.** Each benefit (BEN) leads to an L1 measure (SM). Each L4 measure leads to an output check (OC) in ENG-08, and together the checks cover every core record.
- **Acceptance you can verify.** Every Must FR, every NFR, every rule and every transition has a Given/When/Then criterion in SP-11 with evidence, and rules and transitions have negative cases too. One Should criterion (AC-48) failed and was waived by a named approver, which is why SP-12 carries a condition (COND-01).
- **Honest handover.** Someone who did not write the procedures dry-ran the deploy, rollback and restore. Every limitation (LIM-01 to LIM-04) is collected in SP-12, and each owner recorded their own decision.

The [reviews/](reviews/audit-2026-06-30-capabilities-and-workflows.md) folder holds a teaching audit of the *old* example. Every finding in it is true of that file, and this package fixes each one.

## Documents

| File | Document | Depth | Sections it holds |
|---|---|---|---|
| [docs/SP-00-scope-record.md](docs/SP-00-scope-record.md) | SP-00 Scope Record | D | |
| [docs/SP-10-success-measures.md](docs/SP-10-success-measures.md) | SP-10 Success Measures Register | D | |
| [docs/SP-11-acceptance-criteria-and-verification.md](docs/SP-11-acceptance-criteria-and-verification.md) | SP-11 Acceptance Criteria & Verification Register | D | |
| [docs/SP-12-acceptance-and-handover-record.md](docs/SP-12-acceptance-and-handover-record.md) | SP-12 Acceptance & Handover Record | D | |
| [docs/BUS-01-overview-and-business-case.md](docs/BUS-01-overview-and-business-case.md) | BUS-01 Application Overview & Business Case | D | SP-01 Glossary (S) |
| [docs/BUS-02-capabilities-register.md](docs/BUS-02-capabilities-register.md) | BUS-02 Capabilities Register | D | |
| [docs/BUS-03-business-process-register.md](docs/BUS-03-business-process-register.md) | BUS-03 Business Process Register | D | ENG-02 User Journeys (S) |
| [docs/BUS-04-roles-and-access-matrix.md](docs/BUS-04-roles-and-access-matrix.md) | BUS-04 Roles & Access Matrix | D | |
| [docs/BUS-05-business-rules-and-status-lifecycle.md](docs/BUS-05-business-rules-and-status-lifecycle.md) | BUS-05 Business Rules & Status Lifecycle | D | |
| [docs/BUS-06-data-reports-and-notifications.md](docs/BUS-06-data-reports-and-notifications.md) | BUS-06 Data, Reports & Notifications Register | D | |
| [docs/BUS-07-resource-and-cost-model.md](docs/BUS-07-resource-and-cost-model.md) | BUS-07 Resource & Cost Model | D | |
| [docs/BUS-08-risk-and-controls-register.md](docs/BUS-08-risk-and-controls-register.md) | BUS-08 Risk & Controls Register | D | |
| [docs/BUS-09-user-and-admin-guide.md](docs/BUS-09-user-and-admin-guide.md) | BUS-09 User & Admin Guide | D | |
| [docs/ENG-01-requirements-specification.md](docs/ENG-01-requirements-specification.md) | ENG-01 Requirements Specification | D | |
| [docs/ENG-03-architecture-and-design.md](docs/ENG-03-architecture-and-design.md) | ENG-03 Architecture & Design | D | |
| [docs/ENG-04-data-model.md](docs/ENG-04-data-model.md) | ENG-04 Data Model | D | |
| [docs/ENG-05-integrations-and-dependencies.md](docs/ENG-05-integrations-and-dependencies.md) | ENG-05 Integrations & Dependencies Register | D | |
| [docs/ENG-07-deployment-and-release.md](docs/ENG-07-deployment-and-release.md) | ENG-07 Deployment & Release Guide | D | |
| [docs/ENG-08-operations-and-support-runbook.md](docs/ENG-08-operations-and-support-runbook.md) | ENG-08 Operations & Support Runbook | D | |
| [docs/ENG-09-developer-and-agent-guide.md](docs/ENG-09-developer-and-agent-guide.md) | ENG-09 Developer & Agent Guide | D | ENG-06 Configuration & Environments (S) |
| [docs/ENG-10-decision-log.md](docs/ENG-10-decision-log.md) | ENG-10 Decision Log | D | |
| [AGENTS.md](AGENTS.md) | Root pointer to ENG-09 | — | |

That makes 21 files holding all 24 items: SP-01, ENG-02 and ENG-06 are S sections inside their parents.

## Checking it

```text
python3 tools/doclint.py package examples/lhc_booking_system --today 2026-10-07
```

The linter reports no High or Medium findings. The framework self-check (`python3 tools/doclint.py framework .`) also lints this package.
