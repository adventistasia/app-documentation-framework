---
id: ENG-08
title: Operations & Support Runbook
application: LHC Booking System
version: 1.0
status: Accepted
owner: Mark Lim, ITS Service Desk Lead (Support owner)
audience: [Support desk, Technical operators, Business owner, Agents]
level: Standard
depth: D
contains: []
related: [BUS-01, BUS-04, BUS-06, BUS-08, BUS-09, ENG-01, ENG-03, ENG-05, ENG-06, ENG-07, SP-10, SP-12]
last_reviewed: 2026-09-11
---
# LHC Booking System – Operations & Support Runbook

## Purpose

Tells LHC staff, the ITS Service Desk and ITS engineers how the LHC Booking System is supported and kept running after go-live: who handles what, how issues are triaged and escalated, what is monitored, what to do when something fails, how data is backed up and restored, and how we check that its outputs are right.

## Scope

Covers business support, technical support, monitoring, incidents, runbook entries, backup, recovery, maintenance, output checks and change management. Dependencies are defined in ENG-05, deployment and rollback in ENG-07, environments and secrets in the ENG-06 section of ENG-09, user instructions in BUS-09, access rules in BUS-04. Commands are illustrative of the ITS Azure setup.

## Ownership model

| Area | Primary owner | Backup owner | Escalation owner | Notes |
|---|---|---|---|---|
| Business process questions | Daniel Reyes, LHC Front Office Supervisor | Ana Cruz, Senior LHC Staff | Grace Tan, LHC Manager | Rules in BUS-05 |
| User access and roles | Daniel Reyes, LHC Front Office Supervisor | ITS Service Desk (Mark Lim, ITS Service Desk Lead) | Grace Tan, LHC Manager | Follows BUS-04; ITS does urgent removal |
| Record correction | Daniel Reyes, LHC Front Office Supervisor | Ana Cruz, Senior LHC Staff (within LHC Staff permissions) | Grace Tan, LHC Manager | |
| System issue | ITS Service Desk (Mark Lim, ITS Service Desk Lead) | Leo Santos, ITS Developer | Priya Nair, ITS Application Lead | |
| Reports and outputs | Daniel Reyes, LHC Front Office Supervisor | Leo Santos, ITS Developer | Grace Tan, LHC Manager | Output checks below |
| Dependencies | Priya Nair, ITS Application Lead | Kevin Ho, ITS Network and M365 Administrator | Tom Rivera, ITS Infrastructure Manager | Support paths in ENG-05 |

## Support intake

| Issue type | First contact | Required information | Expected handling | Escalation path |
|---|---|---|---|---|
| Guest question about a request or booking | LHC front office, +1 555 0100 or bookings@lhc.example.org | Booking reference (LHC- followed by year and number), guest name | LHC Staff answer the same day in front office hours | LHC Admin, then LHC Manager |
| Staff question about the process or a record | LHC Admin, bookings-admin@lhc.example.org or ext. 2120 | Booking reference, what was expected | Answered within 1 working day | LHC Manager |
| Cannot sign in, missing role | ITS Service Desk portal (servicedesk.its.example.org) or ext. 4000 | Name, time, screenshot of the message | Service Desk checks Entra ID; LHC Admin checks the role; within 1 working day | ITS Application Lead if an SSO fault |
| Error page, slow pages, emails not arriving | ITS Service Desk ext. 4000 (phone for anything stopping work) | Booking reference, time, the correlation ID shown on the error page | Triage below; Sev1 and Sev2 by phone to on-call | ITS Application Lead |

## Service levels

**Support hours:** ITS Service Desk Monday–Friday 08:00–17:00; LHC front office Monday–Saturday 07:00–21:00. Outside ITS hours, the ITS on-call engineer handles Sev1 only (phone ext. 4999).

| Severity | Response target | Update interval | Resolution or workaround target |
|---|---|---|---|
| Sev1 | 30 min in support hours; 1 h on call | Every 1 h | Service restored within 4 h (NFR-13) |
| Sev2 | 2 h | Every 4 h | 1 working day |
| Sev3 | 1 working day | On change | 5 working days |
| Sev4 | 3 working days | On change | Next planned release |

