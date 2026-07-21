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
|WF-11 | Workflow boundary and cohesion | Each workflow covers one primary trigger-to-outcome process with clear boundaries and ownership. Workflows with multiple unrelated triggers, independently valuable outcomes, different owners, or separate status lifecycles are split into separate entries |
| WF-12 | Appropriate level of detail | Workflow steps describe business-level actions consistently. No entry mixes UI-level click instructions with process summaries. All entries are at the same L1 business-process level |

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
