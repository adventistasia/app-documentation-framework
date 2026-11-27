---
id: BUS-01
title: Application Overview & Business Case
application: LHC Booking System
version: 1.0
status: Accepted
owner: Grace Tan, LHC Manager (Business owner)
audience: [Management, Business owner, Support, Engineering, Agents, Everyone]
level: Standard
depth: D
contains: [SP-01]
related: [SP-00, SP-10, BUS-02, BUS-07, BUS-08, ENG-01, ENG-08, SP-12]
last_reviewed: 2026-09-11
---
# LHC Booking System – Application Overview & Business Case

## Purpose

The first document anyone reads about the LHC Booking System. It explains what the application is, why LHC needs it, what it is worth, what success looks like, and who owns and supports it. The business owner uses it to judge whether the application is worth running; everyone else uses it to find the right detailed document.

## Scope

Covers the identity, business case, success statement, ownership and scope of the LHC Booking System, a map of the documentation package, and the shared glossary (SP-01, held here as a section). Details live in the linked documents: capabilities in BUS-02, costs in BUS-07, risks in BUS-08, success measures in SP-10, requirements in ENG-01, support in ENG-08.

## Application at a glance

Guests ask for a room at the LHC guest house through a public online form. LHC Staff review each request, check availability, and confirm, return or reject it; they then assign a room, check the guest in and check them out. LHC Admins keep the room list, rates and staff access up to date, and LHC Management receives a monthly booking and occupancy report. ITS supports the application technically.

| Item | Value |
|---|---|
| Access point | Guests: https://booking.lhc.example.org (also linked from the LHC website). Staff: https://booking.lhc.example.org/staff |
| Access method | Guests: public form, no account; each booking has a private link sent by email. Staff: organisation single sign-on. |
| How to get access | Staff ask the LHC Admin; see BUS-04 Access request. Guests need no access. |
| Hours of use | Guests 24 hours a day. LHC front office staffed Monday to Saturday 07:00–21:00. |

## Problem statement

| Item | Description |
|---|---|
| Current situation | Before go-live, about 45 booking requests a week arrived by email, phone and walk-in. Staff re-keyed each one into a shared spreadsheet, checked availability by eye, and replied by email. |
| Who is affected | Guests, who waited a median of 3 working days for an answer; LHC Staff, who spent about 6 hours a week re-keying; LHC Management, who had no reliable occupancy figures. |
| Cost today | About 312 staff hours a year of re-keying (about USD 7,800 at USD 25 an hour); about 4 double-bookings a quarter, each costing about USD 150 in upgrades or refunds (USD 2,400 a year); 8 hours a month to compile the monthly report by hand (about USD 2,400 a year). Total about USD 12,600 a year, plus lost bookings from slow replies, which were not measured. |

## Benefits

| ID | Benefit | Beneficiary | Measure | Baseline | Target | By when | Benefit owner |
|---|---|---|---|---|---|---|---|
| BEN-01 | Guests get a decision on their request within one working day | Guests | SM-01 | Median 3 working days (Jan–Mar 2026) | Median ≤ 1 working day | 2026-12-31 | Grace Tan, LHC Manager |
| BEN-02 | Staff no longer re-key requests from email and phone | LHC Staff | SM-02 | 6 hours a week (Feb 2026) | ≤ 1 hour a week | 2026-12-31 | Grace Tan, LHC Manager |
| BEN-03 | No room is double-booked | Guests, LHC | SM-03 | 4 incidents a quarter (2025) | 0 a quarter | 2026-12-31 | Grace Tan, LHC Manager |
| BEN-04 | Management gets monthly occupancy figures without manual spreadsheets | LHC Management | SM-04 | 8 hours a month (2025) | ≤ 0.5 hour a month | 2026-12-31 | Grace Tan, LHC Manager |

## What success looks like

Every booking request gets a decision within one working day, and the guest is told by email. Staff no longer copy requests from email into a spreadsheet. No guest arrives to find their room given to someone else. LHC Management receives the monthly booking and occupancy report on the first working day of each month without anyone building it by hand. When something goes wrong, staff know whom to call and get an answer the same day.

## Impact if unavailable

