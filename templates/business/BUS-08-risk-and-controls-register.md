---
id: BUS-08
title: Risk & Controls Register
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Management, Business owner, Risk and audit, Support, Technical owner]
level: <Foundation | Standard | Full>
depth: <D | D+>
contains: []
related: [BUS-02, BUS-03, BUS-04, BUS-06, ENG-03, ENG-05, SP-12]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Risk & Controls Register

> **How to use this template**
> - **Who writes it:** the producer with the business owner, technical owner and support owner; risk, audit or privacy contacts review it. Derive risks from processes, access, data, reports, dependencies, support, known limitations, technical debt in ENG-03 and incidents.
> - **When it is due:** Draft at stage 4 (Verify), Accepted at stage 5 (Go-live). Update after every incident with a new failure mode and whenever a success measure is missed for two periods.
> - **At Foundation** BUS-08 is usually not needed: the main limitations and risks go in BUS-01 Known limitations.
> - **Depth S:** a section `## BUS-08 Risk & Controls Register` in BUS-01 holding the Risk register table with the High risks only, and one line on the privacy impact assessment when T4 is Yes.
> - **Depth D (Standard):** everything except sections marked (Full).
> - **Depth D+ (Full):** everything, including sections marked (Full).
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

Records what can go wrong with <Application>, how likely and how bad each risk is, the controls that reduce it, who owns it, and what risk remains and who has accepted it.

## Scope

Covers application risks (`RISK-xx`) in every category below. Known limitations stay in their own documents and SP-12; a limitation that could cause harm is also raised here as a risk. Incident handling is in ENG-08; technical debt is described in ENG-03.

## Rating guidance

> **Guide:** rate likelihood and impact, then read the severity from the grid. Severity drives handling: a High risk must have a control and an owner, and either be mitigated or be formally accepted by a named owner with a date.

| Rating | Likelihood | Impact |
|---|---|---|
| High | Expected to happen within a year, or has happened | A business process stops, personal data is exposed, money is lost, or legal or reputational harm |
| Medium | Could happen within a year | Work is delayed or needs rework; a workaround exists |
| Low | Unlikely within a year | Minor inconvenience |

| Likelihood \ Impact | Low | Medium | High |
|---|---|---|---|
| **High** | Medium | High | High |
| **Medium** | Low | Medium | High |
| **Low** | Low | Low | Medium |

## Risk register

> **Guide:**
> - **Risk:** written as cause → event → consequence. Prefer: "If the email service is unavailable, confirmations are not sent, and guests arrive without a confirmed booking." Avoid: "Email risk".
> - **Category:** Operational / Access / Data / Privacy and compliance / Reporting / Dependency / Support / Technical / Financial.
> - **Affects:** the IDs at risk: `C`, `W`, `D`, `REC`, `REP`, `BR`, `LIM`.
> - **Control:** what reduces the likelihood or impact, existing or planned (say which). **Owner:** the person accountable for the control.
> - **Residual risk:** severity after the control. **Accepted by:** the named owner who accepted the residual risk, with date, or "—" while it is being mitigated.

| ID | Risk | Category | Affects | Likelihood | Impact | Severity | Control | Owner | Residual risk | Accepted by | Review cadence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RISK-01 | <Cause → event → consequence> | <…> | <C-xx, D-xx, REC-xx> | <High / Medium / Low> | <High / Medium / Low> | <High / Medium / Low> | <… (existing / planned)> | <Name, role> | <High / Medium / Low> | <Name, role, YYYY-MM-DD, or —> | <Quarterly> |

## Privacy impact assessment

> **Guide:** required when T4 is Yes (personal or confidential data). Answer: has a privacy impact assessment (or data protection impact assessment) been done? Link it with its date and outcome, or state why it is not needed and who decided. Raise any finding as a risk of category Privacy and compliance.

| Item | Value |
|---|---|
| Assessment status | <Done / Planned / Not needed> |
| Link and date | <… or —> |
| Outcome or reason not needed | <…> |
| Decided by | <Name, role> |

## Risk heat map (Full)

> **Guide:** the count of risks in each likelihood × impact cell, before and after controls, so management sees the overall exposure at a glance.

| Likelihood \ Impact | Low | Medium | High |
|---|---|---|---|
| **High** | <n> | <n> | <n> |
| **Medium** | <n> | <n> | <n> |
| **Low** | <n> | <n> | <n> |

## Control testing (Full)

> **Guide:** for each control on a High or Medium risk, how its operation is checked, how often, by whom, and the last result.

| Risk | Control | How tested | Frequency | Tested by | Last result and date |
|---|---|---|---|---|---|
| <RISK-xx> | <…> | <…> | <…> | <Name, role> | <Pass / Fail, YYYY-MM-DD> |

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | <…> | <…> | <YYYY-MM-DD> | <Open / Closed> |

## Known limitations

> **Guide:** for example, a risk category not yet assessed. Every `LIM-xx` also goes into SP-12. Write "No known limitations." if there are none.

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | <…> | <…> | <… or None> | <…> |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | <YYYY-MM-DD> | <Name> | First draft | — |
