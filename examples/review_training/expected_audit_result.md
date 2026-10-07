# Audit Result: Stock Count Sheets – Package review (expected result for review training)

> **Answer key.** This is the audit result a correct review of `stock_count_flawed/` should reach. Do not give it to a reviewer under test. The planted defects are listed first so a trainer can score a review quickly. The rest follows the [audit result template](../../review/01_audit_result_template.md). Line numbers refer to the files in `stock_count_flawed/`.

## Planted defects

| # | Defect | Where | Caught by | Rule or criterion | Severity | Finding |
|---|---|---|---|---|---|---|
| 1 | C-04 lists W-01, but W-01 does not list C-04 | `docs/README.md:262`, `:268` | Linter | X-02 | High | A-BUG-01 |
| 2 | Role R-03 is used in a `Roles` column but never defined | `docs/README.md:261` | Linter | X-03 | High | A-BUG-02 |
| 3 | LIM-02 is missing from SP-12's consolidated known limitations | `AGENTS.md:323`; `docs/README.md:231–235` | Linter | X-12 | High | A-BUG-03 |
| 4 | Must requirement FR-04 has no acceptance criterion | `AGENTS.md:135`; `docs/README.md:206` | Linter | X-19 | High | A-BUG-04 |
| 5 | High dependency D-01 names no runbook entry | `AGENTS.md:189` | Linter | X-21 | High | A-BUG-05 |
| 6 | NFR-04 is defined twice (RTO and RPO) | `AGENTS.md:144–145` | Linter | X-25 | High | A-BUG-06 |
| 7 | SP-12 is Accepted while Must criterion AC-11 is Not run, and its counts say all 12 passed | `docs/README.md:6`, `:210`, `:217` | Linter (and reviewer for the false counts) | X-26, SP-12.3 | High | A-BUG-07 |
| 8 | AC-03 is not testable: "the sheets should be accurate and easy to use" | `docs/README.md:202` | Reviewer only | X-30, SP-11.2 | High | A-BUG-08 |
| 9 | L1 measure SM-02 has a baseline with no date, period or usable source | `docs/README.md:189`, `:49` | Reviewer only | SP-10.2, BUS-01.9 | High | A-BUG-09 |

The linter's expected output is in [`stock_count_flawed/expected_findings.json`](stock_count_flawed/expected_findings.json): one High finding each for X-02, X-03, X-12, X-19, X-21, X-25 and X-26. A reviewer who copies those and also raises defects 8 and 9 has found everything that was planted. Findings beyond the nine are acceptable when they carry true evidence; A-RISK-01, A-RISK-02 and A-IDEA-01 below are examples.

## 1. Review scope

| Field | Value |
|---|---|
| Application | Stock Count Sheets |
| Document reviewed | Whole package: BUS-01 (`docs/README.md`), version 1.0, and ENG-09 (`AGENTS.md`), version 1.0, with every S section they hold |
| Depth in Scope Record | BUS-01 D, ENG-09 D. S sections: SP-00, SP-10, SP-11, SP-12, BUS-02, BUS-03, BUS-04, BUS-05, BUS-06, BUS-09, ENG-02 (in BUS-01); ENG-01, ENG-03 to ENG-08 (in ENG-09). Not in scope: SP-01, BUS-07, BUS-08, ENG-10 (SP-00 section, version 1.0) |
| Review type | Go-live package review |
| Reviewer | Expected result (training answer key) |
| Date | 2026-10-07 |
| Related documents read | All of the above |
| Linter run | `python3 tools/doclint.py package examples/review_training/stock_count_flawed --today 2026-10-07`: 7 High · 0 Medium · 0 Low |

## 2. Rubric summary

Universal (two files): 17 Pass · 3 Partial · 6 Fail · 0 Not in scope or not applicable
Artifact: 64 Pass · 5 Partial · 7 Fail · 7 Not in scope or not applicable
Critical criteria not passing: 15 (U-07 in both files, U-08 in both files, U-12 in `docs/README.md`, BUS-01.9, SP-10.2, SP-11.1, SP-11.2, SP-11.5, SP-12.3, SP-12.7, BUS-02.7, BUS-03.5, ENG-08.7)
Open findings: 9 High · 2 Medium · 0 Low (bugs and risks)

## 3. Universal rubric results

S sections are covered by their parent file's results.

