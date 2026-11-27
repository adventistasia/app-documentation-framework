---
id: SP-10
title: Success Measures Register
application: LHC Booking System
version: 1.0
status: Accepted
owner: Grace Tan, LHC Manager (Business owner)
audience: [Business owner, Management, Operators, Support, Agents]
level: Standard
depth: D
contains: []
related: [BUS-01, BUS-02, BUS-06, SP-11, SP-12, ENG-08]
last_reviewed: 2026-09-11
---
# LHC Booking System – Success Measures Register

## Purpose

States how the LHC Booking System's success is measured at four levels, from "are guests getting faster answers?" down to "is what it produces right?", with the baseline, target, data source and owner of each measure, so the LHC Manager and ITS can judge success with numbers rather than opinion.

## Scope

Covers every success measure. Benefits are defined in BUS-01, application acceptance criteria in SP-11, and the monitoring, alerts and output check procedures that produce L3 and L4 numbers in ENG-08. This register states the measures and links to those items.

## Success measures

| ID | Level | Measure | Definition | Source | Baseline | Target | Threshold for action | Frequency | Owner | Links |
|---|---|---|---|---|---|---|---|---|---|---|
| SM-01 | L1 Business outcome | Median request-to-decision time | Median, over all requests decided in the calendar month, of working days from first reaching Submitted to reaching Confirmed or Rejected; Returned time with the guest is excluded | REP-02 "Response time" sheet | 3 working days (sample of 120 email requests, Jan–Mar 2026) | ≤ 1 working day by 2026-12-31 | Above 1.5 working days in any month | Monthly | Grace Tan, LHC Manager | BEN-01, C-03, C-04 |
| SM-02 | L1 Business outcome | Staff time spent re-keying requests | Hours per week LHC Staff spend copying requests from email, phone notes or paper into a system, from the front office time log, averaged over the month | Front office time log | 6 hours a week (time log, Feb 2026) | ≤ 1 hour a week by 2026-12-31 | Above 2 hours a week in any month | Monthly | Grace Tan, LHC Manager | BEN-02, C-01 |
| SM-03 | L1 Business outcome | Double-booking incidents | Number of times in the quarter a guest arrived to find their room given to another guest, from the front office incident log | Front office incident log; OC-01 results | 4 a quarter (2025 incident log) | 0 a quarter by 2026-12-31 | Any incident | Quarterly | Grace Tan, LHC Manager | BEN-03, C-10 |
| SM-04 | L1 Business outcome | Time to produce the monthly report | Hours the LHC Admin spends producing and checking the monthly booking report, including the reconciliation | LHC Admin time log | 8 hours a month (2025) | ≤ 0.5 hour a month by 2026-12-31 | Above 1 hour in any month | Monthly | Grace Tan, LHC Manager | BEN-04, C-14 |
| SM-05 | L2 Product acceptance | Must acceptance criteria passed | Must criteria in SP-11 with Result Pass or Waived ÷ all Must criteria | SP-11 results summary | 0% (2026-07-01, before the first run) | 100% at go-live | Below 100% blocks SP-12 | Each verification run | Priya Nair, ITS Application Lead | C-01, C-04, C-10 |
| SM-06 | L2 Product acceptance | Open High defects | Defects of High severity open in the issue tracker for the service | ITS issue tracker | 3 (2026-08-14, first UAT run) | 0 at go-live | Any open | Each verification run, then weekly | Priya Nair, ITS Application Lead | C-01, C-04 |
| SM-07 | L3 Operational health | Availability | Successful health checks ÷ all health checks in the calendar month, excluding announced maintenance (NFR-01) | Azure availability test (ENG-08) | 99.96% (staff pilot in production, 2026-08-24 to 2026-09-06) | ≥ 99.5% each month | Below 99.5% in a month; ALR-01 at any outage | Continuous; reported monthly | Priya Nair, ITS Application Lead | C-01, C-11 |
| SM-08 | L3 Operational health | Submission success | Booking submissions answered with HTTP 2xx within 3 s ÷ all submission attempts, excluding HTTP 429 rate-limit refusals, per calendar month | Application Insights requests | 99.8% (staff pilot, 2026-08-24 to 2026-09-06) | ≥ 99% each month | Below 99%; ALR-02 at a spike | Continuous; reported monthly | Priya Nair, ITS Application Lead | C-01 |
| SM-09 | L3 Operational health | Nightly job success | Nights with a nightly_run row of status Success by 03:00 ÷ nights, rolling 30 days | nightly_run table (ENG-08) | 100% (14 of 14 nights, pilot) | 100% | Any miss; ALR-05 | Daily | Priya Nair, ITS Application Lead | C-18 |
| SM-10 | L3 Operational health | Notification delivery | Notifications accepted by M365 within 15 min of their trigger ÷ all notifications, per calendar month | Notification log entries (REC-04) | 99.7% (pilot) | ≥ 99% each month | Below 99%; ALR-03 at a spike | Continuous; reported monthly | Kevin Ho, ITS Network and M365 Administrator | C-12 |
| SM-11 | L4 Output correctness | Double-booked rooms found | Rows returned by OC-01 per daily run | OC-01 results on /health/jobs | 0 (pilot, 14 runs) | 0 every run | 1 or more | Daily | Priya Nair, ITS Application Lead | OC-01, C-10 |
| SM-12 | L4 Output correctness | Monthly report differences | Figures in REP-02 that differ from the OC-02 reconciliation | OC-02 reconciliation sheet | Not measured – capture by 2026-10-01 (first full month, September 2026), owner Daniel Reyes | 0 every month | 1 or more | Monthly | Daniel Reyes, LHC Front Office Supervisor | OC-02, C-14 |
| SM-13 | L4 Output correctness | Confirmed bookings without a logged confirmation | Rows returned by OC-03 per daily run | OC-03 results on /health/jobs | 0 (pilot, 14 runs) | 0 every run | 1 or more | Daily | Priya Nair, ITS Application Lead | OC-03, C-12 |
| SM-14 | L4 Output correctness | Sample audit discrepancies | Bookings in the OC-04 sample of 10 with at least one discrepancy | OC-04 sample audit sheet | Not measured – capture by 2026-10-07 (September 2026 sample), owner Daniel Reyes | 0 of 10 every month | 1 or more | Monthly | Daniel Reyes, LHC Front Office Supervisor | OC-04, C-04 |
| SM-15 | L4 Output correctness | Overdue Returned requests | Rows returned by OC-05 per daily run | OC-05 results on /health/jobs | 0 (pilot, 14 runs) | 0 every run | 1 or more | Daily | Priya Nair, ITS Application Lead | OC-05, C-18 |

