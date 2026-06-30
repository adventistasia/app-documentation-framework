# Consolidated Non-Technical Application Documentation and Audit Guide


---

<!-- Source: README.md -->


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


---

<!-- Source: 01_documentation_model.md -->


# Documentation Model

## Purpose

This model defines how to document a software application from an application ownership, operations, support, and governance perspective. It separates business understanding from technical implementation while preserving enough structure for governance, support, handover, and automated review.

## Core concepts

| Concept | Meaning | Example |
|---|---|---|
| Application | The software product or service being documented | LHC Booking System |
| Capability | What the system can do for users or the business | Submit booking request |
| Workflow | How one or more capabilities are used in a real process | Review and confirm booking |
| Role | A type of user or owner with responsibilities | LHC Staff, LHC Admin, ITS Support |
| Business rule | A required condition or decision rule | A booking cannot be confirmed unless a room is available |
| Status lifecycle | The allowed states and transitions of records | Draft -> Submitted -> Confirmed -> Closed |
| Data register | Business records and fields handled by the application | Booking request, guest record, room record |
| Dependency | Something the application relies on to function | Email, hosting, domain, identity, room inventory data |
| Support model | How issues, access, and operations are handled | LHC owns booking questions; ITS owns technical issues |
| Acceptance record | Evidence of delivered scope, known limitations, and owner sign-off | Handover record |

## Relationship model

```text
Application purpose
  -> Users and roles
  -> Capabilities
  -> Workflows
  -> Business rules and lifecycle
  -> Data, reports, and notifications
  -> Dependencies
  -> Support operations
  -> Risks and controls
  -> Acceptance and handover
```

## Capability vs workflow

A capability is what the system can do. A workflow is how the capability is used in a real business process.

| Capability | Workflow usage |
|---|---|
| Submit booking request | Used when a guest starts a booking request |
| Check room availability | Used when LHC staff reviews or modifies a booking |
| Generate booking reports | Used when management reviews occupancy and activity |

## Traceability expectations

A complete package should support these links:

| Source | Must trace to |
|---|---|
| Capability | At least one workflow, or marked as administrative/support only |
| Workflow | One or more capabilities, roles, statuses, and business rules |
| Role | Permissions, workflow participation, access owner |
| Business rule | Affected workflow, capability, owner, exception path |
| Status | Definition, allowed transitions, responsible role |
| Data item | Owner, required fields, sensitivity, related reports or workflows |
| Report | Audience, purpose, data source, frequency |
| Notification | Trigger, recipient, message purpose, expected action |
| Dependency | Owner, impact, support path, affected capabilities/workflows |
| Risk | Control, owner, affected capability/workflow/dependency |
| Known limitation | Handover record and acceptance decision |

## Plain-language quality standard

The documentation should be understandable by a manager, process owner, support staff member, application owner, or auditor who does not need to know the code, database, deployment pipeline, or API internals.

Avoid making the document a technical feature inventory. Prefer business language:

| Prefer | Avoid |
|---|---|
| Submit booking request | Submit button |
| Review booking request | Admin page |
| Generate monthly report | Excel export button |
| Manage access and roles | User table |
| Send notifications | Email API |


---

<!-- Source: 02_document_set_register.md -->


# Document Set Register

## Purpose

This register defines the recommended documentation set, what each document is for, how each should be produced, and what questions it must answer.

## Recommended document set

| ID | Document | Purpose | Primary audience | Required for acceptance |
|---|---|---|---|---|
| DOC-01 | Application Overview | Explains what the application is, why it exists, who owns it, and what business process it supports. | Management, business owner, support team | Yes |
| DOC-02 | Capabilities Register | Lists what the system can do, the outcome of each capability, who uses it, and which workflows use it. | Business owner, users, support team | Yes |
| DOC-03 | Workflow Register | Documents the major end-to-end processes supported by the system. | Business owner, operations staff, support team | Yes |
| DOC-04 | Roles and Access Matrix | Defines user roles, permissions, responsibilities, and access request/removal process. | Business owner, IT support, auditors | Yes |
| DOC-05 | Business Rules and Status Lifecycle | Documents rules for approvals, availability, pricing, status changes, editing, cancellations, and exceptions. | Business owner, operations staff | Yes |
| DOC-06 | Data, Reports, and Notifications Register | Documents main records, fields, sensitive data, reports, exports, and notifications. | Business owner, IT, support, compliance | Yes |
| DOC-07 | Application Dependencies Register | Documents systems, services, data, people, accounts, infrastructure, vendors, and processes the application depends on. | Business owner, support team, IT | Yes |
| DOC-08 | Support and Operations Guide | Explains how the application is supported, who handles what, escalation paths, known issues, and routine operations. | Operations staff, support team, IT | Yes |
| DOC-09 | Risk and Controls Register | Documents operational, access, data, reporting, dependency, and support risks with controls. | Management, business owner, IT | Recommended |
| DOC-10 | User and Admin Guide | Shows users and admins how to perform common tasks. | End users, admins, support staff | Recommended for launch |
| DOC-11 | Acceptance and Handover Record | Confirms what was delivered, accepted, deferred, and handed over for operations. | Business owner, IT, project owner | Yes |

