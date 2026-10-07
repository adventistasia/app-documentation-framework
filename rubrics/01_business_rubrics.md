# Business Layer Rubrics

These are documentation review criteria for the business-layer documents, BUS-01 to BUS-09. They judge the documents, not the application. Apply them together with the [universal rubric](00_universal_rubric.md). Result values, which criteria apply at each depth, and how the **Critical** and **Full only** flags turn results into a decision are defined only in the [decision rules](04_decision_rules.md). Mechanical cross-document rules (X-xx) are checked by the linter and are not repeated here; a criterion below that touches one asks the reviewer to judge what the linter cannot.

The templates are in `templates/business/`. "Full only" criteria correspond to the template sections marked *(Full)*. The critical criteria of each document are the essentials an S section is judged on.

## BUS-01 Application Overview & Business Case

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| BUS-01.1 | Purpose and what it does | Explains in plain business language what the application does, for whom, and why it exists. | Yes | No |
| BUS-01.2 | Ownership | Names the business owner, support owner and technical owner as people with roles, matching ENG-08 and SP-12. | Yes | No |
| BUS-01.3 | Users and stakeholders | Identifies the main user groups and stakeholders and what each needs, referring to roles by ID; when T2 is No, defines the single role `R-01` and who has access. | No | No |
| BUS-01.4 | Scope | States what is in scope and what people might expect but is out of scope. | No | No |
| BUS-01.5 | Access point | Gives the URL or entry point, the access method and how to get access. | No | No |
| BUS-01.6 | Impact if unavailable | Explains what stops, who is affected, how quickly it hurts, and the manual workaround. | Yes | No |
| BUS-01.7 | Package map | Lists every document in scope with its depth and location, matching SP-00. | No | No |
| BUS-01.8 | Problem statement | Describes the current situation, who is affected and what it costs, in numbers where possible, or `TBD` with an owner and a question ID. | No | No |
| BUS-01.9 | Benefits measured | Every benefit has an ID, a beneficiary and a benefit owner, and names a success measure in SP-10 with a baseline (or a capture date) and a target with a date. | Yes | No |
| BUS-01.10 | What success looks like | A section headed "What success looks like" gives three to five plain, observable sentences consistent with the benefits. | Yes | No |
| BUS-01.11 | Strategic fit | Names the business objective, plan or policy the application supports. | No | No |
| BUS-01.12 | Non-functional commitments | States the top non-functional commitments in plain words with numbers, each linked to its NFR in ENG-01. | No | No |
| BUS-01.13 | Resources and costs | Summarises people, running costs and budget holder in one paragraph linking BUS-07, or names the shared platform when T8 is No. | No | No |
| BUS-01.14 | Sections held here | At Foundation, each S item placed in BUS-01 by the Scope Record is a section headed with its document ID and title, uses its template's core tables, and is listed in `contains`. | No | No |
| BUS-01.15 | Options considered | The alternatives weighed are listed with cost, benefit and the reason for the choice. | No | Yes |
| BUS-01.16 | Stakeholder communication | Who is told about changes, outages and benefit results, how and how often, is stated. | No | Yes |

## BUS-02 Capabilities Register

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| BUS-02.1 | Unique IDs | Every capability has a unique `C-xx` ID that is never reused. | Yes | No |
| BUS-02.2 | Business language | Capability names use business verbs and describe what users or the business can do, not screens, buttons, tables or endpoints. | No | No |
| BUS-02.3 | Description | Every capability explains what the system enables. | No | No |
| BUS-02.4 | Outcome | Every capability states a business or operational outcome. | Yes | No |
| BUS-02.5 | Roles | Every capability lists the roles that use or oversee it by role ID; no non-role actor such as "System" appears in `Roles`. | No | No |
| BUS-02.6 | Owner | Every High-criticality capability has a named owner. | No | No |
| BUS-02.7 | Process mapping | Every capability maps to at least one business process, or is marked `Admin/support only`, and the mapping agrees with BUS-03. | Yes | No |
| BUS-02.8 | Coverage | User, admin, access, support, reporting, notification, audit and automated capabilities are covered where they apply, or the coverage check says why not. | No | No |
| BUS-02.9 | Non-duplication | No capability is repeated under a different name. | No | No |
| BUS-02.10 | Dependency visibility | High-criticality capabilities list the dependencies they rely on, or `None`. | No | No |
| BUS-02.11 | Automated actions marked | Every action the system performs with no person acting is a capability with `Automated` = Yes. | No | No |
| BUS-02.12 | Criticality | Every capability is rated High, Medium or Low, and the launch-critical ones are clear. | No | No |
| BUS-02.13 | Capability map | A captioned diagram groups all capabilities by business area. | No | Yes |