| Measure | SLI | SLO | Window | Alert |
|---|---|---|---|---|
| SM-07 | Successful health checks ÷ all health checks, excluding announced maintenance | ≥ 99.5% | Calendar month | ALR-01 |
| SM-08 | Booking submissions answered with HTTP 2xx within 3 s ÷ all submission attempts | ≥ 99% | Calendar month | ALR-02 |
| SM-09 | Nightly job runs recorded as Success by 03:00 ÷ nights | 100% | Rolling 30 days | ALR-05 |
| SM-10 | Notifications accepted by M365 within 15 min of their trigger ÷ all notifications | ≥ 99% | Calendar month | ALR-03 |

## Triage guide

| Category | Examples | Owner | Initial checks | Dependencies | Escalate when |
|---|---|---|---|---|---|
| Access issue | Cannot sign in; "You do not have permission" | ITS Service Desk | Entra ID account enabled; MFA registered; role shown on /staff/access | D-05 | Role and account are correct and the problem persists, or more than one user is affected |
| Data correction | Wrong dates or guest details on a booking | Daniel Reyes, LHC Front Office Supervisor | Booking history (audit events) shows who changed it | None | The correction needs a status change the screens do not allow |
| Process question | "Why was my request returned?" | Daniel Reyes, LHC Front Office Supervisor | BUS-09 Concepts; the reason on the booking | None | The rule itself seems wrong: ask the rule owner in BUS-05 |
| System error | Error page; pages will not load; slow | ITS Service Desk | Health check; Azure status; recent deployment in ENG-07 release log | D-02, D-03, D-08 | Health check fails, or more than one user is affected |
| Notification issue | Guest says no email arrived | Daniel Reyes, LHC Front Office Supervisor | Notification log on the booking; failed-email list; guest's spam folder | D-04 | More than 5 failures in an hour (ALR-03) |
| Availability looks wrong | A room shows free but is out of use | Daniel Reyes, LHC Front Office Supervisor | Room list on /staff/setup; Facilities notice | D-06 | Counts are wrong for rooms that are correct in the room list |
| Rate looks wrong | Confirmation shows an old rate | Daniel Reyes, LHC Front Office Supervisor | Rate card on /staff/setup; confirmation date versus rate start date (BR-10) | D-07 | The rate card is right but the confirmation used another rate |
| Report issue | Monthly totals look wrong | Daniel Reyes, LHC Front Office Supervisor | Run the reconciliation (OC-02) | None | The reconciliation does not match |
| Requests waiting too long | Requests older than 1 working day in the queue | Daniel Reyes, LHC Front Office Supervisor | Reviewer on leave; staff rota | D-09 | More than 10 requests older than 1 working day |

## Dependency checks during incidents

| Symptom | Dependencies | Owner | Runbook | Notes |
|---|---|---|---|---|
| Nobody can open the site; health check failing | D-02, D-03 | Priya Nair, ITS Application Lead | RB-01, RB-02 | Check Azure status and the certificate first |
| Guests get errors when submitting | D-02 | Priya Nair, ITS Application Lead | RB-04 | |
| Emails not arriving | D-04 | Kevin Ho, ITS Network and M365 Administrator | RB-03 | Check M365 service health |
| Staff cannot sign in; guests unaffected | D-05 | Kevin Ho, ITS Network and M365 Administrator | RB-05 | |
| Only the front desk cannot reach the site | D-08 | Kevin Ho, ITS Network and M365 Administrator | None | Use the front-desk hotspot; ITS Network queue |
| Returned requests not expiring; reminders missing | D-02 | Priya Nair, ITS Application Lead | RB-06 | |

## Access support

| Request | Who may request | Who approves | Who performs | How | Target time |
|---|---|---|---|---|---|
| New role for a staff member | Line manager | Access approver in BUS-04 | LHC Admin (R-03); ITS Support (R-05) for R-03 and R-05 | BUS-09 Admin task "Give a staff member a role" | 2 working days |
| Role change | Line manager | Access approver in BUS-04 | LHC Admin (R-03) | Same task | 2 working days |
| Routine removal | Line manager; HR leaver notice | None needed | LHC Admin (R-03) | BUS-09 Admin task "Remove a staff member's access" | On the effective date |
| Urgent removal | LHC Manager, LHC Admin, ITS security team | None needed | ITS Support (R-05) | Remove the role on /staff/access and disable the Entra ID sign-in | 1 h in support hours; 4 h on call |

