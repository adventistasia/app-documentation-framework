---
id: SP-00
title: Scope Record
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Business owner, Technical owner, Reviewers, Agents]
level: <Foundation | Standard | Full>   # the level this record decides
depth: D                                # SP-00 is D at Standard and Full; at Foundation it is a section in BUS-01
contains: []
related: [BUS-01, ENG-09, SP-12]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Scope Record

> **How to use this template**
> - **Who writes it:** the business owner and technical owner together, in one short session, or the scoping agent drafts it and the owners correct it. Follow the framework's scoping guide; this template only records the result.
> - **When it is due:** Draft and Accepted at stage 1 (Initiate), before any other document is accepted. Re-score at every stage gate and whenever an update trigger adds a role, integration, data type or user group.
> - **Depth S (Foundation):** a section `## SP-00 Scope Record` in BUS-01 (`docs/README.md`) holding the Scores, Triggers, Items and Approval tables. Drop the standard sections; BUS-01's apply.
> - **Depth D (Standard and Full):** everything below. SP-00 has no sections marked (Full).
> - Keep the `Trigger` and `Item` tables exactly as laid out: the linter reads them by their headers and checks that every one of the 24 document IDs is listed.
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

This record states which documents <Application> produces, at what depth, and why. It is the contract the documentation package is reviewed against: reviewers judge the package against this record, not against the full standard.

## Scope

Covers the scoring, triggers, depth of every item, deviations from the depth matrix, owner approval and later re-scoping. It does not describe the application; BUS-01 does.

## Scores

> **Guide:** score each dimension 0–3 by picking the description in the scoping guide that best fits, and give a one-line reason that a second scorer could check. The reason matters more than the number.
> Prefer: "2 – personal data of guests (name, email, phone)". Avoid: "2 – some data".

| Dimension | Score (0–3) | Reason |
|---|---|---|
| D1 Users and reach | <0–3> | <who uses it, how many, internal or external> |
| D2 Impact if down or wrong | <0–3> | <what stops or goes wrong> |
| D3 Data sensitivity | <0–3> | <the most sensitive data it holds> |
| D4 Integrations | <0–3> | <the systems it exchanges data with> |
| D5 Process and rule complexity | <0–3> | <roles, statuses, approvals, calculations> |
| D6 Team and lifespan | <0–3> | <who maintains it, for how long, handover or agents> |
| D7 Regulatory and audit exposure | <0–3> | <policy, audit, contract or regulation that applies> |
| **Total** | <0–21> | 0–7 Foundation · 8–15 Standard · 16–21 Full |

**Level from total:** <Foundation | Standard | Full>

## Floor rules applied

> **Guide:** apply after totalling. Write "None" if no rule applies. The final level is the higher of the total's level and any floor rule's level.

| Floor rule | Applies | Effect |
|---|---|---|
| F1 A 3 on D2, D3 or D7 sets the level to at least Standard | <Yes / No> | <…> |
| F2 A 3 on two or more of D2, D3 and D7 sets the level to Full | <Yes / No> | <…> |
| F3 A 2 or more on D6 makes ENG-09 depth D at any level | <Yes / No> | <…> |

**Final level:** <Foundation | Standard | Full> (must equal `level` in the front-matter of every document)

## Triggers

> **Guide:** answer every trigger Yes or No with a one-line reason. A Yes adds the item at least at depth S, even at Foundation. A No removes the item, or the part named, and records the one-line replacement from the scoping guide in the item's Reason.

| Trigger | Question | Answer | Reason |
|---|---|---|---|
| T1 | Do people use it through a screen (not only through an API or a job)? | <Yes / No> | <…> |
| T2 | Is there more than one role or permission level? | <Yes / No> | <…> |
| T3 | Do records move through statuses or approvals? | <Yes / No> | <…> |
| T4 | Does it store personal or confidential data? | <Yes / No> | <…> |
| T5 | Does it exchange data with other systems? | <Yes / No> | <…> |
| T6 | Does it produce outputs others rely on (reports, exports, calculations, notifications)? | <Yes / No> | <…> |
| T7 | Does it run scheduled or background jobs? | <Yes / No> | <…> |
| T8 | Does it cost anything beyond an existing shared platform (licences, hosting, staff time)? | <Yes / No> | <…> |
| T9 | Does a non-technical person own it or approve its results? | <Yes / No> | <…> |
| T10 | Will a different team or AI agents build or maintain it? | <Yes / No> | <…> |
| T11 | Is it public-facing? | <Yes / No> | <…> |

## Items

