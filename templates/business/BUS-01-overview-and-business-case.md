---
id: BUS-01
title: Application Overview & Business Case
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Management, Business owner, Support, Engineering, Agents, Everyone]
level: <Foundation | Standard | Full>
depth: <D | D+>
contains: []        # at Foundation, the S items held here, e.g. [SP-00, SP-10, SP-11, SP-12, BUS-02, BUS-03, BUS-05, BUS-06, BUS-07, BUS-09]
related: [SP-00, SP-10, BUS-02, BUS-07, BUS-08, ENG-01, ENG-08, SP-12]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Application Overview & Business Case

> **How to use this template**
> - **Who writes it:** the producer, from interviews with the business owner and support owner and from project briefs. The business owner approves it. Keep it short enough for a manager to read first; link to the detailed documents rather than repeating them.
> - **When it is due:** Draft and Accepted at stage 1 (Initiate), including the business case. Update it when benefits, owners or scope change.
> - **BUS-01 is never a section.** At Foundation it is a brief document (`docs/README.md` is allowed) that also holds the S sections of other items; see "Sections held here at Foundation".
> - **Depth D (Foundation and Standard):** everything except sections marked (Full). At Foundation, keep each section to a few lines.
> - **Depth D+ (Full):** everything, including sections marked (Full).
> - "What success looks like" is never dropped, at any level.
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

The first document anyone reads about <Application>. It explains what the application is, why it exists, what it is worth, what success looks like, and who owns and supports it.

## Scope

Covers the identity, business case, success statement, ownership and scope of <Application>, and a map of the documentation package. Details live in the linked documents: capabilities in BUS-02, costs in BUS-07, risks in BUS-08, success measures in SP-10, requirements in ENG-01, support in ENG-08.

## Application at a glance

> **Guide:** two or three sentences on what the application does, in business verbs, then the access point. A manager should know what it is after reading this paragraph.
> Prefer: "Guests submit room booking requests online; booking staff review, confirm or return them; managers see weekly occupancy." Avoid: "A web portal with a form and an admin page."

<What the application does, for whom, in two or three sentences.>

| Item | Value |
|---|---|
| Access point | <URL or entry point> |
| Access method | <Single sign-on / account / public> |
| How to get access | <Request path, or link to BUS-04> |
| Hours of use | <…> |

## Problem statement

> **Guide:** the situation today, who is affected, and what it costs, in numbers where possible (time, money, errors, risk). Unknown costs are `TBD` with an owner and a `Q-xx`.
> Prefer: "Requests arrive by email; staff re-key about 40 a week, taking 3 working days on average to answer." Avoid: "The current process is inefficient."

| Item | Description |
|---|---|
| Current situation | <…> |
| Who is affected | <…> |
| Cost today | <time, money, errors or risk, with numbers> |

## Benefits

> **Guide:** one row per benefit the application should deliver. Each names at least one L1 success measure from SP-10 in `Measure`; that measure holds the definition, source and owner. Baseline and target here must match SP-10.

| ID | Benefit | Beneficiary | Measure | Baseline | Target | By when | Benefit owner |
|---|---|---|---|---|---|---|---|
| BEN-01 | <…> | <…> | <SM-xx> | <value, or Not measured – capture by YYYY-MM-DD> | <…> | <YYYY-MM-DD> | <Name, role> |

## What success looks like

> **Guide:** three to five plain sentences describing the world once the application works, for the business reader. Make each sentence observable and consistent with the benefits above; no technology words.
> Example: "Every booking request gets a decision within one working day. Staff no longer re-key requests from email. Management sees occupancy weekly without manual spreadsheets."

<Three to five sentences.>

## Impact if unavailable

> **Guide:** what stops, who is affected, how fast it hurts, and the manual workaround. This feeds the availability NFRs in ENG-01 and the recovery targets in ENG-08.

| Outage length | Impact | Workaround |
|---|---|---|
| <Up to 4 hours> | <…> | <… or None> |
| <More than 1 working day> | <…> | <… or None> |

## Strategic fit

> **Guide:** the business objective, plan or policy this application supports, in one or two sentences, with a reference.

<…>

## Users and stakeholders

> **Guide:** the main user groups and other stakeholders and what each needs from the application. Roles are defined in BUS-04; refer to them by role ID.
> When T2 is No (one role), there is no BUS-04: define the single role here instead, in a table whose first column is `ID`, with one row `R-01`.

| Stakeholder | Description | Main interest | Role |
|---|---|---|---|
| <…> | <…> | <…> | <R-xx or None> |

<!-- Only when T2 is No: -->
| ID | Name | Who has access | Access approver |
|---|---|---|---|
| R-01 | <Role name> | <…> | <Name, role> |