| Outage length | Impact | Workaround |
|---|---|---|
| Up to 4 hours | Guests cannot submit requests; staff cannot confirm or check guests in on screen. Guests arriving that day are still expected. | Staff use the printed daily arrivals list (REP-01, printed each morning) to check guests in on paper and take new requests by phone on the paper form; entered into the application when it returns. |
| 4 hours to 1 working day | Requests are not answered within the one-working-day target; confirmation emails are delayed. | As above; staff phone guests whose stays start within 2 days. |
| More than 1 working day | Bookings for the coming week cannot be confirmed reliably; risk of double-booking from paper records. | LHC Manager decides to stop taking new bookings beyond 7 days until service returns; ITS restores from backup (ENG-08). |

## Strategic fit

Supports the LHC 2026 service plan goal "answer every guest within one working day" and the organisation's digital services policy, which requires public services to be online and accessible (WCAG 2.2 AA).

## Users and stakeholders

| Stakeholder | Description | Main interest | Role |
|---|---|---|---|
| Guests | Members of the public and visiting staff who want to stay at LHC | A quick, clear answer and a confirmed room | R-01 |
| LHC front office staff | Review requests, confirm bookings, assign rooms, check guests in and out | One accurate place to see and decide requests | R-02 |
| LHC front office supervisor | Maintains rooms, rates and staff access; handles corrections | Accurate room and rate data; control of who can do what | R-03 |
| LHC Manager and management team | Own the service and its results | Occupancy and response-time figures; fewer complaints | R-04 |
| ITS Service Desk and application team | Support, host and change the application | Clear runbooks; few incidents | R-05 |
| LHC Finance | Uses the monthly report for income planning | A report that matches the bookings | None |
| Data Protection Officer | Oversees use of guest personal data | Lawful, minimal, time-limited use of guest data | None |

## Ownership

| Responsibility | Name and role | Team | Contact |
|---|---|---|---|
| Business owner | Grace Tan, LHC Manager | LHC Management | grace.tan@lhc.example.org, ext. 2101 |
| Support owner | Mark Lim, ITS Service Desk Lead | ITS Service Desk | servicedesk@its.example.org, ext. 4000 |
| Technical owner | Priya Nair, ITS Application Lead | ITS Application Team | priya.nair@its.example.org, ext. 4120 |

## In scope and out of scope

**In scope:**
- Submit booking request, Check room availability, Review booking request, Confirm booking, Return or reject request (BUS-02).
- Assign room, Check guests in and out, Modify booking, Cancel booking.
- Manage room records, Manage room rates, Manage user access and roles.
- Send notifications, Expire unanswered returned requests, Track booking status, Generate booking reports, Handle support issue, Maintain audit trail.

**Out of scope:**
- Taking payment or deposits; these stay at the front desk outside the application.
- Guests changing or cancelling their own booking online; they email or phone LHC (LIM-01 in BUS-02).
- Housekeeping, maintenance scheduling and room keys.
- Sending data to the finance system; LHC Finance receives the monthly report as a spreadsheet.

## Key non-functional commitments

| Commitment | Requirement |
|---|---|
| Available 99.5% of each month, around the clock, apart from an announced Sunday 22:00–24:00 maintenance window | NFR-01 |
| Pages open within 2 seconds for 95% of views with 30 people using it at once | NFR-02 |
| Staff sign in with the organisation account and a second factor; guests see only their own booking | NFR-04 |
| Guest personal details are anonymised 2 years after the stay ends | NFR-07 |
| Usable by people with disabilities (WCAG 2.2 AA) on current Chrome, Edge, Firefox and Safari, including phones | NFR-08, NFR-09 |
| After a failure, service is back within 4 hours, losing at most the last hour of changes | NFR-13, NFR-14 |

## Resources and costs summary

Running the application costs about USD 8,500 a year: about USD 1,700 for hosting, database and monitoring in the ITS Azure subscription, USD 20 for the domain, and about USD 6,800 of staff time (6 hours a month of LHC Admin upkeep and checks, 3 hours a month of ITS Service Desk support, 6 hours a month of ITS application maintenance and 1 hour a month of management review). The one-off build and go-live cost was about USD 23,600, mostly ITS developer time. Against the about USD 12,600 a year that the old way cost, the saving is about USD 4,000 a year plus faster answers for guests. The budget holder is Grace Tan, LHC Manager. Detail is in BUS-07.

