---
id: SP-00
title: Scope Record
application: LHC Booking System
version: 1.0
status: Accepted
owner: Grace Tan, LHC Manager (Business owner)
audience: [Business owner, Technical owner, Reviewers, Agents]
level: Standard
depth: D
contains: []
related: [BUS-01, ENG-09, SP-12]
last_reviewed: 2026-09-08
---
# LHC Booking System – Scope Record

## Purpose

This record states which documents the LHC Booking System produces, at what depth, and why. It is the contract the documentation package is reviewed against: reviewers judge the package against this record, not against the full standard.

## Scope

Covers the scoring, triggers, depth of every item, deviations from the depth matrix, owner approval and later re-scoping. It does not describe the application; BUS-01 does.

## Scores

| Dimension | Score (0–3) | Reason |
|---|---|---|
| D1 Users and reach | 3 | Members of the public submit booking requests through a public web form; about 12 LHC staff, admins and managers use it daily. |
| D2 Impact if down or wrong | 2 | If it is down or wrong, booking review and room assignment stop or rooms are double-booked, which costs LHC refunds and upgrades; there is no safety or legal harm. |
| D3 Data sensitivity | 2 | Personal data of guests (name, email, phone, stay dates, special requests); no payment card or special-category data. |
| D4 Integrations | 1 | One simple integration each way of working: it sends email through the organisation's email service and staff sign in through the organisation's single sign-on. No system takes data from it. |
| D5 Process and rule complexity | 3 | Five roles, ten statuses, eleven business rules, an availability calculation and an automated expiry. |
| D6 Team and lifespan | 2 | Built by the ITS application team and handed over to ITS Support and LHC; expected life of five years or more. |
| D7 Regulatory and audit exposure | 1 | Internal policy only: the organisation's privacy policy and records retention schedule. |
| **Total** | 14 | 0–7 Foundation · 8–15 Standard · 16–21 Full |

**Level from total:** Standard

## Floor rules applied

| Floor rule | Applies | Effect |
|---|---|---|
| F1 A 3 on D2, D3 or D7 sets the level to at least Standard | No | No 3 on D2, D3 or D7. |
| F2 A 3 on two or more of D2, D3 and D7 sets the level to Full | No | No 3 on D2, D3 or D7. |
| F3 A 2 or more on D6 makes ENG-09 depth D at any level | Yes | ENG-09 Developer & Agent Guide is at depth D (already D at Standard). |

**Final level:** Standard

## Triggers

| Trigger | Question | Answer | Reason |
|---|---|---|---|
| T1 | Do people use it through a screen (not only through an API or a job)? | Yes | Guests use the public booking form; staff, admins and managers use the staff screens. |
| T2 | Is there more than one role or permission level? | Yes | Five roles: Guest, LHC Staff, LHC Admin, LHC Management, ITS Support. |
| T3 | Do records move through statuses or approvals? | Yes | Each booking request moves from Draft to Submitted, Under Review and a decision, then to Checked In and Completed. |
| T4 | Does it store personal or confidential data? | Yes | Guest name, email, phone and stay details. |
| T5 | Does it exchange data with other systems? | Yes | Sends email through the M365 email service; staff sign in through Microsoft Entra ID single sign-on. |
| T6 | Does it produce outputs others rely on (reports, exports, calculations, notifications)? | Yes | Guests rely on confirmation emails; LHC Management and LHC Finance rely on the monthly booking report; staff rely on the availability figures. |
| T7 | Does it run scheduled or background jobs? | Yes | A nightly job expires Returned requests after 14 days, sends reminders and anonymises old guest data; a worker sends queued email. |
| T8 | Does it cost anything beyond an existing shared platform (licences, hosting, staff time)? | Yes | Its own hosting and database in the ITS cloud subscription, a domain, and ITS and LHC staff time. |
| T9 | Does a non-technical person own it or approve its results? | Yes | The business owner is the LHC Manager. |
| T10 | Will a different team or AI agents build or maintain it? | Yes | Built by the ITS application team, supported by ITS Support; coding agents are used for maintenance. |
| T11 | Is it public-facing? | Yes | The booking request form is open to the public on the internet. |

