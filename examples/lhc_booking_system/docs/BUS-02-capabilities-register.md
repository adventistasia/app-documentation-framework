---
id: BUS-02
title: Capabilities Register
application: LHC Booking System
version: 1.0
status: Accepted
owner: Grace Tan, LHC Manager (Business owner)
audience: [Business owner, Support, Engineering, Agents]
level: Standard
depth: D
contains: []
related: [BUS-03, BUS-04, ENG-01, ENG-05, SP-11]
last_reviewed: 2026-09-11
---
# LHC Booking System – Capabilities Register

## Purpose

Lists what the LHC Booking System can do, in business language, with the outcome of each capability, who uses it, who owns it, how critical it is and which processes use it. It is the reference for scope, requirements (ENG-01), access (BUS-04) and support.

## Scope

Covers every capability the application offers to guests, LHC staff, administrators, management and ITS Support, including the two automated capabilities. How capabilities are used in real work is in BUS-03; detailed requirements are in ENG-01; dependencies are defined in ENG-05.

## Capability register

| ID | Name | Description | Outcome | Roles | Processes | Dependencies | Automated | Criticality | Owner | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| C-01 | Submit booking request | A guest, or a staff member taking a phone or walk-in request, enters guest details, stay dates, room type and number of guests, can save a Draft, and submits it; a guest also uses it to correct and resubmit a Returned request through the booking link. | A booking request exists with a reference and enters the review queue. | R-01, R-02 | W-01 | D-01, D-02, D-03 | No | High | Grace Tan, LHC Manager | Staff use the same public form, so they can submit even when single sign-on is down. |
| C-02 | Check room availability | Shows, for each night of a stay, how many rooms of each type are free and which rooms can be assigned. | Staff know whether a stay can be accepted before deciding. | R-02, R-03 | W-02, W-03, W-04 | D-02, D-03, D-05, D-06, D-08 | No | High | Daniel Reyes, LHC Front Office Supervisor | Enforces BR-04 and BR-05. |
| C-03 | Review booking request | Staff open a request from the queue, take it into review and check completeness, dates, guest details and special requests. | Each request has one reviewer and is ready for a decision. | R-02, R-03 | W-02 | D-02, D-03, D-05, D-08, D-09 | No | High | Daniel Reyes, LHC Front Office Supervisor | |
| C-04 | Confirm booking | Staff confirm a request when a room of the requested type is free for every night; the rate in force is recorded. | The guest has a confirmed booking and a room type held for them. | R-02, R-03 | W-02 | D-02, D-03, D-05, D-08, D-09 | No | High | Daniel Reyes, LHC Front Office Supervisor | |
| C-05 | Return or reject request | Staff return an incomplete request to the guest with what to correct, or reject one that cannot be accepted, giving a reason. | Requests that cannot be confirmed leave the queue with a clear reason for the guest. | R-02, R-03 | W-02 | D-02, D-03, D-05, D-08, D-09 | No | High | Daniel Reyes, LHC Front Office Supervisor | |
| C-06 | Modify booking | Staff change the dates, room type, number of guests or guest details of a Confirmed booking, with availability re-checked. | Bookings stay accurate when plans change. | R-02, R-03 | W-04 | D-02, D-03, D-05, D-08 | No | Medium | Daniel Reyes, LHC Front Office Supervisor | Guests ask by email or phone (LIM-01). |
| C-07 | Cancel booking | Staff cancel a Confirmed booking with a reason; any room assignment is released. | Cancelled bookings no longer hold a room. | R-02, R-03 | W-04 | D-02, D-03, D-05, D-08 | No | Medium | Daniel Reyes, LHC Front Office Supervisor | Guests ask by email or phone (LIM-01). |
| C-08 | Manage room records | Admins add rooms, change their type, and activate or deactivate them. | The room list matches the rooms LHC can actually let. | R-03 | W-05 | D-02, D-03, D-05, D-06, D-08 | No | Medium | Daniel Reyes, LHC Front Office Supervisor | Enforces BR-11. |
| C-09 | Manage room rates | Admins record the nightly rate for each room type with the date it starts to apply. | Confirmations use the approved current rate. | R-03 | W-05 | D-02, D-03, D-05, D-07, D-08 | No | Medium | Grace Tan, LHC Manager | Rates are approved by LHC Management before entry. |
| C-10 | Assign room | Staff link a specific room to a Confirmed booking, or change the room before check-in. | Each arriving guest has a definite room that no one else holds for those nights. | R-02, R-03 | W-03, W-04 | D-02, D-03, D-05, D-06, D-08 | No | High | Daniel Reyes, LHC Front Office Supervisor | An action, not a status (ADR-004). Enforces BR-05. |
| C-11 | Track booking status | Shows the current status and history of a booking: guests through their booking link, staff and ITS Support through the staff screens. | Everyone can see where a booking stands without asking. | R-01, R-02, R-03, R-04, R-05 | W-01, W-02, W-03, W-04, W-06, W-08 | D-02, D-03, D-05, D-08 | No | High | Daniel Reyes, LHC Front Office Supervisor | Uses only the statuses in BUS-05. |
| C-12 | Send notifications | Sends the emails listed in BUS-06 when a booking changes status or a reminder is due, and logs each attempt. | Guests and staff learn of every decision and required action. | Automated | W-01, W-02, W-03, W-04 | D-02, D-04 | Yes | High | Priya Nair, ITS Application Lead | Failed sends are retried, then listed for staff to phone the guest. |
| C-13 | Manage user access and roles | Admins give signed-in staff a role, change it or remove it; ITS Support can remove access urgently. | Only authorised people can review, decide and administer bookings. | R-03, R-05 | W-07 | D-02, D-03, D-05, D-08 | No | High | Daniel Reyes, LHC Front Office Supervisor | Follows BUS-04. |
| C-14 | Generate booking reports | Produces the daily arrivals and departures list, the request queue view and the monthly booking and occupancy report. | Staff plan each day; management sees occupancy and response times. | R-03, R-04 | W-06 | D-02, D-03, D-05, D-08 | No | Medium | Grace Tan, LHC Manager | Reports in BUS-06. |
| C-15 | Handle support issue | Gives ITS Support a read-only view of a booking, its history and its notification log, so issues reported to the service desk can be diagnosed. | Problems are diagnosed from facts and routed to the right owner. | R-02, R-03, R-05 | W-08 | D-02, D-03, D-05, D-08, D-10 | No | Medium | Mark Lim, ITS Service Desk Lead | Issues are logged in the ITS service desk tool, outside the application. |
| C-16 | Maintain audit trail | Records every status change, room assignment, booking change, room and rate change and access change with who, what and when. | Every important change can be traced for support and accountability. | R-03, R-05 | W-01, W-02, W-03, W-04, W-05, W-07, W-08 | D-02 | Yes | High | Priya Nair, ITS Application Lead | Recorded automatically; LHC Admin and ITS Support read it. |
| C-17 | Check guests in and out | Staff record a guest's arrival in their assigned room, and their departure. | Staff know who is in the house; stays are closed when guests leave. | R-02, R-03 | W-03 | D-02, D-03, D-05, D-08 | No | High | Daniel Reyes, LHC Front Office Supervisor | Enforces BR-08. |
| C-18 | Expire unanswered returned requests | Each night, sends a reminder for requests Returned 7 days ago and expires those Returned 14 days ago. | Uncorrected requests do not wait in the queue forever, and guests are warned first. | Automated | W-02 | D-02 | Yes | Medium | Priya Nair, ITS Application Lead | Runs in the nightly job (ENG-08 Scheduled jobs). Enforces BR-07. |