### `docs/README.md` (BUS-01, with its S sections)

| ID | Criterion | Result | Evidence |
|---|---|---|---|
| U-01 | Identity | Pass | Front-matter has all twelve keys; `level: Foundation`, `depth: D`. |
| U-02 | Purpose | Pass | Purpose names the tool, its readers and the sections held. |
| U-03 | Scope | Pass | Scope sends engineering content to ENG-09. |
| U-04 | Required structure | Pass | Five standard sections present; every S section in `contains` has a `## <DOC-ID> <Title>` heading. |
| U-05 | Specificity | Partial | SM-02 Source is just "Finance" (`:189`); AC-03 says "accurate and easy to use" (`:202`). |
| U-06 | Language for its readers | Pass | Plain language throughout the business sections. |
| U-07 | Traceability | Fail | R-03 is referenced but not defined (`:261`); FR-04 is traced to no criterion (A-BUG-04). |
| U-08 | Usable for its readers | Partial | An owner reading SP-12 would believe every Must criterion passed (`:217`) and would never see LIM-02. |
| U-09 | Limitations and unknowns visible | Fail | LIM-02 is referenced in BUS-03 step 2 (`:271`) but is absent from SP-12, so it was never accepted. |
| U-10 | Ownership | Pass | Document owner and owners of benefits, measures, rules and records are named. |
| U-11 | Consistency | Fail | SP-12 counts (`:217`) contradict SP-11 (AC-11 Not run, `:210`); W-01 (`:268`) contradicts C-04 (`:262`) and its own step 4 (`:273`), which uses C-04. |
| U-12 | Acceptance readiness | Fail | `status: Accepted` (`:6`) with a change-log approval (`:353`) resting on an SP-12 that claims results that did not happen. |
| U-13 | Says it once | Pass | Engineering detail is linked to ENG-09, not copied. |

### `AGENTS.md` (ENG-09, with its S sections)

| ID | Criterion | Result | Evidence |
|---|---|---|---|
| U-01 | Identity | Pass | Front-matter complete; `application` and `level` match BUS-01. |
| U-02 | Purpose | Pass | Purpose is specific to developers and agents working on this tool. |
| U-03 | Scope | Pass | Scope sends business content to BUS-01. |
| U-04 | Required structure | Pass | Five standard sections and every listed S section present. |
| U-05 | Specificity | Pass | Exact commands, hosts, schedules and thresholds. |
| U-06 | Language for its readers | Pass | Technical language suitable for engineers; SP-01 is out of scope. |
| U-07 | Traceability | Fail | NFR-04 is defined twice (`:144–145`), so references to it are ambiguous; D-01 links no runbook (`:189`). |
| U-08 | Usable for its readers | Partial | An operator starting from the ENG-05 entry for D-01 finds `Runbook: None`, though RB-01 (`:293`) handles exactly that failure. |
| U-09 | Limitations and unknowns visible | Pass | LIM-02 is listed here (`:323`). |
| U-10 | Ownership | Pass | Owners named for dependencies, alerts, runbooks and output checks. |
| U-11 | Consistency | Fail | D-01 `Runbook: None` contradicts the triage row (`:270`) and ALR-01 (`:281`), which both route D-01 failures to RB-01. |
| U-12 | Acceptance readiness | Pass | Accepted, with the approver and date in the change log (`:330`). |
| U-13 | Says it once | Pass | Business rules and roles are referenced by ID, not restated. |

## 4. Artifact rubric results

BUS-01 and ENG-09 are at depth D (all criteria not marked Full only). Every other item is an S section, judged on its critical criteria only.

