# Audit Result: LHC Booking System – old single-file example (capabilities, workflows and dependencies)

> **About this audit.** This is a teaching example. It reviews the *old* LHC Booking System example (`examples/lhc_booking_system_example.md` on the `main` branch, 280 lines), not the package in this folder's `docs/`. Its purpose is to show findings whose evidence is true: every row below can be confirmed by opening the old file at the line cited. The old file's own "Example Audit Finding" did not meet that standard; for instance its BUG-01 says capabilities use "Support" while workflows use "ITS Support", but every capability row (lines 9–24) already says "ITS Support". The package in `docs/` was rebuilt from the old file and fixes every finding here; section 7 says where.

## 1. Review scope

| Field | Value |
|---|---|
| Application | LHC Booking System |
| Document reviewed | Old single-file example "LHC Booking System Example" (no version): Capabilities Register Example (lines 5–24, judged as BUS-02), Workflow Register Example and Workflow Detail Example (lines 26–243, judged as BUS-03), Example Application Dependencies Register (lines 245–258, judged as ENG-05) |
| Depth in Scope Record | None: the old example has no Scope Record. Judged at depth D, the depth the rebuilt package gives BUS-02, BUS-03 and ENG-05 (SP-00 version 1.0) |
| Review type | Change review |
| Reviewer | Framework maintainers, teaching review |
| Date | 2026-06-30 |
| Related documents read | None exist in the old example: it has no BUS-04, BUS-05 or ENG-08 |
| Linter run | Not run: the old file has no front-matter or `-xx` IDs for the linter to read. Mechanical rules X-01, X-02, X-03, X-09 and X-16 were checked by hand, row by row |

## 2. Rubric summary

Universal: 2 Pass · 2 Partial · 9 Fail · 0 Not in scope or not applicable
Artifact: 11 Pass · 8 Partial · 17 Fail · 5 Not in scope or not applicable
Critical criteria not passing: 14 (U-01, U-02, U-04, U-07, U-08, U-10, U-12, BUS-02.1, BUS-02.7, BUS-03.1, BUS-03.4, BUS-03.5, ENG-05.3, ENG-05.6)
Open findings: 6 High · 3 Medium · 0 Low

## 3. Universal rubric results

| ID | Criterion | Result | Evidence |
|---|---|---|---|
| U-01 | Identity | Fail | No front-matter: line 1 is the heading "# LHC Booking System Example" (A-BUG-09) |
| U-02 | Purpose | Fail | Line 3, "This example shows how capabilities and workflows can be documented", describes the example, not the application (A-BUG-09) |
| U-03 | Scope | Fail | No Scope section (A-BUG-09) |
| U-04 | Required structure | Fail | No Purpose, Scope, Assumptions and open questions, Known limitations or Change log sections; headings at lines 1–275 (A-BUG-09) |
| U-05 | Specificity | Partial | Workflow steps are concrete, but owners are teams ("LHC / ITS", D01 line 249) and W02 says "LHC may close after a defined period" (line 91) |
| U-06 | Language for its readers | Pass | Plain business language throughout |
| U-07 | Traceability | Fail | Four capability↔workflow links are one-sided (A-BUG-01 to A-BUG-04) |
| U-08 | Usable for its readers | Partial | A support person can follow each workflow, but cannot tell which dependency is critical or what to do when it fails (A-BUG-07) |
| U-09 | Limitations and unknowns visible | Fail | No assumptions, open questions or limitations; the open expiry period in line 91 is not raised as a question (A-BUG-09) |
| U-10 | Ownership | Fail | No document owner; capabilities have no owner column; dependency owners are teams (lines 249–258) (A-BUG-07, A-BUG-09) |
| U-11 | Consistency | Fail | C11 and the workflow steps use different status names, and no lifecycle defines either (A-BUG-06) |
| U-12 | Acceptance readiness | Fail | No status, version or change log (A-BUG-09) |
| U-13 | Says it once | Pass | Capabilities, workflows and dependencies each appear in one table |

## 4. Artifact rubric results

