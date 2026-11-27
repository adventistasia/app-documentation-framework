---
id: BUS-08
title: Risk & Controls Register
application: LHC Booking System
version: 1.0
status: Accepted
owner: Grace Tan, LHC Manager (Business owner)
audience: [Management, Business owner, Risk and audit, Support, Technical owner]
level: Standard
depth: D
contains: []
related: [BUS-02, BUS-03, BUS-04, BUS-06, ENG-03, ENG-05, SP-12]
last_reviewed: 2026-09-11
---
# LHC Booking System – Risk & Controls Register

## Purpose

Records what can go wrong with the LHC Booking System, how likely and how bad each risk is, the controls that reduce it, who owns it, and what risk remains and who has accepted it.

## Scope

Covers application risks (`RISK-xx`) in every category below. Known limitations stay in their own documents and SP-12; those that could cause harm are also raised here (LIM-02 as RISK-04, LIM-03 as RISK-03, LIM-04 as RISK-07). Incident handling is in ENG-08; technical debt is described in ENG-03 and linked to RISK-02, RISK-06 and RISK-07.

## Rating guidance

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

| ID | Risk | Category | Affects | Likelihood | Impact | Severity | Control | Owner | Residual risk | Accepted by | Review cadence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RISK-01 | If a guest forwards their booking link or it is read from a shared mailbox, someone else opens the booking, and that guest's name, dates and contact details are disclosed. | Privacy and compliance | C-01, C-11, REC-01 | Medium | High | High | Existing: random 128-bit token per booking (NFR-04); the status page shows no other booking and no staff names (FR-22); links stop working when the booking is anonymised (NFR-07); the booking page warns guests not to share the link. Planned: none. | Priya Nair, ITS Application Lead | Medium | Grace Tan, LHC Manager, 2026-09-11 | Quarterly |
| RISK-02 | If the anonymisation step of the nightly job fails or is skipped without notice, guest personal data is kept beyond 2 years, and LHC breaches the privacy policy and BUS-06 retention. | Privacy and compliance | C-18, REC-01, REC-04 | Low | High | Medium | Existing: every step writes its count to nightly_run; ALR-05 when the run does not succeed; monthly check of purge counts (MT-12); AC-56 in the regression suite. Planned: split the nightly job into separate steps with their own alerts (ENG-03 technical debt). | Priya Nair, ITS Application Lead | Low | — | Quarterly |
| RISK-03 | If M365 email is unavailable or the mailbox is blocked, decisions and reminders are not delivered, and guests arrive unconfirmed or miss the 14-day window. | Dependency | C-12, D-04, LIM-03 | Medium | Medium | Medium | Existing: outbox with 5 retries over 1 hour (FR-18); ALR-03; failed-email list worked daily with phone calls (MT-02); RB-03. | Kevin Ho, ITS Network and M365 Administrator | Low | — | Quarterly |
| RISK-04 | If the single LHC Admin is away or leaves, rooms, rates and staff roles cannot be maintained, and availability or access becomes wrong. | Support | C-08, C-09, C-13, LIM-02 | Medium | Medium | Medium | Existing: ITS Support can remove roles and deactivate rooms on the LHC Manager's written request (BUS-04). Planned: train a second LHC Admin by 2027-01-31 (COND-02). | Grace Tan, LHC Manager | Medium | Grace Tan, LHC Manager, 2026-09-11 | Monthly until COND-02 is closed |
| RISK-05 | If two staff assign the same room for overlapping nights, or a booking is entered outside the system, two guests are given one room, and a guest arrives with nowhere to stay. | Operational | C-02, C-10, BR-05, REC-01, REC-02 | High | High | High | Existing: the database refuses two assignments of one room on one night (ADR-002, ENT-08); availability counts every Confirmed and Checked In booking (BR-04); nightly OC-01 with ALR-06; all bookings, including phone requests, are entered in the application (W-01). | Daniel Reyes, LHC Front Office Supervisor | Low | Grace Tan, LHC Manager, 2026-09-11 | Quarterly |
| RISK-06 | If a script submits large numbers of requests through the public form, the queue fills with junk, and real requests wait past one working day. | Technical | C-01, C-03, W-01, W-02 | Medium | Medium | Medium | Existing: 10 submissions an hour per address (NFR-06); App Service access restrictions to block an address (RB-04); a honeypot field on the form. Planned: move the rate-limit counter from memory to the database so it holds across instances (ENG-03 technical debt). | Priya Nair, ITS Application Lead | Low | — | Quarterly |
| RISK-07 | If the whole Azure region is lost, the service is restored from geo-redundant backups into a region where that has never been tested, and the 4-hour RTO is missed. | Dependency | D-02, LIM-04 | Low | High | Medium | Existing: geo-redundant backups (35 days); tested restore in the primary region (ENG-08); manual business fallback from the printed arrivals list. Planned: a paired-region restore at a future quarterly test (MT-11). | Priya Nair, ITS Application Lead | Medium | Priya Nair, ITS Application Lead, 2026-09-11 | Yearly |
| RISK-08 | If the monthly report counts bookings or rates wrongly, LHC Management and Finance plan income and staffing on wrong figures. | Reporting | C-14, REP-02, REC-01, REC-03 | Medium | Medium | Medium | Existing: golden data test (AC-43); reconciliation before every report (OC-02); monthly sample audit (OC-04). | Daniel Reyes, LHC Front Office Supervisor | Low | — | Quarterly |
| RISK-09 | If LHC Facilities take a room out of use and the LHC Admin is not told, availability includes that room, and a booking is confirmed with no usable room. | Data | C-02, C-08, D-06, REC-02 | Medium | Medium | Medium | Existing: Facilities email room changes to bookings-admin@lhc.example.org on the day (ENG-05 D-06); deactivation is blocked while bookings hold the room (BR-11), so the admin must move them; weekly room list check against the Facilities notice. | Daniel Reyes, LHC Front Office Supervisor | Low | — | Quarterly |
| RISK-10 | If a staff member leaves and their role is not removed, they can still read guest data and change bookings. | Access | C-13, W-07, REC-01, REC-05 | Medium | High | High | Existing: staff sign in only through Entra ID, which HR disables on the last day, so a leaver cannot sign in (ADR-003); routine removal on the HR leaver notice and urgent removal by ITS Support (BUS-04); quarterly access review (MT-10). | Daniel Reyes, LHC Front Office Supervisor | Low | Grace Tan, LHC Manager, 2026-09-11 | Quarterly |

## Privacy impact assessment

| Item | Value |
|---|---|
| Assessment status | Done |
| Link and date | PIA-2026-07 "LHC Booking System", organisation privacy register, 2026-05-20 |
| Outcome or reason not needed | Approved with three actions, all closed before go-live: keep no payment data in the application; anonymise bookings 2 years after the final status and delete Drafts after 30 days (NFR-07, BUS-06); keep guest personal data out of application logs (AC-61). Residual findings are raised as RISK-01 and RISK-02. |
| Decided by | Ruth Ong, Data Protection Officer |

## Assumptions and open questions

No open questions.

## Known limitations

No known limitations.

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-05-20 | Priya Nair | Risks drafted after the privacy impact assessment | — |
| 0.2 | 2026-08-21 | Priya Nair | Pilot risks and controls added at stage 4 | — |
| 1.0 | 2026-09-11 | Priya Nair | Accepted at go-live with the owners' risk acceptances | Grace Tan, LHC Manager; Ruth Ong, Data Protection Officer, 2026-09-11 |
