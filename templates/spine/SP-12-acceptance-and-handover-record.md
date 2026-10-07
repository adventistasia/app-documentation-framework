---
id: SP-12
title: Acceptance & Handover Record
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Business owner, Support owner, Technical owner, Project owner, Auditors]
level: <Foundation | Standard | Full>
depth: <D | D+>
contains: []
related: [SP-00, SP-10, SP-11, BUS-01, BUS-08, ENG-07, ENG-08]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Acceptance & Handover Record

> **How to use this template**
> - **Who writes it:** the project owner or producer compiles it; the business owner, support owner and technical owner each record their own decision. Agents may compile it but never fill in a decision, approval, test result or dry run.
> - **When it is due:** Draft and Accepted at stage 5 (Go-live). Compile it from SP-11 results, SP-10 baselines, the Known limitations section of every document, BUS-08 accepted risks and the open conditions from reviews.
> - **Depth S (Foundation):** a section `## SP-12 Acceptance & Handover Record` in BUS-01 used as a sign-off checklist: Acceptance results (one line of counts), Dry-run evidence, Consolidated known limitations, Support and operations ownership, and Final decisions. Skip the other tables or reduce each to one line.
> - **Depth D (Standard):** everything except sections marked (Full).
> - **Depth D+ (Full):** everything, including sections marked (Full).
> - This record must be honest. It is never `Accepted` while a Must application acceptance criterion is Not run or Fail without a waiver, and no decision is ever pre-filled.
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

The formal readiness and accountability record for <Application>: what was delivered and deferred, what the acceptance results were, which limitations and risks were accepted, who supports and operates the application from now on, and who signed off.

## Scope

Covers the handover at go-live (and any later re-handover). It summarises and links to SP-11 (results), SP-10 (baselines), BUS-08 (risks), ENG-07 and ENG-08 (deploy, rollback and restore procedures); it does not repeat them.

## Delivered scope

> **Guide:** list what is live, by capability and process ID, with the evidence that it was accepted (SP-11 criteria, demonstration, review decision). Write business outcomes, not tickets.

| Item | Description | Evidence | Accepted |
|---|---|---|---|
| <C-xx / W-xx> | <…> | <AC-xx, review link> | <Yes / No> |

## Deferred scope

> **Guide:** list everything agreed but not delivered, with the reason and where it is tracked. Write "Nothing deferred." if that is true.

| Item | Reason deferred | Owner | Target date | Tracked as |
|---|---|---|---|---|
| <C-xx / FR-xx / description> | <…> | <Name, role> | <YYYY-MM-DD> | <COND-xx, ticket or LIM-xx> |

## Acceptance results

> **Guide:** copy the counts from the SP-11 results summary on the date of handover. Every Must criterion must be Pass, or Waived with a named approver. A Must criterion that is Fail or Not run blocks `Accepted`; list it here and as a condition only if the owners decide to go live with it waived.

| Priority | Total | Pass | Fail | Waived | Not run |
|---|---|---|---|---|---|
| Must | <n> | <n> | <n> | <n> | <n> |
| Should | <n> | <n> | <n> | <n> | <n> |
| Could | <n> | <n> | <n> | <n> | <n> |

**SP-11 version and verification date:** <version>, <YYYY-MM-DD>

| Criterion | Result | Reason | Approver | Date |
|---|---|---|---|---|
| <AC-xx> | <Waived / Fail / Not run> | <…> | <Name, role, for Waived> | <YYYY-MM-DD> |

## Success baseline

> **Guide:** say which success measures have a baseline captured, and when each missing baseline will be captured. State the date of the first L1 review.

| Measure | Level | Baseline captured | Value and date | Capture by |
|---|---|---|---|---|
| <SM-xx> | <L1–L4> | <Yes / No> | <…> | <YYYY-MM-DD if No> |

**First L1 benefit review:** <YYYY-MM-DD>, by <Name, role>

## Dry-run evidence

> **Guide:** a deploy, a rollback and a restore must each have been performed from the documents alone, by someone who did not write them, before handover. Record what actually happened, with evidence. A missing or failed dry run fails gate G6.

| Procedure | Followed document | Performed by | Date | Environment | Result | Evidence |
|---|---|---|---|---|---|---|
| Deploy | <ENG-07 section> | <Name, role> | <YYYY-MM-DD> | <ENV-xx> | <Succeeded / Failed / Not done> | <link> |
| Rollback | <ENG-07 section> | <Name, role> | <YYYY-MM-DD> | <ENV-xx> | <Succeeded / Failed / Not done> | <link> |
| Restore | <ENG-08 section> | <Name, role> | <YYYY-MM-DD> | <ENV-xx> | <Succeeded / Failed / Not done> | <link> |

