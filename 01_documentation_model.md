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
