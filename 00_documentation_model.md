# Documentation Model

## Purpose

This model explains what an application's documentation must achieve, how the documents fit together, and when each one is written and kept up to date. Read it before the [document set register](01_document_set_register.md) and the templates.

## What this framework does

The framework does three things, and keeps them separate:

1. **It tells teams what to document** about their application, and how much, through the [scoping guide](03_scoping_guide.md), the [document set register](01_document_set_register.md) and the templates.
2. **It requires the documentation to define how the application's success is judged.** Every package states success measures and **application acceptance criteria**: testable statements, written by the application team, that operators use to judge whether the *application and its output* are right.
3. **It supplies documentation review criteria** (rubrics, cross-document rules, gates and decision rules) that judge whether the *documents* are good enough.

The two kinds of criteria are never mixed:

| Term | Judges | Written by | Lives in |
|---|---|---|---|
| **Application acceptance criteria** | The application and its output: does it do the right thing? | The application team, approved by owners | The application's own SP-11 (`AC-xx`) |
| **Documentation review criteria** | The documents: are they complete, correct and usable? | This framework | `rubrics/` and `review/` |

The bare phrase "acceptance criteria" is not used anywhere in this framework.

## What the documentation must let people answer

These are the outcome requirements. Every template section, rubric criterion and gate exists to serve at least one of them. A package that passes review but leaves one of these unanswered (within its scope) has found a gap in the framework, and that gap should be reported as framework feedback.

### Business readers

| Req | The business reader can answer… | Mainly answered by |
|---|---|---|
| **B1** | What the application contributes to the business if it is used: benefits, outcomes, who gains what | BUS-01, SP-10 (L1) |
| **B2** | Why it matters: the problem, the cost of not having it, strategic fit, impact if unavailable | BUS-01, BUS-08 |
| **B3** | What capabilities it enables | BUS-02, BUS-03, BUS-06 |
| **B4** | What resources are needed to deploy and operate it: people, skills, effort, infrastructure, licences, running costs, renewals | BUS-07, ENG-05 |

### Engineering readers (engineers, operators and AI agents)

| Req | The engineering reader can answer… | Mainly answered by |
|---|---|---|
| **E1** | The technical design and architecture: components, boundaries, technology, deployment topology | ENG-03, ENG-04, ENG-10 |
| **E2** | How the whole thing works end to end: runtime behaviour, data flow, state changes | ENG-03, ENG-04, BUS-05 |
| **E3** | The requirements, functional and non-functional | ENG-01, BUS-05 |
| **E4** | The work needed to deploy, operate and maintain it in a working state | ENG-06, ENG-07, ENG-08, ENG-09, BUS-07 |
| **E5** | The user flows and journeys it must support | ENG-02, BUS-03, BUS-09 |
| **E6** | Its interaction with other applications and systems: interfaces, contracts, dependencies | ENG-05 |

### Both

| Req | The documentation provides… | Mainly answered by |
|---|---|---|
| **S1** | **What success looks like**, stated at the right level for each reader | BUS-01, SP-10 |
| **S2** | **Success measures** at four levels: business outcome, product acceptance, operational health, output correctness | SP-10, ENG-08 |
| **S3** | **Testable application acceptance criteria**, so an operator can objectively judge whether the application and its output are right | SP-11, SP-12 |

At Foundation level these are answered at a glance, inside two files; at Full level, in depth. They are always answered.

## Three layers, one spine

```text
                 ┌──────────────────────────── Shared spine ─────────────────────────────┐
                 │ SP-00 Scope Record · SP-01 Glossary · SP-10 Success Measures ·        │
                 │ SP-11 Acceptance Criteria & Verification · SP-12 Acceptance & Handover│
                 └───────────────────────────────────────────────────────────────────────┘
  Business layer (why, what, who, cost)            Engineering layer (how it is built and run)
  BUS-01 Overview & Business Case                  ENG-01 Requirements
  BUS-02 Capabilities                              ENG-02 User Journeys
  BUS-03 Business Processes                        ENG-03 Architecture & Design
  BUS-04 Roles & Access                            ENG-04 Data Model
  BUS-05 Business Rules & Status Lifecycle         ENG-05 Integrations & Dependencies
  BUS-06 Data, Reports & Notifications             ENG-06 Configuration & Environments
  BUS-07 Resource & Cost Model                     ENG-07 Deployment & Release
  BUS-08 Risk & Controls                           ENG-08 Operations & Support Runbook
  BUS-09 User & Admin Guide                        ENG-09 Developer & Agent Guide
                                                   ENG-10 Decision Log
```

