---
id: SP-12
title: Acceptance & Handover Record
application: LHC Booking System
version: 1.0
status: Accepted
owner: Priya Nair, ITS Application Lead (Project owner)
audience: [Business owner, Support owner, Technical owner, Project owner, Auditors]
level: Standard
depth: D
contains: []
related: [SP-00, SP-10, SP-11, BUS-01, BUS-08, ENG-07, ENG-08]
last_reviewed: 2026-09-11
---
# LHC Booking System – Acceptance & Handover Record

## Purpose

The formal readiness and accountability record for the LHC Booking System: what was delivered and deferred, what the acceptance results were, which limitations and risks were accepted, who supports and operates the application from go-live, and who signed off.

## Scope

Covers the handover for release 1.0.0, decided on 2026-09-11, with go-live on 2026-09-14. It summarises and links to SP-11 (results), SP-10 (baselines), BUS-08 (risks), ENG-07 and ENG-08 (deploy, rollback and restore procedures); it does not repeat them.

## Delivered scope

| Item | Description | Evidence | Accepted |
|---|---|---|---|
| C-01, W-01 | Guests, or staff on their behalf, submit and resubmit booking requests through the public form | AC-01 to AC-06, AC-21, AC-22, AC-65 | Yes |
| C-02, C-03, C-04, C-05, W-02 | Staff review requests against live availability and confirm, return or reject them | AC-07 to AC-12, AC-17 to AC-20, AC-66 | Yes |
| C-18 | Returned requests get one reminder after 7 days and expire after 14 | AC-23 to AC-25 | Yes |
| C-10, C-17, W-03 | Staff assign rooms with no double-booking, and check guests in and out | AC-26 to AC-32, AC-67 | Yes |
| C-06, C-07, W-04 | Staff change and cancel Confirmed bookings | AC-33 to AC-36 | Yes |
| C-08, C-09, W-05 | The LHC Admin maintains rooms and rates; confirmed rates are kept | AC-13 to AC-16, AC-37, AC-38 | Yes |
| C-11 | Guests see their status through the booking link; staff see it on every screen | AC-45 | Yes |
| C-12 | Every notification is sent, retried and logged | AC-06, AC-39 | Yes |
| C-13, W-07 | Staff roles are given and removed, with urgent removal by ITS Support | AC-40 to AC-42, AC-52 | Yes |
| C-14, W-06 | Daily arrivals list and monthly report, reconciled | AC-43, AC-44 | Yes |
| C-15, W-08 | ITS Support handle support issues with a read-only booking view | AC-47; ENG-08 accepted | Yes |
| C-16 | Every change is recorded in the audit trail | AC-46 | Yes |

## Deferred scope

| Item | Reason deferred | Owner | Target date | Tracked as |
|---|---|---|---|---|
| FR-25 Audit trail export (REP-04) | Old and new values are written to the wrong columns (AC-48 failed); the export is switched off by FLAG-01 | Leo Santos, ITS Developer | 2026-11-30 | COND-01; issue LHCB-112 |
| FR-26 Guests change or cancel their own booking | Won't for this release: agreed at stage 2 to keep changes with staff | Grace Tan, LHC Manager | — (reconsider at the 2027 benefit review) | LIM-01 |

## Acceptance results

| Priority | Total | Pass | Fail | Waived | Not run |
|---|---|---|---|---|---|
| Must | 65 | 65 | 0 | 0 | 0 |
| Should | 2 | 1 | 0 | 1 | 0 |
| Could | 0 | 0 | 0 | 0 | 0 |

**SP-11 version and verification date:** 1.0, 2026-09-10

| Criterion | Result | Reason | Approver | Date |
|---|---|---|---|---|
| AC-48 | Waived | Should criterion for the audit trail export; no business process depends on it, and the export is off until fixed | Grace Tan, LHC Manager | 2026-09-10 |

## Success baseline

