---
id: BUS-09
title: User & Admin Guide
application: LHC Booking System
version: 1.0
status: Accepted
owner: Daniel Reyes, LHC Front Office Supervisor (LHC Admin)
audience: [Guests, LHC Staff, LHC Admin, LHC Management, Support]
level: Standard
depth: D
contains: []
related: [BUS-03, BUS-04, BUS-05, BUS-06, ENG-08]
last_reviewed: 2026-09-11
---
# LHC Booking System – User & Admin Guide

## Purpose

Helps guests, LHC Staff, the LHC Admin and LHC Management use the LHC Booking System: get started, complete their tasks, understand what they see, look things up, get help and keep up with changes.

## Scope

Covers every user-facing journey in the ENG-02 section of BUS-03 as a how-to task (J-01 to J-06) or admin task (J-07 to J-09), every status in BUS-05, every notification in BUS-06, and the access tasks in BUS-04. It does not cover technical operations (ENG-08) or deployment (ENG-07).

## Getting started

**Before you start**

| Item | Value |
|---|---|
| Who can use it | Guests, to ask for a room and follow their request; LHC front office staff, to review requests and run stays; the LHC Admin, to keep rooms, rates and staff access up to date; LHC Management, to see reports |
| How to get access | Guests need no account. Staff: sign in once at the staff address with your organisation account, then ask your line manager to email the LHC Admin for a role (BUS-04 Access request) |
| Where to find it | Guests: https://booking.lhc.example.org, or "Book a room" on www.lhc.example.org. Staff: https://booking.lhc.example.org/staff |
| Where to get help | Guests: LHC front office, +1 555 0100 or bookings@lhc.example.org. Staff: see FAQ and help below |

**Your first booking request (guests)**

1. Open https://booking.lhc.example.org.
2. On "Your stay", choose your check-in and check-out dates, the room type and the number of guests, then select Continue.
3. On "Your details", enter your name, email address and phone number with country code, and anything LHC should know in "Special requests".
4. Select Submit.

You should now see "Request received" with your booking reference (for example LHC-2026-0153) and your booking link. An email with the same reference and link arrives within a few minutes. LHC answers within one working day.

**Your first sign-in (staff)**

1. Open https://booking.lhc.example.org/staff and select "Sign in with your organisation account".
2. Sign in as you do for email, including the extra sign-in check on your phone.
3. If you see "You do not have access to the staff screens.", ask your line manager to request your role, then sign out and in again once it is given.

You should now see the request queue, oldest request first.

## How-to tasks

### Submit a booking request

| Item | Value |
|---|---|
| Related journey | J-01 |
| Related process | W-01 |
| Required role | Guest (R-01), or LHC Staff (R-02) entering a phone or walk-in request for a guest |

**Steps**

1. Open https://booking.lhc.example.org (staff: select "New request" on the queue).
2. On "Your stay", choose dates, room type and number of guests, and select Continue. Your request is saved as a Draft and a link to it is shown; you can come back to it from any device within 30 days.
3. On "Your details", enter name, email and phone, and any special requests.
4. Select Submit.

**Expected result:** "Request received" with the reference and booking link; the status is Submitted; the "Request received" email arrives.

**Common mistakes:**
- Choosing a check-out date the same as the check-in date: check-out is the morning you leave.
- More guests than the room type holds: choose a larger room type or send two requests.
- A phone number without the country code.

**If something goes wrong:** each problem is shown next to its field and your entries are kept; correct it and select Submit again. If you see "Too many requests from your connection", wait an hour or phone LHC on +1 555 0100.

### Check where your request stands

| Item | Value |
|---|---|
| Related journey | J-02 |
| Related process | W-01, W-02 |
| Required role | Guest (R-01) |

**Steps**

1. Open the booking link in any email from LHC about your request.

**Expected result:** the page shows your status, what it means (see What the statuses mean), your dates and the room type.

**Common mistakes:**
- Searching for the booking on the LHC website: there is no search; use the link in your email.

**If something goes wrong:** if the page says "We could not find that booking.", check you opened the whole link from the email, or phone LHC with your reference.

### Correct a request LHC returned

| Item | Value |
|---|---|
| Related journey | J-03 |
| Related process | W-01 |
| Required role | Guest (R-01) |

**Steps**

1. Open the booking link in the "Request returned" email. The reason LHC gave is shown at the top.
2. Make the changes asked for.
3. Select Resubmit.

**Expected result:** the status is Submitted again and LHC is told; you get a new "Request received" email.

**Common mistakes:**
- Replying to the email instead of using the link: replies go to an unmonitored mailbox.
- Waiting more than 14 days: the request expires and you must send a new one.

**If something goes wrong:** "This request has expired. Please submit a new request." means the 14 days have passed; send a new request.

