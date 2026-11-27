---
id: SP-11
title: Acceptance Criteria & Verification Register
application: LHC Booking System
version: 1.0
status: Accepted
owner: Priya Nair, ITS Application Lead (Technical owner)
audience: [Business owner, Testers, Operators, Engineering, Agents]
level: Standard
depth: D
contains: []
related: [ENG-01, BUS-03, BUS-05, SP-10, SP-12]
last_reviewed: 2026-09-11
---
# LHC Booking System – Acceptance Criteria & Verification Register

## Purpose

Holds the application acceptance criteria for the LHC Booking System: testable Given/When/Then statements of correct behaviour, how each is verified, and the result. It lets the LHC Manager, a tester or an operator decide objectively whether the application does the right thing, without asking the author.

## Scope

Covers every application acceptance criterion and its verification. The requirements are in ENG-01, journeys in the ENG-02 section of BUS-03, business rules and transitions in BUS-05; tests (`T-xx`) live in the repository under `tests/acceptance/`, one file per criterion, named after the criterion ID. The L2 measures in SP-10 are computed from this register, and SP-12 summarises its results at handover.

## Coverage rule

The register is complete when every Must functional requirement and every non-functional requirement has at least one criterion; every business rule and every transition has at least one positive and one negative criterion; and each Must journey's main path (J-01, J-04, J-05) has an end-to-end criterion. Should requirements in the release (FR-25, NFR-10) also have criteria. Won't requirements (FR-26) have none.

Test data used throughout, unless a criterion says otherwise: today is 2026-09-01 in the test clock, with no public holidays in the test calendar; the Standard Twin room type has capacity 2 and four active rooms (11, 12, 13 and 14); its rate is USD 80 a night from 2026-07-01.

## Application acceptance criteria