## Accepted areas

> **Guide:** the areas the owners confirm as ready to operate. Each row points to the accepted document. Add rows for reports, notifications and dependencies where they matter to this application.

| Area | Document | Accepted | Accepted by | Notes |
|---|---|---|---|---|
| Business processes | BUS-03 | <Yes / No> | <Name, role> | <…> |
| Roles and access model (definitions, permissions, request, removal) | BUS-04 | <Yes / No> | <Name, role> | <…> |
| Support model (intake, triage, escalation, routine tasks) | ENG-08 | <Yes / No> | <Name, role> | <…> |
| Dependency support paths | ENG-05 | <Yes / No> | <Name, role> | <…> |
| Reports and notifications | BUS-06 | <Yes / No> | <Name, role> | <…> |

## Consolidated known limitations

> **Guide:** the consolidated list of every `LIM-xx` raised in any document in the package (the linter checks none is missing). Limitations are defined where they are raised, so this table's first column is `Limitation`, not `ID`. Each one is accepted by a named owner or it becomes a condition.

| Limitation | Description | Raised in | Impact | Workaround | Accepted by | Date |
|---|---|---|---|---|---|---|
| <LIM-xx> | <…> | <DOC-ID> | <…> | <… or None> | <Name, role> | <YYYY-MM-DD> |

## Accepted risks

> **Guide:** list every High risk from BUS-08, and any Medium risk accepted rather than mitigated, with who accepted the residual risk and when it is reviewed again.

| Risk | Severity | Residual risk | Accepted by | Date | Review by |
|---|---|---|---|---|---|
| <RISK-xx> | <High / Medium / Low> | <…> | <Name, role> | <YYYY-MM-DD> | <YYYY-MM-DD> |

## Open items and conditions

> **Guide:** every condition from a document or package decision of Accept with Conditions, every critical Partial, every waived Must criterion that still needs work, and every open handover item. Each has an owner, a target date, and the owner who agreed to go live with it open.

| ID | Condition or open item | Source | Owner | Target date | Agreed by | Status |
|---|---|---|---|---|---|---|
| COND-01 | <…> | <review finding, DOC-ID or AC-xx> | <Name, role> | <YYYY-MM-DD> | <Name, role> | <Open / Closed> |

## Support and operations ownership after handover

> **Guide:** name a person, not only a team, for each responsibility, from the go-live date. The owners named here must match BUS-01 and ENG-08.

| Responsibility | Owner | Team | Contact or support path | From |
|---|---|---|---|---|
| Business ownership and benefits | <Name, role> | <…> | <…> | <YYYY-MM-DD> |
| Business and process support | <Name, role> | <…> | <…> | <YYYY-MM-DD> |
| Technical support and incidents | <Name, role> | <…> | <…> | <YYYY-MM-DD> |
| Hosting and infrastructure | <Name, role> | <…> | <…> | <YYYY-MM-DD> |
| Access administration | <Name, role> | <…> | <…> | <YYYY-MM-DD> |
| Data ownership | <Name, role> | <…> | <…> | <YYYY-MM-DD> |
| Releases and changes | <Name, role> | <…> | <…> | <YYYY-MM-DD> |
| Success measure reporting | <Name, role> | <…> | <…> | <YYYY-MM-DD> |

## Early-life support (Full)

> **Guide:** the period after go-live with extra support: how long it lasts, who is on call, the exit criteria (for example, "no High incident for 4 weeks and L3 SLOs met"), and the date of the post-go-live review.

| Item | Value |
|---|---|
| Early-life support period | <YYYY-MM-DD to YYYY-MM-DD> |
| Extra support arrangements | <…> |
| Exit criteria | <…> |
| Post-go-live review | <YYYY-MM-DD, by Name, role> |

## Final decisions

> **Guide:** each owner records their own decision: Accept, Accept with Conditions (the conditions are listed under Open items and conditions) or Reject. **Never pre-fill** a name, decision or date: leave the cells empty until the owner decides. SP-12 `status` becomes `Accepted` only when all three decisions are Accept or Accept with Conditions, and the change log records it.

| Owner | Role | Decision | Date | Conditions | Notes |
|---|---|---|---|---|---|
| | Business owner | | | | |
| | Support owner | | | | |
| | Technical owner | | | | |

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | <…> | <…> | <YYYY-MM-DD> | <Open / Closed> |

## Known limitations

> **Guide:** limitations of the handover itself (for example, "restore dry run used a test backup only"). Define them here with an `LIM-xx` ID and list them in Consolidated known limitations above too. Write "No known limitations." if there are none.

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | <…> | <…> | <… or None> | <…> |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | <YYYY-MM-DD> | <Name> | First draft | — |