## Writing measures at each level

### L1 Business outcome

SM-01 to SM-04 each measure one BUS-01 benefit directly: response time to guests, staff re-keying time, double-bookings and report effort. Baselines come from the email sample, time logs and incident log kept before go-live.

### L2 Product acceptance

SM-05 and SM-06 come from SP-11 and the ITS issue tracker. At handover (2026-09-10) SM-05 was 100% and SM-06 was 0 (SP-12); go-live followed on 2026-09-14.

### L3 Operational health

SM-07 to SM-10 are SLI/SLO pairs. ENG-08 Service levels monitors each one with the same numbers and names its alert. SM-07 restates NFR-01.

### L4 Output correctness

SM-11 to SM-15 are the results of the five output checks in ENG-08. Together the checks cover every core record in BUS-06: Booking (OC-01 to OC-05), Room (OC-01), Room rate (OC-02, OC-04), Notification log entry (OC-03) and Audit event (OC-04).

## Reporting and review

| Levels | Reviewed by | Frequency | Where reported | First review |
|---|---|---|---|---|
| L1 | Grace Tan, LHC Manager, with the LHC management team | Quarterly | Benefit review at the management meeting; minutes in the LHC management share | 2026-12-15 |
| L2 | Priya Nair, ITS Application Lead, and Grace Tan, LHC Manager | At each verification run and at go-live | SP-11 results summary; SP-12 | 2026-09-10 (done) |
| L3 | Priya Nair, ITS Application Lead | Monthly | ITS monthly service report | 2026-11-02 |
| L4 | Daniel Reyes, LHC Front Office Supervisor (OC-02, OC-04); Priya Nair, ITS Application Lead (OC-01, OC-03, OC-05) | Monthly summary of daily and monthly checks | ITS monthly service report; LHC management meeting | 2026-11-02 |

A measure missed for two periods in a row triggers a review of this register and a risk entry in BUS-08.

## Assumptions and open questions

No open questions.

## Known limitations

No known limitations.

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-02-23 | Priya Nair | L1 measures drafted with the business owner at stage 1 | — |
| 0.2 | 2026-08-21 | Priya Nair | L2 to L4 measures added; pilot baselines recorded | — |
| 1.0 | 2026-09-11 | Priya Nair | Accepted at go-live | Grace Tan, LHC Manager; Priya Nair, ITS Application Lead, 2026-09-11 |
