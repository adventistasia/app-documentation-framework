---
id: ENG-10
title: Decision Log
application: LHC Booking System
version: 1.0
status: Accepted
owner: Priya Nair, ITS Application Lead (Technical owner)
audience: [Engineering, Technical owner, Agents]
level: Standard
depth: D
contains: []
related: [ENG-01, ENG-03, ENG-04, ENG-09, BUS-05]
last_reviewed: 2026-09-11
---
# LHC Booking System – Decision Log

## Purpose

Records the significant technical and product decisions for the LHC Booking System as architecture decision records (ADRs): what was decided, why, what was rejected and what follows. It exists so that nobody, human or agent, undoes a deliberate choice without knowing why it was made.

## Scope

Covers decisions about technology, structure, data, security, hosting and deliberate omissions. Requirements and constraints imposed from outside are in ENG-01; the resulting design is described in ENG-03.

## When to write an ADR

Write an ADR for any choice a new engineer or an agent might otherwise "fix": framework, data store and hosting choices; the authentication approach; deliberate omissions; patterns that look odd but are intended; and anything that replaces an earlier ADR. Choices that follow directly from the ENG-09 coding conventions need none.

## Decision index

| ID | Title | Status | Date | Deciders |
|---|---|---|---|---|
| ADR-001 | One Django application on Azure App Service with PostgreSQL | Accepted | 2026-03-16 | Priya Nair, ITS Application Lead; Tom Rivera, ITS Infrastructure Manager |
| ADR-002 | Prevent double-booking with a database exclusion constraint | Accepted | 2026-06-08 | Priya Nair, ITS Application Lead; Leo Santos, ITS Developer |
| ADR-003 | Entra ID sign-in for staff; booking links, not accounts, for guests | Accepted | 2026-03-16 | Priya Nair, ITS Application Lead; Grace Tan, LHC Manager; Ruth Ong, Data Protection Officer |
| ADR-004 | Room assignment is an action on a Confirmed booking, not a status | Accepted | 2026-04-14 | Priya Nair, ITS Application Lead; Daniel Reyes, LHC Front Office Supervisor |
| ADR-005 | Send email through a transactional outbox and a worker | Accepted | 2026-04-14 | Priya Nair, ITS Application Lead; Leo Santos, ITS Developer |

## Decision records

### ADR-001 One Django application on Azure App Service with PostgreSQL

- **Status:** Accepted
- **Date:** 2026-03-16
- **Deciders:** Priya Nair, ITS Application Lead; Tom Rivera, ITS Infrastructure Manager

**Context**

The application is small (about 45 requests a week, 30 concurrent users at most, NFR-03), must run on ITS-supported Azure services (ENG-01 Constraints), and will be maintained by an ITS team of two whose main language is Python. It must be recoverable within 4 hours (NFR-13).

**Decision**

We will build one Django application, packaged as one container image, that runs as the web application, the outbox worker and the nightly job on one Azure App Service plan, with Azure Database for PostgreSQL Flexible Server as the only data store.

**Alternatives considered**

| Option | Advantages | Disadvantages | Why not chosen |
|---|---|---|---|
| Separate front end (single-page app) and API | Richer screens | Two codebases and deployments; harder accessibility | Not needed for forms and lists; more to maintain |
| Low-code platform (Power Apps with Dataverse) | Fast to build | Guest access needs extra licences; weak control of the no-overlap rule | Licence cost for public users; BR-05 could not be enforced in the data store |
| Azure Functions for the worker and job | Scales to zero | A second deployment model for a tiny load | Simpler to run everything from one image |

**Consequences**

- Positive: one image, one pipeline, one place to look; restart restores all three processes.
- Negative: the worker and nightly job share the web plan's resources; a long nightly step could slow pages at 01:30 (acceptable at night).
- Follow-up: scale to plan B3 above 30 concurrent users (BUS-07).

**Links:** ENG-03 Containers; NFR-02, NFR-03, NFR-13

### ADR-002 Prevent double-booking with a database exclusion constraint

- **Status:** Accepted
- **Date:** 2026-06-08
- **Deciders:** Priya Nair, ITS Application Lead; Leo Santos, ITS Developer

**Context**

Double-booking was the most damaging problem of the old email and spreadsheet process (4 incidents a quarter, BUS-01; RISK-05). A check in application code alone can be beaten by two staff assigning the same room at the same moment, or by a future defect.

**Decision**

We will store one booking_night row per night (ENT-08) and enforce BR-05 with a PostgreSQL exclusion constraint `no_double_booking` on room and night for bookings that hold a room. The application still checks first, to show a clear message; the constraint is the guarantee.

**Alternatives considered**

| Option | Advantages | Disadvantages | Why not chosen |
|---|---|---|---|
| Application check only | Simple | Race conditions; defects can bypass it | Does not guarantee BR-05 |
| Date-range column with a range exclusion constraint on the booking | No extra table | Harder to report per night; room changes mid-stay not possible later | booking_night also serves REP-01 and REP-02 |
| Table lock on every assignment | Guarantees order | Blocks all staff during each assignment | Unnecessary contention |

**Consequences**

- Positive: two guests can never be given one room on one night, whatever the code does; OC-01 should always return 0 rows.
- Negative: an extra table to keep in step with booking dates; date changes rewrite booking_night rows.
- Follow-up: the database error 23P01 is mapped to the BUS-09 message; never remove the constraint (ENG-09 Agent rules).