### Review and decide a request

| Item | Value |
|---|---|
| Related journey | J-04 |
| Related process | W-02 |
| Required role | LHC Staff (R-02) or LHC Admin (R-03) |

**Steps**

1. On the queue at /staff, open the oldest Submitted request and select Take into review. Your name is shown as the reviewer.
2. Check the availability panel: it shows, for each night, how many rooms of that type are free.
3. Choose one:
   - **Confirm** if every night shows a free room. The rate in force on the check-in date is recorded.
   - **Return** if the guest must correct something. Enter what to correct (at least 10 characters); the guest sees it in the email.
   - **Reject** if LHC cannot accept the stay. Enter the reason (at least 10 characters).

**Expected result:** the request is Confirmed, Returned or Rejected, and the guest is emailed.

**Common mistakes:**
- Leaving a request in review overnight: the queue shows it as waiting, and the one-working-day target is missed.
- A vague reason such as "incomplete": say exactly what the guest must change.

**If something goes wrong:** "No Standard Twin room is available on 4 October." (with the room type and night) means that night is full; offer the guest other dates or a room type by returning the request.

### Assign a room and check a guest in and out

| Item | Value |
|---|---|
| Related journey | J-05 |
| Related process | W-03 |
| Required role | LHC Staff (R-02) or LHC Admin (R-03) |

**Steps**

1. Each morning open Reports, "Daily arrivals and departures" for today, and print it.
2. For each arrival without a room, open the booking and select Assign room; choose a room from the list of free rooms. The guest is emailed the room number.
3. When the guest arrives, select Check in.
4. When the guest leaves, select Check out.

**Expected result:** the booking shows the room, then Checked In, then Completed.

**Common mistakes:**
- Checking in before assigning a room: assign it first.

**If something goes wrong:** "Room 12 is not available on 4 October." means another booking holds that room on that night; choose another room. "Check-in opens on 3 October." means the stay has not started yet.

### Change or cancel a booking

| Item | Value |
|---|---|
| Related journey | J-06 |
| Related process | W-04 |
| Required role | LHC Staff (R-02) or LHC Admin (R-03) |

**Steps**

1. Search for the booking by reference or guest name at /staff and open it.
2. To change it, select Edit, change the dates, room type, number of guests or guest details, and select Save.
3. To cancel it, select Cancel booking, enter the reason (for example "Guest cancelled by phone") and confirm.

**Expected result:** the guest is emailed the new details, or the booking is Cancelled and its room is free again.

**Common mistakes:**
- Cancelling and creating a new request to change dates: use Edit so the booking keeps its reference and rate.

**If something goes wrong:** "No Standard Twin room is available on 10 October." means the new dates are full; the booking keeps its old dates.

## Concepts

### What the statuses mean

| Status | What it means for you | What happens next | Who acts next |
|---|---|---|---|
| ST-01 Draft | You have started a request but not sent it to LHC yet. | Finish and submit it from the Draft link; it is deleted after 30 days without change. | You |
| ST-02 Submitted | LHC has your request and will look at it within one working day. | A staff member takes it into review. | Staff |
| ST-03 Under Review | Someone at LHC is checking your request now. | Staff confirm, return or reject it. | Staff |
| ST-04 Returned | LHC needs more information from you. Open your booking link, make the changes asked for and send it again within 14 days. | You get a reminder after 7 days; after 14 days it expires. | You |
| ST-05 Rejected | LHC cannot accept this request. The email tells you why. | Nothing; you may send a new request. | — |
| ST-06 Confirmed | Your stay is booked. We will tell you your room before you arrive. | Staff assign a room and check you in on arrival. | Staff |
| ST-07 Checked In | You are checked in. Enjoy your stay. | Staff check you out when you leave. | Staff |
| ST-08 Completed | Your stay is finished. Thank you for staying with us. | Nothing. | — |
| ST-09 Cancelled | This booking is cancelled. | Nothing; the room is free for others. | — |
| ST-10 Expired | This request expired because it was not completed in time. Please send a new request. | Nothing; send a new request if you still want to stay. | Automatic |

Having a room assigned is not a separate status: a Confirmed booking shows the room number once staff have assigned it.

### How notifications work

All emails come from noreply-booking@lhc.example.org, carry your booking reference and link, and arrive within a few minutes. Do not reply to them; contact bookings@lhc.example.org instead.

