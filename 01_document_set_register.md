# Document Set Register

## Purpose

This register lists every document in the standard: what it is for, who reads it, which outcome requirements it serves, when it is due, how to produce it and what questions it must answer. Which of these a given project actually writes, and at what depth, is decided by its [Scope Record](03_scoping_guide.md); this register describes each document at its full extent.

Requirement codes (B1–B4, E1–E6, S1–S3) are defined in the [documentation model](00_documentation_model.md#what-the-documentation-must-let-people-answer). Stages are defined in the [documentation model](00_documentation_model.md#stages). Depth by level is in the [scoping guide's depth matrix](03_scoping_guide.md#depth-matrix).

## Document set

| ID | Document | Layer | Serves | Primary readers | Draft by stage | Accepted by stage | Replaces | Template |
|---|---|---|---|---|---|---|---|---|
| SP-00 | Scope Record | Spine | all | Owners, reviewers | 1 | 1 | new | [SP-00](templates/spine/SP-00-scope-record.md) |
| SP-01 | Glossary | Spine | all | Everyone | 1 | 5 | new | [SP-01](templates/spine/SP-01-glossary.md) |
| SP-10 | Success Measures Register | Spine | S1, S2 | Business owner, operators | 1 (L1) | 5 | new | [SP-10](templates/spine/SP-10-success-measures.md) |
| SP-11 | Acceptance Criteria & Verification Register | Spine | S3 | Business owner, testers, operators, agents | 2 | 4 | new | [SP-11](templates/spine/SP-11-acceptance-criteria-and-verification.md) |
| SP-12 | Acceptance & Handover Record | Spine | S1, S3 | Owners, project owner | 5 | 5 | DOC-11 | [SP-12](templates/spine/SP-12-acceptance-and-handover-record.md) |
| BUS-01 | Application Overview & Business Case | Business | B1, B2, S1 | Management, business owner, everyone first | 1 | 1 | DOC-01 | [BUS-01](templates/business/BUS-01-overview-and-business-case.md) |
| BUS-02 | Capabilities Register | Business | B3 | Business owner, support, engineering | 2 | 2 | DOC-02 | [BUS-02](templates/business/BUS-02-capabilities-register.md) |
| BUS-03 | Business Process Register | Business | B3, E5 | Process owner, operations staff | 2 | 2 | DOC-03 | [BUS-03](templates/business/BUS-03-business-process-register.md) |
| BUS-04 | Roles & Access Matrix | Business | B3, E3 | Business owner, access approvers, auditors | 2 | 4 | DOC-04 | [BUS-04](templates/business/BUS-04-roles-and-access-matrix.md) |
| BUS-05 | Business Rules & Status Lifecycle | Business | E2, E3, S3 | Business owner, engineering, testers | 2 | 4 | DOC-05 | [BUS-05](templates/business/BUS-05-business-rules-and-status-lifecycle.md) |
| BUS-06 | Data, Reports & Notifications Register | Business | B3, E2 | Data owner, compliance, support | 2 | 4 | DOC-06 | [BUS-06](templates/business/BUS-06-data-reports-and-notifications.md) |
| BUS-07 | Resource & Cost Model | Business | B4, E4 | Budget holder, management | 1 | 5 | new | [BUS-07](templates/business/BUS-07-resource-and-cost-model.md) |
| BUS-08 | Risk & Controls Register | Business | B2, E4 | Management, risk and audit | 4 | 5 | DOC-09 | [BUS-08](templates/business/BUS-08-risk-and-controls-register.md) |
| BUS-09 | User & Admin Guide | Business | E5 | End users, admins, support | 4 | 5 | DOC-10 | [BUS-09](templates/business/BUS-09-user-and-admin-guide.md) |
| ENG-01 | Requirements Specification | Engineering | E3, S3 | Engineering, testers, agents | 2 | 2 | new | [ENG-01](templates/engineering/ENG-01-requirements-specification.md) |
| ENG-02 | User Journeys | Engineering | E5 | Engineering, designers, testers | 2 | 5 | new | [ENG-02](templates/engineering/ENG-02-user-journeys.md) |
| ENG-03 | Architecture & Design | Engineering | E1, E2 | Engineering, technical operators, agents | 2 (context) | 3 | new | [ENG-03](templates/engineering/ENG-03-architecture-and-design.md) |
| ENG-04 | Data Model | Engineering | E1, E2 | Engineering, data owner, agents | 3 | 3 | new | [ENG-04](templates/engineering/ENG-04-data-model.md) |
| ENG-05 | Integrations & Dependencies Register | Engineering | E6, B4 | Engineering, support, owners | 3 | 4 | DOC-07 | [ENG-05](templates/engineering/ENG-05-integrations-and-dependencies.md) |
| ENG-06 | Configuration & Environments | Engineering | E4 | Engineering, technical operators | 3 | 5 | new | [ENG-06](templates/engineering/ENG-06-configuration-and-environments.md) |
| ENG-07 | Deployment & Release Guide | Engineering | E4 | Technical operators, release managers | 4 | 5 | new | [ENG-07](templates/engineering/ENG-07-deployment-and-release.md) |
| ENG-08 | Operations & Support Runbook | Engineering | E4, S2 | Support desk, technical operators | 4 | 5 | DOC-08 | [ENG-08](templates/engineering/ENG-08-operations-and-support-runbook.md) |
| ENG-09 | Developer & Agent Guide | Engineering | E1, E4 | Developers and AI agents (read first) | 3 | 5 | new | [ENG-09](templates/engineering/ENG-09-developer-and-agent-guide.md) |
| ENG-10 | Decision Log | Engineering | E1 | Engineering, agents, future maintainers | 3 | 5 | new | [ENG-10](templates/engineering/ENG-10-decision-log.md) |

IDs SP-02 to SP-09 are reserved for future spine documents.

---

## Spine

### SP-00 Scope Record

**Purpose:** records which items this application documents, at what depth, and why. It is the contract the package is reviewed against.

**How to produce:** follow the [scoping guide](03_scoping_guide.md). Score with the business and technical owners together, or have the scoping agent draft it and the owners correct it. Approve before any other document is accepted.

**Questions to answer:**
- What level is this project, and why (one reason per dimension)?
- Which floor rules and triggers apply?
- For every item: what depth, which parent for S items, and why is any item not needed?
- Who approved the scope, and when? What has changed since?

### SP-01 Glossary

**Purpose:** defines every role, status, record and specialist term once, so every document uses the same names.

**How to produce:** start from the role, status and record tables; add any term a new team member or an agent would not know; list the synonyms people actually use so documents can avoid them.

**Questions to answer:**
- What does each term mean, in one sentence?
- What other names are used for it, and which must be avoided?
- Where is it defined in detail (document and ID)?

### SP-10 Success Measures Register

**Purpose:** states how success is measured at each level (L1 business outcome, L2 product acceptance, L3 operational health, L4 output correctness), with baselines, targets, data sources and owners.

**How to produce:** start from the BUS-01 benefits; for each, ask "what number would show this is happening?" Add L2 from SP-11 pass rates, L3 as SLI/SLO pairs that ENG-08 monitors, and L4 output checks derived from business rules and reports (invariants, reconciliations, completeness, sample audits, golden data). Where no baseline exists, say when it will be captured.

**Questions to answer:**
- How will we know the application is delivering its benefits?
- What exactly is measured, from what data, how often, by whom?
- What is the baseline, the target, and the value at which someone must act?
- How do we know the outputs are correct, not only that the system is up?

### SP-11 Acceptance Criteria & Verification Register

**Purpose:** holds the application acceptance criteria (Given/When/Then), how each is verified, and the result. It is the objective test of "does the application do the right thing?".

**How to produce:** write at least one criterion for every Must requirement and every NFR in ENG-01, and a positive and a negative criterion for every business rule and every status transition in BUS-05. Write so a third party can say pass or fail without asking the author. Fill in results and evidence during the Verify stage.

**Questions to answer:**
- For each requirement, rule and transition, what observable outcome proves it works?
- How is each criterion verified, and where is the test or evidence?
- What passed, what failed, what was waived and by whom?

### SP-12 Acceptance & Handover Record

**Purpose:** the formal readiness and accountability record: what was delivered, what was deferred, what the acceptance results were, which limitations and risks were accepted, who operates the application now, and who signed off.

**How to produce:** compile at go-live from SP-11 results, SP-10 baselines, the Known limitations sections of every document, and the open conditions from reviews. Collect decisions from the business, support and technical owners. Never pre-fill a sign-off.

**Questions to answer:**
- What was delivered and what was deferred?
- Did every Must acceptance criterion pass, or was it waived by an owner?
- Which success measures have baselines, and when is the first benefit review?
- Which limitations and risks are accepted, and by whom?
- Who owns, supports and operates the application from now on?

---

## Business layer

### BUS-01 Application Overview & Business Case

**Purpose:** the first document anyone reads. Explains what the application is, why it exists, what it is worth, what success looks like, and who owns and supports it.

**How to produce:** interview the business owner and support owner; review project briefs and existing descriptions. Keep it short enough for a manager to read first. Link to detailed documents rather than repeating them. At Foundation level it also holds the S sections of the other business and spine items.

**Questions to answer:**
- What is the application, what does it do, and where is it accessed?
- What problem does it solve, who is affected, and what does that problem cost today?
- What benefits will it deliver, to whom, measured how, from what baseline to what target, by when?
- What does success look like, in three to five plain sentences?
- What happens if it is unavailable? Which business objective or policy does it support?
- What will it cost to run, in one paragraph?
- Who owns it, supports it and uses it? What is in and out of scope?
- What are the top non-functional commitments, in plain words ("available during office hours, 99.5%")?

### BUS-02 Capabilities Register

**Purpose:** lists what the system can do, in business language, with the outcome, users, owner, criticality and the processes that use each capability.

**How to produce:** ask what the application can do for users and the business. Use business verbs (Submit, Review, Approve, Assign, Track, Notify, Report, Reconcile, Archive, Audit), not interface words. Validate against the business processes and support needs.

**Questions to answer:**
- What can the system do, and what outcome does each capability produce?
- Who uses each capability (by role), and which processes use it?
- Which are critical for launch, and which dependencies do they rely on?
- Which are administrative, support, reporting, access or audit capabilities?
- Which actions are automated rather than performed by a role?

### BUS-03 Business Process Register

**Purpose:** documents the end-to-end business processes the application supports, including manual work outside the system.

**How to produce:** start from the real work people do. For each process, define the trigger, roles, steps, decisions, statuses, outcome, exceptions and capabilities used. Keep all processes at the same business level: one trigger to one outcome. Validate with process owners and actual users.

**Questions to answer:**
- What starts each process, who takes part, and what is the successful outcome?
- What steps happen in order, and which decisions are made by whom?
- Which statuses and capabilities are used?
- What are the exception and alternate paths?
- What still happens outside the system?

### BUS-04 Roles & Access Matrix

**Purpose:** defines each role, what it may do, who approves access, and how access is requested and removed.

**How to produce:** collect every user type from processes, journeys, support and administration. Define permissions per role. Identify approvers, the removal process and sensitive permissions or risky combinations.

**Questions to answer:**
- What roles exist and what can each do?
- Who approves access, how is it requested, and how is it removed (including urgent removal)?
- Which permissions are sensitive, and which combinations must be separated?
- How often is access reviewed, and by whom?

### BUS-05 Business Rules & Status Lifecycle

**Purpose:** the rules the application must enforce, and every status and allowed transition of its records, written so each can be tested.

**How to produce:** extract rules from processes, policies, decisions, exceptions and support issues. Write each as a condition and an action. Define every status and every allowed transition with the role (or `Automated`) that performs it and the rule that guards it. Assign rule owners and exception authorities.

**Questions to answer:**
- What rules must the application enforce, who owns each, and what exceptions are allowed by whom?
- What statuses exist and what does each mean?
- Which transitions are allowed, by whom, under what condition?
- What validations block progress?

### BUS-06 Data, Reports & Notifications Register

**Purpose:** lists the business records the application holds, how they are classified and kept, and the reports, exports and notifications it produces.

**How to produce:** identify the main records, their required fields, owner, classification, purpose (for personal data), retention period with rationale and disposal method. List every report, export, dashboard and notification with its audience, purpose, source or trigger, and expected action.

**Questions to answer:**
- What records does the application create or manage, and who owns them?
- How is each classified, why is personal data held, how long is it kept, and how is it disposed of?
- What reports and exports are produced, for whom, from what source, how often? Which are official records?
- What notifications are sent, when, to whom, why, and what should the recipient do?

### BUS-07 Resource & Cost Model

**Purpose:** tells the business what it takes to deploy and run the application: people, effort, skills, infrastructure, licences, running costs, renewals and end-of-life.

**How to produce:** start with an estimate at Initiate and refine it. Take every cost-bearing dependency from ENG-05 and every routine task from ENG-08. Estimates are acceptable if marked as estimates with their basis.

**Questions to answer:**
- Who needs to spend how much time on support, administration, data upkeep and releases?
- What one-off effort does deployment need (build, migration, training, cutover)?
- What infrastructure, services and licences are needed, at what cost, renewing when, owned by whom?
- What does it cost per month and per year, under what assumptions, and what makes the cost grow?
- Who holds the budget? What would retiring it involve?

### BUS-08 Risk & Controls Register

**Purpose:** records what can go wrong (operational, access, data, privacy and compliance, reporting, dependency, support, technical) and the controls that reduce it.

**How to produce:** derive risks from processes, access, data, reports, dependencies, support, known limitations, technical debt in ENG-03 and incidents. For each, rate likelihood and impact, name the control and the owner, and state residual risk and review cadence. Ask: has a privacy impact assessment been done? Link it or state why not needed.

**Questions to answer:**
- What can go wrong, how likely is it, and how bad would it be?
- What controls reduce each risk, and who owns them?
- What risk remains, who has accepted it, and when is it reviewed?

### BUS-09 User & Admin Guide

**Purpose:** helps users and administrators succeed with the application, organised by what the reader is trying to do: get started, do a task, understand the system, look something up, get help, see what changed.

**How to produce:** turn each user-facing journey in ENG-02 into a how-to. Explain every user-visible status in the user's own words. Separate user and admin tasks. Include the accessibility statement and supported browsers and devices when in scope. Instructions must never exceed the reader's permissions.

**Questions to answer:**
- How does a new user get access and complete a first task?
- How does a user or admin perform each main task, and what should they see when it works?
- What do the statuses and messages mean, and what should the user do?
- What went wrong, and where do I get help?
- What changed in the latest release?

---

## Engineering layer

### ENG-01 Requirements Specification

**Purpose:** the functional and non-functional requirements the system must meet, each traceable to a capability and verifiable by an acceptance criterion.

**How to produce:** write functional requirements as "The system shall…", one behaviour each, traced to capabilities and business rules. Write non-functional requirements in the fixed categories (availability, performance, capacity, security, privacy, accessibility, compatibility, maintainability, observability, data retention, recoverability) with measurable targets. List constraints. Prioritise with MoSCoW.

**Questions to answer:**
- What must the system do, and for which capability?
- How well must it do it: how fast, how available, how secure, how recoverable, for how many users?
- What constraints apply (technology, hosting, budget, regulation)?
- Which requirements are Must, and what is the status of each?

### ENG-02 User Journeys

**Purpose:** describes each main persona goal as a step-by-step interaction with the system, including error paths and the status changes it causes.

**How to produce:** one journey per main role goal. List entry point, steps with system responses, transitions caused, happy, alternative and error paths, and exit state. Add a Mermaid flow diagram. BUS-03 describes the business process including manual work; ENG-02 describes only the person's interaction with the system.

**Questions to answer:**
- What is each role trying to achieve, and where do they start?
- What do they do at each step, and how does the system respond?
- What can go wrong, and what does the user see then?
- Which statuses change, and which process and requirements does the journey serve?

### ENG-03 Architecture & Design

**Purpose:** explains how the system is built and how it works at run time, using a cut-down arc42 outline and C4 diagrams.

**How to produce:** draw the C4 context and containers at Define; add the runtime view for the most important journeys, the deployment view, cross-cutting concepts, quality goals, the security section and technical risks during Build. At Full level add component views for critical containers. For an existing system, derive from the code and mark inferences.

**Questions to answer:**
- What are the system's parts, what technology does each use, and how do they talk?
- How does a request for each main journey move through the system?
- Where and how is it deployed, and where are the network and trust boundaries?
- How are authentication, authorisation, logging, errors, auditing and time zones handled?
- Which quality goals does the design optimise for?
- What technical risks and debt exist?

### ENG-04 Data Model

**Purpose:** the technical data model: entities, fields, keys, relationships, classification, system of record and retention, mapped to the business records in BUS-06.

**How to produce:** derive from the schema or design. Map each business record to its entities. Carry classification down to fields and stores. Make status fields reference BUS-05 status IDs. Describe migrations and reference data with owners.

**Questions to answer:**
- Which entities store each business record, and how are they related?
- What fields, types, constraints and keys does each entity have?
- Where is each entity the system of record? How long is it kept?
- How are schema changes migrated, and who maintains reference data?

### ENG-05 Integrations & Dependencies Register

**Purpose:** everything the application relies on (systems, services, accounts, data, people, vendors, funding) and the contract for every data exchange with another system.

**How to produce:** list every dependency with owner, purpose, type, criticality, impact if unavailable, support path, workaround, renewal and whether it costs money. For each integration, add an interface entry: direction, protocol, endpoint (non-secret), data exchanged, trigger, authentication, error and retry behaviour, contract link, and the owning team on the other side. Classify upstream and downstream.

**Questions to answer:**
- What must be available for the application to work, who owns it, and what happens if it fails?
- Who supports each dependency, and is there a workaround?
- What data is exchanged with which systems, how, how often, and under what contract?
- What breaks if this application fails (downstream)?
- Which dependencies need renewal, funding or periodic review?

### ENG-06 Configuration & Environments

**Purpose:** the environments, configuration items, secrets (locations only) and feature flags an operator or agent must know to run the system.

**How to produce:** list each environment with purpose, URL, data type and access. List configuration items with defaults and the source of per-environment values. List secrets by name, storage location, rotation and owner, never by value. List feature flags with owner and removal criteria.

**Questions to answer:**
- Which environments exist, what are they for, and who can reach them?
- What configuration does the application read, and where do the values come from?
- What secrets exist, where are they stored, and when are they rotated?
- What feature flags exist, and when will each be removed?

### ENG-07 Deployment & Release Guide

**Purpose:** how a change gets from a merged commit to production safely, how to verify it, and how to roll it back.

**How to produce:** write the pipeline steps, approvals, pre-deployment checklist, per-environment deployment steps with verification (smoke tests), rollback procedure with decision criteria, versioning scheme and release notes location. Dry-run it with someone who did not write it.

**Questions to answer:**
- How is a release built, approved and deployed to each environment?
- What must be checked before and after deploying?
- When do we roll back, and exactly how?
- Where are release notes, and how are versions numbered?

### ENG-08 Operations & Support Runbook

**Purpose:** everything needed to support and operate the application after go-live: ownership, intake, triage, service levels, monitoring, incidents, runbook entries, backup and restore, continuity, maintenance, output checks and change management.

**How to produce:** separate business support from technical support. Define intake, triage and escalation. Take SLOs from SP-10 L3 and output checks from L4. For every alert, every High dependency and every known failure mode, write a runbook entry: symptom, diagnosis, fix, verification, escalation. Test the restore procedure and record the date. Validate with the support owner.

**Questions to answer:**
- How do users get help, and who handles business, access and technical issues?
- What service levels apply, and what is monitored against which thresholds?
- When an alert fires or a dependency fails, what exactly does the operator do?
- How are incidents classified, declared, communicated and reviewed?
- What is backed up, how is it restored, and when was restore last tested? What are the RTO and RPO?
- What routine and calendar tasks keep it healthy, and who does them?
- How do we check the outputs are right?
- How are changes after go-live requested, approved and communicated?

### ENG-09 Developer & Agent Guide

**Purpose:** the document developers and AI agents read first. It explains how the repository is organised, how to build, run and test, the conventions to follow, how to make a change safely, and which documents to update with which change.

**How to produce:** model it on `AGENTS.md` conventions. Give exact commands and verify them by running them. List agent rules: what an agent may change without asking, what needs a human, and the update-trigger table. Place `AGENTS.md` at the repository root, either as this document (Foundation) or as a pointer to it.

**Questions to answer:**
- Where are things in the repository?
- How do I install, run, test, lint and build, exactly?
- What conventions and patterns must my change follow?
- How do I make and ship a change safely, and what is the definition of done?
- What may an agent change on its own, and what needs a person?
- Which documents must I update with my change?

### ENG-10 Decision Log

**Purpose:** records significant technical and product decisions as ADRs, so nobody, human or agent, undoes a deliberate choice without knowing why it was made.

**How to produce:** write an ADR for every choice an agent might otherwise "fix": framework, data store, authentication approach, hosting, deliberate omissions, and any rule that looks wrong but is intended. Keep superseded ADRs and link them to their replacements.

**Questions to answer:**
- What was decided, when, and by whom?
- What problem forced the decision, and which alternatives were rejected and why?
- What follows from the decision, good and bad?
- Is it still in force, or what superseded it?