**Links:** BUS-05 BR-05; ENG-04 ENT-08; ENG-03 J-05 runtime view; RISK-05; AC-27

### ADR-003 Entra ID sign-in for staff; booking links, not accounts, for guests

- **Status:** Accepted
- **Date:** 2026-03-16
- **Deciders:** Priya Nair, ITS Application Lead; Grace Tan, LHC Manager; Ruth Ong, Data Protection Officer

**Context**

Staff already have organisation accounts with MFA, and the ITS identity standard forbids local staff passwords (ENG-01 Constraints). Guests book once or twice a year; asking them to create accounts would add a password store and put off guests, while they still need to see and correct their request (NFR-04).

**Decision**

We will sign staff in only through Entra ID OpenID Connect with MFA, keeping roles in the application (ENT-06). Guests will have no accounts: each booking has a booking link carrying a random 128-bit token, stored only as a hash.

**Alternatives considered**

| Option | Advantages | Disadvantages | Why not chosen |
|---|---|---|---|
| Guest accounts with email and password | Guests see all their bookings | Password store, resets, more personal data | Disproportionate for occasional guests |
| Email one-time codes for guests | No forwarded-link risk | Depends on email for every view; extra step each time | Email delays (D-04) would lock guests out |
| Roles from Entra ID groups | Access managed by ITS | LHC Admin could not manage roles; group changes are slow | LHC wants to give roles the same day (BUS-04) |

**Consequences**

- Positive: no passwords stored; leavers lose access when their organisation account is disabled (RISK-10).
- Negative: anyone holding a forwarded booking link can see that booking (RISK-01).
- Follow-up: the booking page warns guests not to share the link; links stop working when the booking is anonymised.

**Links:** ENG-05 INT-02; ENG-03 Security; RISK-01, RISK-10; NFR-04

### ADR-004 Room assignment is an action on a Confirmed booking, not a status

- **Status:** Accepted
- **Date:** 2026-04-14
- **Deciders:** Priya Nair, ITS Application Lead; Daniel Reyes, LHC Front Office Supervisor

**Context**

The old process used "Room assigned" as if it were a status alongside Confirmed and Modified, which left bookings with unclear states when a room was changed or dates moved. Staff often assign rooms only on the morning of arrival, and may change a room several times.

**Decision**

We will keep room assignment, and changes to dates or details, as actions on a Confirmed booking that are recorded in the audit trail. The status lifecycle in BUS-05 has no "Room assigned" or "Modified" status; check-in requires a room (BR-08).

**Alternatives considered**

| Option | Advantages | Disadvantages | Why not chosen |
|---|---|---|---|
| A "Room Assigned" status between Confirmed and Checked In | Visible in the queue | Reassignment and date changes need extra transitions back | More transitions with no business decision attached |
| A "Modified" status | Shows that a booking changed | Hides the real state; the old process's confusion | History is in the audit trail instead |

**Consequences**

- Positive: ten statuses that each mean a business state; reassignment needs no transition.
- Negative: "has a room" must be shown separately on lists (the arrivals list shows it).
- Follow-up: none.

**Links:** BUS-05 Statuses and transitions; BR-08; ENG-04 ENT-08

### ADR-005 Send email through a transactional outbox and a worker

- **Status:** Accepted
- **Date:** 2026-04-14
- **Deciders:** Priya Nair, ITS Application Lead; Leo Santos, ITS Developer

**Context**

Every decision must reach the guest (FR-03, FR-18), but M365 SMTP is occasionally slow or unavailable (D-04; RISK-03). Sending inside the web request would make submissions fail or hang when M365 does, and an email could be sent for a change that was then rolled back.

**Decision**

We will write each notification as an outbox row (ENT-05) in the same database transaction as the change that triggers it; the outbox worker (CMP-02) sends it, retrying 5 times over 1 hour, and records every attempt.

**Alternatives considered**

| Option | Advantages | Disadvantages | Why not chosen |
|---|---|---|---|
| Send synchronously in the request | Simplest | Page fails when M365 does; no retries | Breaks NFR-02 and FR-18 |
| Azure Service Bus queue | Managed retries | New dependency and cost; email and change not in one transaction | The database already gives transactional safety |
| Microsoft Graph API instead of SMTP | Modern authentication | Needs an Exchange application access policy and more ITS setup | Revisit with Q-03 (SMTP AUTH retirement) |

**Consequences**

- Positive: an email exists exactly when its change exists; outages delay email instead of failing pages; the notification log is the delivery evidence (REC-04).
- Negative: emails can be up to 30 s late; the worker is one more process to watch (ALR-03).
- Follow-up: RB-03 in ENG-08; Q-03 in ENG-05 may lead to an ADR replacing SMTP with Graph.

**Links:** ENG-03 J-01 runtime view; ENG-05 INT-01; FR-18; RISK-03

## Assumptions and open questions

No open questions.

## Known limitations

No known limitations.

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-03-16 | Priya Nair | ADR-001 and ADR-003 at stage 2 | — |
| 0.2 | 2026-06-08 | Leo Santos | ADR-002, ADR-004 and ADR-005 recorded | — |
| 1.0 | 2026-09-11 | Priya Nair | Accepted at go-live | Priya Nair, ITS Application Lead, 2026-09-11 |