## Production guidance by document

### DOC-01 - Application Overview

Recommended way to produce:

- Interview the business owner and support owner.
- Review existing project briefs, handover notes, URLs, and system descriptions.
- Keep it short enough to be read first by a manager.
- Reference detailed registers rather than duplicating them.

Questions to answer:

- What is the application called?
- What does it do?
- Why does it exist?
- What business process does it support?
- Who owns it?
- Who supports it?
- Who uses it?
- Where is it accessed?
- What is in scope and out of scope?
- What is the impact if it is unavailable?

### DOC-02 - Capabilities Register

Recommended way to produce:

- Ask what the application can do for users and the business.
- Write capabilities in business language, not UI language.
- Include outcomes, users, owner, criticality, and workflow mapping.
- Validate the list against actual workflows and support needs.

Questions to answer:

- What can the system do?
- What outcome does each capability produce?
- Who uses each capability?
- Which workflows use each capability?
- Which capabilities are critical for launch?
- Which are administrative, support, reporting, or access capabilities?

### DOC-03 - Workflow Register

Recommended way to produce:

- Start with the real work users perform.
- For each workflow, define trigger, roles, steps, decisions, outcome, exceptions, and capabilities used.
- Include manual steps outside the system.
- Validate with process owners and actual users.

Questions to answer:

- What starts the workflow?
- Who participates?
- What steps happen in sequence?
- What decisions are made?
- What statuses are used?
- What capabilities are used?
- What is the successful outcome?
- What are the exception paths?
- What still happens manually?

### DOC-04 - Roles and Access Matrix

Recommended way to produce:

- Identify all user types from workflows, support operations, and admin functions.
- Define what each role can view, create, update, approve, delete, administer, and report.
- Identify the access approver and removal process.
- Flag sensitive permissions and risky role combinations.

Questions to answer:

- What roles exist?
- What can each role do?
- Who approves access?
- How is access requested?
- How is access removed?
- Which permissions are sensitive?
- Do workflow roles match documented roles?

### DOC-05 - Business Rules and Status Lifecycle

Recommended way to produce:

- Extract rules from workflows, user decisions, policies, exceptions, and support issues.
- Write rules in testable condition/action language.
- Define every status and allowed transition.
- Assign rule owners and exception authorities.

Questions to answer:

- What rules must the application enforce?
- Who owns each rule?
- What exceptions are allowed?
- What statuses exist?
- What does each status mean?
- Who can move a record from one status to another?
- What validations block progress?

### DOC-06 - Data, Reports, and Notifications Register

Recommended way to produce:

- Identify the main business records handled by the application.
- List required fields, sensitive data, data owner, and retention expectations.
- List reports, exports, dashboards, notifications, triggers, audiences, and expected actions.

Questions to answer:

- What records does the application create or manage?
- What fields are required?
- What data is sensitive or confidential?
- Who owns the data?
- What reports or exports are produced?
- Who receives each report?
- What notifications are sent, when, to whom, and why?

### DOC-07 - Application Dependencies Register

Recommended way to produce:

- List business, operational, technical, vendor, data, infrastructure, account, and people dependencies.
- For each dependency, define owner, purpose, impact, criticality, support path, affected workflows, and workaround.
- Validate dependencies against support procedures and launch readiness.

Questions to answer:

- What must be available for the application to function?
- Who owns each dependency?
- What happens if it fails?
- Who supports it?
- Which workflows or capabilities are affected?
- Is there a workaround?
- Which dependencies require renewal, funding, account ownership, or periodic review?

### DOC-08 - Support and Operations Guide

Recommended way to produce:

- Separate business support from technical/application support.
- Define intake, triage, escalation, routine operations, dependency checks, and communications.
- Include known limitations and common issues.
- Validate with support owners before handover.

Questions to answer:

- How do users ask for help?
- Who handles business questions?
- Who handles access issues?
- Who handles system issues?
- What should support check first?
- When does LHC handle the issue?
- When does ITS handle the issue?
- What routine tasks must be performed?
- What limitations are known?

### DOC-09 - Risk and Controls Register

Recommended way to produce:

- Identify risks from workflows, access, data, reports, dependencies, support, and known limitations.
- For each risk, define owner, severity, control, residual risk, and review cadence.
- Cross-reference affected capabilities, workflows, dependencies, or rules.

Questions to answer:

- What can go wrong operationally?
- What access, data, reporting, dependency, or support risks exist?
- What controls reduce those risks?
- Who owns the risk or control?
- What risks remain after controls?
- What must be reviewed periodically?

### DOC-10 - User and Admin Guide

Recommended way to produce:

- Convert accepted workflows into plain task instructions.
- Separate user tasks from admin tasks.
- Include common errors, examples, screenshots where available, and support contact.
- Ensure instructions do not exceed role permissions.

Questions to answer:

- How does a user perform the main tasks?
- How does an admin perform setup or maintenance tasks?
- What should users do when something goes wrong?
- What common mistakes should be avoided?
- Where should users request help?

### DOC-11 - Acceptance and Handover Record

Recommended way to produce:

- Create after the main documentation set is drafted and reviewed.
- List delivered scope, deferred scope, accepted workflows, known limitations, risks, support ownership, and sign-offs.
- Use it as the formal readiness and accountability record.

Questions to answer:

- What was delivered?
- What was deferred?
- What workflows are accepted?
- What limitations or risks are accepted?
- Who owns operations after handover?
- Who supports the application?
- Who signed off?


---

<!-- Source: rubrics/00_universal_rubric.md -->


# Universal Documentation Rubric

Apply this rubric to every artifact in the documentation set.

## Result scale

| Result | Meaning |
|---|---|
| Pass | Criterion is satisfied with clear evidence. |
| Partial | Criterion is partly satisfied but has gaps, ambiguity, or weak evidence. |
| Fail | Criterion is missing, contradicted, or unusable. |
| Not Applicable | Criterion does not apply and the reason is documented. |

## Universal criteria

| ID | Criterion | Pass condition | Fail condition |
|---|---|---|---|
| U-01 | Identity | Document has title, application name, version/date, status, owner, and intended audience. | Missing identity fields or unclear artifact scope. |
| U-02 | Purpose | Document clearly states why it exists and what decision or operation it supports. | Purpose is missing or generic. |
| U-03 | Scope | In-scope and out-of-scope content are clear where relevant. | Reader cannot tell what is covered. |
| U-04 | Required structure | Required sections and tables are present. | Required sections are missing. |
| U-05 | Specificity | Uses actual names, roles, workflows, statuses, reports, dependencies, owners, or placeholders explicitly marked TBD. | Uses vague language without owners or specific references. |
| U-06 | Plain language | Understandable by business, operational, support, and governance readers; unexplained technical terms are avoided. | Reads like technical implementation notes only. |
| U-07 | Traceability | References related artifacts, IDs, roles, workflows, capabilities, dependencies, or risks as needed. | Cannot be connected to the rest of the package. |
| U-08 | Operational usability | A reader can use the document to operate, support, govern, or accept the application. | Document is informational only and not actionable. |
| U-09 | Risk and limitation visibility | Assumptions, limitations, gaps, exceptions, and risks are visible. | Gaps are hidden or falsely implied as complete. |
| U-10 | Ownership and accountability | Owners, approvers, or responsible roles are identified for the artifact content and major decisions. | No clear accountable owner. |
| U-11 | Consistency | Terms, role names, statuses, IDs, and scope are consistent with related documents. | Contradicts other artifacts or uses inconsistent names. |
| U-12 | Acceptance readiness | Document can be reviewed and signed off by the correct owner. | No acceptance state, owner, or review path. |

## Minimum scoring guidance

For artifact acceptance:

- No Fail on U-01, U-02, U-04, U-07, U-08, U-10, or U-12.
- Partial results must have required fixes or conditional acceptance items.
- A document with more than three Partial results should normally be Revise and Resubmit.


---

<!-- Source: rubrics/01_artifact_specific_rubrics.md -->


# Artifact-Specific Rubrics

Use these criteria in addition to the Universal Documentation Rubric.

## DOC-01 - Application Overview

| ID | Criterion | Pass condition |
|---|---|---|
| AO-01 | Purpose and business value | Explains what the application does and why it exists. |
| AO-02 | Ownership | Names business owner, support owner, and technical/application support owner. |
| AO-03 | Users | Identifies main user groups and stakeholders. |
| AO-04 | Scope | Defines in-scope and out-of-scope functions. |
| AO-05 | Access point | Identifies URL, entry point, or access method. |
| AO-06 | Operational importance | Explains impact if unavailable. |
| AO-07 | Related artifacts | References capabilities, workflows, dependencies, support guide, and handover record. |

## DOC-02 - Capabilities Register

| ID | Criterion | Pass condition |
|---|---|---|
| CAP-01 | Unique IDs | Every capability has a unique ID. |
| CAP-02 | Business language | Capability names describe business/user capability, not low-level UI features. |
| CAP-03 | Description | Every capability explains what the system enables. |
| CAP-04 | Outcome | Every capability has a business or operational outcome. |
| CAP-05 | Primary users | Every capability identifies users or roles. |
| CAP-06 | Owner | Critical capabilities identify an owner or reference the ownership matrix. |
| CAP-07 | Workflow mapping | Every capability maps to at least one workflow or is marked administrative/support only. |
| CAP-08 | Coverage | User, admin, access, support, reporting, notification, and audit capabilities are covered where applicable. |
| CAP-09 | Non-duplication | Capabilities are not repeated under different names. |
| CAP-10 | Dependency visibility | Critical capabilities identify related dependencies where relevant. |

## DOC-03 - Workflow Register