| Notification | When you get it | What to do |
|---|---|---|
| NTF-01 Request received | When you submit or resubmit a request | Keep it: it has your booking link |
| NTF-02 New request to review | (LHC staff mailbox) when a request is submitted or resubmitted | Take it into review from the queue |
| NTF-03 Request returned | When LHC returns your request | Open the link, correct and resubmit within 14 days |
| NTF-04 Request rejected | When LHC rejects your request | Nothing; you may send a new request |
| NTF-05 Booking confirmed | When LHC confirms your stay | Keep it for arrival |
| NTF-06 Reminder: your request needs changes | 7 days after LHC returned your request, if you have not resubmitted | Correct and resubmit within 7 days |
| NTF-07 Request expired | 14 days after LHC returned your request, if you have not resubmitted | Send a new request if still needed |
| NTF-08 Booking updated | When your room is assigned or your booking details change | Check the new details |
| NTF-09 Booking cancelled | When LHC cancels your booking | Nothing |

### Why a request can be refused

The form will not submit until every required field is filled in correctly, the dates make sense (check-out after check-in, check-in from today to 365 days ahead, at most 30 nights), and the number of guests fits the room type. Staff cannot confirm a request if any night is already full for that room type, and cannot give a room to two bookings on the same night. These rules are in BUS-05.

### Rates

The nightly rate is the one in force on your check-in date when LHC confirms the booking, and it stays the same even if LHC's rates change later. Only LHC Management can change the rate of a confirmed booking.

## Reference

### Fields

| Field | Meaning | Required | Format or example |
|---|---|---|---|
| Check-in date | The day you arrive | Yes | 3 Oct 2026; from today to 365 days ahead |
| Check-out date | The day you leave | Yes | After the check-in date; at most 30 nights later |
| Room type | The kind of room | Yes | Standard Twin, Standard Single, Family Room |
| Number of guests | People staying in the room | Yes | 1 up to the room type's capacity |
| Name | The lead guest's full name | Yes | Ana Lopez |
| Email | Where LHC sends every update | Yes | ana@example.com |
| Phone | For LHC to call you if needed | Yes | +63 917 555 0199, with country code |
| Special requests | Anything LHC should know | No | Late arrival, ground floor |
| Booking reference | The number LHC uses for your request | Shown | LHC-2026-0153 |

### Error and warning messages

| Message | What it means | What to do |
|---|---|---|
| "Enter an email address" (and similar messages next to a field) | A required field is empty or not in a valid format | Correct the field and submit again |
| "Check-out date must be after check-in date" | The dates do not make a stay | Choose a later check-out date |
| "A Standard Twin room holds up to 2 guests" | Too many guests for the room type | Choose a larger room type or fewer guests |
| "Too many requests from your connection. Please try again in an hour or phone LHC on +1 555 0100." | Many requests were sent from your connection in the last hour | Wait an hour, or phone LHC |
| "This request has expired. Please submit a new request." | The 14 days to correct a returned request have passed | Send a new request |
| "We could not find that booking." | The link is incomplete, or the booking no longer holds personal data | Open the whole link from the email, or phone LHC |
| "No Standard Twin room is available on 4 October." | (Staff) That night is full for that room type | Return the request offering other dates or a room type |
| "Room 12 is not available on 4 October." | (Staff) Another booking holds that room on that night | Choose another room |
| "Assign a room before checking in." | (Staff) The booking has no room | Assign a room, then check in |
| "Check-in opens on 3 October." | (Staff) The stay has not started | Check in on the arrival date |
| "Enter a reason of at least 10 characters." | (Staff) Return or reject needs a clear reason | Write what the guest must change, or why LHC cannot accept |
| "Enter a cancellation reason." | (Staff) Cancel needs a reason | Enter the reason |
| "You do not have permission to do this" | (Staff) Your role does not allow this action | Ask the LHC Admin if you need it |
| "You do not have access to the staff screens." | (Staff) You have no role | Ask your line manager to request one |
| "Something went wrong" with a reference code | An unexpected error | Phone the ITS Service Desk (ext. 4000) and give the reference code |

## Admin tasks

### Update rooms and rates

| Item | Value |
|---|---|
| Related capability or process | C-08, C-09, W-05 (J-07) |
| Required role | LHC Admin (R-03) |

**Steps**

1. Open /staff/setup.
2. Rooms: select Add room, or open a room to change its type or select Deactivate when Facilities take it out of use.
3. Rates: when LHC Management approves a new rate card, select Add rate for each room type with the new nightly rate and its start date. Keep the approval email in the LHC management share.

**Expected result:** the room list and rate card match reality; availability counts change at once.

**If something goes wrong:** "Room 12 is assigned to booking LHC-2026-0153 on 4 October. Move that booking first." means a future booking still holds the room; assign that booking another room, then deactivate.

### Produce the monthly report

| Item | Value |
|---|---|
| Related capability or process | C-14, W-06 (J-08) |
| Required role | LHC Admin (R-03) or LHC Management (R-04) |

**Steps**