## Coverage check

| Kind | Covered by | Or why not needed |
|---|---|---|
| Core user tasks | C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-10, C-17 | — |
| Administration and setup | C-08, C-09 | — |
| Access and role management | C-13 | — |
| Support and correction | C-15; corrections are made with C-06 by LHC Admin | — |
| Reporting and export | C-14 | — |
| Notifications | C-12 | — |
| Audit and history | C-16, C-11 | — |
| Automated and scheduled actions | C-12, C-16, C-18 | — |

## Assumptions and open questions

No open questions.

## Known limitations

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | Guests cannot change or cancel their own booking online; only LHC Staff and LHC Admin can modify or cancel it. | Guests must email or phone during front office hours; changes outside those hours wait until the next morning. | Guests email bookings@lhc.example.org or phone +1 555 0100; staff make the change (BUS-09 FAQ). | Grace Tan, LHC Manager |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-03-30 | Priya Nair | First draft from the earlier single-file example, renumbered; C-01 removed from W-02, C-03 and C-05 removed from W-03, C-11 added to W-08 | — |
| 0.2 | 2026-04-14 | Priya Nair | Added C-17 and C-18 so check-in and the nightly expiry are capabilities; "System" removed from Roles and replaced by the Automated column | — |
| 1.0 | 2026-04-20 | Priya Nair | Accepted at stage 2 | Grace Tan, LHC Manager, 2026-04-20 |
| 1.0 | 2026-09-11 | Priya Nair | Reviewed at go-live, no changes | Grace Tan, LHC Manager, 2026-09-11 |