## BUS-03 Business Process Register

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| BUS-03.1 | Unique IDs | Every process has a unique `W-xx` ID. | No | No |
| BUS-03.2 | Trigger | Every process states what starts it. | Yes | No |
| BUS-03.3 | Outcome | Every process states what successful completion produces. | Yes | No |
| BUS-03.4 | Roles | Every process names its participating roles by role ID. | Yes | No |
| BUS-03.5 | Capabilities used | Every process maps to the capabilities it uses, and the mapping agrees with BUS-02. | Yes | No |
| BUS-03.6 | Steps | The main steps of each process are in order, each with an actor (a role ID or `Automated`) and a business action. | No | No |
| BUS-03.7 | Decision points | Approve, reject, return, cancel, escalate and other decisions are documented with who decides and the result, where relevant. | No | No |
| BUS-03.8 | Statuses | The statuses each process moves records through are listed by ID and agree with the BUS-05 lifecycle. | No | No |
| BUS-03.9 | Manual steps | Work done outside the system is disclosed. | No | No |
| BUS-03.10 | Exceptions | Common failure and alternate paths are included, with handling, owner and escalation. | No | No |
| BUS-03.11 | Boundary and cohesion | Each process covers one primary trigger-to-outcome flow with clear boundaries and one owner. Entries with several unrelated triggers, independently valuable outcomes, different owners or separate status lifecycles are split. | No | No |
| BUS-03.12 | One level of detail | Steps describe business-level actions consistently. No entry mixes screen-click instructions with process summaries, and all entries are at the same business-process level. | No | No |
| BUS-03.13 | Journeys linked | When T1 is Yes, each process lists the user journeys that carry it out, and the links agree with ENG-02. | No | No |
| BUS-03.14 | Process diagrams | Each process has a captioned diagram showing steps, decisions and exception paths. | No | Yes |
| BUS-03.15 | Responsibility matrix | Each process has exactly one accountable party, with responsible, consulted and informed parties named. | No | Yes |

## BUS-04 Roles & Access Matrix

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| BUS-04.1 | Role definitions | Every role has an ID, a name matching SP-01, a plain-language description, typical users and a role owner. | No | No |
| BUS-04.2 | Permissions | Each role states its view, create, update, approve, return, cancel or delete, setup, user management and reporting permissions where they apply, with any limits. | Yes | No |
| BUS-04.3 | Access approver | Every role names who approves its assignment. | Yes | No |
| BUS-04.4 | Access request | The access request steps are documented, from request to working access, with who requests, approves and grants. | No | No |
| BUS-04.5 | Access removal | Routine and urgent access removal are documented, with who triggers and performs each, how fast, and how removal is confirmed. | Yes | No |
| BUS-04.6 | Sensitive permissions and segregation | Administrative and risky permissions, and role combinations one person must not hold, are identified with a control and an owner. | No | No |
| BUS-04.7 | Alignment with processes | Every role used in capabilities, processes, journeys and transitions appears here, and the permissions agree with the actions those documents give each role. | No | No |
| BUS-04.8 | Support alignment | Support roles and access-support responsibilities agree with ENG-08. | No | No |
| BUS-04.9 | Periodic access review | The reviewer, frequency, what is checked and where evidence is kept are stated. | No | No |
| BUS-04.10 | Segregation of duties matrix | Conflicting role pairs are marked with how each conflict is enforced. | No | Yes |
| BUS-04.11 | Access review log | Completed access reviews are recorded with date, reviewer, changes and evidence. | No | Yes |