## Monitoring and alerting

**Health check:** `https://booking.lhc.example.org/health` returns HTTP 200 with `{"status":"ok","version":"1.0.x","db":"ok","outbox_age_s":<n>}`. It checks the database connection and the age of the oldest queued email. An Azure availability test calls it every 5 minutes from two regions.

**Dashboards:** Azure Portal workbook "LHC Booking – Operations" (resource group rg-lhcbook-prod): availability, error rate, p95 response by page, outbox age, last nightly run.

**Logs:** Application Insights `appi-lhcbook-prod`, kept 90 days. Find one request by its correlation ID: in Logs, run `requests | where customDimensions.correlation_id == "<id>"`. Logs never contain guest name, email or phone (NFR-11, NFR-07).

| Signal | Source | Normal range | Where to see it |
|---|---|---|---|
| Error rate (HTTP 5xx) | Application Insights requests | Below 0.5% of requests | Operations workbook |
| p95 response time | Application Insights requests | Below 1 s; target ≤ 2 s (NFR-02) | Operations workbook |
| Oldest queued email | /health outbox_age_s | Below 120 s | Operations workbook |
| Last nightly run | nightly_run table, shown on /health/jobs | Success before 02:30 | Operations workbook |

| ID | Alert | Threshold | Meaning | Severity | Owner | Notifies | Runbook |
|---|---|---|---|---|---|---|---|
| ALR-01 | Site down | 2 consecutive failed health checks from both regions (10 min) | Nobody can use the application | Sev1 | Priya Nair, ITS Application Lead | ITS on-call phone, Teams channel "LHC Booking Ops" | RB-01, RB-02 |
| ALR-02 | Submissions failing | More than 2% of booking submissions return 5xx over 15 min, with at least 5 attempts | Guests cannot send requests | Sev2 | Priya Nair, ITS Application Lead | Teams channel, ITS Service Desk queue | RB-04 |
| ALR-03 | Emails failing | 5 or more notifications marked Failed in 1 h, or oldest queued email older than 30 min | Guests and staff are not being told | Sev3 | Kevin Ho, ITS Network and M365 Administrator | Teams channel; email to bookings-admin@lhc.example.org | RB-03 |
| ALR-04 | Staff sign-in failing | More than 10 sign-in errors in 15 min | Staff cannot sign in | Sev2 | Kevin Ho, ITS Network and M365 Administrator | Teams channel, ITS Service Desk queue | RB-05 |
| ALR-05 | Nightly job missed | No Success record in nightly_run by 03:00 | Expiry, reminders, purges and output checks did not run | Sev3 | Priya Nair, ITS Application Lead | Teams channel | RB-06 |
| ALR-06 | Output check failed | OC-01, OC-03 or OC-05 finds 1 or more rows | An output may be wrong: see the check | Sev2 for OC-01; Sev3 for OC-03 and OC-05 | Priya Nair, ITS Application Lead | Teams channel; email to bookings-admin@lhc.example.org | RB-07 |
| ALR-07 | Certificate expiring | TLS certificate for booking.lhc.example.org expires within 21 days | Automatic renewal has not happened | Sev3 | Kevin Ho, ITS Network and M365 Administrator | Teams channel | RB-02 |

## Scheduled jobs

| Job | Schedule | Purpose | Component | Success signal | Alert | Runbook |
|---|---|---|---|---|---|---|
| Nightly job (`manage.py nightly`) | 01:30 daily (Asia/Singapore) | Sends 7-day reminders and expires 14-day Returned requests (BR-07); deletes old Drafts and anonymises bookings (NFR-07); deletes old notification log entries and audit events (NFR-12); runs OC-01, OC-03 and OC-05 | CMP-03 | A nightly_run row with status Success and the count of each step, usually finished by 01:45 | ALR-05; ALR-06 for the checks | RB-06 |
| Outbox worker (`manage.py run_worker`) | Continuous, polls every 30 s | Sends queued emails with retries (INT-01) | CMP-02 | Oldest queued email below 120 s | ALR-03 | RB-03 |

Each step of the nightly job is safe to re-run: it only acts on rows that still meet its condition, so running it twice on one night changes nothing the second time.