| ID | Criterion | Critical | Result | Evidence |
|---|---|---|---|---|
| BUS-01.1 | Purpose and what it does | Yes | Pass | Application at a glance. |
| BUS-01.2 | Ownership | Yes | Pass | Morgan Lee, Priya Shah and Tomás Berg, matching ENG-08 and SP-12. |
| BUS-01.3 | Users and stakeholders | No | Pass | Counters R-01, team lead R-02, finance with no access. |
| BUS-01.4 | Scope | No | Pass | In and out of scope listed. |
| BUS-01.5 | Access point | No | Pass | URL, company sign-in, request path. |
| BUS-01.6 | Impact if unavailable | Yes | Pass | Two outage lengths with the spreadsheet workaround. |
| BUS-01.7 | Package map | No | Pass | Documentation package table matches SP-00. |
| BUS-01.8 | Problem statement | No | Partial | Quantifies time and delay but not errors, so BEN-02's baseline has no support (`:42`). |
| BUS-01.9 | Benefits measured | Yes | Partial | BEN-02 baseline "18 corrections a month" has no date or period (`:49`); see A-BUG-09. |
| BUS-01.10 | What success looks like | Yes | Pass | Four observable sentences. |
| BUS-01.11 | Strategic fit | No | Pass | Stock-count policy and close timetable. |
| BUS-01.12 | Non-functional commitments | No | Partial | The recovery commitment cites NFR-04 for both RTO and RPO (`:95`), but NFR-04 is defined twice. |
| BUS-01.13 | Resources and costs | No | Pass | Names the shared platform (T8 No). |
| BUS-01.14 | Sections held here | No | Pass | Every section is headed and listed in `contains`. |
| BUS-01.15 | Options considered | No | Not in scope | Full only; BUS-01 is D. |
| BUS-01.16 | Stakeholder communication | No | Not in scope | Full only; BUS-01 is D. |
| SP-00.1 | Scores with reasons | Yes | Pass | D1–D7 each with a reason; total 7, Foundation. |
| SP-00.2 | Floor rules | Yes | Pass | "None", consistent with the scores. |
| SP-00.3 | Triggers answered | Yes | Pass | T1–T11 answered with reasons, consistent with the package. |
| SP-00.4 | Item table complete and correct | Yes | Pass | All 24 items; depths match the matrix after triggers. |
| SP-00.5 | Never-dropped minimum | Yes | Pass | All five present. |
| SP-00.7 | Approval recorded | Yes | Pass | Both owners, 2026-08-04. |
| SP-10.1 | Measures exist at the right number | Yes | Pass | Three measures: two L1 and one L4. |
| SP-10.2 | L1 measures complete | Yes | Fail | SM-02: Baseline "18 a month" with no date, Source "Finance" (`:189`). |
| SP-10.8 | L4 output checks | Yes | Pass | SM-03 links OC-01; REC-01 and REC-02 are covered. |
| SP-11.1 | Coverage | Yes | Fail | FR-04 has no criterion (A-BUG-04); FR-02 is covered only by the untestable AC-03 (A-BUG-08). |
| SP-11.2 | Well-formed Given/When/Then | Yes | Fail | AC-03 Then clause is "the sheets should be accurate and easy to use" (`:202`). |
| SP-11.4 | Verification method | Yes | Pass | Every criterion has a Method. |
| SP-11.5 | Evidence for results | Yes | Partial | AC-03 records Pass for an outcome nobody could observe (`:202`). |
| SP-12.3 | Acceptance results honest | Yes | Fail | "Must: 12 total · 12 Pass · … 0 Not run" (`:217`) while AC-11 is Not run (`:210`); status Accepted. |
| SP-12.5 | Dry-run evidence | Yes | Pass | Deploy, rollback and restore by Jun Park, 2026-09-22, with evidence. |
| SP-12.7 | Known limitations consolidated | Yes | Fail | Only LIM-01 is listed (`:235`); LIM-02 is missing. |
| SP-12.10 | Ownership after handover | Yes | Pass | All eight responsibilities named, matching BUS-01 and ENG-08. |
| SP-12.11 | Sign-off | Yes | Pass | Three owner decisions with dates. They were made on false counts, which is raised under SP-12.3. |
| BUS-02.1 | Unique IDs | Yes | Pass | C-01 to C-04. |
| BUS-02.4 | Outcome | Yes | Pass | Every capability states an outcome. |
| BUS-02.7 | Process mapping | Yes | Fail | C-04 maps to W-01, but W-01 does not map back (`:262`, `:268`). |
| BUS-03.2 | Trigger | Yes | Pass | Last working day of the month. |
| BUS-03.3 | Outcome | Yes | Pass | Checked variance file by the next working day. |
| BUS-03.4 | Roles | Yes | Pass | R-01, R-02. |
| BUS-03.5 | Capabilities used | Yes | Fail | Capabilities lists C-01 to C-03, but step 4 (`:273`) uses C-04. |
| BUS-04.2 | Permissions | Yes | Pass | Permissions matrix for both roles. |
| BUS-04.3 | Access approver | Yes | Pass | Morgan Lee for both roles. |
| BUS-04.5 | Access removal | Yes | Pass | Routine, role change and urgent removal, with timing and confirmation. |
| BUS-05.1 | Testable rules | Yes | Pass | BR-01 to BR-04 written as conditions and actions. |
| BUS-05.4 | Status definitions | Yes | Not in scope | T3 No: lifecycle dropped (SP-00 BUS-05 row). |
| BUS-05.5 | Status transitions | Yes | Not in scope | T3 No. |
| BUS-06.3 | Classification | Yes | Pass | Both records Internal. |
| BUS-06.4 | Data ownership | Yes | Pass | Morgan Lee. |
| BUS-06.7 | Notifications | Yes | Not applicable | No notifications are sent. |
| BUS-06.9 | Personal data justified | Yes | Not applicable | No Personal records. |
| BUS-09.6 | Support path | Yes | Pass | Matches the ENG-08 intake. |
| BUS-09.7 | Role alignment | Yes | Pass | Count-day steps are for R-02 and match BUS-04. |
| BUS-09.8 | Getting started | Yes | Pass | Access, sign-in and first task. |
| ENG-02.1 | Journey coverage | Yes | Pass | J-01 and J-02 cover both roles' goals. |
| ENG-02.2 | Traceability | Yes | Pass | Roles, processes, requirements and `Transitions: None`. |
| ENG-09.1 | Exact, verified commands | Yes | Pass | Eight commands, each verified with a date and name. |
| ENG-09.2 | Agent rules | Yes | Pass | May, needs-a-human (naming Tomás Berg) and never lists. |
| ENG-09.3 | Update-trigger table | Yes | Pass | Identical to the model, cites its source and states the fail rule. |
| ENG-09.4 | What the application is | No | Pass | One paragraph with a link to BUS-01. |
| ENG-09.5 | Repository map and prerequisites | No | Pass | Map and versioned prerequisites. |
| ENG-09.6 | Conventions with examples | No | Pass | Four rules, each with an exemplar file. ENG-10 is out of scope. |
| ENG-09.7 | Safe change and definition of done | No | Pass | Five steps and a definition of done. |
| ENG-09.8 | Where to find things | No | Pass | Table of in-scope documents. |
| ENG-09.9 | Placement and held sections | No | Pass | Root `AGENTS.md` holds ENG-01 and ENG-03 to ENG-08. |
| ENG-01.2 | Traces to capability | Yes | Pass | Every FR lists a capability and its rule. |
| ENG-01.4 | Measurable NFR targets | Yes | Pass | Every target has a number and unit. The duplicate ID is raised under X-25. |
| ENG-03.1 | Context view | Yes | Pass | Mermaid context diagram includes D-01 and D-02. |
| ENG-03.2 | Containers and stack | Yes | Pass | CMP-01 to CMP-03 with technology and responsibility. |
| ENG-03.7 | Security section | Yes | Not in scope | T4 and T11 No; the one-line statement is present. |
| ENG-04.1 | Records mapped to entities | Yes | Pass | ENT-01 to ENT-03 map to REC-01 and REC-02. |
| ENG-04.2 | Classification and retention | Yes | Pass | Internal, with retention enforced by CMP-02. |
| ENG-05.3 | Owner | Yes | Pass | D-01 to D-03 owned. |
| ENG-05.4 | Impact | Yes | Pass | Business impact stated for each. |
| ENG-05.6 | Support path | Yes | Pass | Service desk queues. |
| ENG-06.1 | Environments | Yes | Pass | ENV-01 and ENV-02. |
| ENG-06.2 | Secrets by location only | Yes | Pass | SEC-01 and SEC-02 by location. |
| ENG-07.2 | Deployment steps with verification | Yes | Pass | Five steps and a smoke test. |
| ENG-07.3 | Rollback | Yes | Pass | Criteria, decider, steps (no database step needed) and verification. |
| ENG-08.1 | Support ownership | Yes | Pass | Three areas with named primary, backup and escalation owners. |
| ENG-08.4 | Escalation | Yes | Pass | Concrete escalation conditions per category. |
| ENG-08.7 | Dependency checks | Yes | Partial | Triage maps the D-01 symptom to RB-01 (`:270`), but the D-01 dependency entry names no runbook (`:189`). |
| ENG-08.14 | Backup and restore | Yes | Pass | Nightly, 30 days, where, restore steps, last test 2026-09-22. |

