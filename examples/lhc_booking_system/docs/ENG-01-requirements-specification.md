---
id: ENG-01
title: Requirements Specification
application: LHC Booking System
version: 1.0
status: Accepted
owner: Priya Nair, ITS Application Lead (Technical owner)
audience: [Engineering, Testers, Agents]
level: Standard
depth: D
contains: []
related: [BUS-02, BUS-05, ENG-02, ENG-03, ENG-08, SP-11]
last_reviewed: 2026-09-11
---
# LHC Booking System – Requirements Specification

## Purpose

States what the LHC Booking System must do and how well it must do it, so engineers and agents build the right behaviour and testers can verify it. Every functional requirement traces to a capability in BUS-02 and to the business rules it enforces, and every requirement is verified by an application acceptance criterion in SP-11.

## Scope

Covers functional requirements, non-functional requirements and constraints. Business rules are defined in BUS-05 and referenced here by ID; acceptance criteria and results are in SP-11; user journeys are in the ENG-02 section of BUS-03.

## Functional requirements

| ID | Requirement | Capabilities | Rules | Priority | Status | Notes |
|---|---|---|---|---|---|---|
| FR-01 | The system shall let a guest, or a staff member on a guest's behalf, enter a booking request in two steps ("Your stay", then "Your details") and submit it, refusing submission until BR-01, BR-02 and BR-03 are met. | C-01 | BR-01, BR-02, BR-03 | Must | Verified | TR-01 |
| FR-02 | The system shall save the request as Draft when the first step is completed and show a link that reopens that Draft. | C-01 | None | Must | Verified | |
| FR-03 | The system shall, on submission, show the booking reference and booking link, and queue NTF-01 to the guest and NTF-02 to LHC within 1 minute. | C-01, C-12 | None | Must | Verified | |
| FR-04 | The system shall show LHC Staff and LHC Admin a queue of Submitted and Under Review requests, oldest first, with each request's age in working days (REP-03). | C-03, C-11, C-14 | None | Must | Verified | |
| FR-05 | The system shall show, for a request's room type and each night of its stay, how many active rooms are not held by Confirmed or Checked In bookings, and which rooms are free to assign. | C-02 | BR-04, BR-05 | Must | Verified | |
| FR-06 | The system shall let LHC Staff or LHC Admin take a Submitted request into review and record them as its reviewer. | C-03 | None | Must | Verified | TR-02 |
| FR-07 | The system shall let the reviewer confirm a request only while BR-04 holds, and record the nightly rate in force on the check-in date. | C-04 | BR-04, BR-10 | Must | Verified | TR-05 |
| FR-08 | The system shall let the reviewer return or reject a request only with a reason that meets BR-06. | C-05 | BR-06 | Must | Verified | TR-03, TR-04 |
| FR-09 | The system shall let a guest open a Returned request from the booking link, correct it and resubmit it, until it Expires. | C-01 | BR-01, BR-02, BR-03, BR-07 | Must | Verified | TR-06 |
| FR-10 | The system shall run a nightly job at 01:30 that sends NTF-06 for requests Returned 7 days earlier and sets requests Returned 14 days earlier to Expired with NTF-07. | C-18, C-12 | BR-07 | Must | Verified | TR-07 |
| FR-11 | The system shall let LHC Staff assign or change the room of a Confirmed booking only to an active room of the booked type that meets BR-05, and send NTF-08. | C-10 | BR-05 | Must | Verified | |
| FR-12 | The system shall let LHC Staff check a guest in when BR-08 allows, and check a Checked In guest out. | C-17 | BR-08 | Must | Verified | TR-08, TR-09 |
| FR-13 | The system shall let LHC Staff change the dates, room type, number of guests or guest details of a Confirmed booking, re-applying BR-02, BR-03, BR-04 and BR-05, and send NTF-08. | C-06 | BR-02, BR-03, BR-04, BR-05 | Must | Verified | |
| FR-14 | The system shall let LHC Staff cancel a Confirmed booking only with a reason, remove its room assignment and send NTF-09. | C-07 | BR-09 | Must | Verified | TR-10 |
| FR-15 | The system shall let LHC Admin add rooms, change their room type, and activate or deactivate them, refusing a deactivation that breaks BR-11. | C-08 | BR-11 | Must | Verified | |
| FR-16 | The system shall let LHC Admin record a nightly rate per room type with a start date, and use for each confirmation the rate with the latest start date on or before the check-in date. | C-09 | BR-10 | Must | Verified | |
| FR-17 | The system shall let only LHC Management change the nightly rate of a Confirmed booking, and only with a reason of at least 10 characters. | C-09 | BR-10 | Must | Verified | BUS-05 Exceptions |
| FR-18 | The system shall send each notification in BUS-06 on its trigger, retry a failed send 5 times over 1 hour, and log every attempt and its result as a Notification log entry. | C-12 | None | Must | Verified | |
| FR-19 | The system shall let LHC Admin give, change and remove the role of a staff user account, refuse any change to the admin's own role, and let ITS Support remove any role. | C-13 | None | Must | Verified | |
| FR-20 | The system shall produce the monthly booking and occupancy report (REP-02) for a chosen calendar month as an XLSX file. | C-14 | None | Must | Verified | |
| FR-21 | The system shall produce the daily arrivals and departures list (REP-01) for a chosen date, on screen and as a PDF. | C-14 | None | Must | Verified | |
| FR-22 | The system shall show a guest, through the booking link only, the booking's status with its meaning for users from BUS-05, its dates and room type, and nothing about any other booking. | C-11 | None | Must | Verified | |
| FR-23 | The system shall record an Audit event for every status change, room assignment, booking change, room or rate change and role change, with user, time, old value and new value. | C-16 | None | Must | Verified | |
| FR-24 | The system shall give ITS Support a read-only view of any booking with its Audit events and Notification log entries. | C-11, C-15 | None | Must | Verified | |
| FR-25 | The system shall let ITS Support export the Audit events of a booking or staff user account as a CSV file (REP-04). | C-15, C-16 | None | Should | Built | Off in production (FLAG-01) until COND-01 |
| FR-26 | The system shall let guests change or cancel their own Confirmed booking through the booking link. | C-06, C-07 | None | Won't | Proposed | Not in this release (LIM-01) |