| ID | Criterion | Critical | Result | Evidence |
|---|---|---|---|---|
| BUS-02.1 | Unique IDs | Yes | Partial | C01–C16 are unique but not in the `C-xx` format (A-BUG-09) |
| BUS-02.2 | Business language | No | Pass | Names are business verbs ("Submit booking request", "Assign rooms") |
| BUS-02.3 | Description | No | Pass | Every row has a description |
| BUS-02.4 | Outcome | Yes | Pass | Every row has an outcome |
| BUS-02.5 | Roles | No | Fail | C12 Primary users "System, Guest, LHC Staff" (line 20); role names, not IDs (A-BUG-05) |
| BUS-02.6 | Owner | No | Fail | No owner column (A-BUG-09) |
| BUS-02.7 | Process mapping | Yes | Fail | C01, C03, C05 and C11 disagree with the workflow table (A-BUG-01 to A-BUG-04) |
| BUS-02.8 | Coverage | No | Partial | No automated capability for the unanswered Returned request in line 91; no coverage check (A-BUG-05) |
| BUS-02.9 | Non-duplication | No | Pass | No capability repeated |
| BUS-02.10 | Dependency visibility | No | Fail | No Dependencies column; C12 does not show its reliance on D04 (A-BUG-07) |
| BUS-02.11 | Automated actions marked | No | Fail | Automated sends and status updates are shown as actor "System" (A-BUG-05) |
| BUS-02.12 | Criticality | No | Fail | No Criticality column (A-BUG-09) |
| BUS-02.13 | Capability map | No | Not in scope | Full-only criterion |
| BUS-03.1 | Unique IDs | Yes | Partial | W01–W08 are unique but not in the `W-xx` format (A-BUG-09) |
| BUS-03.2 | Trigger | Yes | Pass | Every workflow row has a trigger |
| BUS-03.3 | Outcome | Yes | Pass | Every workflow row has a main outcome |
| BUS-03.4 | Roles | Yes | Fail | Roles by name, not ID; step actors include "System" (A-BUG-05, A-BUG-09) |
| BUS-03.5 | Capabilities used | Yes | Fail | W02, W03 and W08 disagree with the capability table (A-BUG-01 to A-BUG-04) |
| BUS-03.6 | Steps | No | Partial | Steps are ordered, but 17 step rows have actor "System" (for example lines 46–49) (A-BUG-05) |
| BUS-03.7 | Decision points | No | Partial | Decision tables exist; the W01 decision owner is "System" (line 55) (A-BUG-05) |
| BUS-03.8 | Statuses | No | Fail | Status names are free text with no lifecycle (A-BUG-06) |
| BUS-03.9 | Manual steps | No | Pass | Change requests made by phone or email are disclosed (line 124) |
| BUS-03.10 | Exceptions | No | Pass | Every workflow has an exceptions table with handling, owner and escalation |
| BUS-03.11 | Boundary and cohesion | No | Partial | C04 Confirm booking appears in both W02 (line 31) and W03 (line 32); see A-BUG-02, A-BUG-03 |
| BUS-03.12 | One level of detail | No | Pass | All steps are business-level actions |
| BUS-03.13 | Journeys linked | No | Fail | No journeys although people use the application through screens (A-BUG-09) |
| BUS-03.14 | Process diagrams | No | Not in scope | Full-only criterion |
| BUS-03.15 | Responsibility matrix | No | Not in scope | Full-only criterion |
| ENG-05.1 | Dependency coverage | No | Partial | Ten dependencies cover hosting, domain, email, identity, data, network, people and process; no funding dependency or downstream consumers (A-BUG-07) |
| ENG-05.2 | Purpose | No | Pass | Every row has a purpose |
| ENG-05.3 | Owner | Yes | Fail | Owners are teams such as "LHC / ITS" (D01) and "ITS" (D02, D03, D10), not named people (A-BUG-07) |
| ENG-05.4 | Impact | Yes | Pass | "Impact if unavailable" is stated in user terms for every row |
| ENG-05.5 | Criticality and type | No | Fail | No Criticality column; no Type value is in the fixed list (A-BUG-07, A-BUG-08) |
| ENG-05.6 | Support path | Yes | Partial | Paths name teams only ("ITS support", "ITS helpdesk"), with no channel or contract reference (A-BUG-07) |
| ENG-05.7 | Traceability | No | Fail | No Capabilities affected column (A-BUG-07) |
| ENG-05.8 | Workaround | No | Fail | No Workaround column (A-BUG-07) |
| ENG-05.9 | Interfaces | No | Fail | No interface entries for email (D04) or sign-in (D05) (A-BUG-07) |
| ENG-05.10 | Runbook, cost and renewal | No | Fail | No Runbook, Cost or Renewal columns (A-BUG-07) |
| ENG-05.11 | Direction and downstream impact | No | Fail | No direction or downstream consumers (A-BUG-07) |
| ENG-05.12 | Interface details | No | Not in scope | Full-only criterion |
| ENG-05.13 | Exit and substitution | No | Not in scope | Full-only criterion |

