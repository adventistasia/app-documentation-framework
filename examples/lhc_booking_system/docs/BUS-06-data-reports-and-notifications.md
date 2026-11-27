---
id: BUS-06
title: Data, Reports & Notifications Register
application: LHC Booking System
version: 1.0
status: Accepted
owner: Daniel Reyes, LHC Front Office Supervisor (Data owner)
audience: [Data owner, Compliance, Business owner, Support, Engineering]
level: Standard
depth: D
contains: []
related: [BUS-03, BUS-05, BUS-08, ENG-04, ENG-08, SP-10]
last_reviewed: 2026-09-11
---
# LHC Booking System – Data, Reports & Notifications Register

## Purpose

Lists the business records the LHC Booking System holds, how each is classified and kept, and the reports and notifications it produces, so the data owner, the Data Protection Officer and support know what data exists, why, for how long, and who relies on each output.

## Scope

Covers business records, reports and notifications. The technical entities and fields that store records are in ENG-04; statuses of a Booking in BUS-05; the output checks that confirm records and reports are correct in ENG-08 and SP-10 (L4). Amounts are in USD.

## Records

| ID | Name | Description | Required fields | Core | Classification | Purpose | Retention | Disposal | Owner | Processes |
|---|---|---|---|---|---|---|---|---|---|---|
| REC-01 | Booking | One guest's stay request and its history, from Draft to its final status, including the assigned room and confirmed rate. | Reference, guest name, email, phone, check-in date, check-out date, room type, number of guests, status | Yes | Personal | To arrange and host the guest's stay at their request (steps before and performance of a contract), organisation privacy policy section 3. | Drafts: 30 days after last change. Other bookings: personal details kept 2 years after the final status date, privacy policy section 5; the anonymised booking (dates, room type, rate, status) kept 7 years for financial records, records retention schedule entry FIN-7. | Nightly job deletes old Drafts and replaces name, email, phone and special requests with "Anonymised"; ITS deletes anonymised bookings older than 7 years each January (MT-12). | Daniel Reyes, LHC Front Office Supervisor | W-01, W-02, W-03, W-04 |
| REC-02 | Room | One bookable room with its number, room type and whether it is active. | Room number, room type, active flag | Yes | Internal | — | Kept while LHC has the room; inactive rooms kept 7 years so old bookings still show their room, retention schedule entry FIN-7. | Deleted by ITS on request of the LHC Admin after 7 years inactive. | Daniel Reyes, LHC Front Office Supervisor | W-03, W-05 |
| REC-03 | Room rate | The nightly price for a room type from a start date, as approved by LHC Management. | Room type, nightly rate, start date, approved by | Yes | Internal | — | 7 years after the rate stops applying, records retention schedule entry FIN-7. | Deleted by ITS each January (MT-12). | Grace Tan, LHC Manager | W-05 |
| REC-04 | Notification log entry | One email the application sent or tried to send: type, recipient, booking, time and result. | Notification type, recipient email, booking reference, time, result | Yes | Personal | To show that guests were told of each decision and to resend failed emails, privacy policy section 3. | 2 years after sending, privacy policy section 5. | Deleted by the nightly job. | Daniel Reyes, LHC Front Office Supervisor | W-01, W-02, W-03, W-04 |
| REC-05 | Staff user account | A staff member's access: name, organisation email, role, last sign-in, active flag. | Name, email, role, active flag | No | Personal | To control and record who can use the staff screens (employment), ITS acceptable use policy. | Deactivated when access is removed; deleted 3 years after last sign-in so audit events can still name the person until they are deleted. | Deleted by the nightly job. | Daniel Reyes, LHC Front Office Supervisor | W-07 |
| REC-06 | Audit event | Who did what, to which booking, room, rate or user account, and when, with old and new values. | Time, user, action, record and reference, old value, new value | Yes | Personal | To trace changes for support, accountability and internal audit (legitimate interest), internal audit policy section 2. | 3 years after the event, internal audit policy section 4. | Deleted by the nightly job. | Priya Nair, ITS Application Lead | W-01, W-02, W-03, W-04, W-05, W-07, W-08 |

## Reports, exports and dashboards

