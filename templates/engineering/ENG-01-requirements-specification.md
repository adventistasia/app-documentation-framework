---
id: ENG-01
title: Requirements Specification
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Engineering, Testers, Agents]
level: <Foundation | Standard | Full>
depth: <D | D+>
contains: []
related: [BUS-02, BUS-05, ENG-02, ENG-03, ENG-08, SP-11]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Requirements Specification

> **How to use this template**
> - **Who writes it:** the technical owner, with the business owner or product owner for priorities. An agent may draft from tickets, designs or code; mark drafted content as inferred until confirmed.
> - **When it is due:** Draft by stage 2 (Define); Accepted by stage 2 (Define), before the build starts.
> - **Depth S** (section `## ENG-01 Requirements Specification` in ENG-09): the functional requirements table for Must requirements only, and the non-functional requirements table for the key categories (at least availability, performance, security and recoverability with RTO and RPO). Keep every linked column (the linter checks them; other columns may be left out) and use level-3 subheadings named after this template's sections, so the section can later be promoted to its own file without restructuring.
> - **Depth D (Standard):** every section except those marked (Full).
> - **Depth D+ (Full):** every section, including (Full).
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

<Two to four sentences. Example: "States what <Application> must do and how well it must do it, so engineers and agents build the right behaviour and testers can verify it. Every requirement traces to a capability in BUS-02 and is verified by an application acceptance criterion in SP-11.">

## Scope

<What this document covers and what it leaves to others. Example: "Covers functional requirements, non-functional requirements and constraints. Business rules are defined in BUS-05 and referenced here by ID; acceptance criteria and results live in SP-11; user journeys are in ENG-02.">

## Functional requirements

> **Guide:** Write one behaviour per row, as "The system shall…". A requirement an engineer could build two different ways and both be "right" is too vague; split it or add the rule it enforces. Trace every requirement to at least one capability (`C-xx`) and to the business rules (`BR-xx`) it enforces. Do not restate the rule's wording; link it.
>
> Good: "The system shall prevent confirmation of a booking whose dates overlap a confirmed booking for the same resource (BR-03)." Weak: "The system shall handle bookings correctly."
>
> **Priority** is MoSCoW: Must / Should / Could / Won't. Record Won't items so nobody builds them by accident.
> **Status:** Proposed (written, not agreed) → Agreed (owner accepted) → Built (merged and deployed to test) → Verified (its acceptance criteria in SP-11 pass).

| ID | Requirement | Capabilities | Rules | Priority | Status | Notes |
|---|---|---|---|---|---|---|
| FR-01 | The system shall <one observable behaviour> | <C-01> | <BR-01, or None> | <Must / Should / Could / Won't> | <Proposed / Agreed / Built / Verified> | <…> |

## Non-functional requirements

> **Guide:** Use the fixed categories below. Every NFR has a **measurable target** with a number, a unit and a timeframe or load, and a **measurement method** saying how the target is checked. An adjective ("fast", "secure", "highly available") is not a target.
>
> | Category | What a measurable target looks like |
> |---|---|
> | Availability | "99.5% monthly, measured 07:00–19:00 local time on working days" |
> | Performance | "p95 page load ≤ 2 s at 50 concurrent users" |
> | Capacity | "10 000 records per year; 200 concurrent sessions" |
> | Security | "All access requires single sign-on with multi-factor authentication"; "no High findings open in the latest scan" |
> | Privacy | "Personal data is deleted within 30 days of the retention period ending" |
> | Accessibility | "Meets WCAG 2.2 AA on every user-facing screen" |
> | Compatibility | "Latest two versions of <browsers>; screens from 360 px wide" |
> | Maintainability | "Automated test suite runs in ≤ 10 min; line coverage ≥ 70% on domain code" |
> | Observability | "Every request carries a correlation ID; errors visible on the dashboard within 1 min" |
> | Data retention | "Audit records are kept 7 years, then deleted" (period from BUS-06) |
> | Recoverability | RTO and RPO, see below |
>
> **RTO and RPO are recoverability NFRs.** RTO (recovery time objective) is the longest acceptable time to restore service after a failure; RPO (recovery point objective) is the most data, measured in time, that may be lost. ENG-08 backup, restore and disaster recovery sections must use the same values.
>
> List every category. If a category does not apply, say so in the line under the table with a reason; do not leave it out silently.

| ID | Category | Requirement | Target | Measurement method | Priority | Status |
|---|---|---|---|---|---|---|
| NFR-01 | <Availability> | <The service is available during business hours> | <99.5% monthly, 07:00–19:00 working days> | <Uptime monitor on the health check, monthly report> | <Must> | <Proposed> |
| NFR-02 | Recoverability | Recovery time objective (RTO) | <≤ 4 h from declared outage to service restored> | <Timed restore test, see ENG-08> | <Must> | <Proposed> |
| NFR-03 | Recoverability | Recovery point objective (RPO) | <≤ 24 h of data loss> | <Backup frequency and restore test, see ENG-08> | <Must> | <Proposed> |

Categories not applicable: <Category: reason, or "None">.

> **Guide:** The plain-language summary of the top NFRs ("available during office hours, 99.5%") lives in BUS-01; keep the values identical. L3 success measures in SP-10 usually restate availability and performance NFRs as SLI/SLO pairs; link them by ID rather than restating different numbers.

## Constraints

> **Guide:** Constraints are decisions already made for you: mandated technology, hosting, budget, regulation, deadlines, organisational standards. Each one should say where it comes from, so an agent knows not to "improve" it. A constraint that results from a team decision belongs in ENG-10 as an ADR instead.

| Constraint | Type | Source | Impact on design |
|---|---|---|---|
| <Must run on the organisation's shared hosting platform> | <Technology / Hosting / Budget / Regulatory / Schedule / Organisational> | <Policy, contract or person> | <…> |

## Verification rule

Every FR and NFR has at least one application acceptance criterion in SP-11 whose `Verifies` column lists its ID. A requirement cannot move to **Verified** until those criteria pass. A Must FR or any NFR without a criterion fails X-19 and blocks acceptance.

> **Guide:** Do not copy acceptance criteria here. SP-11 holds them and links back by ID.

## Requirement sources and rationale (Full)

> **Guide:** For audited or long-lived applications, record where each requirement came from and why, so later changes can be judged against the original intent.

| Requirement | Source | Rationale | Agreed by | Date |
|---|---|---|---|---|
| <FR-01> | <Stakeholder interview, policy, ticket, regulation> | <…> | <Name and role> | <YYYY-MM-DD> |

## NFR verification plan (Full)

> **Guide:** Say when and how each NFR target is proven before go-live and kept true afterwards (load test, accessibility audit, penetration test, restore test, monitoring). Link the evidence once it exists.

| Requirement | Before go-live | In operation | Evidence |
|---|---|---|---|
| <NFR-01> | <Load test at 2× expected peak> | <Monthly availability report from ENG-08 monitoring> | <Link, or "Not yet run"> |

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | <…> | <…> | <YYYY-MM-DD> | <Open / Closed> |

## Known limitations

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | <…> | <…> | <…, or None> | <…> |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | <YYYY-MM-DD> | <Name> | First draft | — |
