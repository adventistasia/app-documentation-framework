---
id: BUS-07
title: Resource & Cost Model
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Budget holder, Management, Business owner, Technical owner]
level: <Foundation | Standard | Full>
depth: <D | D+>
contains: []
related: [BUS-01, ENG-05, ENG-08]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Resource & Cost Model

> **How to use this template**
> - **Who writes it:** the producer with the budget holder and the technical owner; the support owner confirms support effort. Start with an estimate and refine it.
> - **When it is due:** initial estimate Draft at stage 1 (Initiate), refined through the build, Accepted at stage 5 (Go-live). Update when a dependency's cost, a licence or the support model changes.
> - **In scope only when T8 is Yes** (it costs something beyond an existing shared platform). When T8 is No, BUS-01 names the shared platform in one line instead.
> - **Depth S (Foundation):** a section `## BUS-07 Resource & Cost Model` in BUS-01 holding a few cost lines (one table, keeping `Basis`, `Dependency` and `Owner`), the yearly total and the budget holder.
> - **Depth D (Standard):** everything except sections marked (Full).
> - **Depth D+ (Full):** everything, including sections marked (Full).
> - Estimates are fine. Mark each line's `Basis` as Estimate, Quote or Actual, and say what the estimate is based on.
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

Tells the business what it takes to deploy and run <Application>: people and effort, skills, infrastructure, services, licences, running costs, renewals and what retiring it would involve, so the budget holder can fund it and plan for it.

## Scope

Covers every cost and effort line (`COST-xx`), one-off and recurring. Dependencies and their renewal dates are defined in ENG-05; routine operations tasks in ENG-08. Every dependency marked `Cost` = Yes in ENG-05 appears here in a `Dependency` column.

> **Guide:** amounts are in <currency>, excluding or including tax as stated here: <…>. Every table that holds `COST-xx` lines has a `Dependency` column holding a `D-xx` ID or `None`.

## People and effort

> **Guide:** recurring effort to keep the application running: support, administration, data upkeep, access administration, releases, monitoring and output checks. Use ENG-08 routine tasks (`MT-xx`) and runbook duties as the list; name the tasks each line covers.

| ID | Role | Activity | Covers | Effort per month | Team | Skills needed | Cost per year | Basis | Dependency | Owner |
|---|---|---|---|---|---|---|---|---|---|---|
| COST-01 | <Role or job> | <…> | <MT-xx, or description> | <hours> | <…> | <…> | <amount> | <Estimate / Quote / Actual> | <D-xx or None> | <Name, role> |

## One-off deployment resources

> **Guide:** effort and spend needed once, to go live: build, data migration, training, cutover, early-life support.

| ID | Item | Effort or cost | When | Basis | Dependency | Owner |
|---|---|---|---|---|---|---|
| COST-02 | <…> | <hours or amount> | <stage or date> | <Estimate / Quote / Actual> | <D-xx or None> | <Name, role> |

## Infrastructure and services

> **Guide:** hosting, database, storage, email, domain, monitoring, backup. Give the sizing and number of environments, since these drive cost.

| ID | Item | Sizing | Environments | Monthly cost | Annual cost | Basis | Dependency | Owner |
|---|---|---|---|---|---|---|---|---|
| COST-03 | <…> | <…> | <ENV-xx> | <amount> | <amount> | <Estimate / Quote / Actual> | <D-xx> | <Name, role> |

## Licences and subscriptions

> **Guide:** every paid product or service, with renewal date and notice period so nothing lapses by surprise. Renewal dates must match ENG-05.

| ID | Item | Cost | Billing cycle | Renewal date | Notice period | Basis | Dependency | Owner |
|---|---|---|---|---|---|---|---|---|
| COST-04 | <…> | <amount> | <Monthly / Annual> | <YYYY-MM-DD> | <…> | <Estimate / Quote / Actual> | <D-xx> | <Name, role> |

## Running cost summary

> **Guide:** recurring totals by group, with the assumptions behind them. One-off costs are shown separately.

| Cost group | Monthly | Annual | Main assumptions |
|---|---|---|---|
| People and effort | <amount> | <amount> | <…> |
| Infrastructure and services | <amount> | <amount> | <…> |
| Licences and subscriptions | <amount> | <amount> | <…> |
| **Total recurring** | <amount> | <amount> | |
| One-off (deployment) | — | <amount> | <…> |

## Scaling assumptions

> **Guide:** what makes the cost grow (users, records, storage, messages sent), the current value and expected growth, and which cost lines change.
> Prefer: "Email cost grows with notifications sent: 2,000 a month today, about 5,000 expected next year (COST-03)." Avoid: "Costs may increase."

| Driver | Current | Expected | Effect on cost | Cost lines affected |
|---|---|---|---|---|
| <…> | <…> | <…> | <…> | <COST-xx> |

## Funding and ownership

| Item | Value |
|---|---|
| Budget holder | <Name, role> |
| Cost centre or budget line | <…> |
| Funding period | <…> |
| Next budget review | <YYYY-MM-DD> |

## End of life

> **Guide:** what retiring the application would involve: exporting or archiving data (respecting retention in BUS-06), notice to users and downstream systems, cancelling licences and their notice periods, decommissioning infrastructure, and the effort needed.

- <…>

## Cost scenarios (Full)

> **Guide:** low, expected and high cases for the next one to three years, with the assumptions that change between them.

| Scenario | Assumptions | Year 1 | Year 2 | Year 3 |
|---|---|---|---|---|
| <Expected> | <…> | <amount> | <amount> | <amount> |

## Total cost of ownership (Full)

> **Guide:** one-off plus recurring cost over the planned lifetime, compared with the benefits in BUS-01 where they can be valued.

| Item | Value |
|---|---|
| Planned lifetime | <years> |
| One-off total | <amount> |
| Recurring total over lifetime | <amount> |
| Total cost of ownership | <amount> |

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | <…> | <…> | <YYYY-MM-DD> | <Open / Closed> |

## Known limitations

> **Guide:** for example, a cost not yet quoted. Every `LIM-xx` also goes into SP-12. Write "No known limitations." if there are none.

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | <…> | <…> | <… or None> | <…> |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | <YYYY-MM-DD> | <Name> | First draft | — |