| ID | Verifies | Criterion | Type | Method | Evidence | Priority | Result | Verified by | Date | Approver |
|---|---|---|---|---|---|---|---|---|---|---|
| AC-01 | FR-01, TR-01, BR-01, BR-02, BR-03 | Given REC-01 in ST-01 Draft created by R-01 for 1 Standard Twin, 3 to 5 October 2026, 2 guests, with name, a valid email and a valid phone, when the guest selects Submit, then the status is ST-02 Submitted and the screen shows a reference of the form LHC-2026-nnnn and the booking link. | Functional | Automated test | T-01 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-02 | BR-01, TR-01 | Given REC-01 in ST-01 Draft with every field valid except an empty email, when R-01 selects Submit, then submission is refused, "Enter an email address" is shown next to the email field, and the status remains ST-01 Draft. | Functional | Automated test | T-02 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-03 | BR-02 | Given REC-01 in ST-01 Draft with check-in and check-out both 3 October 2026, when R-01 selects Submit, then submission is refused, "Check-out date must be after check-in date" is shown, and the status remains ST-01 Draft. | Functional | Automated test | T-03 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-04 | BR-03 | Given REC-01 in ST-01 Draft for 1 Standard Twin with 3 guests, when R-01 selects Submit, then submission is refused, "A Standard Twin room holds up to 2 guests" is shown, and the status remains ST-01 Draft. | Functional | Automated test | T-04 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-05 | FR-02 | Given R-01 has completed the "Your stay" step and the Draft link is shown, when the guest opens that link on a different device, then the form opens at "Your details" with the dates and room type already filled in, and the status is ST-01 Draft. | Functional | Automated test | T-05 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-06 | FR-03 | Given R-01 has just submitted a request as in AC-01, when 1 minute has passed, then a Notification log entry for NTF-01 to the guest's email and one for NTF-02 to bookings@lhc.example.org both exist with result Queued or Sent. | Functional | Automated test | T-06 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-07 | FR-04 | Given three requests in ST-02 Submitted on 2026-09-01, 2026-09-02 and 2026-09-04, and today is 2026-09-07, when R-02 opens the queue, then they are listed oldest first with ages of 4, 3 and 1 working days. | Functional | Automated test | T-07 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-08 | FR-05 | Given rooms 11 and 12 are assigned to Confirmed bookings on 3 October and a third Confirmed Standard Twin booking on 3 October has no room yet, when R-02 opens availability for a Standard Twin request for 3 to 5 October, then 3 October shows "1 of 4 free" and rooms 13 and 14 are listed as free to assign. | Functional | Automated test | T-08 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-09 | FR-06, TR-02 | Given REC-01 in ST-02 Submitted, when a user with R-02 selects Take into review, then the status is ST-03 Under Review and that user is shown as the reviewer. | Functional | Automated test | T-09 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-10 | TR-02 | Given REC-01 in ST-02 Submitted, when a user with R-04 sends the Take into review action, then it is refused with "You do not have permission to do this" and the status remains ST-02 Submitted. | Security | Automated test | T-10 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-11 | FR-07, TR-05, BR-04 | Given REC-01 in ST-03 Under Review for 1 Standard Twin, 3 to 5 October, and two of the four Standard Twin rooms held by Confirmed bookings on each of those nights, when R-02 selects Confirm, then the status is ST-06 Confirmed and the nightly rate recorded is USD 80. | Functional | Automated test | T-11 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-12 | TR-05, BR-04 | Given REC-01 in ST-03 Under Review for 1 Standard Twin, 3 to 5 October, and all four Standard Twin rooms held by Confirmed bookings on 4 October, when R-02 selects Confirm, then confirmation is refused, "No Standard Twin room is available on 4 October." is shown, and the status remains ST-03 Under Review. | Functional | Automated test | T-12 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-13 | BR-10 | Given REC-01 in ST-06 Confirmed on 2026-09-02 for 3 to 5 November at USD 80, when R-03 adds a Standard Twin rate of USD 90 from 2026-11-01, then the booking still shows USD 80 a night. | Data | Automated test | T-13 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-14 | FR-16 | Given Standard Twin rates of USD 80 from 2026-07-01 and USD 90 from 2026-11-01, when R-02 confirms a request with check-in 3 November, then the nightly rate recorded is USD 90. | Data | Automated test | T-14 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-15 | BR-10, FR-17 | Given REC-01 in ST-06 Confirmed at USD 80, when a user with R-02 tries to change its nightly rate, then the change is refused, "Only LHC Management can change the rate of a confirmed booking." is shown, and the rate remains USD 80. | Security | Automated test | T-15 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-16 | FR-17 | Given REC-01 in ST-06 Confirmed at USD 80, when a user with R-04 sets the rate to USD 70 with the reason "Goodwill for room change", then the booking shows USD 70 and an Audit event records old value 80, new value 70, the reason, the user and the time. | Functional | Automated test | T-16 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-17 | FR-08, TR-03, BR-06 | Given REC-01 in ST-03 Under Review, when R-02 selects Return with the reason "Please give a phone number with country code", then the status is ST-04 Returned and the NTF-03 email contains that reason. | Functional | Automated test | T-17 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-18 | TR-03, BR-06 | Given REC-01 in ST-03 Under Review, when R-02 selects Return with the reason "ok", then it is refused, "Enter a reason of at least 10 characters." is shown, and the status remains ST-03 Under Review. | Functional | Automated test | T-18 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-19 | FR-08, TR-04, BR-06 | Given REC-01 in ST-03 Under Review, when R-02 selects Reject with the reason "Dates fall in the annual closure", then the status is ST-05 Rejected and the NTF-04 email contains that reason. | Functional | Automated test | T-19 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-20 | TR-04 | Given REC-01 in ST-02 Submitted (not yet taken into review), when R-02 sends the Reject action, then it is refused with "Take this request into review first." and the status remains ST-02 Submitted. | Functional | Automated test | T-20 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-21 | FR-09, TR-06, J-03 | Given REC-01 in ST-04 Returned 3 days ago asking for a phone number, when R-01 opens the booking link, adds a valid phone number and selects Resubmit, then the status is ST-02 Submitted and an NTF-02 Notification log entry exists. | Functional | Automated test | T-21 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-22 | TR-06, BR-07 | Given REC-01 in ST-10 Expired, when R-01 opens the booking link, then "This request has expired. Please submit a new request." is shown, no Resubmit action is offered, and the status remains ST-10 Expired. | Functional | Automated test | T-22 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-23 | FR-10, TR-07, BR-07 | Given REC-01 Returned at 2026-09-01 10:00 and not resubmitted, when the nightly job runs at 01:30 on 2026-09-16, then the status is ST-10 Expired and an NTF-07 Notification log entry exists. | Functional | Automated test | T-23 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-24 | TR-07, BR-07 | Given REC-01 Returned at 2026-09-01 10:00 and not resubmitted, when the nightly job runs at 01:30 on 2026-09-15, then the status remains ST-04 Returned. | Functional | Automated test | T-24 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-25 | FR-10, BR-07 | Given REC-01 Returned at 2026-09-01 10:00, when the nightly job runs on 2026-09-09 and again on 2026-09-10, then exactly one NTF-06 Notification log entry exists for the booking. | Functional | Automated test | T-25 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-26 | FR-11, BR-05 | Given REC-01 in ST-06 Confirmed for a Standard Twin, 3 to 5 October, and room 13 free on both nights, when R-02 assigns room 13, then the booking shows room 13, an NTF-08 Notification log entry exists, and the status remains ST-06 Confirmed. | Functional | Automated test | T-26 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-27 | BR-05 | Given booking B in ST-06 Confirmed for 3 to 5 October, and room 12 assigned to another Confirmed booking for 4 October, when R-02 assigns room 12 to booking B, then it is refused, "Room 12 is not available on 4 October." is shown, and booking B has no room assigned. | Functional | Automated test | T-27 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-28 | FR-12, TR-08, BR-08 | Given REC-01 in ST-06 Confirmed with room 13 assigned and check-in 3 October, and today is 3 October, when R-02 selects Check in, then the status is ST-07 Checked In. | Functional | Automated test | T-28 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-29 | TR-08, BR-08 | Given REC-01 in ST-06 Confirmed with no room assigned and check-in today, when R-02 selects Check in, then it is refused, "Assign a room before checking in." is shown, and the status remains ST-06 Confirmed. | Functional | Automated test | T-29 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-30 | BR-08 | Given REC-01 in ST-06 Confirmed with room 13 assigned and check-in 3 October, and today is 2 October, when R-02 selects Check in, then it is refused, "Check-in opens on 3 October." is shown, and the status remains ST-06 Confirmed. | Functional | Automated test | T-30 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-31 | FR-12, TR-09 | Given REC-01 in ST-07 Checked In, when R-02 selects Check out, then the status is ST-08 Completed. | Functional | Automated test | T-31 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-32 | TR-09 | Given REC-01 in ST-06 Confirmed, when R-02 sends the Check out action, then it is refused with "This guest has not checked in." and the status remains ST-06 Confirmed. | Functional | Automated test | T-32 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-33 | FR-13, J-06 | Given REC-01 in ST-06 Confirmed for 3 to 5 October with room 13, and room 13 free on 5 October, when R-02 changes the check-out date to 6 October, then the booking shows 3 to 6 October and room 13, an NTF-08 Notification log entry exists, and the status remains ST-06 Confirmed. | Functional | Automated test | T-33 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-34 | FR-13, BR-04 | Given REC-01 in ST-06 Confirmed for 3 to 5 October, and all four Standard Twin rooms held by Confirmed bookings on 10 October, when R-02 changes the dates to 9 to 11 October, then it is refused, "No Standard Twin room is available on 10 October." is shown, and the booking keeps 3 to 5 October. | Functional | Automated test | T-34 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-35 | FR-14, TR-10, BR-09 | Given REC-01 in ST-06 Confirmed for 3 to 5 October with room 13, when R-02 cancels it with the reason "Guest cancelled by phone", then the status is ST-09 Cancelled, room 13 shows as free on 3 and 4 October, and an NTF-09 Notification log entry exists. | Functional | Automated test | T-35 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-36 | TR-10, BR-09 | Given REC-01 in ST-06 Confirmed, when R-02 selects Cancel with no reason, then it is refused, "Enter a cancellation reason." is shown, and the status remains ST-06 Confirmed. | Functional | Automated test | T-36 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-37 | FR-15, BR-11, J-07 | Given room 14 has no assignment on any night from today, when R-03 deactivates it, then room 14 shows Inactive and the Standard Twin availability shows 3 rooms in total. | Functional | Automated test | T-37 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-38 | BR-11 | Given room 12 is assigned to Confirmed booking LHC-2026-0153 on 4 October, when R-03 deactivates room 12, then it is refused, "Room 12 is assigned to booking LHC-2026-0153 on 4 October. Move that booking first." is shown, and room 12 remains active. | Functional | Automated test | T-38 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-39 | FR-18 | Given the test SMTP server refuses every message for one notification, when the worker processes it, then 5 attempts are logged within 1 hour, the Notification log entry result is Failed, and it appears on the failed-email list. | Operational | Automated test | T-39 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-40 | FR-19, J-09 | Given a staff user account that has signed in once and has no role, when R-03 gives it the LHC Staff role, then at its next sign-in the user sees the request queue, and an Audit event records the change. | Security | Automated test | T-40 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-41 | FR-19 | Given a user with R-03, when they try to change their own role, then it is refused, "You cannot change your own role." is shown, and the role is unchanged. | Security | Automated test | T-41 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-42 | FR-19 | Given a signed-in user with R-02, when a user with R-05 removes that role, then the R-02 user's next page request shows "You do not have access to the staff screens." | Security | Automated test | T-42 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-43 | FR-20, J-08 | Given the golden data set "September 2026" (120 bookings with nights in September 2026, 310 nights, USD 25,400 at confirmed rates), when R-03 produces REP-02 for September 2026, then the spreadsheet totals are 120 bookings, 310 nights and USD 25,400. | Data | Automated test | T-43 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-44 | FR-21 | Given 5 bookings with check-in on 3 October and 3 with check-out on 3 October, when R-02 opens REP-01 for 3 October, then it lists 5 arrivals and 3 departures with their room numbers, and the PDF download lists the same 8 rows. | Functional | Automated test | T-44 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-45 | FR-22, J-02 | Given REC-01 in ST-03 Under Review, when R-01 opens its booking link, then the page shows "Under Review", "Someone at LHC is checking your request now.", the dates and the room type, and no staff names. | Usability | Automated test | T-45 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-46 | FR-23 | Given REC-01 in ST-03 Under Review, when R-02 confirms it, then an Audit event exists with that user, the time, old value Under Review and new value Confirmed. | Data | Automated test | T-46 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-47 | FR-24 | Given a user with R-05, when they open booking LHC-2026-0153, then its audit events and notification log are shown with no action buttons, and a Confirm action sent directly is refused with HTTP 403. | Security | Automated test | T-47 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-48 | FR-25 | Given a booking with 6 audit events, when R-05 exports its audit trail, then the CSV file has 6 rows with the columns time, user, action, old value and new value in that order and with the right values. | Data | Automated test | T-48 (failed 2026-09-03: old and new values swapped, issue LHCB-112) | Should | Waived | Hannah Wong, ITS Test Analyst | 2026-09-03 | Grace Tan, LHC Manager, 2026-09-10: export switched off (FLAG-01) until fixed; COND-01 |
| AC-49 | NFR-01 | Given the production environment during the staff pilot from 2026-08-24 to 2026-09-06, when the availability test calls /health every 5 minutes from two regions, then at least 99.5% of checks succeed. | Non-functional | Measurement | Availability report for the pilot: 99.96% | Must | Pass | Joel Park, ITS Operations Engineer | 2026-09-07 | |
| AC-50 | NFR-02 | Given 30 virtual users and 10,000 bookings in ENV-02, when each user opens the queue, a booking and the guest form once a minute for 30 minutes and submits 1 request every 5 minutes, then p95 page response is ≤ 2 s and p95 submission is ≤ 3 s. | Non-functional | Measurement | Load test report LT-2026-08-27: p95 0.9 s pages, 1.4 s submission | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-08-27 | |
| AC-51 | NFR-03 | Given ENV-02 loaded with 40 rooms, 10,000 active bookings and 50,000 anonymised bookings, when R-02 opens availability for a 30-night stay, then the page responds in ≤ 2 s at p95 over 100 requests. | Non-functional | Measurement | Load test report LT-2026-08-27: p95 1.1 s | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-08-27 | |
| AC-52 | NFR-04 | Given the Entra ID conditional-access policy assigned to the application, when the sign-in logs for 2026-08-24 to 2026-09-06 are inspected, then 100% of successful staff sign-ins show MFA satisfied. | Security | Inspection | Sign-in log export and policy screenshot, ITS change record CHG-2026-0852 | Must | Pass | Kevin Ho, ITS Network and M365 Administrator | 2026-09-07 | |
| AC-53 | NFR-04 | Given a valid booking link, when one character of its token is changed and the link is opened, then "We could not find that booking." is shown with HTTP 404 and no booking data. | Security | Automated test | T-53 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-54 | NFR-05 | Given the external penetration test of ENV-02 completed on 2026-08-19, when its report and the retest are inspected, then no High or Critical finding remains open. | Security | Inspection | Penetration test report PT-2026-031 and retest letter 2026-08-26: 0 High, 0 Critical open | Must | Pass | Priya Nair, ITS Application Lead | 2026-08-26 | |
| AC-55 | NFR-06 | Given 10 submissions from one IP address in the last hour, when an 11th is sent from that address, then it is refused with HTTP 429 and "Too many requests from your connection. Please try again in an hour or phone LHC on +1 555 0100.", and no booking is created. | Security | Automated test | T-55 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-56 | NFR-07 | Given a Draft unchanged for 31 days and a Completed booking whose final status was set 2 years and 1 day ago, when the nightly job runs, then the Draft no longer exists and the booking's name, email, phone and special requests all read "Anonymised". | Data | Automated test | T-56 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-57 | NFR-08 | Given every guest and staff screen in ENV-02, when the automated accessibility scan and the manual keyboard and screen-reader check of J-01 to J-09 are carried out, then 0 WCAG 2.2 AA failures remain. | Usability | Inspection | ITS accessibility audit AA-2026-014 and retest 2026-08-28: 0 AA failures | Must | Pass | ITS Accessibility Team (Mei Chen) | 2026-08-28 | |
| AC-58 | NFR-09 | Given the latest two major versions of Chrome, Edge, Firefox and Safari on macOS, Safari on iOS and Chrome on Android at 360 px width, when the journey tests for J-01 to J-09 run on each, then all pass. | Non-functional | Automated test | T-58 browser matrix run 2026-09-08 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-08 | |
| AC-59 | NFR-10 | Given the main branch at release 1.0.0, when the CI pipeline runs the full test suite, then it finishes in ≤ 10 min and line coverage of the bookings domain module is ≥ 80%. | Non-functional | Measurement | CI run 1.0.0: 7 min 40 s, coverage 86% | Should | Pass | Leo Santos, ITS Developer | 2026-09-09 | |
| AC-60 | NFR-11 | Given a submission forced to fail in ENV-02, when the error page appears, then it shows a correlation ID, and a log query for that ID in Application Insights returns the failed request within 2 minutes. | Operational | Automated test | T-60 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-61 | NFR-07 | Given 1,000 application log entries sampled at random from the pilot, when they are searched for the names, emails and phone numbers of the pilot guests, then none is found. | Security | Inspection | Log sample check, ITS change record CHG-2026-0853 | Must | Pass | Ruth Ong, Data Protection Officer | 2026-09-08 | |
| AC-62 | NFR-12 | Given an Audit event 3 years and 1 day old, an Audit event 3 years less 1 day old, and a Notification log entry 2 years and 1 day old, when the nightly job runs, then the first and third are deleted and the second remains. | Data | Automated test | T-62 | Must | Pass | Hannah Wong, ITS Test Analyst | 2026-09-09 | |
| AC-63 | NFR-13 | Given a declared outage of the ENV-02 database, when an engineer who did not write ENG-08 follows its restore procedure, then the service is verified working within 4 hours of the declaration. | Operational | Measurement | Restore test 2026-08-28, 1 h 35 min, change record CHG-2026-0841 | Must | Pass | Joel Park, ITS Operations Engineer | 2026-08-28 | |
| AC-64 | NFR-14 | Given bookings created every minute in ENV-02 up to the moment of failure, when the database is restored to the latest available point, then no more than 1 hour of bookings is missing. | Operational | Measurement | Restore test 2026-08-28: 5 minutes of bookings missing | Must | Pass | Joel Park, ITS Operations Engineer | 2026-08-28 | |
| AC-65 | J-01 | Given a guest on the LHC website in a supported browser, when they follow the booking link, complete both steps for an available stay and submit, then within 5 minutes they receive the "Request received" email with the reference and a working booking link. | Functional | Manual test | UAT script U-01, run sheet in the ITS test share | Must | Pass | Ana Cruz, Senior LHC Staff | 2026-09-04 | |
| AC-66 | J-04 | Given a new Submitted request in the queue, when an LHC Staff member takes it into review, checks availability and confirms it, then the booking is Confirmed and the guest's test mailbox receives "Booking confirmed" with the dates, room type and rate within 5 minutes. | Functional | Manual test | UAT script U-04 | Must | Pass | Ana Cruz, Senior LHC Staff | 2026-09-04 | |
| AC-67 | J-05 | Given a Confirmed booking arriving today, when an LHC Staff member assigns a room from the daily arrivals list, checks the guest in, and later checks them out, then the booking ends Completed and its history shows the assignment, check-in and check-out with times. | Functional | Manual test | UAT script U-05 | Must | Pass | Ana Cruz, Senior LHC Staff | 2026-09-04 | |

