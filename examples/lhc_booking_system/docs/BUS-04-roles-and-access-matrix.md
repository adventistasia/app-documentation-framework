---
id: BUS-04
title: Roles & Access Matrix
application: LHC Booking System
version: 1.0
status: Accepted
owner: Grace Tan, LHC Manager (Business owner)
audience: [Business owner, Access approvers, Support, Auditors, Engineering]
level: Standard
depth: D
contains: []
related: [BUS-02, BUS-03, BUS-05, ENG-03, ENG-08, SP-01]
last_reviewed: 2026-09-11
---
# LHC Booking System – Roles & Access Matrix

## Purpose

Defines each role in the LHC Booking System, what it may do, who approves access to it, and how access is requested, removed and reviewed, so the LHC Admin can make access decisions and an auditor can check them from this document alone.

## Scope

Covers the five roles used in capabilities (BUS-02), processes and journeys (BUS-03), and transitions (BUS-05). How sign-in and permission checks are built is in ENG-03; how ITS Support handles access requests day to day is in ENG-08.

## Roles

| ID | Name | Description | Typical users | Role owner | Access approver |
|---|---|---|---|---|---|
| R-01 | Guest | A person asking to stay at LHC. Has no account: submits through the public form and sees only their own booking through its private link. | Members of the public, visiting staff from other sites | Grace Tan, LHC Manager | None needed: the form is public and a booking can be reached only through its link |
| R-02 | LHC Staff | Reviews and decides requests, assigns rooms, checks guests in and out, and changes or cancels bookings. | Front office officers (about 6) | Daniel Reyes, LHC Front Office Supervisor | Daniel Reyes, LHC Front Office Supervisor |
| R-03 | LHC Admin | Everything LHC Staff can do, plus maintaining rooms and rates, giving staff roles, and correcting records. | Front office supervisor (1, see LIM-02) | Grace Tan, LHC Manager | Grace Tan, LHC Manager |
| R-04 | LHC Management | Reads all bookings and reports, and approves exceptions to the confirmed-rate rule. Does not process bookings. | LHC Manager, deputy manager, finance officer (3) | Grace Tan, LHC Manager | Grace Tan, LHC Manager |
| R-05 | ITS Support | Diagnoses issues with a read-only view of bookings, history and notification logs; removes access urgently; grants the LHC Admin role. | ITS Service Desk analysts and application team (about 4) | Mark Lim, ITS Service Desk Lead | Priya Nair, ITS Application Lead |

## Permissions matrix

| Role | View | Create | Update | Approve / confirm | Return / reject | Cancel / delete | Manage setup | Manage users and roles | Generate reports | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| R-01 | Own booking only, through its link | Own requests | Own Draft and Returned request only | No | No | No (asks LHC, LIM-01) | No | No | No | Link shows no other guest's data |
| R-02 | All bookings | Requests for guests (phone, walk-in) | Confirmed bookings: details, room assignment, check-in, check-out | Yes | Yes | Cancel Confirmed bookings; no deletion | No | No | Daily arrivals and departures (REP-01), request queue (REP-03) | |
| R-03 | All bookings | As R-02 | As R-02, plus corrections to any field except status | Yes | Yes | As R-02 | Rooms and rates | Give and remove R-02 and R-04; never their own role | All reports | |
| R-04 | All bookings, read-only | No | Approve a rate exception on a Confirmed booking (BR-10) | No | No | No | No | No | All reports | |
| R-05 | All bookings, read-only, with history and notification log | No | No | No | No | No | Deactivate a room only on the LHC Manager's written request (LIM-02) | Remove any role urgently; give R-03 on the LHC Manager's approval | Audit trail export (REP-04) | All actions audited (C-16) |

Capability view (agrees with the `Roles` column of BUS-02): C-01 R-01, R-02 · C-02 to C-07, C-10, C-17 R-02, R-03 · C-08, C-09 R-03 · C-11 all roles · C-13 R-03, R-05 · C-14 R-03, R-04 · C-15 R-02, R-03, R-05 · C-16 R-03, R-05 (reading) · C-12, C-18 Automated.