| ID | Criterion | Pass condition |
|---|---|---|
| WF-01 | Unique IDs | Every workflow has a unique ID. |
| WF-02 | Trigger | Every workflow states what starts it. |
| WF-03 | Outcome | Every workflow states what successful completion produces. |
| WF-04 | Roles | Every workflow identifies participating roles. |
| WF-05 | Capabilities used | Every workflow maps to documented capabilities. |
| WF-06 | Steps | Main steps are sequenced clearly. |
| WF-07 | Decision points | Approve, reject, return, cancel, escalate, or exception paths are documented where relevant. |
| WF-08 | Statuses | Statuses used in workflows are documented and consistent with lifecycle guide. |
| WF-09 | Manual steps | Work outside the system is disclosed. |
| WF-10 | Exceptions | Common failure or alternate paths are included. |

## DOC-04 - Roles and Access Matrix

| ID | Criterion | Pass condition |
|---|---|---|
| RA-01 | Role definitions | Every role is defined in plain language. |
| RA-02 | Permissions | Each role states view, create, update, approve, return, cancel/delete, administer, and report permissions where applicable. |
| RA-03 | Access approval | Role assignment approver is identified. |
| RA-04 | Access request | Access request process is documented. |
| RA-05 | Access removal | Access removal process is documented. |
| RA-06 | Sensitive permissions | Admin or risky permissions are identified. |
| RA-07 | Workflow alignment | Roles used in workflows appear in the matrix. |
| RA-08 | Support alignment | Support roles and responsibilities align with support guide. |

## DOC-05 - Business Rules and Status Lifecycle

| ID | Criterion | Pass condition |
|---|---|---|
| BR-01 | Testable rules | Rules are written clearly enough to verify. |
| BR-02 | Rule owner | Each major rule has an owner or decision authority. |
| BR-03 | Exceptions | Exception authority and override handling are documented. |
| BR-04 | Status definitions | Every status is defined. |
| BR-05 | Status transitions | Allowed transitions are documented. |
| BR-06 | Actor permissions | Who can perform status changes is clear. |
| BR-07 | Validation rules | Required data, date, availability, pricing, or submission rules are documented where relevant. |
| BR-08 | Workflow linkage | Rules and statuses reference affected workflows or capabilities. |

## DOC-06 - Data, Reports, and Notifications Register

| ID | Criterion | Pass condition |
|---|---|---|
| DRN-01 | Main records | Major business records are identified. |
| DRN-02 | Required fields | Required business fields are listed for core records. |
| DRN-03 | Sensitive data | Personal or confidential data is identified. |
| DRN-04 | Data ownership | Each major data group has an owner. |
| DRN-05 | Reports | Standard reports, dashboards, or exports are documented. |
| DRN-06 | Report purpose | Every report has audience and purpose. |
| DRN-07 | Notifications | Every notification has trigger, recipient, purpose, and expected action. |
| DRN-08 | Retention | Retention or archive expectations are stated, even if provisional. |

## DOC-07 - Application Dependencies Register

| ID | Criterion | Pass condition |
|---|---|---|
| DEP-01 | Dependency coverage | Critical systems, services, data, people, vendors, hosting, email, identity, domain, network, and support dependencies are listed where applicable. |
| DEP-02 | Purpose | Each dependency explains why it is needed. |
| DEP-03 | Owner | Each dependency has an owner. |
| DEP-04 | Impact | Each dependency states what happens if unavailable. |
| DEP-05 | Criticality | Each dependency has a criticality rating. |
| DEP-06 | Support path | Each dependency has a support or escalation path. |
| DEP-07 | Traceability | Critical dependencies map to affected workflows or capabilities. |
| DEP-08 | Workaround | High-criticality dependencies identify fallback/workaround or explicitly state none. |

## DOC-08 - Support and Operations Guide

| ID | Criterion | Pass condition |
|---|---|---|
| SO-01 | Support ownership | Business, application, and technical support ownership are separated. |
| SO-02 | Intake process | User support intake process is clear. |
| SO-03 | Triage | Issue categories and initial checks are documented. |
| SO-04 | Escalation | Escalation path is clear. |
| SO-05 | Routine operations | Recurring admin/support tasks are listed. |
| SO-06 | Known issues | Known limitations or issues are listed, or explicitly none known. |
| SO-07 | Dependency checks | Support guide references dependency checks. |
| SO-08 | Access support | Account creation, role changes, and removal support are explained. |
| SO-09 | Communication | Communication expectations during issues are defined. |

## DOC-09 - Risk and Controls Register

| ID | Criterion | Pass condition |
|---|---|---|
| RC-01 | Risk coverage | Operational, access, data, reporting, dependency, support, and compliance risks are considered. |
| RC-02 | Control mapping | Each risk has at least one control or mitigation. |
| RC-03 | Owner | Each risk/control has an accountable owner. |
| RC-04 | Severity | Likelihood, impact, or severity is rated. |
| RC-05 | Residual risk | Remaining risk is stated where relevant. |
| RC-06 | Review cadence | Risk review cadence is documented. |
| RC-07 | Traceability | Risks map to capabilities, workflows, dependencies, rules, or limitations where applicable. |