## 5. Cross-document rules

Mechanical results are copied from the linter.

| Rule | Type | Result | Evidence |
|---|---|---|---|
| X-01 | Mechanical | Pass | Linter |
| X-02 | Mechanical | Fail | Linter: `docs/README.md:262` C-04 lists W-01, but W-01 does not list C-04 in Capabilities. |
| X-03 | Mechanical | Fail | Linter: `docs/README.md:261` R-03 is referenced but not defined. |
| X-04 | Mechanical | Pass | Linter |
| X-05 | Mechanical | Not in scope | T3 No |
| X-06 | Mechanical | Pass | Linter |
| X-07 | Mechanical | Pass | Linter |
| X-08 | Mechanical | Pass | Linter (no notifications) |
| X-09 | Mechanical | Pass | Linter |
| X-10 | Judgment | Pass | The triage guide's four categories each have an owner and a concrete escalation condition. |
| X-11 | Mechanical | Not in scope | BUS-08 is — |
| X-12 | Mechanical | Fail | Linter: `docs/README.md:271` LIM-02 is not in SP-12's consolidated table. |
| X-13 | Mechanical | Not in scope | SP-01 is — |
| X-14 | Mechanical and Judgment | Pass | Front-matter matches; access point and owners agree across BUS-01, ENG-06, ENG-08 and SP-12. |
| X-15 | Mechanical | Pass | Linter |
| X-16 | Mechanical | Pass | Linter |
| X-17 | Mechanical | Pass | Linter |
| X-18 | Mechanical | Pass | Linter |
| X-19 | Mechanical | Fail | Linter: `AGENTS.md:135` FR-04 is not in any Verifies column. |
| X-20 | Mechanical | Pass | Linter |
| X-21 | Mechanical | Fail | Linter: `AGENTS.md:189` D-01 lists no runbook entry. |
| X-22 | Mechanical | Pass | Linter. Mechanically, SM-02's columns are filled; their quality fails SP-10.2 (A-BUG-09). |
| X-23 | Mechanical | Pass | Linter |
| X-24 | Mechanical | Not in scope | BUS-07 is — (T8 No) |
| X-25 | Mechanical | Fail | Linter: `AGENTS.md:145` NFR-04 is defined twice. |
| X-26 | Mechanical | Fail | Linter: `docs/README.md:210` SP-12 is Accepted but Must criterion AC-11 is Not run. |
| X-27 | Mechanical | Pass | Linter |
| X-28 | Mechanical | Pass | Linter (last reviewed 2026-09-30) |
| X-29 | Judgment | Pass | D-01 is in the context view; CMP-03 maps to ENT-01 to ENT-03; the journeys match the flow. |
| X-30 | Judgment | Fail | AC-03 is not observable or binary (`docs/README.md:202`). |