| Measure | Level | Baseline captured | Value and date | Capture by |
|---|---|---|---|---|
| SM-01 | L1 | Yes | 3 working days, Jan–Mar 2026 | |
| SM-02 | L1 | Yes | 6 hours a week, Feb 2026 | |
| SM-03 | L1 | Yes | 4 a quarter, 2025 | |
| SM-04 | L1 | Yes | 8 hours a month, 2025 | |
| SM-05 | L2 | Yes | 100%, 2026-09-10 | |
| SM-06 | L2 | Yes | 0, 2026-09-10 | |
| SM-07 | L3 | Yes | 99.96%, pilot 2026-08-24 to 2026-09-06 | |
| SM-08 | L3 | Yes | 99.8%, pilot | |
| SM-09 | L3 | Yes | 100%, pilot | |
| SM-10 | L3 | Yes | 99.7%, pilot | |
| SM-11 | L4 | Yes | 0, pilot | |
| SM-12 | L4 | No | — | 2026-10-01 |
| SM-13 | L4 | Yes | 0, pilot | |
| SM-14 | L4 | No | — | 2026-10-07 |
| SM-15 | L4 | Yes | 0, pilot | |

**First L1 benefit review:** 2026-12-15, by Grace Tan, LHC Manager

## Dry-run evidence

| Procedure | Followed document | Performed by | Date | Environment | Result | Evidence |
|---|---|---|---|---|---|---|
| Deploy | ENG-07 Deployment procedure | Joel Park, ITS Operations Engineer | 2026-08-27 | ENV-02 | Succeeded | ITS change record CHG-2026-0838; dry-run record in ENG-07 |
| Rollback | ENG-07 Rollback | Joel Park, ITS Operations Engineer | 2026-08-27 | ENV-02 | Succeeded | ITS change record CHG-2026-0838; dry-run record in ENG-07 |
| Restore | ENG-08 Restore procedure | Joel Park, ITS Operations Engineer | 2026-08-28 | ENV-02 | Succeeded | ITS change record CHG-2026-0841; ENG-08 Restore tests |

Joel Park did not write ENG-07 or ENG-08 and worked from the documents alone.

## Accepted areas

| Area | Document | Accepted | Accepted by | Notes |
|---|---|---|---|---|
| Business processes | BUS-03 | Yes | Grace Tan, LHC Manager | Pilot with all LHC Staff, 2026-08-24 to 2026-09-06 |
| Roles and access model (definitions, permissions, request, removal) | BUS-04 | Yes | Grace Tan, LHC Manager | Single LHC Admin accepted with COND-02 |
| Support model (intake, triage, escalation, routine tasks) | ENG-08 | Yes | Mark Lim, ITS Service Desk Lead | Service desk briefed 2026-09-08 |
| Dependency support paths | ENG-05 | Yes | Priya Nair, ITS Application Lead | Contacts checked 2026-09-04 |
| Reports and notifications | BUS-06 | Yes | Grace Tan, LHC Manager | REP-04 off until COND-01 |
| Privacy | BUS-08 | Yes | Ruth Ong, Data Protection Officer | PIA completed 2026-05-20 |

## Consolidated known limitations

| Limitation | Description | Raised in | Impact | Workaround | Accepted by | Date |
|---|---|---|---|---|---|---|
| LIM-01 | Guests cannot change or cancel their own booking online | BUS-02 | Changes outside front office hours wait until the next morning | Guests email or phone LHC; staff make the change | Grace Tan, LHC Manager | 2026-09-11 |
| LIM-02 | Only one person holds the LHC Admin role | BUS-04 | Room, rate and role changes wait while the LHC Admin is away (RISK-04) | ITS Support remove roles and deactivate rooms on the LHC Manager's request | Grace Tan, LHC Manager | 2026-09-11 |
| LIM-03 | Notifications are sent by email only | BUS-06 | Guests with a wrong email or who do not read email are not told | Staff phone guests on the failed-email list and those arriving within 2 days who have not replied | Grace Tan, LHC Manager | 2026-09-11 |
| LIM-04 | The restore dry run used ENV-02; a restore into the paired Azure region has not been tested | SP-12 | Recovery from a full regional outage may take longer than the 4-hour RTO (RISK-07) | Follow the ENG-08 restore procedure with the paired region as the target | Priya Nair, ITS Application Lead | 2026-09-11 |

## Accepted risks

