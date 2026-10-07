---
id: SP-11
title: Acceptance Criteria & Verification Register
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Business owner, Testers, Operators, Engineering, Agents]
level: <Foundation | Standard | Full>
depth: <D | D+>
contains: []
related: [ENG-01, ENG-02, BUS-05, SP-10, SP-12]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Acceptance Criteria & Verification Register

> **How to use this template**
> - **Who writes it:** the producer with the business owner (who approves the criteria) and testers. Engineers and agents link each criterion to its automated test. Results are filled in by whoever ran the verification, never by the author on their behalf.
> - **When it is due:** criteria for Must requirements Draft at stage 2 (Define); results and evidence filled in and Accepted at stage 4 (Verify).
> - **Depth S (Foundation):** a section `## SP-11 Acceptance Criteria & Verification Register` in BUS-01 holding the Application acceptance criteria table for every Must feature (and every transition when T3 is Yes), each with a method and result. Skip the summary and the (Full) sections.
> - **Depth D (Standard):** everything except sections marked (Full), with full coverage (see Coverage rule).
> - **Depth D+ (Full):** everything, including sections marked (Full).
> - These are **application acceptance criteria**: they judge whether the application and its output are right. They are not documentation review criteria.
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

Holds the application acceptance criteria for <Application>: testable Given/When/Then statements of correct behaviour, how each is verified, and the result. It lets a business owner, tester or operator decide objectively whether the application does the right thing, without asking the author.

## Scope

Covers every application acceptance criterion (`AC-xx`) and its verification. The requirements are in ENG-01, journeys in ENG-02, business rules and transitions in BUS-05; tests (`T-xx`) live in the code repository and are referenced here. The L2 measures in SP-10 are computed from this register, and SP-12 summarises its results at handover.

## Coverage rule

> **Guide:** the register is complete when:
> - every **Must** functional requirement (`FR`) has at least one criterion;
> - every non-functional requirement (`NFR`) has at least one criterion that measures its target;
> - every business rule (`BR`) and every status transition (`TR`) has at least **one positive** criterion (the rule allows or the transition happens) and **one negative** criterion (the rule blocks or the transition is refused);
> - every journey (`J`) that is the main path of a Must feature has an end-to-end criterion.
> Should and Could requirements get criteria when they are in the release. The linter checks coverage through the `Verifies` column.

## Application acceptance criteria

> **Guide:**
> - **Verifies:** the IDs this criterion proves: `FR`, `NFR`, `BR`, `J` or `TR`.
> - **Criterion:** one Given/When/Then statement (rules below).
> - **Type:** Functional / Non-functional / Data / Security / Usability / Operational.
> - **Method:** Automated test / Manual test / Inspection / Demonstration / Measurement.
> - **Evidence:** the test ID (`T-xx`), test file path, script, or a link to the evidence (run log, screenshot set, measurement report). Required for every result other than Not run.
> - **Priority:** Must / Should / Could, inherited from the requirement it verifies (a BR or TR criterion is Must unless the owner says otherwise).
> - **Result:** Not run / Pass / Fail / Waived. Record only what actually happened.
> - **Approver:** for a Waived result, the owner who waived it, with the reason in this row or in SP-12. Leave empty otherwise.

| ID | Verifies | Criterion | Type | Method | Evidence | Priority | Result | Verified by | Date | Approver |
|---|---|---|---|---|---|---|---|---|---|---|
| AC-01 | <FR-xx, NFR-xx, BR-xx, J-xx, TR-xx> | Given <starting state and actor>, when <action>, then <observable outcome>. | <Functional / Non-functional / Data / Security / Usability / Operational> | <Automated test / Manual test / Inspection / Demonstration / Measurement> | <T-xx, path or link> | <Must / Should / Could> | Not run | <Name> | <YYYY-MM-DD> | <Name, role, if Waived> |

## Writing rules