## Non-functional requirements

| ID | Category | Requirement | Target | Measurement method | Priority | Status |
|---|---|---|---|---|---|---|
| NFR-01 | Availability | The guest form and staff screens are available | ≥ 99.5% of 5-minute health checks succeed per calendar month, 24 hours a day, excluding announced maintenance on Sundays 22:00–24:00 (at most 2 h a month) | Azure availability test on /health every 5 minutes from two regions; monthly availability report (SM-07) | Must | Verified |
| NFR-02 | Performance | Pages and submissions respond quickly under normal peak load | p95 page response ≤ 2 s and p95 submission ≤ 3 s at 30 concurrent users with 10,000 bookings stored | Load test before go-live; Application Insights p95 by page in operation | Must | Verified |
| NFR-03 | Capacity | The system handles the expected volume with room to grow | 5,000 bookings a year, 40 rooms, 30 concurrent users, 10 years of anonymised bookings, within NFR-02 targets | Load test with 10,000 bookings and 30 virtual users; yearly volume check | Must | Verified |
| NFR-04 | Security | Only authorised people see booking data | 100% of staff sign-ins through Entra ID single sign-on with MFA; guests reach a booking only with a booking link carrying a random token of at least 128 bits; 0 bookings readable without a valid token | Entra ID conditional-access policy and sign-in log review; penetration test | Must | Verified |
| NFR-05 | Security | Known vulnerabilities are fixed promptly | 0 High or Critical findings open from the pre-go-live penetration test; no High or Critical dependency alert open more than 30 days | Penetration test report; weekly dependency scan in CI | Must | Verified |
| NFR-06 | Security | The public form resists automated abuse | At most 10 submissions per hour from one client IP address; the 11th is refused with HTTP 429 | Automated test; WAF and application logs | Must | Verified |
| NFR-07 | Privacy | Guest personal data is kept no longer than BUS-06 allows | Drafts deleted within 1 day after 30 days without change; booking personal fields anonymised within 1 day after 2 years from the final status; no guest name, email or phone in application logs | Nightly job counts in its log; monthly purge check (MT-12); log sample inspection | Must | Verified |
| NFR-08 | Accessibility | Every guest and staff screen is accessible | Meets WCAG 2.2 AA: 0 AA failures in the accessibility audit | Automated scan of every page plus a manual keyboard and screen-reader check of J-01 to J-09 | Must | Verified |
| NFR-09 | Compatibility | Works on the browsers guests and staff use | Latest two major versions of Chrome, Edge, Firefox and Safari (macOS and iOS), and Chrome on Android; screens from 360 px wide | Journey test run on each browser before each major release | Must | Verified |
| NFR-10 | Maintainability | Changes can be tested quickly | Full automated test suite runs in ≤ 10 min in CI; line coverage ≥ 80% on the bookings domain module | CI run time and coverage report | Should | Verified |
| NFR-11 | Observability | Problems can be found quickly | Every request carries a correlation ID shown on error pages; errors appear in Application Insights within 2 minutes; logs kept 90 days | Inspection of error page and log query; log retention setting | Must | Verified |
| NFR-12 | Data retention | Audit and notification records are kept for their periods and then removed | Audit events kept 3 years and deleted within 1 day after; Notification log entries kept 2 years and deleted within 1 day after | Nightly job log; retention configuration inspection | Must | Verified |
| NFR-13 | Recoverability | Recovery time objective (RTO) | ≤ 4 h from declared outage to service restored | Timed restore test, ENG-08 Restore tests | Must | Verified |
| NFR-14 | Recoverability | Recovery point objective (RPO) | ≤ 1 h of data loss | Point-in-time restore test and backup configuration, ENG-08 | Must | Verified |