## DOC-10 - User and Admin Guide

| ID | Criterion | Pass condition |
|---|---|---|
| UG-01 | Audience separation | User tasks and admin tasks are separated or separate guides exist. |
| UG-02 | Workflow coverage | Main workflows are covered or exclusions are explained. |
| UG-03 | Step clarity | Steps are plain-language and sequenced. |
| UG-04 | Expected result | Each task states expected result. |
| UG-05 | Error handling | Common mistakes and what to do are included. |
| UG-06 | Support path | Guide tells users where to get help. |
| UG-07 | Role alignment | Tasks match permissions in the Roles and Access Matrix. |

## DOC-11 - Acceptance and Handover Record

| ID | Criterion | Pass condition |
|---|---|---|
| AH-01 | Delivered scope | Delivered scope is listed. |
| AH-02 | Deferred scope | Deferred items/open issues are listed or explicitly none. |
| AH-03 | Accepted workflows | Workflows accepted by business owner are identified. |
| AH-04 | Accepted access model | Roles and access model acceptance is recorded. |
| AH-05 | Accepted support model | Support ownership and escalation acceptance are recorded. |
| AH-06 | Known limitations | Known limitations and accepted risks are listed. |
| AH-07 | Operational readiness | Dependencies, reports, notifications, and support process readiness are confirmed. |
| AH-08 | Sign-off | Business owner, support owner, and technical/application owner decisions are recorded. |


---

<!-- Source: rubrics/02_acceptance_thresholds.md -->


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


---

<!-- Source: review/01_audit_result_template.md -->


# Documentation Artifact Review Result

## 1. Audit Scope

Application: [Application name]  
Artifact reviewed: [Document name]  
Artifact version/date: [Version or date]  
Review pass: Pass 1 / Pass 2 / Final Acceptance  
Reviewer: [Automated review agent / human reviewer]  
Related artifacts checked:

- [Artifact]
- [Artifact]

## 2. Review Decision

Status: Pass / Partial / Fail  
Acceptance recommendation: Accept / Accept with Conditions / Revise and Resubmit / Reject

Summary:

[Short explanation of the decision.]

## 3. Universal Rubric Results

| ID | Criterion | Result | Evidence | Notes |
|---|---|---|---|---|
| U-01 | Identity | Pass / Partial / Fail / N/A |  |  |
| U-02 | Purpose | Pass / Partial / Fail / N/A |  |  |
| U-03 | Scope | Pass / Partial / Fail / N/A |  |  |
| U-04 | Required structure | Pass / Partial / Fail / N/A |  |  |
| U-05 | Specificity | Pass / Partial / Fail / N/A |  |  |
| U-06 | Plain language | Pass / Partial / Fail / N/A |  |  |
| U-07 | Traceability | Pass / Partial / Fail / N/A |  |  |
| U-08 | Operational usability | Pass / Partial / Fail / N/A |  |  |
| U-09 | Risk and limitation visibility | Pass / Partial / Fail / N/A |  |  |
| U-10 | Ownership and accountability | Pass / Partial / Fail / N/A |  |  |
| U-11 | Consistency | Pass / Partial / Fail / N/A |  |  |
| U-12 | Acceptance readiness | Pass / Partial / Fail / N/A |  |  |

## 4. Artifact-Specific Criteria

| ID | Criterion | Result | Evidence | Notes |
|---|---|---|---|---|
| [Criterion ID] | [Criterion] | Pass / Partial / Fail / N/A | [Evidence] | [Comment] |

## 5. Coherence Checks

| Check | Result | Notes |
|---|---|---|
| Related document references are valid | Pass / Partial / Fail |  |
| Role names are consistent | Pass / Partial / Fail |  |
| Workflow IDs are consistent | Pass / Partial / Fail |  |
| Capability IDs are consistent | Pass / Partial / Fail |  |
| Status names are consistent | Pass / Partial / Fail |  |
| Dependency references are consistent | Pass / Partial / Fail |  |
| Known limitations are carried to handover | Pass / Partial / Fail |  |

## 6. Findings

### Bugs

Items that make the document incorrect, inconsistent, or unusable.

| ID | Finding | Severity | Evidence | Required action |
|---|---|---|---|---|
| BUG-01 |  | High / Medium / Low |  |  |

### Risks

Items that may cause operational, governance, support, or acceptance problems.

| ID | Finding | Severity | Evidence | Required action or mitigation |
|---|---|---|---|---|
| RISK-01 |  | High / Medium / Low |  |  |

### Ideas

Non-blocking improvements.

| ID | Finding | Value | Evidence | Suggested action |
|---|---|---|---|---|
| IDEA-01 |  | High / Medium / Low |  |  |

## 7. Required Fixes Before Acceptance

- [Required fix]

## 8. Conditional Acceptance Items

- [Condition]

## 9. Final Recommendation

Recommendation: Accept / Accept with Conditions / Revise and Resubmit / Reject

Reason:

[Brief explanation.]

Next action:

[What should happen next.]