> **Guide:** a criterion is well formed when a third party can say Pass or Fail without asking the author.
> 1. **Given** states the starting state: the record and its status (by name and `ST` ID), relevant data, and the actor by role ID.
> 2. **When** states one action by that actor, or one event (a scheduled job runs, a date passes).
> 3. **Then** states what can be observed: the resulting status, the message shown (exact wording), the record or notification created, the number measured.
> 4. **Concrete values:** dates, amounts, counts, times with units. Never "fast", "easy", "correct", "appropriate".
> 5. **One behaviour per criterion.** If you need "and also", write a second criterion.
> 6. **No implementation detail** (button colours, table names, API paths) unless that detail is the requirement.
> 7. **Negative criteria** say what must not happen and what the user sees instead, and that the state is unchanged.
> Prefer: "Then the status remains Submitted and the message 'Room 12 is not available on 4 May' is shown." Avoid: "Then the system handles the conflict correctly."

> **Guide: worked example (generic room booking).** A pair of criteria for one rule and one transition:
>
> **Positive** – Verifies the rule "a room cannot be confirmed for dates it is already confirmed for" and the transition Submitted → Confirmed.
> Given a booking request in status *Submitted* for room 12 on 3–5 May, and no other booking for room 12 *Confirmed* on any of those dates,
> When a user with the booking staff role selects Confirm,
> Then the status changes to *Confirmed*, and a confirmation notification to the requester is logged within 5 minutes.
> Method: Automated test, evidence: the test ID and path.
>
> **Negative** – Verifies the same rule and transition.
> Given a booking request in status *Submitted* for room 12 on 3–5 May, and room 12 already *Confirmed* for 4 May for another booking,
> When a user with the booking staff role selects Confirm,
> Then confirmation is blocked, the message "Room 12 is not available on 4 May" is shown, and the status remains *Submitted*.
> Method: Automated test.
>
> **Non-functional** – Verifies a performance requirement.
> Given 50 concurrent signed-in users and 10,000 booking records in the test environment,
> When each user opens the booking queue once a minute for 30 minutes,
> Then the 95th-percentile page load time is ≤ 2 s.
> Method: Measurement, evidence: the load-test report link.
>
> In the register, write the IDs in `Verifies` and the role, status and record IDs in the criterion, for example "Given REC-01 in ST-02 Submitted…, when a user with R-02 selects Confirm…".

## Criterion details

> **Guide:** optional. When a criterion needs test data, preconditions or several observable outcomes that do not fit in one cell, add a `### AC-xx` subsection here with the detail. Do not define new IDs here; the register row is the definition. Write "No additional details." if none are needed.

## Results summary

> **Guide:** recompute after every verification run. Counts must match the register. Every Must criterion that is Fail or Not run is listed in SP-12, and SP-12 cannot be Accepted while one remains without a waiver.

| Priority | Total | Pass | Fail | Waived | Not run |
|---|---|---|---|---|---|
| Must | <n> | <n> | <n> | <n> | <n> |
| Should | <n> | <n> | <n> | <n> | <n> |
| Could | <n> | <n> | <n> | <n> | <n> |

**Last verification run:** <YYYY-MM-DD>, environment <ENV-xx>, run by <Name, role>.

**Failed and waived Must criteria:**

| Criterion | Result | Reason | Defect or waiver reference | Owner |
|---|---|---|---|---|
| <AC-xx> | <Fail / Waived> | <…> | <…> | <Name, role> |

## Traceability matrix (Full)

> **Guide:** one row per requirement, rule, transition and Must journey, showing which criteria verify it and the combined result. Any row with no criterion is a coverage gap to fix before review. Generate it from the register where possible rather than maintaining it by hand.

| Verified item | Priority | Criteria | Combined result |
|---|---|---|---|
| <FR-xx / NFR-xx / BR-xx / TR-xx / J-xx> | <Must / Should / Could> | <AC-xx, AC-yy> | <Pass / Fail / Partly run / Not run> |

## Re-verification after go-live (Full)

> **Guide:** say which criteria run automatically on every change (regression suite), which are re-run manually and when (each release, quarterly), and who owns the regression suite.

| Criteria | When re-run | How | Owner |
|---|---|---|---|
| <All automated AC> | <Every merge to main> | <CI pipeline> | <Name, role> |

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | <…> | <…> | <YYYY-MM-DD> | <Open / Closed> |

## Known limitations

> **Guide:** for example, a criterion that can only be verified in production. Every `LIM-xx` also goes into SP-12. Write "No known limitations." if there are none.

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | <…> | <…> | <… or None> | <…> |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | <YYYY-MM-DD> | <Name> | First draft | — |