## Access request

1. The staff member signs in once at https://booking.lhc.example.org/staff with their organisation account, so their staff user account exists with no role.
2. Their line manager emails the LHC Admin (bookings-admin@lhc.example.org) naming the person and the role needed.
3. The LHC Admin checks that the access approver in the Roles table has approved (for R-02 the supervisor's own approval; for R-04 the LHC Manager's email).
4. The LHC Admin gives the role (BUS-09 Admin task "Give a staff member a role"). For R-03 and R-05, ITS Support gives the role after the approver's email.
5. The staff member signs out and in again; the role works. Target: within 2 working days of the request.

## Access removal

**Routine removal:**
1. The line manager tells the LHC Admin of a leaver or role change at least 2 working days before it takes effect; HR leaver notices also reach ITS, which disables the organisation account on the last day.
2. The LHC Admin removes or changes the role on the effective date and replies to confirm; the audit trail records the change.

**Urgent removal:**
1. The LHC Manager, the LHC Admin or the ITS security team phones the ITS Service Desk (ext. 4000) and says "urgent access removal".
2. ITS Support removes the role in the application and disables sign-in for the person within 1 hour in support hours, then emails the LHC Manager to confirm. Outside support hours the on-call ITS engineer does this within 4 hours.
3. The LHC Admin checks the audit trail the next working day for any action taken by the person since the call.

## Periodic access review

| Item | Value |
|---|---|
| Reviewer | Grace Tan, LHC Manager |
| Frequency | Quarterly (MT-10 in ENG-08); next due 2026-12-15 |
| What is checked | Every staff user account still needs its role; no leavers; no one holds R-03 who is not the front office supervisor; R-05 holders are on the current ITS list |
| Evidence kept in | The signed access list in the LHC management shared folder, Access reviews, by quarter |

## Sensitive permissions and segregation

| Permission or combination | Risk | Control | Owner |
|---|---|---|---|
| Manage users and roles (R-03, R-05) | Someone gives themselves or a friend more access | The application refuses any change to one's own role; every change is audited and reviewed quarterly | Grace Tan, LHC Manager |
| Rate exception on a Confirmed booking (R-04) | Unfair or unapproved discounts | Only R-04 may approve; a reason is required and audited (BUS-05 Exceptions) | Grace Tan, LHC Manager |
| Read-only access to all guest data (R-04, R-05) | Disclosure of guest personal data | Need-to-know roles only; access reviewed quarterly; ITS staff bound by the ITS confidentiality agreement | Ruth Ong, Data Protection Officer |
| Holding R-03 and approving one's own room or rate change | Errors or abuse in room or rate data go unnoticed | Rate changes need the LHC Manager's written approval first (W-05); the monthly sample audit (OC-04) checks rates | Grace Tan, LHC Manager |

## Assumptions and open questions

No open questions.

## Known limitations

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-02 | Only one person, the front office supervisor, holds the LHC Admin role and is trained to maintain rooms, rates and staff roles. | When the LHC Admin is away, room and rate changes and new staff roles wait; key-person risk (RISK-04). | Urgent room deactivation and role removal by ITS Support on the LHC Manager's written request; a second LHC Admin to be trained by 2027-01-31 (COND-02). | Grace Tan, LHC Manager |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-04-14 | Priya Nair | First draft from the roles in BUS-02 and BUS-03 | — |
| 0.2 | 2026-07-20 | Priya Nair | Urgent removal and the self-role check added after UAT feedback | — |
| 1.0 | 2026-08-21 | Priya Nair | Accepted at stage 4 | Grace Tan, LHC Manager, 2026-08-21 |
| 1.0 | 2026-09-11 | Priya Nair | Reviewed at go-live, no changes | Grace Tan, LHC Manager, 2026-09-11 |