- The **business layer** is written in plain language for owners, managers, support staff and auditors.
- The **engineering layer** is written for engineers, technical operators and AI agents that build and maintain the application. Technical language is expected; unfamiliar terms are defined in SP-01.
- The **spine** joins them. It holds the scope decision, the shared vocabulary, and the success chain, which runs through both layers.

## Core concepts

| Concept | Meaning | ID | Example |
|---|---|---|---|
| Application | The software product or service being documented | — | A room booking system |
| Capability | What the system can do for users or the business | `C` | Submit booking request |
| Business process | How one or more capabilities are used in real work, including steps outside the system | `W` | Review and decide a booking request |
| User journey | One person's interaction *with the system* to reach a goal | `J` | Guest submits a request and receives an acknowledgement |
| Role | A type of user or owner with permissions and responsibilities | `R` | Booking staff |
| Business rule | A condition the business requires the application to enforce | `BR` | A room cannot be confirmed for dates it is already confirmed for |
| Status and transition | The allowed states of a record and the moves between them | `ST`, `TR` | Submitted → Confirmed |
| Record | A business record the application creates or manages | `REC` | Booking request |
| Requirement | A behaviour (functional) or quality target (non-functional) the system must meet | `FR`, `NFR` | p95 page load ≤ 2 s |
| Component | A deployable or logical part of the system | `CMP` | Web front end, API, database |
| Dependency and interface | Something the application relies on, and the contract for exchanging data with it | `D`, `INT` | Email service; outbound SMTP |
| Success measure | A number that shows whether the application is succeeding, at one of four levels | `SM` | Median request-to-decision time |
| Application acceptance criterion | A testable statement of correct behaviour, in Given/When/Then form | `AC` | Given a Submitted booking… |
| Output check | A repeatable check that what the application produces is right | `OC` | Confirmed bookings in the app = bookings in the monthly report |

### Capability vs business process vs journey

| | Capability (BUS-02) | Business process (BUS-03) | User journey (ENG-02) |
|---|---|---|---|
| Answers | What can the system do? | How is the work done? | How does a person use the system to do it? |
| Includes manual work outside the system | No | Yes | No |
| Example | Check room availability | Booking staff review a request, check availability, phone the guest if unclear, decide | Staff member opens the queue, filters by date, opens a request, sees availability, selects Confirm |

## The success chain

Every level links to the one above it by ID, so an operator can go from "is it working?" to "is it delivering the benefit?" without guessing.

```text
Benefit (BUS-01)                          BEN-01 Guests get a decision the same day
 └─ Success measure (SP-10)               SM-01 Median request→decision time, baseline 3 d, target ≤ 1 d
     └─ Capability / requirement          C-03 Review booking request · FR-07
         └─ Acceptance criterion (SP-11)  AC-14 Given a complete request… Then status is Under Review within 5 min
             └─ Verification (SP-11)      T-14 automated test · evidence link · Result: Pass
                 └─ Operational check     SM-06 (L3 SLO) and OC-03 (L4 output check) in ENG-08, alert owner on breach
```

### Four levels of success measure

| Level | Question it answers | Typical measures | Read by | When |
|---|---|---|---|---|
| **L1 Business outcome** | Is the application delivering the benefit it was built for? | Cycle time, cost per transaction, error rate in the business process, adoption, satisfaction | Business owner, management | Quarterly, or at benefit review |
| **L2 Product acceptance** | Does the application do what was agreed? | Pass rate of Must acceptance criteria, defects open by severity | Business owner, project owner | At UAT and go-live |
| **L3 Operational health** | Is it up and performing now? | Availability, latency, job success rate, queue age, written as SLI with an SLO target | Operators, support | Continuously |
| **L4 Output correctness** | Is what it produces actually right? | Reconciliations, rule-invariant checks, sample audits, report-vs-source checks | Operators, data owner | Per run, daily or monthly |

L4 is what lets an operator judge whether the application's *output* is right, not only whether it is running. It applies whenever trigger T6 is Yes.

## Traceability

A complete package supports these links. The [cross-document rules](review/02_cross_document_rules.md) check them, and most are checked by the [linter](review/05_linter_spec.md).