## Documentation package

| Document | Depth | Where |
|---|---|---|
| SP-00 Scope Record | D | SP-00-scope-record.md |
| SP-01 Glossary | S | Section in this file |
| SP-10 Success Measures Register | D | SP-10-success-measures.md |
| SP-11 Acceptance Criteria & Verification Register | D | SP-11-acceptance-criteria-and-verification.md |
| SP-12 Acceptance & Handover Record | D | SP-12-acceptance-and-handover-record.md |
| BUS-01 Application Overview & Business Case | D | This file |
| BUS-02 Capabilities Register | D | BUS-02-capabilities-register.md |
| BUS-03 Business Process Register | D | BUS-03-business-process-register.md |
| BUS-04 Roles & Access Matrix | D | BUS-04-roles-and-access-matrix.md |
| BUS-05 Business Rules & Status Lifecycle | D | BUS-05-business-rules-and-status-lifecycle.md |
| BUS-06 Data, Reports & Notifications Register | D | BUS-06-data-reports-and-notifications.md |
| BUS-07 Resource & Cost Model | D | BUS-07-resource-and-cost-model.md |
| BUS-08 Risk & Controls Register | D | BUS-08-risk-and-controls-register.md |
| BUS-09 User & Admin Guide | D | BUS-09-user-and-admin-guide.md |
| ENG-01 Requirements Specification | D | ENG-01-requirements-specification.md |
| ENG-02 User Journeys | S | Section in BUS-03-business-process-register.md |
| ENG-03 Architecture & Design | D | ENG-03-architecture-and-design.md |
| ENG-04 Data Model | D | ENG-04-data-model.md |
| ENG-05 Integrations & Dependencies Register | D | ENG-05-integrations-and-dependencies.md |
| ENG-06 Configuration & Environments | S | Section in ENG-09-developer-and-agent-guide.md |
| ENG-07 Deployment & Release Guide | D | ENG-07-deployment-and-release.md |
| ENG-08 Operations & Support Runbook | D | ENG-08-operations-and-support-runbook.md |
| ENG-09 Developer & Agent Guide | D | ENG-09-developer-and-agent-guide.md (root AGENTS.md points to it) |
| ENG-10 Decision Log | D | ENG-10-decision-log.md |

## SP-01 Glossary

### Terms