## Criterion details

### AC-43

The golden data set is the file `tests/fixtures/golden_september_2026.json` in the repository. Its expected totals were calculated by hand by Daniel Reyes, LHC Front Office Supervisor, on 2026-08-12 and are stored with the file.

### AC-48

The defect swaps the old-value and new-value columns. Because no business process depends on the export (ITS Support reads history on screen through FR-24), the business owner waived the criterion for go-live; the export stays switched off by FLAG-01 until it is fixed and AC-48 passes (COND-01 in SP-12).

## Results summary

| Priority | Total | Pass | Fail | Waived | Not run |
|---|---|---|---|---|---|
| Must | 65 | 65 | 0 | 0 | 0 |
| Should | 2 | 1 | 0 | 1 | 0 |
| Could | 0 | 0 | 0 | 0 | 0 |

**Last verification run:** 2026-09-09, environment ENV-02, run by Hannah Wong, ITS Test Analyst (automated suite); measurements and inspections on the dates shown.

**Failed and waived Must criteria:** none. The only waived criterion is AC-48 (Should), approved by Grace Tan, LHC Manager.

## Assumptions and open questions

No open questions.

## Known limitations

No known limitations.

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-04-20 | Priya Nair | Criteria for Must requirements drafted at stage 2 | — |
| 0.2 | 2026-08-14 | Hannah Wong | Criteria for every rule and transition completed; first UAT results | — |
| 1.0 | 2026-09-10 | Hannah Wong | Accepted at stage 4 with final results; AC-48 waiver recorded | Grace Tan, LHC Manager; Priya Nair, ITS Application Lead, 2026-09-10 |