| Source | Must trace to |
|---|---|
| Benefit | At least one success measure |
| Capability | At least one business process, or marked `Admin/support only`; its roles; its critical dependencies |
| Business process | Its capabilities (both directions), roles, statuses, and journeys (both directions) |
| Journey | Its process, roles and the transitions it causes |
| Functional requirement | At least one capability; business rules where relevant |
| Every Must requirement, every NFR, every business rule, every transition | At least one application acceptance criterion |
| Acceptance criterion | A verification method and, once run, a result with evidence |
| Role | Its permissions, access approver and access removal process |
| Status | Its meaning and its allowed transitions |
| Record | Its owner, classification, retention, and the entities that store it |
| Report and notification | Audience or recipient, purpose, owner, source or trigger |
| Dependency | Owner, criticality, impact, support path, workaround; runbook entry if High; cost line if it costs money |
| Alert | A runbook entry |
| Risk | A control and an owner |
| Known limitation | The SP-12 handover record |

## Stages

Documentation is written alongside the build, not at the end. Each stage has documents that must exist (at least Draft) and documents that must be Accepted before the stage is passed. Items the Scope Record marks — are skipped; S items are due with their parent.

| Stage | Must be at least Draft | Must be Accepted |
|---|---|---|
| **1. Initiate** (before the build is approved) | SP-00, BUS-01 (with business case), SP-10 (L1 measures), BUS-07 (initial estimate), SP-01 | SP-00, BUS-01 |
| **2. Define** (before the build starts) | BUS-02 to BUS-06, ENG-01, ENG-02, ENG-03 (context and containers), SP-11 (criteria for Must requirements) | BUS-02, BUS-03, ENG-01 |
| **3. Build** | ENG-03 (complete), ENG-04, ENG-05, ENG-06, ENG-09, ENG-10 (kept current as decisions are made) | ENG-03, ENG-04 |
| **4. Verify** (user acceptance testing) | ENG-07, ENG-08, BUS-08, BUS-09, SP-11 (results filled in) | BUS-04, BUS-05, BUS-06, ENG-05, SP-11 |
| **5. Go-live** | SP-12 | Every item in the Scope Record |
| **6. Operate** | — | Periodic re-review (below) and updates on change |

Re-score the Scope Record at each stage gate.

When documenting an existing application (reverse documentation), all stages collapse into one: draft everything in scope from the code and from people, then review and accept as for go-live.

## Update triggers

Documentation is kept true by updating it in the same change that alters the application. When something in the left column changes, the documents on the right are updated in the same pull request and re-reviewed.

| Change | Documents to update |
|---|---|
| New or changed feature | BUS-02, ENG-01, SP-11, BUS-09, release notes (ENG-07) |
| New status or transition | BUS-05, ENG-04, ENG-02, BUS-09 (Concepts), SP-11 |
| New or changed business rule | BUS-05, ENG-01, SP-11 |
| New role or permission | BUS-04, SP-01, BUS-09 |
| New record, field classification or retention change | BUS-06, ENG-04 |
| New report, export or notification | BUS-06, SP-10 or ENG-08 output checks if others rely on it |
| New integration or dependency | ENG-05, ENG-03, ENG-08, BUS-07 if cost changes, SP-00 (re-score D4) |
| Architecture or technology decision | ENG-10, ENG-03 |
| New configuration item, secret or feature flag | ENG-06 |
| Deployment or release process change | ENG-07 |
| Incident with a new failure mode | ENG-08 (runbook entry), BUS-08 |
| Success measure missed for two periods | SP-10 (review), BUS-08 |
| New user group, data type or regulatory exposure | SP-00 (re-score) |

ENG-09 repeats this table as the rule agents follow. A pull request that changes behaviour without touching the listed documents fails review.

## Review cadence

Every document records `last_reviewed` in its front-matter. A document not reviewed within its interval is **Stale**, which the linter reports as a Low finding.

| Level | Review interval |
|---|---|
| Foundation | 12 months |
| Standard | 6 months |
| Full | 3 months |

A review that finds nothing to change still updates `last_reviewed` and adds a change-log line ("Reviewed, no changes").

## Ownership

| Role | Accountable for |
|---|---|
| **Business owner** | Business accuracy, benefits, success measures (L1), the Scope Record, and business acceptance |
| **Technical owner** | Engineering-layer accuracy, the Scope Record, and technical acceptance |
| **Support owner** | Support model, runbooks and operational acceptance |
| **Document owner** | The content of one document (named in its front-matter) |
| **Producer** (person or agent) | Drafting and updating documents |
| **Reviewer** (person or agent) | Applying the documentation review criteria and writing findings |
| **Verifier** (person or agent) | Applying the decision rules and gates to reach a decision |

One person may hold several roles in a small project. The producer and the reviewer of the same document are never the same agent run.