## 6. Findings

Severity definitions: [decision rules §4](../../rubrics/04_decision_rules.md#4-severity).

### Bugs

| ID | Finding | Severity | Evidence | Required action |
|---|---|---|---|---|
| A-BUG-01 | Capability↔process link is one-sided: the variance export is not part of the monthly count process. | High | Linter X-02; `docs/README.md:262` C-04 Processes `W-01`; `:268` W-01 Capabilities `C-01, C-02, C-03`; step 4 (`:273`) uses C-04. | Add C-04 to W-01 Capabilities. |
| A-BUG-02 | Undefined role R-03 can record counted quantities. A reader cannot tell who may enter counts. | High | Linter X-03; `docs/README.md:261` C-03 Roles `R-02, R-03`; BUS-04 defines only R-01 and R-02. | Remove R-03, or define it in BUS-04 with its approver and permissions. |
| A-BUG-03 | Known limitation LIM-02 is hidden from handover, so nobody has accepted it. | High | Linter X-12; defined at `AGENTS.md:323` and referenced at `docs/README.md:271`; SP-12 consolidated table (`:231–235`) lists only LIM-01. | Add LIM-02 to SP-12 and have Morgan Lee accept it or raise a condition. |
| A-BUG-04 | Must requirement FR-04 (variance export) has no acceptance criterion, so the output finance relies on was never accepted against a requirement. | High | Linter X-19; `AGENTS.md:135` FR-04 Priority Must; `docs/README.md:206` AC-07 Verifies `J-02` only. | Add FR-04 to AC-07 Verifies (and BR-04 criteria as needed). |
| A-BUG-05 | High dependency D-01 names no runbook entry. | High | Linter X-21; `AGENTS.md:189` D-01 Criticality High, Runbook `None`; RB-01 (`:293`) covers D-01. | Set D-01 Runbook to RB-01. |
| A-BUG-06 | NFR-04 is defined twice, for RTO and RPO. The RPO has no ID of its own, so it cannot be traced or shown verified. | High | Linter X-25; `AGENTS.md:144` and `:145`; AC-12 Verifies `NFR-04` (`docs/README.md:211`). | Give the RPO a new ID (never reuse one) and add it to AC-12 Verifies and the BUS-01 commitments. |
| A-BUG-07 | SP-12 claims acceptance and test results that did not happen: it is Accepted and reports 12 of 12 Must criteria passed while AC-11 is Not run. | High | Linter X-26; `docs/README.md:6` status Accepted; `:210` AC-11 Result `Not run`, no evidence; `:217` "12 Pass … 0 Not run". | Run AC-11 and record its result with evidence, or have an owner waive it with name and date. Correct the counts. Set the status back until then. |
| A-BUG-08 | AC-03 cannot be judged Pass or Fail by a third party, yet it records Pass. FR-02 and J-01 are verified only by it, and the blind-count rule BR-02 only negatively (AC-04). | High | `docs/README.md:202` "then the sheets should be accurate and easy to use"; SP-11 writing rule 4 forbids "correct" and similar words. | Rewrite with observable outcomes (one sheet per location, columns shown, no system quantity) and re-run. |
| A-BUG-09 | L1 baseline for SM-02 has no date, period or usable source, and nothing else in the package supports it. Per conventions §9 a baseline is never invented. | High | `docs/README.md:189` Source `Finance`, Baseline `18 a month`; BEN-02 repeats it (`:49`); the problem statement gives no error figure (`:42`); SP-12 says only "baselines captured" (`:229`). | Cite the data source and period it was measured over, or write "Not measured – capture by <date>" with an owner. If it cannot be sourced, it was invented, and decision rules §8 then make SP-10 a Reject. |

### Risks

| ID | Finding | Severity | Evidence | Mitigation or required action |
|---|---|---|---|---|
| A-RISK-01 | Picking on count morning could put false variances into the file finance adjusts stock from. The control for this (no picking until a location is counted) depends on an unaccepted limitation. | Medium | LIM-02 (`AGENTS.md:323`); BUS-03 step 2 (`docs/README.md:271`); not in SP-12. | Covered by A-BUG-03; the owner accepts LIM-02 and the picking rule explicitly. |
| A-RISK-02 | Sheet generation speed on count day is unverified (NFR-02). A slow print would delay the count. | Medium | AC-11 Not run (`docs/README.md:210`). The workaround is the old spreadsheet method (BUS-01 Impact if unavailable). | Run AC-11 before the first live count on 2026-10-30. |

### Ideas

| ID | Finding | Value | Evidence | Suggested action |
|---|---|---|---|---|
| A-IDEA-01 | Have the SP-11 counts in SP-12 generated rather than typed, so they cannot drift from the register. | Medium | Defect A-BUG-07 came from hand-copied counts (`docs/README.md:217`). | Add a small script, or have the linter print the counts. |

## 7. Required fixes

| Finding | Fix | Owner |
|---|---|---|
| A-BUG-01 | Add C-04 to W-01 Capabilities | Tomás Berg (producer), Morgan Lee to confirm |
| A-BUG-02 | Remove or define R-03 | Morgan Lee |
| A-BUG-03 | Add LIM-02 to SP-12 and record its acceptance | Morgan Lee |
| A-BUG-04 | Add FR-04 to an AC's Verifies | Tomás Berg |
| A-BUG-05 | Set D-01 Runbook to RB-01 | Tomás Berg |
| A-BUG-06 | New ID for the RPO; update AC-12 and BUS-01 | Tomás Berg |
| A-BUG-07 | Run or waive AC-11; correct the SP-12 counts and status | Priya Shah (run), Morgan Lee (decision) |
| A-BUG-08 | Rewrite and re-run AC-03 | Priya Shah |
| A-BUG-09 | Source the SM-02 baseline or mark it Not measured with a capture date | Morgan Lee |

## 8. Proposed conditions

None. Every open bug is High, so no document can be accepted with conditions.

## 9. Decision

### Document decisions

| Document | Decision | Decision rule applied |
|---|---|---|
| BUS-01 (`docs/README.md`) | Reject | §5 Reject: the file claims Accepted on the strength of SP-12, which claims test results without evidence (A-BUG-07), and it hides LIM-02 from handover (A-BUG-03). |
| SP-00 | Accept | All critical criteria Pass; no findings. |
| SP-10 | Revise and Resubmit | Critical SP-10.2 Fail; open High A-BUG-09. It becomes Reject if the baseline turns out to be invented (§8). |
| SP-11 | Revise and Resubmit | Critical SP-11.1 and SP-11.2 Fail; open High A-BUG-04 and A-BUG-08. |
| SP-12 | Reject | §5 Reject: claims acceptance and test results without evidence (A-BUG-07); hides a known limitation (A-BUG-03). |
| BUS-02 | Revise and Resubmit | Critical BUS-02.7 Fail; open High A-BUG-01 and A-BUG-02. |
| BUS-03 | Revise and Resubmit | Critical BUS-03.5 Fail; open High A-BUG-01. |
| BUS-04, BUS-05, BUS-06, BUS-09, ENG-02 | Accept | Applicable critical criteria Pass; no findings. |
| ENG-09 (`AGENTS.md`) | Revise and Resubmit | Critical U-07 Fail; open High A-BUG-05 and A-BUG-06 in its held sections. |
| ENG-01 | Revise and Resubmit | Open High A-BUG-06. |
| ENG-05 | Revise and Resubmit | Open High A-BUG-05. |
| ENG-08 | Revise and Resubmit | Critical ENG-08.7 Partial with no agreed condition (rests on A-BUG-05). |
| ENG-03, ENG-04, ENG-06, ENG-07 | Accept | Applicable critical criteria Pass; no findings. |

### Gate results

| Gate | Result | Why |
|---|---|---|
| G1 Completeness | Fail | X-25 failed (High). The Scope Record approval check passes. |
| G2 Business understanding | Fail | BUS-01 is Reject. X-24 is not in scope; "What success looks like" is present. |
| G3 Capability and journey traceability | Fail | X-02 and X-03 failed (High); BUS-02, BUS-03 and ENG-01 are Revise and Resubmit. |
| G4 Governance and control | Pass | X-06, X-07, X-08 and X-17 pass; X-11 and X-13 are not in scope; BUS-04, BUS-05 and BUS-06 are Accept. |
| G5 Engineering readiness | Fail | ENG-05 and ENG-09 are Revise and Resubmit. X-20 and X-29 pass. |
| G6 Operational readiness | Fail | X-21 failed (High); ENG-08 is Revise and Resubmit. The dry-run check passes (SP-12 Dry-run evidence). |
| G7 Success measurability | Fail | X-19 and X-30 failed (High); SP-10 and SP-11 are Revise and Resubmit. |
| G8 Handover | Fail | X-12 and X-26 failed (High); SP-12 is Reject. Owner decisions are recorded but were made on false counts. |

Decision: **Revise and Resubmit**

Decision rule applied: §6 Package decision, row "Revise and Resubmit". Seven gates are Fail, and rules in G1 (X-25), G3 (X-02, X-03) and G8 (X-12, X-26) have failed.

Next action: Tomás Berg fixes A-BUG-01 to A-BUG-06. Priya Shah re-runs AC-03 and AC-11 and records the results. Morgan Lee sources or withdraws the SM-02 baseline and accepts LIM-02. SP-12 status returns to Draft until the three owners decide again on correct counts. Then the package is re-linted and re-reviewed.

## 10. Framework feedback (optional, never affects the decision)

- How a finding in an S section affects the parent file's document decision is not stated. This result treats open bugs in held sections as open against the parent file as well. That is why BUS-01 is Reject and ENG-09 is Revise and Resubmit.
- X-22 passes mechanically for any non-empty Baseline and Source. Adding a check that an L1 Baseline contains a date, or "Not measured", would let the linter catch defect 9.
