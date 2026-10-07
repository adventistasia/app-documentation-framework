---
id: ENG-08
title: Operations & Support Runbook
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Support desk, Technical operators, Business owner, Agents]
level: <Foundation | Standard | Full>
depth: <D | D+>
contains: []
related: [BUS-01, BUS-04, BUS-06, BUS-08, BUS-09, ENG-01, ENG-03, ENG-05, ENG-06, ENG-07, SP-10, SP-12]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Operations & Support Runbook

> **How to use this template**
> - **Who writes it:** the support owner, with the technical owner for monitoring, runbook entries, backup and recovery, and the business owner for business support and communication. Validate it with the people who will actually do the support.
> - **When it is due:** Draft by stage 4 (Verify); Accepted by stage 5 (Go-live). Never dropped: who supports the application, and how to reach them, is always in scope.
> - **Depth S** (section `## ENG-08 Operations & Support Runbook` in ENG-09): the ownership model, support intake (how users get help), the triage guide with dependency checks, the health check and where to look when it fails, backup and restore with the last restore test, and a runbook entry for each High dependency. Add output checks when T6 is Yes and scheduled job monitoring when T7 is Yes. Keep every linked column (the linter checks them; other columns may be left out) and use level-3 subheadings named after this template's sections, so the section can later be promoted to its own file without restructuring.
> - **Depth D (Standard):** every section except those marked (Full).
> - **Depth D+ (Full):** every section, including (Full).
> - This document replaces DOC-08 Support and Operations Guide; all its sections are kept.
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

<Two to four sentences. Example: "Tells support staff and operators how <Application> is supported and kept running after go-live: who handles what, how issues are triaged and escalated, what is monitored, what to do when something fails, how data is backed up and restored, and how we check its outputs are right.">

## Scope

<Example: "Covers business support, technical support, monitoring, incidents, runbook entries, backup, recovery, maintenance, output checks and change management. Dependencies are defined in ENG-05, deployment and rollback in ENG-07, user instructions in BUS-09, access rules in BUS-04.">

## Ownership model

> **Guide:** Separate business support (questions about the process, decisions, data meaning) from technical support (the system is broken). Name people or teams, not "the team". Every area needs a backup owner and an escalation owner.

| Area | Primary owner | Backup owner | Escalation owner | Notes |
|---|---|---|---|---|
| Business process questions | <…> | <…> | <…> | <…> |
| User access and roles | <…> | <…> | <…> | <Follows BUS-04> |
| Record correction | <…> | <…> | <…> | <…> |
| System issue | <…> | <…> | <…> | <…> |
| Reports and outputs | <…> | <…> | <…> | <…> |
| Dependencies | <…> | <…> | <…> | <See ENG-05 support paths> |

## Support intake

> **Guide:** How a user gets help. Give the real channel (address, form, queue, phone) and what the user must include so the first responder does not have to ask.

| Issue type | First contact | Required information | Expected handling | Escalation path |
|---|---|---|---|---|
| <Cannot sign in> | <Service desk form, link> | <User name, time, screenshot of the error> | <Access owner checks role within 1 working day> | <Technical owner if SSO fault> |

## Service levels

> **Guide:** Support hours and response and resolution targets per incident severity (defined below), plus the operational service level objectives (SLOs). SLOs are the L3 success measures in SP-10: every L3 measure has one row here, referenced by `SM` ID with the same numbers, and names the alert that fires on breach.

**Support hours:** <e.g. Monday–Friday 08:00–17:00 local time, excluding public holidays. Outside hours: best effort, or the on-call rota.>

| Severity | Response target | Update interval | Resolution or workaround target |
|---|---|---|---|
| Sev1 | <30 min in support hours> | <Every 1 h> | <4 h> |
| Sev2 | <2 h> | <Every 4 h> | <1 working day> |
| Sev3 | <1 working day> | <On change> | <5 working days> |
| Sev4 | <3 working days> | <On change> | <Next planned release> |

| Measure | SLI | SLO | Window | Alert |
|---|---|---|---|---|
| <SM-05> | <Successful requests ÷ all requests at the load balancer> | <≥ 99.5%> | <Rolling 30 days> | <ALR-01> |