## Items

| Item | Depth | Parent | Reason |
|---|---|---|---|
| SP-00 Scope Record | D | — | Matrix |
| SP-01 Glossary | S | BUS-01 | Matrix |
| SP-10 Success Measures Register | D | — | Matrix; T6 and T9 Yes (L4 checks and owner-level L1 measures) |
| SP-11 Acceptance Criteria & Verification Register | D | — | Matrix; T3 Yes (criteria for every transition) |
| SP-12 Acceptance & Handover Record | D | — | Matrix |
| BUS-01 Application Overview & Business Case | D | — | Matrix; T9 Yes (plain-language business case) |
| BUS-02 Capabilities Register | D | — | Matrix |
| BUS-03 Business Process Register | D | — | Matrix |
| BUS-04 Roles & Access Matrix | D | — | Matrix; T2 Yes |
| BUS-05 Business Rules & Status Lifecycle | D | — | Matrix; T3 Yes |
| BUS-06 Data, Reports & Notifications Register | D | — | Matrix; T4 and T6 Yes |
| BUS-07 Resource & Cost Model | D | — | Matrix; T8 Yes |
| BUS-08 Risk & Controls Register | D | — | Matrix |
| BUS-09 User & Admin Guide | D | — | Matrix; T1 and T11 Yes (accessibility statement) |
| ENG-01 Requirements Specification | D | — | Matrix |
| ENG-02 User Journeys | S | BUS-03 | Matrix; T1 Yes |
| ENG-03 Architecture & Design | D | — | Matrix; T4 and T11 Yes (security section and threat model summary) |
| ENG-04 Data Model | D | — | Matrix |
| ENG-05 Integrations & Dependencies Register | D | — | Matrix; T5 Yes (interface entries) |
| ENG-06 Configuration & Environments | S | ENG-09 | Matrix |
| ENG-07 Deployment & Release Guide | D | — | Matrix |
| ENG-08 Operations & Support Runbook | D | — | Matrix; T6 and T7 Yes (output checks and job monitoring) |
| ENG-09 Developer & Agent Guide | D | — | Matrix; F3 and T10 Yes |
| ENG-10 Decision Log | D | — | Matrix; T10 Yes |

## Deviations

No deviations from the depth matrix.

## Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Business owner | Grace Tan, LHC Manager | Approved | 2026-03-02 |
| Technical owner | Priya Nair, ITS Application Lead | Approved | 2026-03-02 |

## Re-scope log

| Date | Stage or reason | What changed | New level or depths | Approved by |
|---|---|---|---|---|
| 2026-03-02 | Stage 1 Initiate | First scoring | Standard; depths as above | Grace Tan, LHC Manager; Priya Nair, ITS Application Lead |
| 2026-04-20 | Stage 2 Define | Re-scored, no change | No change | Grace Tan, LHC Manager |
| 2026-06-15 | Stage 3 Build | Re-scored after adding the nightly anonymisation step; T7 already Yes, no change | No change | Grace Tan, LHC Manager |
| 2026-08-21 | Stage 4 Verify | Re-scored, no change | No change | Grace Tan, LHC Manager |
| 2026-09-08 | Stage 5 Go-live | Re-scored, no change | No change | Grace Tan, LHC Manager; Priya Nair, ITS Application Lead |

## Assumptions and open questions

No open questions.

## Known limitations

No known limitations.

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-02-23 | Priya Nair | First draft from the scoping session | — |
| 1.0 | 2026-03-02 | Priya Nair | Accepted at stage 1 | Grace Tan, LHC Manager; Priya Nair, ITS Application Lead |
| 1.0 | 2026-09-08 | Priya Nair | Re-scored at stage 5, no changes | Grace Tan, LHC Manager |
