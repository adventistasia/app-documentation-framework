---
id: SP-10
title: Success Measures Register
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Business owner, Management, Operators, Support, Agents]
level: <Foundation | Standard | Full>
depth: <D | D+>
contains: []
related: [BUS-01, BUS-02, BUS-06, SP-11, SP-12, ENG-08]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Success Measures Register

> **How to use this template**
> - **Who writes it:** the business owner (L1, with the producer's help), the project owner (L2), the technical owner and support owner (L3 and L4). Agents may draft from BUS-01 benefits, SP-11 and ENG-08, marking drafts inferred.
> - **When it is due:** L1 measures Draft at stage 1 (Initiate); L2–L4 added by stage 4 (Verify); Accepted at stage 5 (Go-live).
> - **Depth S (Foundation):** a section `## SP-10 Success Measures Register` in BUS-01 holding the Success measures table with 1–3 measures in total: at least one L1 with baseline, target, source and owner, and one L4 when T6 is Yes. Skip the per-level guidance and the review section.
> - **Depth D (Standard):** everything except sections marked (Full). Each level L1–L4 has at least one measure (L4 only when T6 is Yes).
> - **Depth D+ (Full):** everything, including sections marked (Full).
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

States how <Application>'s success is measured at four levels, from "is it delivering the benefit?" down to "is what it produces right?", with the baseline, target, data source and owner of each measure, so success can be judged with numbers rather than opinion.

## Scope

Covers every success measure (`SM-xx`). Benefits are defined in BUS-01, application acceptance criteria in SP-11, and the monitoring, alerts and output check procedures (`OC-xx`) that produce L3 and L4 numbers in ENG-08. This register states the measures and links to those items.

## Success measures

> **Guide:** one row per measure.
> - **Level:** `L1` Business outcome · `L2` Product acceptance · `L3` Operational health · `L4` Output correctness. Start the cell with the level code.
> - **Measure:** plain-language name. **Definition:** exactly how the number is calculated (numerator, denominator, filters, time window), so two people get the same value.
> - **Source:** where the number comes from: a report (`REP-xx`), a log, a dashboard, a query, a survey.
> - **Baseline:** today's value with the date measured, or `Not measured – capture by <YYYY-MM-DD>` with an owner. Never invent a baseline.
> - **Target:** value and timeframe ("≤ 1 working day by <YYYY-MM-DD>"). **Threshold for action:** the value at which the owner must act.
> - **Owner:** a named person who reports the measure and acts on it. **Links:** the benefit (`BEN-xx`) for L1, the capability (`C-xx`) where relevant, and the output check (`OC-xx`) for L4.
> Prefer: "Median working days from Submitted to decision, all requests decided in the month". Avoid: "Faster bookings".

| ID | Level | Measure | Definition | Source | Baseline | Target | Threshold for action | Frequency | Owner | Links |
|---|---|---|---|---|---|---|---|---|---|---|
| SM-01 | <L1 / L2 / L3 / L4> | <…> | <…> | <REP-xx, log, dashboard, query> | <value and date, or Not measured – capture by YYYY-MM-DD> | <value and timeframe> | <…> | <…> | <Name, role> | <BEN-xx, C-xx, OC-xx> |

## Writing measures at each level

> **Guide:** at Foundation, 1–3 measures in total are enough: at least one L1, plus one L4 when T6 is Yes. At Standard and Full, give each level at least one measure.

### L1 Business outcome

> **Guide:** answers "is the application delivering the benefit it was built for?". Read by the business owner and management, usually quarterly or at benefit review. Derive one or more from each benefit in BUS-01: ask "what number would show this benefit is happening?". Every benefit's `Measure` column must name an L1 measure, and every L1 measure needs `Baseline`, `Target`, `Source` and `Owner`. Typical measures: cycle time, cost per transaction, error rate in the business process, adoption, satisfaction.

### L2 Product acceptance

> **Guide:** answers "does the application do what was agreed?". Read at user acceptance testing and go-live. Typical measures: pass rate of Must application acceptance criteria in SP-11 (target 100% Pass or Waived), open defects by severity (target: no open High). The source is SP-11 and the defect tracker.

### L3 Operational health

> **Guide:** answers "is it up and performing now?". Write each as an SLI with an SLO: the indicator, the good-event definition and the target over a window. Example: "99.5% of request submissions succeed (HTTP 2xx within 3 s), measured over each calendar month." ENG-08 monitors each L3 measure and names the alert that fires on breach. Typical measures: availability, latency, job success rate, queue age.

### L4 Output correctness

> **Guide:** answers "is what it produces actually right?". Required when T6 is Yes. Each L4 measure links to an output check (`OC-xx`) whose procedure, frequency and owner are in ENG-08, and every record marked `Core` = Yes in BUS-06 is covered by at least one output check. Derive checks from business rules and reports:
> - **Invariant:** a rule that must always hold, from a business rule ("no room is confirmed twice for overlapping dates", from `BR-xx`).
> - **Reconciliation:** two counts that must agree ("confirmed bookings in the application = confirmed bookings in the monthly report `REP-xx`").
> - **Completeness:** every item that should have something has it ("every Confirmed booking has a confirmation notification logged").
> - **Sample audit:** a person checks a random sample against its source ("10 random bookings per month checked against the original request").
> - **Golden data:** a fixed test dataset that must produce a known result ("the test month produces a report total of 1,240").
> Write the measure as the result of the check, for example "Number of invariant violations found per daily run, target 0".

## Reporting and review

> **Guide:** say who reviews which levels, when, and where the result is recorded. State the date of the first L1 review (SP-12 repeats it). A measure missed for two periods triggers a review of this register and a risk entry in BUS-08.

| Levels | Reviewed by | Frequency | Where reported | First review |
|---|---|---|---|---|
| <L1> | <Name, role> | <Quarterly> | <…> | <YYYY-MM-DD> |

## Measure review log (Full)

> **Guide:** at each L1 review, record the values and the decision. This is the evidence that benefits are being tracked after go-live.

| Date | Measure | Value | Against target | Decision or action | Reviewed by |
|---|---|---|---|---|---|
| <YYYY-MM-DD> | <SM-xx> | <…> | <Met / Not met / Trend> | <…> | <Name, role> |

## Source data quality (Full)

> **Guide:** for each source, say how trustworthy it is and what could distort the number (manual entry, missing records, time-zone cut-offs), and what is done about it.

| Source | Used by | Known quality issues | Mitigation | Owner |
|---|---|---|---|---|
| <…> | <SM-xx> | <…> | <…> | <…> |

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | <…> | <…> | <YYYY-MM-DD> | <Open / Closed> |

## Known limitations

> **Guide:** for example, a measure that cannot be captured until a report exists. Every `LIM-xx` also goes into SP-12. Write "No known limitations." if there are none.

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | <…> | <…> | <… or None> | <…> |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | <YYYY-MM-DD> | <Name> | First draft | — |