## Incident management

| Severity | Definition | Examples | Who is told |
|---|---|---|---|
| Sev1 | Service unavailable, data loss, or guest data exposed | Site down; database lost; a booking link shows another guest's booking | Grace Tan, LHC Manager; Priya Nair, ITS Application Lead; Ruth Ong, Data Protection Officer if data exposed; all LHC staff |
| Sev2 | A Must capability is unavailable or wrong and the workaround is hard | Submissions failing; staff cannot sign in; a room double-booked (OC-01) | Grace Tan, LHC Manager; Priya Nair, ITS Application Lead |
| Sev3 | Degraded; a workaround exists | Emails delayed; nightly job missed one night | Daniel Reyes, LHC Front Office Supervisor |
| Sev4 | Minor or cosmetic | A typo on a screen | Logged only |

**Who declares an incident:** any ITS Service Desk analyst or LHC Admin can declare Sev3–Sev4; Sev1–Sev2 are declared by the ITS on-call engineer, the ITS Application Lead or the ITS Service Desk Lead.

**Communication templates:**

```text
Initial: [Sev<n>] LHC Booking System – <what users see>. Started <time>. We are investigating. Next update by <time>.
Update:  [Sev<n>] LHC Booking System – <what we know, what we are doing, workaround>. Next update by <time>.
Resolved:[Sev<n>] LHC Booking System – resolved at <time>. Cause: <one line>. <Any action users need to take>.
```

**Post-incident review:** required for every Sev1 and Sev2 within 5 working days; blameless; records timeline, cause, impact and actions with owners. New failure modes get a runbook entry here and a risk in BUS-08. Reviews are stored in the ITS service desk tool under the service "LHC Booking System".

## Runbook entries

| ID | Failure mode | Triggered by | Dependencies | Owner |
|---|---|---|---|---|
| RB-01 | Application or database unavailable | ALR-01; triage "System error" | D-02 | Priya Nair, ITS Application Lead |
| RB-02 | Address does not resolve or certificate invalid | ALR-01, ALR-07 | D-03 | Kevin Ho, ITS Network and M365 Administrator |
| RB-03 | Emails not being delivered | ALR-03; triage "Notification issue" | D-04 | Kevin Ho, ITS Network and M365 Administrator |
| RB-04 | Guest submissions failing | ALR-02 | D-02 | Priya Nair, ITS Application Lead |
| RB-05 | Staff cannot sign in | ALR-04; triage "Access issue" | D-05 | Kevin Ho, ITS Network and M365 Administrator |
| RB-06 | Nightly job failed or missed | ALR-05; ALR-06 for OC-05 | D-02 | Priya Nair, ITS Application Lead |
| RB-07 | Output check found a problem | ALR-06 | None | Priya Nair, ITS Application Lead |

### RB-01 Application or database unavailable

- **Symptom:** ALR-01; users see "This site can't be reached" or an Azure error page.
- **Diagnosis:**
  1. Check https://status.azure.com for App Service or PostgreSQL incidents in the region. If there is one, follow its updates and go to step 3 of the fix.
  2. Run `az webapp show -g rg-lhcbook-prod -n app-lhcbook-prod --query state`. "Stopped" means the app was stopped; "Running" means look at the logs.
  3. In Application Insights, look at failures in the last 30 minutes. Database connection errors point to PostgreSQL: run `az postgres flexible-server show -g rg-lhcbook-prod -n psql-lhcbook-prod --query state`.
  4. Check the ENG-07 release log: was there a deployment in the last 2 hours?
- **Fix:**
  1. If a deployment preceded the failure, roll back (ENG-07 Rollback).
  2. If the app is stopped or unhealthy, run `az webapp restart -g rg-lhcbook-prod -n app-lhcbook-prod`.
  3. If PostgreSQL is down for more than 1 hour with no Azure estimate, start a restore (Backup and restore below) and tell LHC to use the paper fallback.
- **Verification:** /health returns 200 with `"db":"ok"`; submit a test request as the smoke-test guest (ENG-07 smoke tests); ALR-01 clears.
- **Escalation:** after 30 minutes without progress, phone Priya Nair, ITS Application Lead (ext. 4120); Azure support through the ITS contract ITS-AZ-2024-07 (ENG-05 D-02).