## Triage guide

> **Guide:** One row per category of issue a support person will meet. **Initial checks** are things the first responder can do without engineering access. **Dependencies** names the ENG-05 dependencies to check, by `D` ID, or `None` (X-15). **Escalate when** is a concrete condition, not "if needed".

| Category | Examples | Owner | Initial checks | Dependencies | Escalate when |
|---|---|---|---|---|---|
| Access issue | <Cannot sign in; missing menu item> | <…> | <User's role in the admin screen; account active> | <D-02> | <Role is correct and the problem persists> |
| Data correction | <Wrong date on a record> | <…> | <Record history; who changed it> | <None> | <Correction needs a status the user cannot set> |
| Process question | <Why was my request returned?> | <…> | <BUS-09 Concepts; record history> | <None> | <Rule seems wrong (BUS-05 rule owner)> |
| System error | <Error page; page will not load> | <…> | <Health check; status page; recent deployment> | <D-…> | <Health check fails or more than one user affected> |
| Notification issue | <Email not received> | <…> | <Spam folder; notification log> | <D-01> | <Several users affected> |
| Report issue | <Totals look wrong> | <…> | <Run the related output check (OC)> | <…> | <Output check fails> |

## Dependency checks during incidents

> **Guide:** A symptom map: when users see this, check these dependencies first. Each row points to the runbook entry that says what to do.

| Symptom | Dependencies | Owner | Runbook | Notes |
|---|---|---|---|---|
| <No emails being received> | <D-01> | <…> | <RB-01> | <Check provider status page first> |

## Access support

> **Guide:** How support handles account creation, role changes and access removal, following BUS-04. Include urgent removal (for example when someone leaves suddenly).

| Request | Who may request | Who approves | Who performs | How | Target time |
|---|---|---|---|---|---|
| <New account> | <Line manager> | <Access approver from BUS-04> | <Administrator R-…> | <BUS-09 admin task> | <2 working days> |
| <Urgent removal> | <Manager, security> | <None needed> | <…> | <…> | <1 h in support hours> |

## Monitoring and alerting

> **Guide:** What "normal" looks like and where to look. Every alert has an owner and links to at least one runbook entry (X-21); an alert with no runbook entry is noise. Prefer few, actionable alerts.

**Health check:** <URL or command, what it checks, expected response>

**Dashboards:** <Link and what each shows>

**Logs:** <Where they are, how to search them, retention, how to find one request by correlation ID>

| Signal | Source | Normal range | Where to see it |
|---|---|---|---|
| <Error rate> | <Load balancer logs> | <Below 0.5% of requests> | <Dashboard link> |

| ID | Alert | Threshold | Meaning | Severity | Owner | Notifies | Runbook |
|---|---|---|---|---|---|---|---|
| ALR-01 | <High error rate> | <Above 2% 5xx responses over 5 min> | <Users are seeing errors> | <Sev2> | <…> | <Channel, on-call> | <RB-02> |

## Scheduled jobs

> **Guide:** Required when T7 is Yes; otherwise write "No scheduled jobs." Every job needs a way to tell it ran and succeeded, an alert when it does not, and a runbook entry for re-running it safely.

| Job | Schedule | Purpose | Component | Success signal | Alert | Runbook |
|---|---|---|---|---|---|---|
| <Nightly export> | <02:00 daily> | <Sends confirmed records to D-04> | <CMP-05> | <Export file present, row count logged> | <ALR-03> | <RB-03> |

## Incident management

> **Guide:** Shared definitions so everyone agrees how bad something is. Examples make the definitions usable.

| Severity | Definition | Examples | Who is told |
|---|---|---|---|
| Sev1 | <Service unavailable or data loss or breach, many users affected> | <Nobody can sign in; data exposed> | <Business owner, technical owner, users> |
| Sev2 | <A Must capability is unavailable or wrong; workaround is hard> | <Requests cannot be submitted> | <Business owner, technical owner> |
| Sev3 | <Degraded; workaround exists> | <Reports delayed> | <Support owner> |
| Sev4 | <Minor or cosmetic> | <Typo on a screen> | <Logged only> |