---

<!-- Source: review/02_verifier_control_rules.md -->


# Verifier and Control Agent Rules

## Purpose

This document defines deterministic pass/fail checks that automated verifier or control agents can apply after a review agent produces an audit result.

The review agent evaluates quality. The verifier agent determines whether the artifact or package passes the control gate.

## Inputs expected by verifier

For each artifact:

- Artifact content
- Artifact type or document ID
- Audit result
- Universal rubric results
- Artifact-specific rubric results
- Bug/Risk/Idea findings
- Required fixes
- Conditional acceptance items
- Related artifacts needed for coherence checks

## Artifact pass/fail control rules

### Automatic fail conditions

Fail the artifact if any of these are true:

1. Artifact is missing.
2. Artifact type does not match expected document.
3. Application identity is missing.
4. Owner is missing.
5. Purpose is missing.
6. Required structure is substantially missing.
7. A critical universal criterion is marked Fail.
8. A critical artifact-specific criterion is marked Fail.
9. Any high-severity Bug remains open.
10. Any high-severity Risk has no mitigation, acceptance, or owner.
11. Artifact contradicts a previously accepted artifact.
12. Artifact claims accepted/complete status while required acceptance evidence is missing.

### Conditional pass conditions

Allow Accept with Conditions only if all are true:

1. No automatic fail condition exists.
2. Remaining Bugs are low or medium severity.
3. Remaining Risks have owners and mitigation or explicit acceptance.
4. Conditional items are listed.
5. Conditional items have owners or are assigned to the handover/open items list.
6. The artifact remains operationally usable despite the conditions.

### Full pass conditions

Accept the artifact only if all are true:

1. All required universal criteria pass.
2. All required artifact-specific criteria pass.
3. No open high or medium Bugs.
4. No unmitigated high or medium Risks.
5. Cross-document references are valid.
6. No required fixes remain.
7. Acceptance owner is named.

## Cross-document verification rules

| Rule ID | Verification rule | Fail condition |
|---|---|---|
| X-01 | Every capability maps to at least one workflow or is marked administrative/support only. | Capability exists but has no workflow mapping or classification. |
| X-02 | Every workflow maps to at least one capability. | Workflow cannot be traced to system capability. |
| X-03 | Every workflow role exists in Roles and Access Matrix. | Undefined role appears in workflow. |
| X-04 | Every status used in workflows exists in Status Lifecycle. | Undefined status appears. |
| X-05 | Every status transition used in workflows is allowed in Status Lifecycle. | Workflow uses unauthorized transition. |
| X-06 | Every major business rule references an owner. | Rule has no owner or authority. |
| X-07 | Every report has audience, purpose, owner, and data source. | Report is vague or unowned. |
| X-08 | Every notification has trigger, recipient, purpose, and expected action. | Notification is incomplete. |
| X-09 | Every critical dependency has owner, impact, criticality, support path, and affected workflow/capability. | Critical dependency is incomplete. |
| X-10 | Every support category has owner and escalation path. | Support issue cannot be routed. |
| X-11 | Every high risk has control, owner, and mitigation or formal acceptance. | High risk is unmanaged. |
| X-12 | Every known limitation appears in Acceptance and Handover Record. | Limitation is hidden from handover. |
| X-13 | Role names are consistent across capabilities, workflows, access matrix, support guide, and user guide. | Same role appears under inconsistent names without mapping. |
| X-14 | Application name, owner, URL/access point, and status are consistent across all artifacts. | Identity inconsistency exists. |
| X-15 | Support Guide references Dependencies Register for dependency checks. | Support cannot troubleshoot dependency failure. |

## Package-level pass/fail rules

### Package automatic fail

Fail the package if any of these are true:

1. Required artifact is missing.
2. DOC-01, DOC-02, DOC-03, DOC-04, DOC-05, DOC-07, DOC-08, or DOC-11 is Rejected or Revise and Resubmit.
3. Capabilities and workflows are not traceable.
4. Roles and access are not defined.
5. Support model is missing or unowned.
6. Critical dependencies are missing or unowned.
7. Known limitations are not disclosed in handover.
8. Business owner or support owner acceptance is missing from handover.

### Package conditional pass

Accept with Conditions only if:

1. All required artifacts exist.
2. Core operational artifacts are at least Accept with Conditions.
3. Open conditions are documented in the Handover Record.
4. No high-severity unresolved Bugs remain.
5. No high-severity unmanaged Risks remain.
6. Business owner and support owner accept the conditions.

### Package full pass

Accept the package only if:

1. All required artifacts are Accept.
2. All cross-document verification rules pass.
3. No required fixes remain.
4. Handover record contains final sign-off.
5. Support ownership, dependencies, limitations, and accepted scope are clear.


---

<!-- Source: review/03_package_acceptance_gates.md -->


# Package Acceptance Gates

## Gate 1 - Completeness

The package passes Gate 1 when:

- All required artifacts are present.
- Missing optional artifacts are identified as not applicable or deferred.
- Every artifact has metadata: title, application name, version/date, owner, status.

