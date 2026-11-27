# Engineering Layer Rubrics

These are the documentation review criteria for the engineering-layer documents ENG-01 to ENG-10. They judge the documents, not the application. Apply them together with the [universal rubric](00_universal_rubric.md). Which criteria apply to an item at depth S, D or D+, what the result values mean, how the **Critical** and **Full only** flags are used, and how results turn into a decision are defined only in the [decision rules](04_decision_rules.md).

Where a criterion names a cross-document rule (`X-xx`), the [linter](../review/05_linter_spec.md) checks the mechanical part of that rule and its output is authoritative; the criterion judges what the linter cannot see (meaning, completeness, usability). Do not report the same linter finding again as a criterion failure. Criteria that depend on a trigger say so; when the Scope Record answers that trigger No, the result is Not in scope.

Templates: [templates/engineering/](../templates/engineering/). Criterion IDs follow [conventions §7](../02_conventions.md#7-rubric-criterion-ids).

## ENG-01 Requirements Specification

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| ENG-01.1 | Functional requirement form | Every FR is written as "The system shall…", states one observable behaviour, and could not reasonably be built two different ways that both satisfy it. | No | No |
| ENG-01.2 | Traces to capability | Every FR lists at least one capability in `Capabilities`, and the business rules it enforces in `Rules` by ID, without restating the rule text. At depth D or D+, every capability not marked `Admin/support only` is covered by at least one FR (X-18). | Yes | No |
| ENG-01.3 | Must coverage | Every Must capability in BUS-02 has its Must FRs; nothing the application must do for launch is missing. Won't items are recorded so they are not built by accident. | No | No |
| ENG-01.4 | Measurable NFR targets | Every NFR has a `Target` with a number, unit and timeframe or load (for example "p95 ≤ 2 s at 50 concurrent users"), and a measurement method saying how it is checked. No target is an adjective. | Yes | No |
| ENG-01.5 | NFR categories covered | Every fixed category (availability, performance, capacity, security, privacy, accessibility, compatibility, maintainability, observability, data retention, recoverability) has at least one NFR or is listed as not applicable with a reason. RTO and RPO are stated as recoverability NFRs. | No | No |
| ENG-01.6 | Priority and status | Every FR and NFR has `Priority` (Must / Should / Could / Won't) and a status (Proposed / Agreed / Built / Verified). No requirement is Verified unless its application acceptance criteria in SP-11 have passed. | No | No |
| ENG-01.7 | Verifiable | Every FR and NFR is specific enough that a tester could write its application acceptance criterion without asking the author, and each is in the `Verifies` column of at least one SP-11 criterion (X-19 checks Must FRs and all NFRs). | No | No |
| ENG-01.8 | Constraints | Technology, hosting, budget, regulatory and schedule constraints are listed with their source and impact on the design, or the document states there are none. | No | No |
| ENG-01.9 | Agrees with business layer | NFR values match the plain-language summary in BUS-01; rules are referenced from BUS-05, not redefined; L3 measures in SP-10 use the same numbers as the NFRs they restate. | No | No |
| ENG-01.10 | Sources and rationale | Each requirement has a recorded source, rationale, approver and date. | No | Yes |
| ENG-01.11 | NFR verification plan | Each NFR says how it is proven before go-live and kept true in operation, with evidence linked once it exists. | No | Yes |

## ENG-02 User Journeys

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| ENG-02.1 | Journey coverage | There is a journey for each main goal of every role that uses the application through a screen; no main role goal in BUS-03 or BUS-09 is missing. | Yes | No |
| ENG-02.2 | Traceability | Every journey names its `Roles`, `Processes`, `Requirements` and `Transitions` (or `None`) by ID; process links are two-way with BUS-03 (X-16), and the transitions are ones defined in BUS-05. | Yes | No |
| ENG-02.3 | Goal, entry and exit | Each journey states the goal, the entry point and the exit state in terms a tester can check (including the resulting status). | No | No |
| ENG-02.4 | Steps and responses | Each journey has numbered steps, each with the user action and the system response, and names the transition at every step that changes a status. | No | No |
| ENG-02.5 | Alternative and error paths | Validation, permission, conflict, dependency-failure and cancel paths are given where they can occur, each saying exactly what the user sees and where the journey ends. | No | No |
| ENG-02.6 | Flow diagram | Each journey has a Mermaid flow diagram with a caption that matches its steps and paths. | No | No |
| ENG-02.7 | Boundary with BUS-03 | Journeys describe only interaction with the system; manual work outside the system is left to BUS-03 and not repeated. | No | No |

## ENG-03 Architecture & Design

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| ENG-03.1 | Context view | A C4 level 1 diagram shows the application, its user roles and every external system it exchanges data with; every integration in ENG-05 appears (X-29), and arrows say what flows. | Yes | No |
| ENG-03.2 | Containers and stack | Every separately deployed or run part (front end, API, worker, job, database, queue, file store) is listed with technology and version, responsibility and owner; every container that stores data lists its ENG-04 entities (X-29). At depth S a stack list with technology and responsibility is enough. | Yes | No |
| ENG-03.3 | Runtime view | Sequence diagrams cover the 3–5 most important journeys, show where data is written and what happens when an external call fails, and match the steps in ENG-02 (X-29). | No | No |
| ENG-03.4 | Deployment view | Shows where each container runs in production, the environments by ENG-06 `ENV` ID, network and trust boundaries, and how users and external systems reach it. | No | No |
| ENG-03.5 | Cross-cutting concepts | Authentication, authorisation (linked to BUS-04), logging, error handling, auditing, caching, time zones and internationalisation each have an approach and the code location, or say "Not used". | No | No |
| ENG-03.6 | Quality goals | The top three NFRs are named by ID in priority order, each with how the design achieves it. | No | No |
| ENG-03.7 | Security section | When T4 or T11 is Yes, or at depth D+: states the authentication method, authorisation model, trust boundaries, encryption in transit and at rest, audit logging, and the highest data classification held in each store. Otherwise Not in scope, with the one-line statement present. | Yes | No |
| ENG-03.8 | Threat model summary | When T4 or T11 is Yes, or at depth D+: lists the main threats per trust boundary or asset with the control for each, and links residual risks to BUS-08 by `RISK` ID. | No | No |
| ENG-03.9 | Technical risks and debt | Known weaknesses and debt are listed with impact and plan or trigger; each that could affect the business is linked to a BUS-08 risk by ID. | No | No |
| ENG-03.10 | Diagrams usable and current | Diagrams are Mermaid with captions, agree with each other and with the code; content derived from code is marked inferred until confirmed. | No | No |
| ENG-03.11 | Component views | Each critical container has a C4 level 3 component view with responsibilities and code locations. | No | Yes |

## ENG-04 Data Model

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| ENG-04.1 | Records mapped to entities | Every entity lists the BUS-06 records it stores in `Records`, and every record is stored by at least one entity (X-17). | Yes | No |
| ENG-04.2 | Classification and retention | Every entity has a `Classification` at least as high as its records, and a retention period matching BUS-06 with how it is enforced; personal and confidential fields are marked at field level. | Yes | No |
| ENG-04.3 | System of record and owner | Each entity says whether this application is the system of record (or names the one that is) and who owns the data. | No | No |
| ENG-04.4 | Field detail | Each entity lists its fields with type, required, constraints and keys, enough for an engineer or agent to write a correct query or migration without reading the schema. | No | No |
| ENG-04.5 | Status fields | Every status field lists the BUS-05 status IDs it may hold, and these match the BUS-05 status table. | No | No |
| ENG-04.6 | Relationships | An ER diagram with a caption shows the entities and relationships, consistent with the keys in the field tables. | No | No |
| ENG-04.7 | Migrations | The migration tool, location, naming, how to create, apply and reverse, and the approach to destructive and data migrations are stated. | No | No |
| ENG-04.8 | Reference data | Each set of reference data has a source, an owner and an update process. | No | No |
| ENG-04.9 | Data lifecycle and deletion | For each entity with personal or regulated data: retention trigger, deletion method, effect on backups and evidence of purges. | No | Yes |

## ENG-05 Integrations & Dependencies Register

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| ENG-05.1 | Dependency coverage | Hosting, domain, email, identity, integrations, data, vendors, network, people, process and funding dependencies are listed where they apply, and downstream consumers are included; nothing a support person would need to check during an outage is missing. | No | No |
| ENG-05.2 | Purpose | Each dependency says why the application needs it. | No | No |
| ENG-05.3 | Owner | Each dependency has a named owner (X-09). | Yes | No |
| ENG-05.4 | Impact | Each dependency states what users and the business experience if it is unavailable, not only the technical error (X-09). | Yes | No |
| ENG-05.5 | Criticality and type | Each dependency has a `Criticality` (High / Medium / Low) consistent with its impact, and a `Type` from the fixed list (X-20). | No | No |
| ENG-05.6 | Support path | Each dependency has a support or escalation path a support person can actually use: team, channel and contract or account reference (X-09). | Yes | No |
| ENG-05.7 | Traceability | High and Medium dependencies list the capabilities affected, consistent with the `Dependencies` column of BUS-02 (X-09). | No | No |
| ENG-05.8 | Workaround | Each High dependency has a business workaround, or explicitly states `None` (X-09). | No | No |
| ENG-05.9 | Interfaces | When T5 is Yes: every integration has an interface entry (X-20) giving direction, protocol, non-secret endpoint or location, data exchanged by `ENT` ID, trigger or frequency, authentication (by `SEC` ID, never a value), error and retry behaviour, contract link and the owner on the other side. | No | No |
| ENG-05.10 | Runbook, cost and renewal | Every High dependency names its ENG-08 runbook entry (X-21); every dependency that costs money is marked `Cost` Yes and has a BUS-07 cost line (X-24); renewal dates are given where something can lapse. | No | No |
| ENG-05.11 | Direction and downstream impact | Every dependency is marked Upstream or Downstream; each downstream consumer states what it consumes, the impact on it if this application fails, and how it is told. | No | No |
| ENG-05.12 | Interface details | Each integration where a change on either side could break the other has its version and change policy, rate limits, idempotency, ordering, other-side service level and test environment. | No | Yes |
| ENG-05.13 | Exit and substitution | Each High vendor or external platform dependency states the data it holds, how to export it, alternatives, notice period and effort to switch. | No | Yes |

## ENG-06 Configuration & Environments

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| ENG-06.1 | Environments | Every environment has an `ENV` entry with purpose, URL, whether data is real, synthetic or masked, who has access, and hosting. | Yes | No |
| ENG-06.2 | Secrets by location only | Every secret the application uses is listed with where it is stored, what uses it, rotation and owner, and no secret value appears in this or any other document. | Yes | No |
| ENG-06.3 | Configuration items | Every non-secret setting the application reads has name, purpose, default, value source per environment and who may change it. | No | No |
| ENG-06.4 | Feature flags | Every flag has purpose, owner, default, state per environment and removal criteria, or the document says there are none. | No | No |
| ENG-06.5 | Real data protected | Any non-production environment holding real personal or confidential data is identified, with access controls equal to production or a reason and a BUS-08 risk. | No | No |
| ENG-06.6 | Promotion and parity | How configuration changes reach each environment is stated, and known differences between environments are listed with the risk they create. | No | No |
| ENG-06.7 | Matches the code | The configuration items and secrets match what the code actually reads; an operator could configure a new environment from this document alone. | No | No |

## ENG-07 Deployment & Release Guide

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| ENG-07.1 | Pipeline | Every step from merge to production is listed with trigger, action, approval, where it is defined and what happens on failure. | No | No |
| ENG-07.2 | Deployment steps with verification | Deployment to production (and to each other environment that is not fully automatic) is given as exact, numbered steps, each ending with smoke tests that state how to run them and the expected result. | Yes | No |
| ENG-07.3 | Rollback | Rollback has decision criteria with thresholds, who decides, exact steps (including what to do about database changes), and verification after rollback. | Yes | No |
| ENG-07.4 | Pre-deployment checklist | A checklist covers application acceptance criteria, migrations, configuration and flags, release notes, user and downstream communication, and rollback cover. | No | No |
| ENG-07.5 | Database migrations | States when migrations run, the compatibility rule between code and schema, how to reverse a migration, and when to take a backup first. | No | No |
| ENG-07.6 | Versioning | The versioning scheme is stated, and where the running version can be seen. | No | No |
| ENG-07.7 | Release notes | Release notes have a location and a format written for users, and feed the BUS-09 What's new section. | No | No |
| ENG-07.8 | Post-deployment monitoring | The monitoring window after a production deployment, who watches, and what is watched are stated, tied to the rollback criteria. | No | No |
| ENG-07.9 | Dry-run record | A deployment and a rollback have been performed from this document by someone other than its author, with date, environment, result, issues and evidence; nothing is recorded that did not happen. | No | No |
| ENG-07.10 | Emergency release | The shortened path for an urgent fix states which steps may be skipped, who approves and what follows, consistent with ENG-08 emergency changes. | No | Yes |
| ENG-07.11 | Progressive delivery | Where releases are rolled out gradually, each stage has exposure, duration and proceed and stop signals; or the document states releases are not staged. | No | Yes |

## ENG-08 Operations & Support Runbook

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| ENG-08.1 | Support ownership | Business, application and technical support are separated; every area in the ownership model has a named primary, backup and escalation owner. | Yes | No |
| ENG-08.2 | Intake process | Users can tell how to get help: the real channel and the information to include. | No | No |
| ENG-08.3 | Triage | Issue categories have examples, an owner, initial checks a first responder can do, and the dependencies to check by `D` ID (X-15). | No | No |
| ENG-08.4 | Escalation | Every category and support area has a concrete escalation condition and an escalation owner, so a support person could route a real issue (X-10). | Yes | No |
| ENG-08.5 | Routine operations | Recurring support and administration tasks are listed with an `MT` ID, frequency, owner, procedure and evidence of completion, so BUS-07 can count their effort. | No | No |
| ENG-08.6 | Known issues | Open known issues are listed with symptom, workaround and owner, or the document states none are known. | No | No |
| ENG-08.7 | Dependency checks | Symptoms map to the ENG-05 dependencies to check and to the runbook entry to follow. | Yes | No |
| ENG-08.8 | Access support | Account creation, role changes and access removal, including urgent removal, are explained with who requests, approves and performs them, consistent with BUS-04. | No | No |
| ENG-08.9 | Communication | Who communicates what to users, stakeholders and downstream consumers, through which channel and when, is defined for incidents, planned maintenance, changes and fixes. | No | No |
| ENG-08.10 | Service levels | Support hours, and response, update and resolution targets per severity, are stated; every SP-10 L3 measure has an SLO row, referenced by ID with the same numbers and naming the alert that fires on breach. | No | No |
| ENG-08.11 | Monitoring and alerting | The health check, dashboards, logs and normal ranges are stated with locations; every alert has a threshold, meaning, severity, owner and at least one runbook entry (X-21). | No | No |
| ENG-08.12 | Runbook entries | Every alert, every High dependency (X-21), every scheduled job and every failure mode from past incidents has a runbook entry with symptom, diagnosis, fix, verification and escalation, written so an operator who did not build the system can follow it. | No | No |
| ENG-08.13 | Incident management | Sev1–Sev4 are defined with examples, who declares an incident is stated, communication templates exist, and a post-incident review is required for the higher severities. | No | No |
| ENG-08.14 | Backup and restore | What is backed up, how often, for how long and where is stated; the restore procedure has exact steps and a verification step; the last restore test is recorded with date and result, or "Not yet tested" with a `Q-xx`. | Yes | No |
| ENG-08.15 | Recovery objectives and fallback | RTO and RPO are stated and identical to the recoverability NFRs in ENG-01; backup frequency meets the RPO; a manual business fallback is described. | No | No |
| ENG-08.16 | Maintenance calendar | Every certificate, domain, licence and secret rotation that can lapse, and patching, dependency upgrades, access reviews and data purges, has an `MT` entry with owner, frequency or next due date, and evidence. | No | No |
| ENG-08.17 | Output checks | When T6 is Yes: output checks of the stated types cover every core record (X-23), and each has `Records`, `Procedure`, `Frequency`, `Owner` and what to do on failure. | No | No |
| ENG-08.18 | Scheduled job monitoring | When T7 is Yes: every scheduled job has a schedule, a success signal, an alert and a runbook entry; when T7 is No, the one-line statement is present. | No | No |
| ENG-08.19 | Change management | Standard, normal and emergency changes are defined with examples, approval, lead time and communication, and how to request a change is stated. | No | No |
| ENG-08.20 | Disaster recovery procedure | A step-by-step procedure rebuilds the service after loss of its location or account, with expected times that fit within the RTO. | No | Yes |
| ENG-08.21 | Disaster recovery tests | A test cadence is set, and tests are recorded with scenario, achieved RTO and RPO, result and actions. | No | Yes |

## ENG-09 Developer & Agent Guide

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| ENG-09.1 | Exact, verified commands | Install, run, test, lint, build and migrate commands are exact and copy-pasteable from the repository root, each with its expected result and a "verified on" date and name; unverified commands are marked with a `Q-xx`. | Yes | No |
| ENG-09.2 | Agent rules | Specific lists state what an agent may change without asking, what needs a human (naming the role), and what it must never do, including never writing secret values and never inventing approvals or results. | Yes | No |
| ENG-09.3 | Update-trigger table | The update-trigger table is identical to the one in the documentation model, cites it as the source, and states that a pull request changing behaviour without the listed documents fails review. | Yes | No |
| ENG-09.4 | What the application is | One paragraph says what the application does and for whom, and links BUS-01. | No | No |
| ENG-09.5 | Repository map and prerequisites | Key directories are mapped, generated folders are marked, and prerequisites are listed with versions and how to obtain access. | No | No |
| ENG-09.6 | Conventions with examples | Coding conventions and patterns are stated as rules, each with an example or exemplar file to copy and what to avoid; deliberate unusual choices link to ENG-10. | No | No |
| ENG-09.7 | Safe change and definition of done | The steps to make and ship a change (branch, tests, review) and a definition of done that includes the documentation updates are given. | No | No |
| ENG-09.8 | Where to find things | Links to ENG-03, ENG-04, SP-11, SP-01 and the other documents in scope resolve, and say what each is used for. | No | No |
| ENG-09.9 | Placement and held sections | At Foundation the root `AGENTS.md` is this document and holds, as `## <DOC-ID> <Title>` sections listed in `contains`, every item the Scope Record places in it; at Standard and Full the root `AGENTS.md` points to this document. | No | No |

## ENG-10 Decision Log

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| ENG-10.1 | ADR format | Every decision record states status, date, deciders, context, the decision as a rule, at least one real alternative considered with why it was not chosen, and consequences including the negative ones. | Yes | No |
| ENG-10.2 | Index and status | Every ADR is in the index with a three-digit `ADR` ID, title, status (Proposed / Accepted / Superseded by ADR-xxx / Rejected), date and deciders; per-file ADRs are linked from the index. | No | No |
| ENG-10.3 | Decision coverage | ADRs exist for the choices an agent or new engineer might otherwise "fix": framework, data store, authentication approach, hosting, deliberate omissions, and patterns that look wrong but are intended. | Yes | No |
| ENG-10.4 | Supersession | Superseded ADRs are kept, and old and new records link to each other; no ADR has been deleted or its ID reused. | No | No |
| ENG-10.5 | Consistent with design | Accepted ADRs agree with ENG-03 and the code; where they no longer do, the ADR is superseded or the gap is raised as a `Q-xx`. | No | No |
| ENG-10.6 | Linked | Each ADR links the requirements, constraints, risks or incidents that drove it, and the ENG-03 sections it shapes. | No | No |

## Mapping from the 2026-06-30 criteria

The 2026-06-30 release reviewed DOC-07 Application Dependencies Register and DOC-08 Support and Operations Guide. Their criteria are kept in ENG-05 and ENG-08 with the same numbering.

| 2026-06-30 criterion | New criterion | Change |
|---|---|---|
| DEP-01 Dependency coverage | ENG-05.1 | Adds downstream consumers. |
| DEP-02 Purpose | ENG-05.2 | Unchanged. |
| DEP-03 Owner | ENG-05.3 | Now Critical. |
| DEP-04 Impact | ENG-05.4 | Now Critical; impact stated in business terms. |
| DEP-05 Criticality | ENG-05.5 | Adds the fixed `Type` list. |
| DEP-06 Support path | ENG-05.6 | Now Critical. |
| DEP-07 Traceability | ENG-05.7 | Maps to capabilities (BUS-02); workflows are reached through capabilities. |
| DEP-08 Workaround | ENG-05.8 | Unchanged. |
| — | ENG-05.9 to ENG-05.13 | New: interfaces, runbook and cost links, direction, interface details, exit. |
| SO-01 Support ownership | ENG-08.1 | Now Critical; adds backup and escalation owners. |
| SO-02 Intake process | ENG-08.2 | Unchanged. |
| SO-03 Triage | ENG-08.3 | Dependencies referenced by `D` ID. |
| SO-04 Escalation | ENG-08.4 | Now Critical. |
| SO-05 Routine operations | ENG-08.5 | Adds `MT` IDs and evidence of completion. |
| SO-06 Known issues | ENG-08.6 | Permanent limitations move to the standard Known limitations section and SP-12. |
| SO-07 Dependency checks | ENG-08.7 | Now Critical; links to runbook entries. |
| SO-08 Access support | ENG-08.8 | Adds urgent removal. |
| SO-09 Communication | ENG-08.9 | Adds downstream consumers. |
| — | ENG-08.10 to ENG-08.21 | New: service levels, monitoring, runbooks, incidents, backup and restore, recovery, maintenance, output checks, jobs, change management, disaster recovery. |