### RB-02 Address does not resolve or certificate invalid

- **Symptom:** browsers show a certificate warning or "server not found"; ALR-07 for an expiring certificate.
- **Diagnosis:**
  1. Run `nslookup booking.lhc.example.org`; it must return the App Service address.
  2. In the Azure Portal, App Service, Certificates: check the managed certificate's expiry and state.
- **Fix:**
  1. DNS wrong or missing: Kevin Ho restores the CNAME record in the organisation's DNS (registrar account ITS-DNS-01).
  2. Certificate not renewed: in App Service, Certificates, select the managed certificate and Renew; if that fails, delete and re-create the managed certificate for the custom domain.
  3. While fixing, ITS may give LHC the temporary address lhcbooking.azurewebsites.net.
- **Verification:** the site opens with a valid certificate from a phone on mobile data; ALR-01 and ALR-07 clear.
- **Escalation:** Tom Rivera, ITS Infrastructure Manager, if DNS cannot be fixed within 1 hour.

### RB-03 Emails not being delivered

- **Symptom:** ALR-03; guests say they did not receive emails; the failed-email list on /staff/notifications grows.
- **Diagnosis:**
  1. Check M365 service health (admin.microsoft.com) for Exchange Online incidents.
  2. Open /staff/notifications and read the last error: "535 Authentication unsuccessful" means the mailbox password or SMTP AUTH setting; "554 5.2.0" means the mailbox is blocked for sending; timeouts mean network or M365.
  3. Check the worker is running: Operations workbook, oldest queued email.
- **Fix:**
  1. Authentication error: Kevin Ho checks SMTP AUTH is enabled for noreply-booking@lhc.example.org and rotates the password into SEC-02 (ENG-06), then restarts the worker.
  2. Mailbox blocked: Kevin Ho releases it in the M365 admin centre.
  3. Worker stopped: restart the app (RB-01 fix step 2).
  4. When sending works, select "Retry all failed" on /staff/notifications.
  5. Meanwhile LHC Staff phone guests on the failed-email list whose stays start within 7 days.
- **Verification:** a test notification to bookings-admin@lhc.example.org arrives within 2 minutes; the failed list is empty after retry; ALR-03 clears.
- **Escalation:** Microsoft 365 support through Kevin Ho if not fixed within 4 hours.

### RB-04 Guest submissions failing

- **Symptom:** ALR-02; guests see "Something went wrong" with a correlation ID when they submit.
- **Diagnosis:**
  1. In Application Insights, filter failed requests to `POST /book/submit` in the last hour and open the top exception.
  2. A database error: follow RB-01. A validation exception with HTTP 500 is a defect.
  3. A spike in HTTP 429 is the rate limit (NFR-06), not a failure; check whether one address is sending many requests.
- **Fix:**
  1. Defect after a release: roll back (ENG-07).
  2. Abuse from one address: add a block rule in the App Service access restrictions and record it in the ticket.
  3. Tell LHC to take requests by phone until fixed.
- **Verification:** the smoke-test submission succeeds; the 5xx rate is below 0.5% for 15 minutes; ALR-02 clears.
- **Escalation:** Leo Santos, ITS Developer, for a code defect; Priya Nair, ITS Application Lead, after 1 hour.

### RB-05 Staff cannot sign in

- **Symptom:** ALR-04; staff see "Sign-in is not available right now".
- **Diagnosis:**
  1. Check M365 service health for Entra ID incidents.
  2. In Entra ID, App registrations, "LHC Booking System", Certificates & secrets: check whether the client secret has expired (SEC-03).
  3. Check the Entra sign-in logs for the application for the error code.
- **Fix:**
  1. Expired secret: create a new client secret, store it in SEC-03 (ENG-06), restart the app, and update MT-09 with the new expiry.
  2. Entra ID incident: wait; LHC uses the printed daily arrivals list and the public form.
- **Verification:** a staff member signs in and opens the queue; ALR-04 clears.
- **Escalation:** Tom Rivera, ITS Infrastructure Manager, if Entra ID is unavailable for more than 2 hours.

### RB-06 Nightly job failed or missed

