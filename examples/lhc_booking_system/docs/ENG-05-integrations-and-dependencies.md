---
id: ENG-05
title: Integrations & Dependencies Register
application: LHC Booking System
version: 1.0
status: Accepted
owner: Priya Nair, ITS Application Lead (Technical owner)
audience: [Engineering, Support, Business owner, Agents]
level: Standard
depth: D
contains: []
related: [BUS-02, BUS-07, BUS-08, ENG-03, ENG-04, ENG-06, ENG-08]
last_reviewed: 2026-09-11
---
# LHC Booking System – Integrations & Dependencies Register

## Purpose

Lists everything the LHC Booking System relies on, with owners, impact if unavailable, support paths and workarounds, and the contract for its two data exchanges (email and staff sign-in). ITS Support uses it during incidents; engineers use it when changing an integration; the business owner uses it for renewals and costs.

## Scope

Covers systems, services, data, people and processes the application depends on. No system depends on this application. Runbook entries are in ENG-08, cost lines in BUS-07, connection settings and secret locations in the ENG-06 section of ENG-09.

## Dependency types

Values used in the `Type` column, as fixed by the framework: Hosting, Domain, Email, Identity, Integration, Data, Vendor, Network, People, Process, Funding. The LHC public website is typed Hosting, because the type covers websites.

## Dependency register

| ID | Dependency | Type | Purpose | Owner | Criticality | Impact | Support path | Capabilities affected | Workaround | Runbook | Cost | Renewal | Direction | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D-01 | LHC public website (www.lhc.example.org) | Hosting | Links guests to the booking form | Joy Bautista, LHC Communications Officer | Medium | Guests browsing the LHC website cannot find the booking form; the direct address still works | LHC Communications (ext. 2150); website hosting by ITS Web Team, ITS Service Desk queue "Web" | C-01 | Staff give the direct address booking.lhc.example.org by phone or email | None | No | None | Upstream | Existing site; no cost to this application |
| D-02 | ITS Azure hosting platform: App Service, Azure Database for PostgreSQL, Key Vault, Application Insights | Hosting | Runs the web application, worker, nightly job and database | Priya Nair, ITS Application Lead | High | Nobody can submit, review, confirm or check in on screen; emails stop | ITS Service Desk ext. 4000, queue "Applications"; Microsoft Azure support, ITS contract ITS-AZ-2024-07 | C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18 | Paper fallback in BUS-01 Impact if unavailable, using the printed daily arrivals list | RB-01, RB-04, RB-06 | Yes | 2027-06-30 (ITS charge-back year) | Upstream | |
| D-03 | Domain booking.lhc.example.org and its TLS certificate | Domain | Gives guests and staff a trusted address | Kevin Ho, ITS Network and M365 Administrator | High | The address does not resolve or shows a certificate warning; guests and staff cannot reach the application | ITS Service Desk ext. 4000, queue "Network"; registrar account ITS-DNS-01 | C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-13, C-14, C-15, C-17 | ITS can point the temporary address lhcbooking.azurewebsites.net to the service; staff give it to guests | RB-02 | Yes | Domain 2027-03-31; certificate renews automatically, expiry 2027-01-15 | Upstream | |
| D-04 | M365 email (Exchange Online SMTP) and mailbox noreply-booking@lhc.example.org | Email | Sends every notification | Kevin Ho, ITS Network and M365 Administrator | High | Guests are not told of decisions, returns or expiry; staff are not alerted to new requests | ITS Service Desk ext. 4000, queue "M365"; Microsoft 365 service health page | C-12 | Emails wait in the outbox; staff phone guests from the failed-email list and check the queue screen instead of the alert mailbox | RB-03 | No | None | Upstream | Covered by the organisation's M365 tenant |
| D-05 | Microsoft Entra ID single sign-on | Identity | Signs staff in, with MFA | Kevin Ho, ITS Network and M365 Administrator | High | Staff cannot sign in to review, confirm, assign rooms or check guests in; guests are not affected | ITS Service Desk ext. 4000, queue "Identity" | C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-13, C-14, C-15, C-17 | Staff use the printed daily arrivals list and take requests on the public form, which needs no sign-in | RB-05 | No | Client secret expiry 2027-08-31 (MT-09) | Upstream | Existing organisation licences |
| D-06 | Room inventory from LHC Facilities | Data | Tells the LHC Admin which rooms exist and are usable | Daniel Reyes, LHC Front Office Supervisor | Medium | If not passed on, availability counts include rooms that cannot be let, or miss new ones | LHC Facilities office ext. 2170 | C-02, C-08, C-10 | Staff stop assigning a room reported unusable until the LHC Admin updates it | None | No | None | Upstream | Entered by hand through C-08 |
| D-07 | Approved rate card from LHC Management | Data | Sets the nightly rates the LHC Admin enters | Grace Tan, LHC Manager | Medium | Confirmations use an out-of-date rate | LHC Manager ext. 2101 | C-09 | The rate exception (BUS-05) corrects individual bookings | None | No | Yearly review each 1 December | Upstream | |
| D-08 | LHC office network and internet link | Network | Lets staff at the front desk reach the application | Kevin Ho, ITS Network and M365 Administrator | Medium | Front desk staff cannot use the staff screens; guests elsewhere are not affected | ITS Service Desk ext. 4000, queue "Network"; internet provider contract ITS-ISP-2023-02 | C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-13, C-14, C-15, C-17 | Staff use the mobile hotspot kept at the front desk | None | No | None | Upstream | |
| D-09 | LHC booking staff on duty | People | Review and decide requests within one working day | Daniel Reyes, LHC Front Office Supervisor | Medium | Requests wait and miss the one-working-day target | LHC Front Office Supervisor ext. 2120 | C-03, C-04, C-05 | LHC Admin reviews the queue; LHC Manager arranges cover | None | No | None | Upstream | |
| D-10 | ITS Service Desk support process | Process | Takes, triages and routes technical and access issues | Mark Lim, ITS Service Desk Lead | Medium | Technical issues are not routed or fixed consistently | ITS Service Desk ext. 4000, servicedesk@its.example.org | C-15 | LHC Admin phones the ITS Application Lead directly for Sev1 | None | Yes | Yearly service agreement review each 1 July | Upstream | ITS staff time charged to LHC (BUS-07 COST-02) |