| Risk | Severity | Residual risk | Accepted by | Date | Review by |
|---|---|---|---|---|---|
| RISK-01 | High | Medium: a forwarded booking link shows that booking's details to whoever holds it | Grace Tan, LHC Manager | 2026-09-11 | 2026-12-15 |
| RISK-05 | High | Low: the database refuses double assignment; OC-01 checks nightly | Grace Tan, LHC Manager | 2026-09-11 | 2026-12-15 |
| RISK-10 | High | Low: leavers lose sign-in when their Entra ID account is disabled; quarterly review | Grace Tan, LHC Manager | 2026-09-11 | 2026-12-15 |
| RISK-04 | Medium | Medium until a second LHC Admin is trained (COND-02) | Grace Tan, LHC Manager | 2026-09-11 | 2027-01-31 |
| RISK-07 | Medium | Medium: paired-region restore untested (LIM-04) | Priya Nair, ITS Application Lead | 2026-09-11 | 2027-03-31 |

## Open items and conditions

| ID | Condition or open item | Source | Owner | Target date | Agreed by | Status |
|---|---|---|---|---|---|---|
| COND-01 | Fix the audit trail export column order, pass AC-48, then switch FLAG-01 on in production | AC-48; FR-25 | Leo Santos, ITS Developer, with Priya Nair, ITS Application Lead | 2026-11-30 | Grace Tan, LHC Manager | Open |
| COND-02 | Train a second LHC Admin and give them the role, removing the single-admin limitation | LIM-02; RISK-04 | Grace Tan, LHC Manager | 2027-01-31 | Grace Tan, LHC Manager | Open |

## Support and operations ownership after handover

| Responsibility | Owner | Team | Contact or support path | From |
|---|---|---|---|---|
| Business ownership and benefits | Grace Tan, LHC Manager | LHC Management | ext. 2100 | 2026-09-14 |
| Business and process support | Daniel Reyes, LHC Front Office Supervisor | LHC Front Office | bookings-admin@lhc.example.org, ext. 2120 | 2026-09-14 |
| Technical support and incidents | Mark Lim, ITS Service Desk Lead | ITS Service Desk | servicedesk.its.example.org, ext. 4000; on call ext. 4999 | 2026-09-14 |
| Hosting and infrastructure | Priya Nair, ITS Application Lead | ITS Application Team | ITS service desk queue "LHC Booking System" | 2026-09-14 |
| Access administration | Daniel Reyes, LHC Front Office Supervisor | LHC Front Office | BUS-04 Access request; urgent removal through ITS Service Desk | 2026-09-14 |
| Data ownership | Grace Tan, LHC Manager | LHC Management | ext. 2100 | 2026-09-14 |
| Releases and changes | Priya Nair, ITS Application Lead | ITS Application Team | ENG-08 Change management | 2026-09-14 |
| Success measure reporting | Grace Tan, LHC Manager (L1); Priya Nair, ITS Application Lead (L2 to L4) | LHC Management; ITS Application Team | SP-10 Reporting and review | 2026-09-14 |

Early-life support with extra ITS cover runs from 2026-09-14 to 2026-10-09 (BUS-07 COST-09).

## Final decisions

| Owner | Role | Decision | Date | Conditions | Notes |
|---|---|---|---|---|---|
| Grace Tan, LHC Manager | Business owner | Accept with Conditions | 2026-09-11 | COND-01, COND-02 | Go-live approved for 2026-09-14 |
| Mark Lim, ITS Service Desk Lead | Support owner | Accept | 2026-09-11 | None | |
| Priya Nair, ITS Application Lead | Technical owner | Accept | 2026-09-11 | None | Accepts RISK-07 and LIM-04 |

## Assumptions and open questions

No open questions.

## Known limitations

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-04 | The restore dry run restored a masked copy of the data in ENV-02 within the primary region; a restore into the paired Azure region has not been tested. | Recovery from a full regional outage may take longer than the 4-hour RTO (NFR-13). | Follow the ENG-08 restore procedure with the paired region as the target; test it at a future quarterly restore test (MT-11). | Priya Nair, ITS Application Lead |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-09-08 | Priya Nair | Compiled from SP-11, SP-10, BUS-08 and the dry runs | — |
| 1.0 | 2026-09-11 | Priya Nair | Accepted with the three owner decisions | Grace Tan, LHC Manager; Mark Lim, ITS Service Desk Lead; Priya Nair, ITS Application Lead, 2026-09-11 |