Fail if:

- A required artifact is missing.
- The package does not identify the application clearly.
- Document versions or ownership are absent.

## Gate 2 - Business understanding

The package passes Gate 2 when:

- Application purpose and business value are clear.
- Users and stakeholders are identified.
- In-scope and out-of-scope functions are clear.
- Operational impact is documented.

Fail if:

- The reader cannot explain what the application does or why it exists.
- Ownership is missing.
- Impact of unavailability is not documented.

## Gate 3 - Capability and workflow traceability

The package passes Gate 3 when:

- Capabilities describe what the system can do.
- Each capability has an outcome.
- Workflows describe how the system is used.
- Capabilities and workflows map to each other.
- Roles and statuses used in workflows are defined.

Fail if:

- Capabilities are just UI features.
- Workflows are missing triggers, outcomes, or roles.
- Capabilities and workflows do not trace.

## Gate 4 - Governance and control

The package passes Gate 4 when:

- Business rules are documented and owned.
- Status lifecycle is defined.
- Access roles and sensitive permissions are documented.
- Data, reports, and notifications have owners and purposes.
- Risks and controls are documented for major issues.

Fail if:

- Rules are vague or unowned.
- Access is unclear.
- Sensitive data is not identified.
- Reports or notifications lack purpose or owner.

## Gate 5 - Support readiness

The package passes Gate 5 when:

- Support ownership is clear.
- Issue intake, triage, escalation, and routine operations are documented.
- Critical dependencies have owners, support paths, and impact statements.
- Known limitations and workarounds are documented.

Fail if:

- Users cannot know where to get help.
- Support team cannot triage issues.
- Dependency failures have no support path.

## Gate 6 - Handover readiness

The package passes Gate 6 when:

- Delivered and deferred scope are recorded.
- Accepted workflows are listed.
- Roles/access model and support model are accepted.
- Known limitations and accepted risks are disclosed.
- Business owner, support owner, and technical/application owner acceptance are recorded.

Fail if:

- Acceptance record is missing.
- Known limitations are hidden.
- Handover does not identify owners.


---

<!-- Source: review/04_review_process.md -->


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


---

<!-- Source: examples/lhc_booking_system_example.md -->


# LHC Booking System Example

This example shows how capabilities and workflows can be documented for the LHC Booking System.

## Capabilities Register Example

| ID | Capability | Description | Outcome | Primary users | Used in workflows |
|---|---|---|---|---|---|
| C01 | Submit booking request | Allows a guest or staff member to submit a room booking request with guest details, stay dates, room needs, and contact information. | A booking request is created and enters the official review process. | Guest, LHC Staff | W01, W02 |
| C02 | Check room availability | Allows staff to see whether rooms are available for requested dates and avoid double-booking. | Staff can determine whether the requested stay can be accommodated. | LHC Staff, LHC Admin | W02, W03, W04 |
| C03 | Review booking request | Allows LHC staff to review completeness, dates, guest details, special requirements, and operational feasibility. | Staff can decide whether the request is ready for confirmation, needs correction, or cannot be accepted. | LHC Staff, LHC Admin | W02, W03 |
| C04 | Confirm booking | Allows authorized staff to approve and confirm a booking. | The guest receives a confirmed booking. | LHC Staff, LHC Admin | W02, W03 |
| C05 | Return or reject request | Allows staff to return incomplete requests or reject requests that cannot be accommodated. | Invalid, incomplete, or unavailable requests are removed from the active confirmation path. | LHC Staff, LHC Admin | W02, W03 |
| C06 | Modify booking | Allows authorized staff to change dates, room assignments, guest details, or booking notes. | Booking records remain accurate when guest or operational needs change. | LHC Staff, LHC Admin | W04 |
| C07 | Cancel booking | Allows authorized users to cancel a booking and release the room allocation. | Canceled bookings no longer occupy room availability. | LHC Staff, LHC Admin | W04 |
| C08 | Manage room records | Allows administrators to add, edit, activate, deactivate, or update room information. | Room inventory stays accurate and usable for booking operations. | LHC Admin | W05 |
| C09 | Manage pricing/rates | Allows authorized users to update room rates or pricing references. | Booking charges and rate references remain current. | LHC Admin | W05, W06 |
| C10 | Assign rooms | Allows staff to assign a specific room to a confirmed booking. | Confirmed guests are linked to actual room assignments. | LHC Staff, LHC Admin | W03, W04 |
| C11 | Track booking status | Allows users to track whether a booking is pending, confirmed, modified, canceled, checked in, completed, or closed. | Staff can monitor where each booking stands in the operational process. | LHC Staff, LHC Admin, ITS Support | W01, W02, W03, W04, W06 |
| C12 | Send notifications | Sends confirmation, status update, cancellation, or action-required messages to guests or staff. | Guests and staff are informed when action is needed or booking status changes. | System, Guest, LHC Staff | W01, W02, W03, W04 |
| C13 | Manage user access and roles | Allows authorized administrators to create accounts, assign roles, change access, or remove access. | Only authorized users can perform booking, administrative, or support actions. | LHC Admin, ITS Support | W07 |
| C14 | Generate booking reports | Produces reports for occupancy, bookings, cancellations, guest stays, or management review. | LHC management receives visibility into booking activity and room usage. | LHC Admin, LHC Management | W06 |
| C15 | Support issue handling | Allows issues to be reported, reviewed, escalated, and resolved by LHC or ITS depending on ownership. | User issues and system problems have a clear resolution path. | LHC Staff, ITS Support | W08 |
| C16 | Maintain audit/history trail | Records important actions such as booking confirmation, modification, cancellation, access changes, and pricing updates. | Important changes can be reviewed for accountability, support, and operational traceability. | LHC Admin, ITS Support | W03, W04, W05, W07, W08 |