## 5. Cross-document rules

| Rule | Type | Result | Evidence |
|---|---|---|---|
| X-01 | Mechanical | Pass | Every capability lists at least one workflow (lines 9–24) |
| X-02 | Mechanical | Fail | Four one-sided links (A-BUG-01 to A-BUG-04) |
| X-03 | Mechanical | Fail | "System" in C12 Primary users (line 20); role names, not role IDs (A-BUG-05) |
| X-04 | Mechanical | Fail | No status table exists, so no status name used is defined (A-BUG-06) |
| X-09 | Mechanical | Fail | No Criticality, Workaround or Capabilities affected columns (A-BUG-07) |
| X-16 | Mechanical | Fail | No journeys (A-BUG-09) |
| X-20 | Mechanical | Fail | No dependency is typed from the fixed list, so integrations needing interface entries cannot be identified (A-BUG-08) |
| X-21 | Mechanical | Fail | No Runbook column (A-BUG-07) |
| X-25 | Mechanical | Fail | No front-matter; IDs not in `TYPE-xx` format (A-BUG-09) |

## 6. Findings

Severity definitions: [decision rules §4](../../../rubrics/04_decision_rules.md#4-severity).

### Bugs

| ID | Finding | Severity | Evidence | Required action |
|---|---|---|---|---|
| A-BUG-01 | C01 lists W02, but W02 does not use C01. | High | Capability table row C01, line 9: "W01, W02". Workflow table row W02, line 31: "C02, C03, C04, C05, C11, C12". Critical criteria BUS-02.7 and BUS-03.5 cannot pass. | Remove W02 from C01: staff entering a request for a guest is part of W01. |
| A-BUG-02 | C03 lists W03, but W03 does not use C03. | High | Row C03, line 11: "W02, W03". Row W03, line 32: "C02, C04, C10, C11, C12, C16". | Remove W03 from C03: review happens in W02, and W03 starts after confirmation. |
| A-BUG-03 | C05 lists W03, but W03 does not use C05. | High | Row C05, line 13: "W02, W03". Row W03, line 32 (as above). | Remove W03 from C05: return and reject happen in W02. |
| A-BUG-04 | W08 uses C11, but C11 does not list W08. | High | Row W08, line 37: "C11, C15, C16". Row C11, line 19: "W01, W02, W03, W04, W06". | Add W08 to C11: support staff check booking status when handling an issue. |
| A-BUG-05 | "System" is listed as a user, and automated actions have no marking or owner. | Medium | Row C12, line 20: Primary users "System, Guest, LHC Staff". Workflow steps give "System" as the actor in 17 rows, for example W01 steps 2–5 (lines 46–49); W01 decision owner "System" (line 55). | Remove "System" from every role column; use role IDs; mark automated capabilities with `Automated` = Yes and show automated steps with actor `Automated`. |
| A-BUG-06 | Status names drift between C11 and the workflows, and no lifecycle defines them. | Medium | Row C11, line 19: "pending, confirmed, modified, canceled, checked in, completed, or closed". The workflow steps use Draft, Pending review, Confirmed, Returned, Rejected, Room assigned, Modification requested, Cancellation requested, Modified and Canceled (lines 46–130). "Checked in", "completed" and "closed" appear in no workflow; Returned and Rejected are missing from C11. The file has no status table. | Define one lifecycle (statuses and transitions) in BUS-05 and use exactly those names in C11, every workflow and the glossary. |
| A-BUG-07 | The dependency register lacks the columns a support person needs during an outage. | High | Header, line 247: "ID, Dependency, Type, Purpose, Owner, Impact if unavailable, Support path". No Criticality, Capabilities affected or Workaround (X-09), no Runbook, Cost or Renewal, and no interface entries for email (D04) or staff sign-in (D05). Owners are teams ("LHC / ITS", "ITS"), so critical criterion ENG-05.3 cannot pass. | Use the full ENG-05 columns with named owners; add interface entries for email and sign-in; give each High dependency a workaround and a runbook entry; list each dependency in the Dependencies column of the capabilities it affects. |
| A-BUG-08 | Dependency types are not from the fixed type list. | Medium | D01 type "Website" (line 249); other rows use "Application platform", "Domain/DNS", "Communication", "Identity/access", "Business data", "Infrastructure", "Operational dependency" and "Support dependency" (lines 250–258). The ENG-05 type list is Hosting, Domain, Email, Identity, Integration, Data, Vendor, Network, People, Process, Funding. | Map each row to a listed type (for example D01 Hosting, D04 Email, D05 Identity, D09 People, D10 Process). |
| A-BUG-09 | The file does not follow the document structure, so it has no identity, owner, status or standard sections. | High | Line 1 is a heading with no front-matter; no Purpose, Scope, Assumptions and open questions, Known limitations or Change log; IDs are "C01" and "W01", not `C-xx` and `W-xx`; no capability Owner or Criticality columns; no journeys. Critical criteria U-01, U-02, U-04, U-10 and U-12 cannot pass. | Split the file into the template documents for its depth, each with front-matter, the standard sections and IDs in `TYPE-xx` format. |

### Risks

| ID | Finding | Severity | Evidence | Mitigation or required action |
|---|---|---|---|---|
| A-RISK-01 | If email (D04) fails, nobody knows which capabilities stop or what staff should do instead, so guests are not told of decisions and may arrive unconfirmed. | Medium | D04 row, line 252: impact "Guests and staff may not receive booking updates", support path "ITS support"; no workaround, and C12 (line 20) does not reference D04. | Covered by A-BUG-07: add the workaround (staff phone guests) and the runbook entry. |

### Ideas

| ID | Finding | Value | Evidence | Suggested action |
|---|---|---|---|---|
| A-IDEA-01 | Keep each capability↔workflow link in one place, or check symmetry mechanically, so the two tables cannot drift again. | High | All four link errors (A-BUG-01 to A-BUG-04) are one-sided edits of a two-sided link. | Run the linter's X-02 check on every change. |
| A-IDEA-02 | Make the unanswered Returned request an automated expiry with a stated period. | Medium | W02 exception, line 91: "LHC may close after a defined period". | Add an automated capability and a rule with the period in days. |

## 7. Required fixes

| Finding | Fix | Owner |
|---|---|---|
| A-BUG-01 to A-BUG-04 | Make every link two-way. Done in the rebuilt package: C-01 lists W-01 only; C-03 and C-05 list W-02 only; C-11 lists W-08 (docs/BUS-02, docs/BUS-03) | Daniel Reyes, LHC Front Office Supervisor |
| A-BUG-05 | Role IDs only; automated work as `Automated`. Done: C-12 Roles "Automated"; C-18 added for expiry; workflow steps use `Automated` (docs/BUS-02, docs/BUS-03) | Daniel Reyes, LHC Front Office Supervisor |
| A-BUG-06 | One lifecycle. Done: ST-01 to ST-10 and TR-01 to TR-10 in docs/BUS-05; room assignment is an action, not a status (ADR-004) | Grace Tan, LHC Manager |
| A-BUG-07, A-BUG-08 | Full dependency register. Done: D-01 to D-10 with every ENG-05 column, INT-01 and INT-02, runbooks RB-01 to RB-06 (docs/ENG-05, docs/ENG-08) | Priya Nair, ITS Application Lead |
| A-BUG-09 | Template documents with front-matter. Done: the 24-item package in docs/, scoped in SP-00 | Priya Nair, ITS Application Lead |

## 8. Proposed conditions

None: the decision is Revise and Resubmit.

## 9. Decision

Decision: **Revise and Resubmit**

Decision rule applied: [decision rules §5](../../../rubrics/04_decision_rules.md#5-document-decision), row **Revise and Resubmit** ("None of the above"). Reject does not apply: the content is the right content for its readers and is usable, it claims no acceptance or test result, and there is no Accepted document for it to contradict. Accept and Accept with Conditions do not apply because six High Bugs are open (A-BUG-01 to A-BUG-04, A-BUG-07, A-BUG-09) and critical criteria fail.

Next action: the producer rebuilds the example as a scoped package and resubmits it with a linter run. (Done: see `docs/` in this folder.)

## 10. Framework feedback (optional, never affects the decision)

The old example has no Scope Record, so the depth used for judging had to be borrowed from the rebuilt package. A review of an unscoped document could say which depth to assume.