**Who declares an incident:** <Any support person or operator can declare Sev3–Sev4; Sev1–Sev2 by the named on-call or support owner.>

**Communication templates:**

```text
Initial: [Sev<n>] <Application> – <what users see>. Started <time>. We are investigating. Next update by <time>.
Update:  [Sev<n>] <Application> – <what we know, what we are doing, workaround>. Next update by <time>.
Resolved:[Sev<n>] <Application> – resolved at <time>. Cause: <one line>. <Any action users need to take>.
```

**Post-incident review:** <Required for every Sev1 and Sev2 within 5 working days; blameless; records timeline, cause, impact, actions with owners. New failure modes get a runbook entry here and a risk in BUS-08. Store reviews at <location>.>

## Runbook entries

> **Guide:** One entry per alert, per High dependency (X-21), per scheduled job and per failure mode learned from incidents. Write for an operator at 03:00 who has never seen the code: exact commands, exact places to look, and how to tell the fix worked. Every entry ends with a **verification** step and an **escalation** contact.

| ID | Failure mode | Triggered by | Dependencies | Owner |
|---|---|---|---|---|
| RB-01 | <Emails not being delivered> | <ALR-02, triage "Notification issue"> | <D-01> | <…> |

### RB-01 <Failure mode>

- **Symptom:** <What users or monitoring see>
- **Diagnosis:**
  1. <Check, with exact command or link, and what each result means>
  2. <…>
- **Fix:**
  1. <Exact step>
  2. <…>
- **Verification:** <How to prove it is fixed, e.g. "Send a test notification; it arrives within 2 min; ALR-02 clears.">
- **Escalation:** <Who, how, after how long; vendor support path from ENG-05>

## Backup and restore

> **Guide:** What is backed up and how to get it back. A backup that has never been restored is a hope, not a backup: record the last restore test honestly, including failures. Frequency and retention must meet the RPO in ENG-01.

| Data or store | Method | Frequency | Retention | Location | Encrypted | Owner |
|---|---|---|---|---|---|---|
| <CMP-03 Database> | <Managed snapshots + point-in-time log> | <Daily + continuous> | <35 days> | <Separate account or region> | <Yes> | <…> |

### Restore procedure

1. <Exact step, e.g. "Create a new database instance from the snapshot or point in time.">
2. <…>
3. **Verification:** <e.g. "Record counts for ENT-01 match the last known count within the RPO; open the application and find a known recent record.">

### Restore tests

| Date | Performed by | What was restored | Environment | Time taken | Result | Evidence |
|---|---|---|---|---|---|---|
| <YYYY-MM-DD, or "Not yet tested"> | <Name> | <Full database to point in time> | <ENV-02> | <1 h 20 min> | <Pass / Fail> | <Link> |

## Disaster recovery and continuity

> **Guide:** RTO and RPO here must be identical to the recoverability NFRs in ENG-01; reference them by ID. The **manual business fallback** is what the business does while the system is down, drawn from the ENG-05 workarounds.

| Objective | Value | Requirement |
|---|---|---|
| Recovery time objective (RTO) | <≤ 4 h> | <NFR-02> |
| Recovery point objective (RPO) | <≤ 24 h> | <NFR-03> |

**Manual business fallback:** <What users do while the application is unavailable, who decides to invoke it, and how data captured meanwhile is entered afterwards.>

### Disaster recovery procedure (Full)

> **Guide:** Steps to rebuild the service in a different location or from nothing (lost account, region outage, ransomware), in order, with the expected time per step. Total must fit within the RTO.

1. <…>

### Disaster recovery tests (Full)

**Cadence:** <e.g. yearly, and after any major architecture change>

| Date | Scenario | Performed by | Achieved RTO | Achieved RPO | Result | Actions |
|---|---|---|---|---|---|---|
| <YYYY-MM-DD> | <Region loss> | <…> | <…> | <…> | <Pass / Fail> | <…> |

## Routine operations