## Ownership

> **Guide:** named people, not only teams. These names must match ENG-08 and SP-12.

| Responsibility | Name and role | Team | Contact |
|---|---|---|---|
| Business owner | <…> | <…> | <…> |
| Support owner | <…> | <…> | <…> |
| Technical owner | <…> | <…> | <…> |

## In scope and out of scope

> **Guide:** list what the application does and, just as important, what people might expect it to do but it does not. Use capability names from BUS-02.

**In scope:**
- <…>

**Out of scope:**
- <…>

## Key non-functional commitments

> **Guide:** the three to six commitments a business reader cares about, in plain words, each linked to its NFR in ENG-01.
> Prefer: "Available Monday to Friday 08:00–18:00, 99.5% of the time (NFR-01)." Avoid: "High availability."

| Commitment | Requirement |
|---|---|
| <…> | <NFR-xx> |

## Resources and costs summary

> **Guide:** one paragraph: the people and effort it ties up, the main running costs per year, and the budget holder, linking BUS-07 for detail. When T8 is No, one line naming the shared platform it runs on and who funds it.

<…>

## Documentation package

> **Guide:** copy the depth of every item in scope from SP-00, so a reader knows where to look. Do not list items marked —.

| Document | Depth | Where |
|---|---|---|
| <DOC-ID Title> | <S / D / D+> | <file name, or section in this file> |

## Sections held here at Foundation

> **Guide:** at Foundation level, BUS-01 holds the S sections of the spine and business items the Scope Record places here. Each is a level-2 heading `## <DOC-ID> <Title>`, uses its own template's core tables cut down to what answers the question, and has no front-matter or standard sections of its own (this file's apply). Use level-3 headings inside a section. List every section's ID under `contains` in the front-matter. Place them after this section and before "Assumptions and open questions". Delete this guide section and keep only the S sections. An illustrative skeleton:
>
> ```markdown
> ## SP-00 Scope Record
> | Dimension | Score (0–3) | Reason |  … scores, level, floor rules
> | Trigger | Question | Answer | Reason |  … T1–T11
> | Item | Depth | Parent | Reason |  … all 24 items
> | Role | Name | Decision | Date |  … business owner, technical owner
>
> ## SP-10 Success Measures Register
> | ID | Level | Measure | Definition | Source | Baseline | Target | Threshold for action | Frequency | Owner | Links |
> (1–3 measures: at least one L1; one L4 if T6 is Yes)
>
> ## SP-11 Acceptance Criteria & Verification Register
> | ID | Verifies | Criterion | Type | Method | Evidence | Priority | Result | Verified by | Date | Approver |
> (every Must feature)
>
> ## SP-12 Acceptance & Handover Record
> Sign-off checklist: acceptance results, dry-run evidence, consolidated known limitations, support ownership, final decisions
>
> ## BUS-02 Capabilities Register
> | ID | Name | Outcome | Roles | Processes | Dependencies | Automated | Criticality |
>
> ## BUS-03 Business Process Register
> | ID | Name | Trigger | Outcome | Roles | Capabilities | Statuses | Journeys |
>
> ## BUS-05 Business Rules & Status Lifecycle
> Rules, statuses and transitions tables, a few rows each
>
> ## BUS-06 Data, Reports & Notifications Register
> Records table; one line each for reports and notifications if few
>
> ## BUS-07 Resource & Cost Model
> A few cost lines and the yearly total, or one line naming the shared platform
>
> ## BUS-09 User & Admin Guide
> Quick start: get access, first task, where to get help
> ```

## Options considered (Full)

> **Guide:** the alternatives that were weighed (do nothing, buy, build, extend an existing system), with cost, benefit and the reason this option was chosen. Link ENG-10 for technical decisions.

| Option | Summary | Cost | Benefit | Why chosen or rejected |
|---|---|---|---|---|
| <Do nothing> | <…> | <…> | <…> | <…> |

## Stakeholder communication (Full)

> **Guide:** who needs to hear about changes, outages and benefit results, how and how often.

| Stakeholder | What they need to know | Channel | Frequency | Owner |
|---|---|---|---|---|
| <…> | <…> | <…> | <…> | <Name, role> |

## Assumptions and open questions

> **Guide:** IDs are unique across the whole package. Continue numbering from the last `Q-xx` used in any document.

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | <…> | <…> | <YYYY-MM-DD> | <Open / Closed> |

## Known limitations

> **Guide:** at Foundation, when BUS-08 is not in scope, this is where the application's main limitations and risks are listed. Every `LIM-xx` also goes into SP-12. Write "No known limitations." if there are none.

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | <…> | <…> | <… or None> | <…> |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | <YYYY-MM-DD> | <Name> | First draft | — |