1. On the first working day of the month, open /staff/reports.
2. Select "Monthly booking and occupancy", choose last month and select Download.
3. LHC Admin: select "Run reconciliation" and check every figure matches before sending the file to LHC Management.

**Expected result:** a spreadsheet with occupancy, nights, income at confirmed rates, cancellations and response times.

**If something goes wrong:** if the reconciliation does not match, do not send the report; raise a support issue with the ITS Service Desk.

### Give a staff member a role

| Item | Value |
|---|---|
| Related capability or process | C-13, W-07 (J-09) |
| Required role | LHC Admin (R-03) for LHC Staff and LHC Management roles; ITS Support (R-05) for the LHC Admin and ITS Support roles |

**Steps**

1. Check the line manager's email and the approver's approval (BUS-04 Roles).
2. Open /staff/access and search for the person.
3. Select their role and Save.
4. Reply to the line manager that the role is given.

**Expected result:** the person sees the screens for their role after signing out and in again; the change is in the audit trail.

**If something goes wrong:** "No account found. Ask the person to sign in once, then try again." means the person has not signed in yet.

### Remove a staff member's access

| Item | Value |
|---|---|
| Related capability or process | C-13, W-07 (J-09) |
| Required role | LHC Admin (R-03); ITS Support (R-05) for urgent removal |

**Steps**

1. Open /staff/access and search for the person.
2. Select Remove role and Save, on the effective date given by the line manager or HR.
3. Reply to the line manager to confirm.
4. For urgent removal, phone the ITS Service Desk on ext. 4000 and say "urgent access removal" instead.

**Expected result:** the person's next page shows "You do not have access to the staff screens."

**If something goes wrong:** you cannot change your own role; ask ITS Support.

## FAQ and help

| Question | Answer |
|---|---|
| Can I change or cancel my booking online? | Not yet. Email bookings@lhc.example.org or phone +1 555 0100 in front office hours, and staff will change or cancel it for you. |
| I did not get the email. | Check your spam folder. Your booking link also works from the "Request received" screen. If you still have nothing, phone LHC. |
| How long will LHC take to answer? | Within one working day of your request. |
| Do I pay through the booking system? | No. Payment is taken at the front desk on arrival. |
| Can I book more than one room? | Send one request per room. |
| (Staff) A room shows free but it is out of use. | Tell the LHC Admin to deactivate it (Update rooms and rates). |
| (Staff) The site will not load. | Phone the ITS Service Desk on ext. 4000. During a long outage the supervisor will start the paper fallback using the printed arrivals list. |

| Problem | Contact | How | Hours |
|---|---|---|---|
| Question about a request, a booking or the process | LHC front office; for staff, the LHC Admin | +1 555 0100 or bookings@lhc.example.org; staff: bookings-admin@lhc.example.org or ext. 2120 | Monday–Saturday 07:00–21:00 |
| Access problem | ITS Service Desk | servicedesk.its.example.org or ext. 4000 | Monday–Friday 08:00–17:00 |
| Something is broken | ITS Service Desk | ext. 4000 by phone if it stops work; give the reference code on the error page | Monday–Friday 08:00–17:00; on call for outages (ext. 4999) |

## What's new

| Version | Date | What changed for you | Release |
|---|---|---|---|
| 1.0.0 | 2026-09-14 | First release: online booking requests with status tracking, staff review and room assignment, monthly report | ENG-07 release 1.0.0 |

## Accessibility statement

| Item | Value |
|---|---|
| Target standard | WCAG 2.2 AA |
| Requirement | NFR-08 |
| How and when checked | Automated scan of every page and a manual keyboard and screen-reader check of every journey by the ITS Accessibility Team, 2026-08-28 (audit AA-2026-014); repeated before each major release |
| Known gaps | None known |
| Report a problem | bookings@lhc.example.org or +1 555 0100; we reply within 2 working days and can take your request by phone meanwhile |

## Supported browsers and devices

| Browser or device | Supported versions | Requirement |
|---|---|---|
| Chrome, Edge, Firefox on Windows and macOS | Latest two major versions | NFR-09 |
| Safari on macOS and iOS | Latest two major versions | NFR-09 |
| Chrome on Android | Latest two major versions | NFR-09 |
| Screen size | 360 px wide and above (phones, tablets, desktops) | NFR-09 |

## Assumptions and open questions

No open questions.

## Known limitations

No known limitations beyond LIM-01 (guests cannot change or cancel online, BUS-02) and LIM-03 (email only, BUS-06), both answered in the FAQ.

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-08-14 | Daniel Reyes | Drafted from the journeys for the pilot | — |
| 1.0 | 2026-09-11 | Daniel Reyes | Accepted at go-live after the pilot; FAQ from pilot questions | Grace Tan, LHC Manager; Mark Lim, ITS Service Desk Lead, 2026-09-11 |