## Workflow Register Example

| ID | Workflow | Trigger | Main outcome | Main roles | Capabilities used |
|---|---|---|---|---|---|
| W01 | Guest submits booking request | Guest needs accommodation at LHC | Booking request is created and ready for review | Guest, LHC Staff | C01, C11, C12 |
| W02 | LHC reviews booking request | New booking request is submitted | Request is confirmed, returned, or rejected | LHC Staff, LHC Admin | C02, C03, C04, C05, C11, C12 |
| W03 | LHC confirms and assigns room | Request is accepted for accommodation | Guest has a confirmed booking and assigned room | LHC Staff, LHC Admin | C02, C04, C10, C11, C12, C16 |
| W04 | Booking is modified or canceled | Guest or LHC needs to change the booking | Booking is updated, canceled, or room allocation is released | Guest, LHC Staff, LHC Admin | C02, C06, C07, C10, C11, C12, C16 |
| W05 | LHC manages rooms and pricing | Room inventory or pricing changes | Room and rate information stays current | LHC Admin | C08, C09, C16 |
| W06 | LHC reviews booking activity | Management or operations needs visibility | Booking, occupancy, and activity reports are produced | LHC Admin, LHC Management | C09, C11, C14 |
| W07 | Access is created or changed | New staff member, role change, or access removal request | Correct users have correct permissions | LHC Admin, ITS Support | C13, C16 |
| W08 | Support issue is handled | User reports an issue or system problem occurs | Issue is resolved by LHC or escalated to ITS | LHC Staff, LHC Admin, ITS Support | C11, C15, C16 |

## Example Application Dependencies Register

| ID | Dependency | Type | Purpose | Owner | Impact if unavailable | Support path |
|---|---|---|---|---|---|---|
| D01 | Public website / landing page | Website | Directs guests to booking information and booking entry point. | LHC / ITS | Guests may not find the booking service. | ITS support |
| D02 | Booking application hosting | Application platform | Runs the guest booking system. | ITS | Booking system becomes unavailable. | ITS / hosting provider |
| D03 | Application domain | Domain/DNS | Provides public access to the booking system URL. | ITS | Users cannot access the application by URL. | ITS / DNS administrator |
| D04 | Email service | Communication | Sends booking confirmations, status updates, and staff notifications. | ITS / M365 Admin | Guests and staff may not receive booking updates. | ITS support |
| D05 | Staff user accounts | Identity/access | Allows LHC staff and admins to log in. | LHC Admin / ITS | Staff cannot process bookings. | LHC Admin, then ITS |
| D06 | Room inventory data | Business data | Provides available rooms, room types, and capacity. | LHC Admin | Staff may assign incorrect or unavailable rooms. | LHC Admin |
| D07 | Pricing/rate data | Business data | Provides room rates or pricing references. | LHC Admin / Management | Incorrect pricing may be used. | LHC Admin / Management |
| D08 | Internet connectivity | Infrastructure | Allows guests and staff to access the system. | User site / ITS | Users may not be able to access the system. | Local IT / ISP |
| D09 | LHC booking staff | Operational dependency | Reviews, confirms, modifies, and cancels bookings. | LHC | Requests may remain unprocessed. | LHC management |
| D10 | ITS support process | Support dependency | Handles technical issues, access issues, and escalations. | ITS | Issues may not be resolved consistently. | ITS helpdesk |

## Example Audit Finding

```markdown
### Bugs

| ID | Finding | Severity | Evidence | Required action |
|---|---|---|---|---|
| BUG-01 | Role names are not normalized across capabilities and workflows. | Medium | Capabilities use Support while workflows use ITS Support. | Use the same role names as the Roles and Access Matrix. |

### Risks

| ID | Finding | Severity | Evidence | Required action |
|---|---|---|---|---|
| RISK-01 | Email dependency affects notifications but is not mapped to affected capabilities. | Medium | D04 exists but C12 does not reference dependency D04. | Link D04 to C12 and related workflows W01-W04. |

### Ideas

| ID | Finding | Value | Evidence | Suggested action |
|---|---|---|---|---|
| IDEA-01 | Add criticality to capabilities. | Medium | Capabilities do not yet show launch-critical functions. | Add Criticality column to Capabilities Register. |
```