> **Guide:** Day-to-day or weekly tasks that keep the application useful (clearing queues, reviewing stuck records, answering access requests). Calendar items with due dates go in the maintenance calendar below. Routine tasks and calendar tasks share the `MT` numbering, so BUS-07 can count the effort of each one by ID.

| ID | Task | Frequency | Owner | Procedure | Evidence of completion |
|---|---|---|---|---|---|
| MT-01 | <Review records stuck in a status for more than 5 days> | <Weekly> | <…> | <BUS-09 admin task or RB ID> | <Ticket or log entry> |

## Maintenance calendar

> **Guide:** Tasks that must happen on a date or a cycle, or something expires. Include every certificate, domain, licence and secret rotation that can lapse, with the next due date. Missed renewals are a common cause of outages. Renewal dates must match ENG-05 `Renewal` and the BUS-07 licence lines.

| ID | Task | Type | Frequency | Next due | Owner | Procedure | Evidence |
|---|---|---|---|---|---|---|---|
| MT-02 | <Renew TLS certificate for app domain> | <Patching / Certificate / Domain / Licence / Dependency upgrade / Access review / Data purge / Secret rotation> | <Yearly, or automatic> | <YYYY-MM-DD> | <…> | <RB ID or link> | <Where completion is recorded> |

## Output checks

> **Guide:** Required when T6 is Yes; otherwise write "No outputs others rely on." These are the L4 output-correctness checks from SP-10: repeatable checks that what the application produces is right, not only that it is running. Every record with `Core` = Yes in BUS-06 is covered by at least one check (X-23).
>
> **Type:** Invariant (a rule that must always hold, from BUS-05) · Reconciliation (two sources must agree) · Completeness (everything that should exist does) · Sample audit (a person checks a sample against the source) · Golden data (a fixed input must give a known output).

| ID | Check | Type | Records | Procedure | Frequency | Owner | On failure |
|---|---|---|---|---|---|---|---|
| OC-01 | <No resource is confirmed twice for overlapping dates> | <Invariant> | <REC-01> | <Run query `checks/double_booking.sql`; expect zero rows> | <Daily, automated> | <…> | <Raise ALR-04; follow RB-04; tell the record owner> |

## Known issues

> **Guide:** Open defects or operational quirks support should know about, with the workaround to give users. Permanent limitations go in Known limitations below (and SP-12).

| Issue | Symptom | Workaround | Owner | Target date | Tracking |
|---|---|---|---|---|---|
| <…> | <…> | <…> | <…> | <YYYY-MM-DD> | <Ticket link> |

## Communication

> **Guide:** Who tells users and stakeholders about outages, planned maintenance, changes and completed fixes, through which channel, and how far in advance. Include downstream consumers from ENG-05.

| Event | Who communicates | To whom | Channel | When |
|---|---|---|---|---|
| <Planned maintenance> | <Support owner> | <All users, downstream consumers> | <Email, banner> | <3 working days before> |
| <Incident Sev1–Sev2> | <Incident lead> | <Affected users, business owner> | <Status page, email> | <Within response target, then per update interval> |

## Change management

> **Guide:** How changes after go-live are requested, assessed, approved and communicated. Releases follow ENG-07; this section decides whether a change may go ahead.

| Change type | Definition | Examples | Approval | Lead time | Communication |
|---|---|---|---|---|---|
| Standard | <Pre-approved, low-risk, repeatable> | <Add a reference data value; rotate a secret> | <None beyond the procedure> | <None> | <None, or log> |
| Normal | <Anything else> | <New feature, schema change> | <Technical owner; business owner if user-visible> | <n working days> | <Release notes; user notice if visible> |
| Emergency | <Fix needed to resolve a Sev1–Sev2> | <Hotfix> | <Named role, recorded afterwards> | <None> | <Incident updates; review afterwards> |

**How to request a change:** <Channel, required information, who assesses it>

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | <…> | <…> | <YYYY-MM-DD> | <Open / Closed> |

## Known limitations

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | <…> | <…> | <…, or None> | <…> |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | <YYYY-MM-DD> | <Name> | First draft | — |