## BUS-05 Business Rules & Status Lifecycle

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| BUS-05.1 | Testable rules | Every rule is written as a condition and an action, clearly enough that a positive and a negative test could be written from it. | Yes | No |
| BUS-05.2 | Rule owner | Every rule has an owner or decision authority. | No | No |
| BUS-05.3 | Exceptions and overrides | Where exceptions are allowed, the exception authority, the allowed override and the audit requirement are documented. | No | No |
| BUS-05.4 | Status definitions | Every status has an ID, a name matching SP-01, the record it belongs to, a business meaning and whether it is terminal. | Yes | No |
| BUS-05.5 | Status transitions | Every allowed transition is listed with its from and to statuses; anything not listed is understood as not allowed. | Yes | No |
| BUS-05.6 | Who changes status | Every transition names the roles that may perform it, or `Automated`, and the rule that guards it where one applies. | No | No |
| BUS-05.7 | Validation rules | Required data, date, availability, amount and submission checks are documented as validation rules, with whether each blocks or warns. | No | No |
| BUS-05.8 | Process linkage | Rules and transitions reference the processes and capabilities they affect. | No | No |
| BUS-05.9 | Meaning for users | Every user-visible status has a meaning written in the user's words. | No | No |
| BUS-05.10 | Lifecycle complete | Every non-terminal status has a way out, every status except the first can be reached, and any diagram matches the transitions table. | No | No |
| BUS-05.11 | Consistency with processes | No rule, status or transition contradicts the process steps and decisions in BUS-03. | No | No |

## BUS-06 Data, Reports & Notifications Register

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| BUS-06.1 | Main records | The major business records are identified with an ID, a name matching SP-01 and a description. | No | No |
| BUS-06.2 | Required fields | The required business fields of each core record are listed. | No | No |
| BUS-06.3 | Classification | Every record is classified as Public, Internal, Confidential, Personal or Special-category, consistent with the most sensitive data it holds. | Yes | No |
| BUS-06.4 | Data ownership | Every record has a named owner. | Yes | No |
| BUS-06.5 | Reports | The standard reports, dashboards and exports others use are documented, with frequency and format. | No | No |
| BUS-06.6 | Report purpose | Every report has an audience, a purpose, an owner and a source, and official records are identified. | No | No |
| BUS-06.7 | Notifications | Every notification has a trigger, a recipient, a purpose and an expected action. | Yes | No |
| BUS-06.8 | Retention | Every record has a retention period with its rationale and a disposal method, even if provisional. | No | No |
| BUS-06.9 | Personal data justified | Every Personal or Special-category record states the purpose and lawful basis for holding it, a retention period with rationale, and how it is disposed of. | Yes | No |
| BUS-06.10 | Core records marked | Records the business relies on being right are marked `Core` = Yes, so output checks can be planned when T6 is Yes. | No | No |
| BUS-06.11 | Data subject requests | How requests to see, correct, export or delete personal data are received, handled and completed, with time limits, is stated. | No | Yes |
| BUS-06.12 | Report lineage | Each official or core report traces from source records through filters and calculations to its figures. | No | Yes |

## BUS-07 Resource & Cost Model

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| BUS-07.1 | People and effort | Every recurring activity (support, administration, data upkeep, access administration, releases, routine tasks in ENG-08) has a role, an effort per month and an owner. | Yes | No |
| BUS-07.2 | Cost lines owned and based | Every cost line has an ID, an owner and a basis (Estimate, Quote or Actual), and estimates say what they are based on. | Yes | No |
| BUS-07.3 | Dependency costs present | Every dependency that costs money appears in a cost line, and the cost lines name their dependency or `None`. | No | No |
| BUS-07.4 | One-off deployment | Build, migration, training, cutover and early-life support effort or spend are stated. | No | No |
| BUS-07.5 | Running cost summary | Monthly and annual recurring totals are given by group, with their assumptions, and one-off costs are shown separately. | Yes | No |
| BUS-07.6 | Licences and renewals | Every licence and subscription has its cost, billing cycle, renewal date, notice period and owner, matching ENG-05. | No | No |
| BUS-07.7 | Scaling assumptions | The drivers that make cost grow are named with current and expected values and the cost lines they affect. | No | No |
| BUS-07.8 | Funding and ownership | The budget holder, cost centre and funding period are named. | No | No |
| BUS-07.9 | End of life | What retiring the application would involve is described, including data export within retention rules and licence notice periods. | No | No |
| BUS-07.10 | Cost scenarios | Low, expected and high cost cases for the next one to three years are given with their assumptions. | No | Yes |
| BUS-07.11 | Total cost of ownership | One-off and recurring costs are totalled over the planned lifetime. | No | Yes |