- **Symptom:** ALR-05; or ALR-06 from OC-05 (Returned requests older than 14 days not expired).
- **Diagnosis:**
  1. Open /health/jobs: the last nightly_run row shows which step failed and the error.
  2. In the Azure Portal, App Service, WebJobs, "nightly": check the last run log.
- **Fix:**
  1. Fix the cause (database unavailable: RB-01).
  2. Re-run it: App Service, WebJobs, "nightly", Run. It is safe to re-run.
- **Verification:** a new nightly_run row shows Success; OC-05 shows 0 rows; ALR-05 clears.
- **Escalation:** Leo Santos, ITS Developer, if the same step fails twice.

### RB-07 Output check found a problem

- **Symptom:** ALR-06 naming OC-01, OC-03 or OC-05.
- **Diagnosis:**
  1. Open /health/jobs and read the rows the check returned.
  2. OC-01: the two bookings holding the same room on the same night. OC-03: Confirmed bookings with no logged confirmation email. OC-05: see RB-06.
- **Fix:**
  1. OC-01: phone Daniel Reyes, LHC Front Office Supervisor, at once; LHC Staff move one booking to another free room and phone that guest. Then raise a Sev2 defect, because the database rule should make this impossible.
  2. OC-03: retry the emails from /staff/notifications; LHC Staff phone guests whose stay starts within 7 days.
- **Verification:** run the check again from /health/jobs ("Run checks now"); it returns 0 rows.
- **Escalation:** Priya Nair, ITS Application Lead, for any OC-01 result.

## Backup and restore

| Data or store | Method | Frequency | Retention | Location | Encrypted | Owner |
|---|---|---|---|---|---|---|
| CMP-04 Database | Azure PostgreSQL automated backups with point-in-time restore | Daily full backup; transaction logs every 5 minutes | 35 days | Geo-redundant backup storage in the paired region | Yes | Priya Nair, ITS Application Lead |
| Application code and images | GitHub repository and Azure container registry | Every merge | Indefinite (code); last 20 images | GitHub organisation; registry in rg-lhcbook-shared | Yes | Priya Nair, ITS Application Lead |
| Secrets | Azure Key Vault with soft delete | On change | 90-day soft delete | kv-lhcbook-prod | Yes | Priya Nair, ITS Application Lead |

### Restore procedure

1. Declare an incident and agree the restore point with the technical owner: the latest minute before the failure or bad change.
2. Restore to a new server: `az postgres flexible-server restore -g rg-lhcbook-prod --name psql-lhcbook-restore --source-server psql-lhcbook-prod --restore-time "<YYYY-MM-DDTHH:MM:00+08:00>"` (about 30–60 minutes).
3. Put the new server's connection string into SEC-01 in Key Vault (ENG-06), then restart the app: `az webapp restart -g rg-lhcbook-prod -n app-lhcbook-prod`.
4. Re-run the nightly job if the restore point is before last night's run (RB-06).
5. **Verification:** /health returns `"db":"ok"`; the count of bookings matches the last known count from the Operations workbook within the RPO; open three bookings changed shortly before the restore point and check they are present; run OC-01 and OC-03 ("Run checks now").
6. Tell LHC which changes after the restore point must be re-entered (they are in the paper fallback or in staff emails).

### Restore tests

| Date | Performed by | What was restored | Environment | Time taken | Result | Evidence |
|---|---|---|---|---|---|---|
| 2026-08-28 | Joel Park, ITS Operations Engineer | Full database to a point in time 20 minutes earlier, following this procedure | ENV-02 | 1 h 35 min from start to verified service | Pass; data loss 5 minutes | ITS change record CHG-2026-0841, restore log in the ITS operations share |

The next restore test is MT-11.

## Disaster recovery and continuity

| Objective | Value | Requirement |
|---|---|---|
| Recovery time objective (RTO) | ≤ 4 h | NFR-13 |
| Recovery point objective (RPO) | ≤ 1 h | NFR-14 |

Backups every 5 minutes (transaction logs) meet the RPO. A loss of the whole Azure region is covered by geo-redundant backups, but a restore into the paired region has not been tested (LIM-04, RISK-07).

**Manual business fallback:** the LHC Front Office Supervisor (or the LHC Manager) decides to use it when the application is down for more than 30 minutes during front office hours. Staff check guests in from the printed daily arrivals list (REP-01, printed at 06:00 each day), take new requests by phone on the paper request form, and enter them into the application within 1 working day after service returns, oldest first.