| Term | Definition | Synonyms to avoid | Defined in | Category |
|---|---|---|---|---|
| Audit event | A record of who did what to a booking, room, rate or user account, and when. | Log, history | BUS-06 REC-06 | Record |
| Booking | One guest's stay request and everything that happens to it, from Draft to its final status. | Reservation | BUS-06 REC-01 | Record |
| Booking link | The private web link, sent to the guest by email, that shows one booking's status and lets the guest correct a Returned request. | Guest login, account | ENG-03 Security | Business term |
| Booking request | A Booking that has not yet been decided: Draft, Submitted, Under Review or Returned. | Pending booking | BUS-05 | Business term |
| Cancelled | The booking was confirmed but has been called off; the room is free again for those nights. | Canceled, Voided | BUS-05 ST-09 | Status |
| Checked In | The guest has arrived and is staying in the assigned room. | In house, Occupied | BUS-05 ST-07 | Status |
| Completed | The guest has checked out; the stay is finished. | Closed, Checked out | BUS-05 ST-08 | Status |
| Confirmed | LHC has accepted the booking and holds a room of the requested type for every night of the stay. | Approved, Accepted, Room assigned | BUS-05 ST-06 | Status |
| Draft | A request that has been started and saved but not yet sent to LHC. | Incomplete | BUS-05 ST-01 | Status |
| Exclusion constraint | A database rule that refuses to store two rows whose values overlap, used here so a room can never hold two bookings on the same night. | None | ENG-04 ENT-08 | Technical term |
| Expired | A Returned request that the guest did not correct within 14 days; it is closed and cannot be resubmitted. | Lapsed, Timed out | BUS-05 ST-10 | Status |
| Guest | A person who asks to stay at LHC, using the public form and their booking link; guests have no account. | Customer, Client, User | BUS-04 R-01 | Role |
| ITS Support | ITS Service Desk and application team members who support, fix and administer the application technically. | IT, Support, Admin | BUS-04 R-05 | Role |
| LHC Admin | LHC front office supervisor who maintains rooms, rates and staff access, and corrects records. | Admin, Administrator | BUS-04 R-03 | Role |
| LHC Management | LHC Manager and management team, who own the service, read reports and approve exceptions. | Manager, Owner | BUS-04 R-04 | Role |
| LHC Staff | Front office staff who review requests and manage bookings and stays. | Booking staff, Reception, Front desk | BUS-04 R-02 | Role |
| Night | One overnight stay counted by its date; a stay from 3 May to 5 May has the nights of 3 and 4 May. | Day | BUS-05 BR-04 | Business term |
| Notification log entry | A record of one email the application sent or tried to send, with its result. | Email log | BUS-06 REC-04 | Record |
| Outbox | The database table where emails wait until the worker sends them, so a slow email service never blocks a page. | Mail queue | ENG-03 CMP-02 | Technical term |
| Point-in-time restore | Restoring the database to its state at a chosen minute in the last 35 days. | PITR | ENG-08 Backup and restore | Technical term |
| Rejected | LHC has decided it cannot accept the request; the decision is final. | Declined, Denied | BUS-05 ST-05 | Status |
| Returned | LHC needs the guest to correct or complete the request before deciding. | Sent back, On hold | BUS-05 ST-04 | Status |
| Room | One bookable room at LHC, with its number, type and whether it is active. | Unit | BUS-06 REC-02 | Record |
| Room assignment | Linking a specific room to a Confirmed booking; it is an action, not a status, and can be changed until check-in. | Allocation | BUS-05 BR-05 | Business term |
| Room rate | The nightly price for a room type from a given date. | Price, Tariff | BUS-06 REC-03 | Record |
| Room type | A group of identical rooms, for example Standard Twin, with a capacity in guests. | Category | ENG-04 ENT-03 | Business term |
| Staff user account | A staff member's access to the staff screens and the role they hold. | Login | BUS-06 REC-05 | Record |
| Submitted | The guest has sent the request and it is waiting for LHC to start reviewing it. | Pending, New | BUS-05 ST-02 | Status |
| Under Review | An LHC Staff member is reviewing the request. | In progress, Processing | BUS-05 ST-03 | Status |
| Working day | Monday to Friday excluding public holidays, the unit used for response-time targets. | Business day | SP-10 SM-01 | Business term |

### Abbreviations

| Abbreviation | Stands for | Meaning or see |
|---|---|---|
| ADR | Architecture decision record | ENG-10 |
| CI | Continuous integration | The pipeline that tests every change, ENG-07 |
| ITS | Information Technology Services | The organisation's IT department |
| LHC | The guest house that runs the application | — |
| M365 | Microsoft 365 | Provides the email service (ENG-05 D-04) |
| MFA | Multi-factor authentication | A second sign-in step, for example a phone app prompt |
| OIDC | OpenID Connect | The single sign-on protocol (ENG-05 INT-02) |
| PIA | Privacy impact assessment | BUS-08 |
| RPO | Recovery point objective | The most data, in time, that may be lost after a failure (NFR-14) |
| RTO | Recovery time objective | The longest time to restore service after a failure (NFR-13) |
| SLI / SLO | Service level indicator / objective | A measured indicator and its target (SP-10 L3) |
| SMTP | Simple Mail Transfer Protocol | How the application hands email to M365 (ENG-05 INT-01) |
| SSO | Single sign-on | Staff sign in with their organisation account (ENG-05 D-05) |
| WCAG | Web Content Accessibility Guidelines | NFR-08 |

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | Assumption: request volume stays below 5,000 a year (NFR-03); check at the first benefit review. | Grace Tan, LHC Manager | 2026-12-15 | Open |

## Known limitations

No known limitations of this overview. Application limitations are raised in the documents that describe them and listed in SP-12.

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-02-23 | Priya Nair | First draft with business case | — |
| 1.0 | 2026-03-02 | Priya Nair | Accepted at stage 1 with business case, benefits linked to SP-10 and glossary | Grace Tan, LHC Manager, 2026-03-02 |
| 1.0 | 2026-09-11 | Priya Nair | Reviewed at go-live: costs, NFR commitments and glossary checked against the final package, no changes | Grace Tan, LHC Manager, 2026-09-11 |