## BUS-08 Risk & Controls Register

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| BUS-08.1 | Risk coverage | Operational, access, data, privacy and compliance, reporting, dependency, support and technical risks are considered, drawing on processes, dependencies, known limitations, technical debt and incidents. | No | No |
| BUS-08.2 | Control mapping | Every risk has at least one control or mitigation, marked existing or planned. | Yes | No |
| BUS-08.3 | Owner | Every risk and its control have an accountable owner. | Yes | No |
| BUS-08.4 | Severity | Every risk has likelihood, impact and severity rated consistently with the rating guidance. | No | No |
| BUS-08.5 | Residual risk | The risk remaining after controls is stated. | No | No |
| BUS-08.6 | Review cadence | Every risk has a review cadence. | No | No |
| BUS-08.7 | Traceability | Risks name the capabilities, processes, dependencies, records, rules or limitations they affect, by ID. | No | No |
| BUS-08.8 | High risks handled | Every High risk is either mitigated to a lower residual risk or formally accepted by a named owner with a date. | Yes | No |
| BUS-08.9 | Privacy impact assessment | When T4 is Yes, the privacy impact assessment status is recorded: done (with link, date and outcome), planned (with owner and date), or not needed (with reason and who decided); findings are raised as Privacy and compliance risks. | Yes | No |
| BUS-08.10 | Clear risk statements | Each risk states a cause, an event and a consequence, not just a topic. | No | No |
| BUS-08.11 | Heat map | The count of risks by likelihood and impact is shown before and after controls. | No | Yes |
| BUS-08.12 | Control testing | Each control on a High or Medium risk has a test method, frequency, tester and last result. | No | Yes |

## BUS-09 User & Admin Guide

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| BUS-09.1 | Audience separation | User tasks and admin tasks are clearly separated. | No | No |
| BUS-09.2 | Journey coverage | Every user-facing journey in ENG-02 has a how-to task that names it, or its exclusion is explained. | No | No |
| BUS-09.3 | Step clarity | Steps are short, numbered, in plain language and in the user's words. | No | No |
| BUS-09.4 | Expected result | Each task states what the user should see when it worked. | No | No |
| BUS-09.5 | Error handling | Each task gives common mistakes and what to do if something goes wrong. | No | No |
| BUS-09.6 | Support path | The guide tells users where to get help for each kind of problem, matching ENG-08. | Yes | No |
| BUS-09.7 | Role alignment | No task tells a user to do something their role does not allow in BUS-04, and each task names its required role. | Yes | No |
| BUS-09.8 | Getting started | A new user can get access and complete a first task end to end from the getting-started section, with what they should see. | Yes | No |
| BUS-09.9 | Statuses explained | Every user-visible status in BUS-05 is explained in the user's words, with what happens next, and how notifications work is explained. | No | No |
| BUS-09.10 | Reference | Field meanings and every error or warning message a user can see are listed, with what to do. | No | No |
| BUS-09.11 | Release notes | A What's new section gives changes per release in user language, linked to ENG-07, or states "First release". | No | No |
| BUS-09.12 | Accessibility statement | When T11 is Yes, the statement gives the target standard, how and when conformance was checked, known gaps with workarounds, and how to report a problem, traced to an NFR. | No | No |
| BUS-09.13 | Supported browsers and devices | Supported browsers, versions and devices are listed and traced to an NFR. | No | No |
| BUS-09.14 | Keyboard and assistive technology | Keyboard and assistive-technology methods are given for the main tasks. | No | Yes |
| BUS-09.15 | Training materials | Training materials for each role are listed with location and owner. | No | Yes |

## Mapping from the 2026-06-30 criteria

DEP-xx (DOC-07) and SO-xx (DOC-08) moved to the engineering layer (ENG-05 and ENG-08); see the engineering rubrics.