> **Guide:** for every item, read the depth for the final level from the scoping guide's depth matrix, then apply the triggers.
> - **Depth** is one of `—` (not needed), `S` (section in a parent), `D` (own file) or `D+` (own file with the template's (Full) sections).
> - **Parent** is filled only for S items: BUS-01 for spine and business items, ENG-09 for engineering items, BUS-03 for ENG-02 (BUS-01 when BUS-03 is itself S). Write `—` otherwise.
> - **Reason** is required for every `—` (for example "T2 No: single role R-01 recorded in BUS-01") and for any depth that differs from the matrix (also record it under Deviations). For other rows, "Matrix" is enough.
> - Never set these to `—`: BUS-01 (holds What success looks like), SP-10 (at least one measure), SP-11 (criteria for every Must feature), ENG-07 (how to run and deploy, or its section in ENG-09), ENG-08 (who supports it, or its section).

| Item | Depth | Parent | Reason |
|---|---|---|---|
| SP-00 Scope Record | <S / D> | <BUS-01 if S> | <…> |
| SP-01 Glossary | <— / S / D> | <BUS-01 if S> | <…> |
| SP-10 Success Measures Register | <S / D / D+> | <BUS-01 if S> | <…> |
| SP-11 Acceptance Criteria & Verification Register | <S / D / D+> | <BUS-01 if S> | <…> |
| SP-12 Acceptance & Handover Record | <S / D / D+> | <BUS-01 if S> | <…> |
| BUS-01 Application Overview & Business Case | <D / D+> | — | <…> |
| BUS-02 Capabilities Register | <S / D / D+> | <BUS-01 if S> | <…> |
| BUS-03 Business Process Register | <S / D / D+> | <BUS-01 if S> | <…> |
| BUS-04 Roles & Access Matrix | <— / S / D / D+> | <BUS-01 if S> | <…> |
| BUS-05 Business Rules & Status Lifecycle | <— / S / D> | <BUS-01 if S> | <…> |
| BUS-06 Data, Reports & Notifications Register | <— / S / D / D+> | <BUS-01 if S> | <…> |
| BUS-07 Resource & Cost Model | <— / S / D / D+> | <BUS-01 if S> | <…> |
| BUS-08 Risk & Controls Register | <— / S / D / D+> | <BUS-01 if S> | <…> |
| BUS-09 User & Admin Guide | <— / S / D / D+> | <BUS-01 if S> | <…> |
| ENG-01 Requirements Specification | <S / D / D+> | <ENG-09 if S> | <…> |
| ENG-02 User Journeys | <— / S / D> | <BUS-03 if S> | <…> |
| ENG-03 Architecture & Design | <S / D / D+> | <ENG-09 if S> | <…> |
| ENG-04 Data Model | <S / D / D+> | <ENG-09 if S> | <…> |
| ENG-05 Integrations & Dependencies Register | <S / D / D+> | <ENG-09 if S> | <…> |
| ENG-06 Configuration & Environments | <S / D> | <ENG-09 if S> | <…> |
| ENG-07 Deployment & Release Guide | <S / D / D+> | <ENG-09 if S> | <…> |
| ENG-08 Operations & Support Runbook | <S / D / D+> | <ENG-09 if S> | <…> |
| ENG-09 Developer & Agent Guide | <D> | — | <…> |
| ENG-10 Decision Log | <— / S / D> | <ENG-09 if S> | <…> |

## Deviations

> **Guide:** list every item whose depth or parent differs from the depth matrix after triggers, with the reason and who agreed. Raising a depth needs no approval; lowering one needs the business owner. Write "No deviations from the depth matrix." if there are none.

| Item | Matrix depth | Recorded depth | Reason | Agreed by | Date |
|---|---|---|---|---|---|
| <DOC-ID Title> | <…> | <…> | <…> | <Name, role> | <YYYY-MM-DD> |

## Approval

> **Guide:** both owners approve the record before any other document is accepted. Record only an approval that actually happened; never pre-fill a name, decision or date.

| Role | Name | Decision | Date |
|---|---|---|---|
| Business owner | <…> | <Approved / Not approved> | <YYYY-MM-DD> |
| Technical owner | <…> | <Approved / Not approved> | <YYYY-MM-DD> |

## Re-scope log

> **Guide:** add a row each time the record is re-scored (at every stage gate) or changed. Lowering a level or depth needs the business owner's approval in this row. A re-score with no change still gets a row ("Re-scored at stage 3, no change").

| Date | Stage or reason | What changed | New level or depths | Approved by |
|---|---|---|---|---|
| <YYYY-MM-DD> | <…> | <…> | <…> | <Name, role> |

## Assumptions and open questions

> **Guide:** IDs are unique across the whole package. Continue numbering from the last `Q-xx` used in any document.

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | <…> | <…> | <YYYY-MM-DD> | <Open / Closed> |

## Known limitations

> **Guide:** list limitations of the scoping decision itself (for example, "D4 scored on planned integrations; re-score when the finance export is confirmed"). Every `LIM-xx` also goes into SP-12. Write "No known limitations." if there are none.

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | <…> | <…> | <… or None> | <…> |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | <YYYY-MM-DD> | <Name> | First draft | — |