## Routine operations

| ID | Task | Frequency | Owner | Procedure | Evidence of completion |
|---|---|---|---|---|---|
| MT-01 | Check the request queue for requests older than 1 working day; reassign any held by an absent reviewer | Daily, 09:00 | Daniel Reyes, LHC Front Office Supervisor | REP-03 queue screen | Front office daily checklist |
| MT-02 | Work through the failed-email list and phone the guests | Daily, 09:00 | Daniel Reyes, LHC Front Office Supervisor | /staff/notifications; RB-03 step 5 | Each entry marked "Phoned" |
| MT-03 | Reconcile the monthly report before sending it | Monthly, first working day | Daniel Reyes, LHC Front Office Supervisor | OC-02 | Reconciliation sheet saved with the report |
| MT-04 | Monthly sample audit of 10 bookings | Monthly, by the 5th working day | Daniel Reyes, LHC Front Office Supervisor | OC-04 | Sample audit sheet in the LHC management share |

## Maintenance calendar

| ID | Task | Type | Frequency | Next due | Owner | Procedure | Evidence |
|---|---|---|---|---|---|---|---|
| MT-05 | Apply runtime and package security patches | Patching | Monthly, in the Sunday 22:00–24:00 window | 2026-10-11 | Priya Nair, ITS Application Lead | ENG-07 normal release | Release log entry |
| MT-06 | Review and upgrade dependencies (Django minor versions, Python packages) | Dependency upgrade | Quarterly | 2026-12-13 | Priya Nair, ITS Application Lead | ENG-09 safe change steps | Pull request link |
| MT-07 | Renew the domain booking.lhc.example.org | Domain | Yearly | 2027-03-01 (expires 2027-03-31) | Kevin Ho, ITS Network and M365 Administrator | Registrar account ITS-DNS-01 | Registrar receipt in the ticket |
| MT-08 | Confirm the managed TLS certificate renewed | Certificate | Yearly | 2026-12-15 (expires 2027-01-15) | Kevin Ho, ITS Network and M365 Administrator | RB-02 diagnosis step 2 | Ticket note with the new expiry |
| MT-09 | Rotate the Entra ID client secret (SEC-03) and the mailbox password (SEC-02) | Secret rotation | Yearly | 2027-08-01 (SEC-03 expires 2027-08-31) | Kevin Ho, ITS Network and M365 Administrator | RB-05 fix step 1; RB-03 fix step 1 | Key Vault version date |
| MT-10 | Quarterly access review | Access review | Quarterly | 2026-12-15 | Grace Tan, LHC Manager | BUS-04 Periodic access review | Signed access list |
| MT-11 | Restore test | Restore test | Quarterly | 2026-11-29 | Priya Nair, ITS Application Lead | Restore procedure above, into ENV-02 | Row in Restore tests |
| MT-12 | Check nightly purge counts; delete anonymised bookings and rates older than 7 years | Data purge | Monthly check; deletion each January | 2026-10-05 | Priya Nair, ITS Application Lead | /health/jobs counts; `manage.py purge_retention --older-than-years 7` | Ticket note with the counts |
| MT-13 | Review the rate card, hosting charge-back and ITS service agreement | Licence | Yearly: rates by 1 December; charge-back and service agreement by 1 July | 2026-12-01 | Grace Tan, LHC Manager | W-05; BUS-07 Funding and ownership | Management meeting minutes |

## Output checks

