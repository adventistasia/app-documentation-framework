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