Categories not applicable: None.

## Constraints

| Constraint | Type | Source | Impact on design |
|---|---|---|---|
| Must run in the ITS Azure subscription on ITS-supported services | Hosting | ITS cloud hosting policy, 2025 | Azure App Service and Azure Database for PostgreSQL (ADR-001) |
| Staff must sign in with their organisation account through Entra ID | Technology | ITS identity standard | OpenID Connect sign-in; no local staff passwords (ADR-003) |
| Email must be sent through the organisation's M365 tenant | Technology | ITS email standard | SMTP to M365 with a dedicated mailbox (ADR-005) |
| Public services must meet WCAG 2.2 AA | Regulatory | Organisation digital services policy | Server-rendered accessible pages (NFR-08) |
| Guest personal data handled under the organisation privacy policy | Regulatory | Privacy policy, sections 3 and 5 | Retention and anonymisation (NFR-07), privacy impact assessment (BUS-08) |
| Infrastructure running cost at most USD 3,000 a year | Budget | LHC 2026 budget, Grace Tan | Small single-region service tiers (ENG-03 Technical risks and debt) |
| Live before the peak season starting 2026-10-01 | Schedule | LHC service plan | Guest self-service changes deferred (FR-26) |

## Verification rule

Every FR and NFR has at least one application acceptance criterion in SP-11 whose `Verifies` column lists its ID. A requirement moves to Verified only when those criteria pass. FR-25 is Built, not Verified: its criterion was waived at go-live (SP-11, SP-12).

## Assumptions and open questions

No open questions.

## Known limitations

No known limitations beyond FR-26 (Won't, recorded as LIM-01 in BUS-02).

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-04-06 | Priya Nair | First draft | — |
| 0.9 | 2026-04-20 | Priya Nair | Accepted at stage 2 | Priya Nair, ITS Application Lead; Grace Tan, LHC Manager (priorities), 2026-04-20 |
| 1.0 | 2026-09-11 | Leo Santos | Statuses updated to Verified or Built from the SP-11 results; accepted at go-live | Priya Nair, ITS Application Lead, 2026-09-11 |