## Interfaces

| ID | Dependency | Direction | Protocol | Endpoint or location | Data exchanged | Trigger / frequency | Authentication | Error and retry behaviour | Contract | Other-side owner |
|---|---|---|---|---|---|---|---|---|---|---|
| INT-01 | D-04 | Out | SMTP with STARTTLS, port 587 | smtp.office365.com | ENT-05: recipient email, subject, body with booking reference, status and booking link | On each notification trigger; the worker polls the outbox every 30 s | Mailbox noreply-booking@lhc.example.org with SMTP AUTH, password SEC-02 | 5 attempts with back-off over 1 h; then marked Failed and listed for staff; 5 or more failures in 1 h raise ALR-03 | ITS email standard ES-3; M365 sending limits of 10,000 recipients a day | Kevin Ho, ITS Network and M365 Administrator |
| INT-02 | D-05 | In | OpenID Connect (authorisation code flow) | https://login.microsoftonline.com/(organisation tenant)/v2.0 | ENT-06: name, email, Entra object ID; no group claims | On each staff sign-in | Application registration "LHC Booking System", client secret SEC-03 | Sign-in page shows "Sign-in is not available right now. Please try again or call ITS on ext. 4000."; more than 10 failures in 15 min raise ALR-04 | ITS identity standard IS-2 | Kevin Ho, ITS Network and M365 Administrator |

## Downstream consumers

No system consumes data from the application. People who rely on its outputs (LHC Finance for REP-02) are listed in BUS-06 and told of outages through ENG-08 Communication.

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-03 | Microsoft is retiring basic SMTP AUTH for Exchange Online; will ITS move the noreply mailbox to OAuth before then, and when? INT-01 and SEC-02 change if so. | Kevin Ho, ITS Network and M365 Administrator | 2027-03-31 | Open |

## Known limitations

No known limitations.

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-06-08 | Priya Nair | First draft from the earlier single-file example's ten dependencies, with criticality, impact, workaround, runbook, cost and renewal added; D-01 typed Hosting | — |
| 1.0 | 2026-08-21 | Priya Nair | Accepted at stage 4 | Priya Nair, ITS Application Lead; Mark Lim, ITS Service Desk Lead, 2026-08-21 |
| 1.0 | 2026-09-11 | Priya Nair | Reviewed at go-live, no changes | Priya Nair, ITS Application Lead, 2026-09-11 |