| ID | Check | Type | Records | Procedure | Frequency | Owner | On failure |
|---|---|---|---|---|---|---|---|
| OC-01 | No room is held by two Confirmed or Checked In bookings on the same night (BR-05) | Invariant | REC-01, REC-02 | The nightly job runs `checks/double_booking.sql`, which counts pairs of booking nights with the same room and night whose bookings are in ST-06 or ST-07; expect 0 rows | Daily, automated | Priya Nair, ITS Application Lead | ALR-06 (Sev2); RB-07; tell Daniel Reyes at once |
| OC-02 | The monthly report agrees with the bookings: confirmed bookings, nights by room type and income at confirmed rates | Reconciliation | REC-01, REC-03 | Before sending REP-02, the LHC Admin selects "Run reconciliation" on /staff/reports, which counts the same figures directly from the bookings; every figure must match exactly | Monthly, first working day | Daniel Reyes, LHC Front Office Supervisor | Do not send the report; raise a support issue (W-08) |
| OC-03 | Every booking Confirmed more than 1 hour ago has a "Booking confirmed" email logged as sent | Completeness | REC-01, REC-04 | The nightly job runs `checks/confirmation_sent.sql`; expect 0 rows | Daily, automated | Priya Nair, ITS Application Lead | ALR-06 (Sev3); RB-07; staff phone the guests listed |
| OC-04 | A sample of bookings matches its request, its rate and its history | Sample audit | REC-01, REC-03, REC-06 | The LHC Admin opens "Sample audit" on /staff/reports, which picks 10 random bookings decided last month, and checks for each: dates, room type and guest details against the submitted request; the confirmed rate against the rate card on the confirmation date (BR-10); an audit event for every status change | Monthly, by the 5th working day | Daniel Reyes, LHC Front Office Supervisor | Correct the booking (W-04); raise a support issue if the cause is the system; tell Grace Tan |
| OC-05 | No request stays Returned more than 14 days (BR-07) | Invariant | REC-01 | The nightly job, after its expiry step, counts bookings in ST-04 returned more than 15 days ago; expect 0 rows | Daily, automated | Priya Nair, ITS Application Lead | ALR-06 (Sev3); RB-06 |

## Known issues

| Issue | Symptom | Workaround | Owner | Target date | Tracking |
|---|---|---|---|---|---|
| Audit trail export puts the old and new values in the wrong columns | REP-04 CSV unusable; export switched off (FLAG-01) | Read the history on the booking screen | Leo Santos, ITS Developer | 2026-11-30 | COND-01; issue LHCB-112 |

## Communication

| Event | Who communicates | To whom | Channel | When |
|---|---|---|---|---|
| Planned maintenance outside the Sunday window | Mark Lim, ITS Service Desk Lead | LHC staff; a banner for guests | Email to LHC staff; site banner | 3 working days before |
| Incident Sev1–Sev2 | Incident lead (ITS) | Grace Tan, LHC Manager; Daniel Reyes, LHC Front Office Supervisor; LHC staff | Phone, then email using the templates above | Within the response target, then each update interval |
| Guests affected by an outage or email failure | Daniel Reyes, LHC Front Office Supervisor | Affected guests | Phone or email from bookings@lhc.example.org | Same day |
| Release with visible changes | Priya Nair, ITS Application Lead | LHC staff | Email with the release notes (BUS-09 What's new) | On release day |
| Monthly report delayed by a failed reconciliation | Daniel Reyes, LHC Front Office Supervisor | LHC Management, LHC Finance | Email | The day it is found |

## Change management

| Change type | Definition | Examples | Approval | Lead time | Communication |
|---|---|---|---|---|---|
| Standard | Pre-approved, low-risk, repeatable | Add a room or rate; give a role; rotate a secret; monthly patching in the window | None beyond the procedure | None | Logged in the ticket |
| Normal | Anything else | New feature, rule or status change, schema change, new dependency | Priya Nair, ITS Application Lead; Grace Tan, LHC Manager if users will notice | 5 working days | Release notes; staff email if visible |
| Emergency | A fix needed to end a Sev1 or Sev2 | Hotfix; rollback | ITS on-call engineer or Priya Nair, ITS Application Lead, recorded within 1 working day | None | Incident updates; review afterwards |

**How to request a change:** raise a request in the ITS service desk tool under the service "LHC Booking System" with what should change, why, and who asked for it; the ITS Application Lead assesses it within 5 working days and agrees business changes with the LHC Manager.

## Assumptions and open questions

No open questions.

## Known limitations

No known limitations beyond LIM-04 (SP-12): the paired-region restore has not been tested.

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-07-27 | Priya Nair | First draft | — |
| 0.2 | 2026-08-28 | Mark Lim | Restore test recorded; triage reviewed with the ITS Service Desk | — |
| 1.0 | 2026-09-11 | Mark Lim | Accepted at go-live | Mark Lim, ITS Service Desk Lead; Priya Nair, ITS Application Lead; Daniel Reyes, LHC Front Office Supervisor, 2026-09-11 |