| Old ID | New ID |
|---|---|
| AO-01 Purpose and business value | BUS-01.1 (business value now also BUS-01.8 and BUS-01.9) |
| AO-02 Ownership | BUS-01.2 |
| AO-03 Users | BUS-01.3 |
| AO-04 Scope | BUS-01.4 |
| AO-05 Access point | BUS-01.5 |
| AO-06 Operational importance | BUS-01.6 |
| AO-07 Related artifacts | BUS-01.7 (package map) |
| CAP-01 Unique IDs | BUS-02.1 |
| CAP-02 Business language | BUS-02.2 |
| CAP-03 Description | BUS-02.3 |
| CAP-04 Outcome | BUS-02.4 |
| CAP-05 Primary users | BUS-02.5 (roles by ID; "System" not allowed) |
| CAP-06 Owner | BUS-02.6 |
| CAP-07 Workflow mapping | BUS-02.7 |
| CAP-08 Coverage | BUS-02.8 |
| CAP-09 Non-duplication | BUS-02.9 |
| CAP-10 Dependency visibility | BUS-02.10 |
| WF-01 Unique IDs | BUS-03.1 |
| WF-02 Trigger | BUS-03.2 |
| WF-03 Outcome | BUS-03.3 |
| WF-04 Roles | BUS-03.4 |
| WF-05 Capabilities used | BUS-03.5 |
| WF-06 Steps | BUS-03.6 |
| WF-07 Decision points | BUS-03.7 |
| WF-08 Statuses | BUS-03.8 |
| WF-09 Manual steps | BUS-03.9 |
| WF-10 Exceptions | BUS-03.10 |
| WF-11 Workflow boundary and cohesion | BUS-03.11 |
| WF-12 Appropriate level of detail | BUS-03.12 |
| RA-01 Role definitions | BUS-04.1 |
| RA-02 Permissions | BUS-04.2 |
| RA-03 Access approval | BUS-04.3 |
| RA-04 Access request | BUS-04.4 |
| RA-05 Access removal | BUS-04.5 (now includes urgent removal) |
| RA-06 Sensitive permissions | BUS-04.6 (now includes segregation) |
| RA-07 Workflow alignment | BUS-04.7 |
| RA-08 Support alignment | BUS-04.8 |
| BR-01 Testable rules | BUS-05.1 |
| BR-02 Rule owner | BUS-05.2 |
| BR-03 Exceptions | BUS-05.3 |
| BR-04 Status definitions | BUS-05.4 |
| BR-05 Status transitions | BUS-05.5 |
| BR-06 Actor permissions | BUS-05.6 |
| BR-07 Validation rules | BUS-05.7 |
| BR-08 Workflow linkage | BUS-05.8 |
| DRN-01 Main records | BUS-06.1 |
| DRN-02 Required fields | BUS-06.2 |
| DRN-03 Sensitive data | BUS-06.3 (Yes/No replaced by a five-level classification) |
| DRN-04 Data ownership | BUS-06.4 |
| DRN-05 Reports | BUS-06.5 |
| DRN-06 Report purpose | BUS-06.6 |
| DRN-07 Notifications | BUS-06.7 |
| DRN-08 Retention | BUS-06.8 (personal data also BUS-06.9) |
| RC-01 Risk coverage | BUS-08.1 (adds privacy and compliance, and technical) |
| RC-02 Control mapping | BUS-08.2 |
| RC-03 Owner | BUS-08.3 |
| RC-04 Severity | BUS-08.4 |
| RC-05 Residual risk | BUS-08.5 |
| RC-06 Review cadence | BUS-08.6 |
| RC-07 Traceability | BUS-08.7 |
| UG-01 Audience separation | BUS-09.1 |
| UG-02 Workflow coverage | BUS-09.2 (now coverage of ENG-02 journeys) |
| UG-03 Step clarity | BUS-09.3 |
| UG-04 Expected result | BUS-09.4 |
| UG-05 Error handling | BUS-09.5 |
| UG-06 Support path | BUS-09.6 |
| UG-07 Role alignment | BUS-09.7 |
| DEP-01 to DEP-08 | Moved to ENG-05 (engineering rubrics) |
| SO-01 to SO-09 | Moved to ENG-08 (engineering rubrics) |