| ID | Name | Purpose | Audience | Frequency | Format | Source | Owner | Official record |
|---|---|---|---|---|---|---|---|---|
| REP-01 | Daily arrivals and departures | Plan rooms and check-ins for the day; printed each morning as the paper fallback during an outage | LHC Staff (R-02) | Daily at 06:00, and on demand | Screen and printable PDF | REC-01, REC-02 | Daniel Reyes, LHC Front Office Supervisor | No |
| REP-02 | Monthly booking and occupancy report | Occupancy by room type, nights sold, income at confirmed rates, cancellations and median request-to-decision time, for management review and income planning | LHC Management (R-04), LHC Finance | Monthly, first working day, for the previous calendar month | Spreadsheet (XLSX) | REC-01, REC-02, REC-03 | Grace Tan, LHC Manager | Yes |
| REP-03 | Request queue | Show open requests by status and age so none waits more than 1 working day | LHC Staff (R-02), LHC Admin (R-03) | Continuous | Screen | REC-01 | Daniel Reyes, LHC Front Office Supervisor | No |
| REP-04 | Audit trail export | Give ITS Support and internal audit the history of a booking or user as a file | ITS Support (R-05), internal audit | On demand | CSV file | REC-06 | Priya Nair, ITS Application Lead | No |

REP-04 is switched off in production until its column defect is fixed (FR-25, COND-01); until then ITS Support reads the history on screen.

## Notifications

All notifications are emails from noreply-booking@lhc.example.org. Every email to a guest includes the booking reference and the booking link.

| ID | Name | Trigger | Recipient | Purpose | Expected action | Channel | Processes | Owner |
|---|---|---|---|---|---|---|---|---|
| NTF-01 | Request received | TR-01 or TR-06 | R-01 | Confirm LHC has the request; give the reference and booking link | None, information only; keep the email | Email | W-01 | Daniel Reyes, LHC Front Office Supervisor |
| NTF-02 | New request to review | TR-01 or TR-06 | R-02, through the bookings@lhc.example.org shared mailbox | Tell staff a request is waiting | Take it into review within 1 working day | Email | W-01, W-02 | Daniel Reyes, LHC Front Office Supervisor |
| NTF-03 | Request returned | TR-03 | R-01 | Tell the guest what to correct, with the reason | Correct and resubmit through the booking link within 14 days | Email | W-02 | Daniel Reyes, LHC Front Office Supervisor |
| NTF-04 | Request rejected | TR-04 | R-01 | Tell the guest the decision and the reason | None; the guest may send a new request | Email | W-02 | Daniel Reyes, LHC Front Office Supervisor |
| NTF-05 | Booking confirmed | TR-05 | R-01 | Give dates, room type, nightly rate and arrival information | Keep for arrival; contact LHC to change anything | Email | W-02 | Daniel Reyes, LHC Front Office Supervisor |
| NTF-06 | Reminder: your request needs changes | Nightly job, 7 days after TR-03 (BR-07) | R-01 | Warn that the request will expire in 7 days | Correct and resubmit within 7 days | Email | W-02 | Daniel Reyes, LHC Front Office Supervisor |
| NTF-07 | Request expired | TR-07 | R-01 | Tell the guest the request has closed | Send a new request if still needed | Email | W-02 | Daniel Reyes, LHC Front Office Supervisor |
| NTF-08 | Booking updated | A room is assigned or changed (C-10), or booking details change (C-06), on a Confirmed booking | R-01 | Give the new details or the room number | Check the details; contact LHC if they are wrong | Email | W-03, W-04 | Daniel Reyes, LHC Front Office Supervisor |
| NTF-09 | Booking cancelled | TR-10 | R-01 | Confirm the cancellation and its reason | None, information only | Email | W-04 | Daniel Reyes, LHC Front Office Supervisor |

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-02 | LHC Finance asked whether 7 years for anonymised bookings is still required now that payments are not held in the application; if not, REC-01 and REC-03 retention drop to 2 years. | Ruth Ong, Data Protection Officer | 2026-12-31 | Open |

## Known limitations

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-03 | Notifications are sent by email only; there is no SMS or phone message. | A guest who gives a mistyped email or does not read email does not learn of a decision, return or expiry. | Staff phone guests listed on the failed-email list (MT-02), and confirm by phone any stay starting within 2 days whose guest has not replied to LHC. | Daniel Reyes, LHC Front Office Supervisor |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-04-14 | Priya Nair | First draft | — |
| 0.2 | 2026-06-01 | Priya Nair | Retention and purposes confirmed with the Data Protection Officer after the privacy impact assessment | — |
| 1.0 | 2026-08-21 | Priya Nair | Accepted at stage 4 | Daniel Reyes, LHC Front Office Supervisor, 2026-08-21; Ruth Ong, Data Protection Officer, 2026-08-21 |
| 1.0 | 2026-09-11 | Priya Nair | Reviewed at go-live, no changes | Daniel Reyes, LHC Front Office Supervisor, 2026-09-11 |
