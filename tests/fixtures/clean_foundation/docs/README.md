---
id: BUS-01
title: Application Overview & Business Case
application: Sample Request Tracker
version: 1.0
status: Draft
owner: Alex Owner, Business owner
audience: [Business owner, Support, Engineering, Agents]
level: Foundation
depth: D
contains: [SP-00, SP-10, SP-11, SP-12, BUS-02, BUS-03, BUS-05, BUS-06]
related: [ENG-09]
last_reviewed: 2026-09-01
---
# Sample Request Tracker – Application Overview & Business Case

## Purpose
Explains what the Sample Request Tracker is for and why it exists, so the owner can decide whether it is worth running.

## Scope
Covers the business case and, at Foundation level, the S sections listed in `contains`. Engineering detail is in ENG-09 (`AGENTS.md`).

## Business case
Staff log facility requests in one place instead of by email. Only one role exists (T2 is No): R-01 Staff member can do everything.

| ID | Name | Description |
|---|---|---|
| R-01 | Staff member | Any member of the team |

| ID | Benefit | Measure |
|---|---|---|
| BEN-01 | Fewer lost requests | SM-01 |

## What success looks like
No request is lost, measured by SM-01.

## SP-00 Scope Record

| Trigger | Question | Answer | Reason |
|---|---|---|---|
| T1 | Trigger question | No | Used through a shared form only; no screens of its own |
| T2 | Trigger question | No | One role |
| T3 | Trigger question | No | No statuses |
| T4 | Trigger question | No | No personal or confidential data |
| T5 | Trigger question | No | No integrations |
| T6 | Trigger question | No | Nobody relies on its outputs |
| T7 | Trigger question | No | No scheduled jobs |
| T8 | Trigger question | No | Runs on the shared team platform |
| T9 | Trigger question | Yes | The business owner is non-technical |
| T10 | Trigger question | No | Same maintainer throughout |
| T11 | Trigger question | No | Internal only |

| Item | Depth | Parent | Reason |
|---|---|---|---|
| SP-00 Scope Record | S | BUS-01 | Foundation |
| SP-01 Glossary | — | — | One team, shared vocabulary |
| SP-10 Success Measures | S | BUS-01 | Foundation |
| SP-11 Acceptance Criteria & Verification | S | BUS-01 | Foundation |
| SP-12 Acceptance & Handover Record | S | BUS-01 | Foundation |
| BUS-01 Overview & Business Case | D | — | Foundation |
| BUS-02 Capabilities | S | BUS-01 | Foundation |
| BUS-03 Business Processes | S | BUS-01 | Foundation |
| BUS-04 Roles & Access | — | — | T2 is No |
| BUS-05 Rules & Status Lifecycle | S | BUS-01 | Foundation |
| BUS-06 Data, Reports & Notifications | S | BUS-01 | Foundation |
| BUS-07 Resource & Cost | — | — | T8 is No; shared team platform |
| BUS-08 Risk & Controls | — | — | Limitations held in BUS-01 |
| BUS-09 User & Admin Guide | — | — | T1 is No |
| ENG-01 Requirements | S | ENG-09 | Foundation |
| ENG-02 User Journeys | — | — | T1 is No |
| ENG-03 Architecture & Design | S | ENG-09 | Foundation |
| ENG-04 Data Model | S | ENG-09 | Foundation |
| ENG-05 Integrations & Dependencies | S | ENG-09 | Foundation |
| ENG-06 Configuration & Environments | S | ENG-09 | Foundation |
| ENG-07 Deployment & Release | S | ENG-09 | Foundation |
| ENG-08 Operations & Support Runbook | S | ENG-09 | Foundation |
| ENG-09 Developer & Agent Guide | D | — | Foundation |
| ENG-10 Decision Log | — | — | T10 is No |

## SP-10 Success Measures Register

| ID | Measure | Level | Baseline | Target | Source | Owner |
|---|---|---|---|---|---|---|
| SM-01 | Requests lost per month | L1 | 3 | 0 by 2026-12-31 | Monthly owner check | Alex Owner |

## SP-11 Acceptance Criteria & Verification Register

| ID | Criterion | Verifies | Method | Priority | Result |
|---|---|---|---|---|---|
| AC-01 | A submitted request appears in the list within 1 minute | FR-01 | Manual test | Must | Not run |
| AC-02 | The list loads in under 2 s with 500 requests | NFR-01 | Measurement | Must | Not run |
| AC-03 | A request without a location is refused | BR-01 | Manual test | Must | Not run |

## SP-12 Acceptance & Handover Record
Sign-off checklist: not yet accepted.

### Consolidated known limitations

| Limitation | Raised in | Accepted by |
|---|---|---|
| LIM-01 | BUS-01 | Alex Owner |

## BUS-02 Capabilities Register

| ID | Capability | Processes | Roles | Dependencies |
|---|---|---|---|---|
| C-01 | Log a facility request | W-01 | R-01 | D-01 |

## BUS-03 Business Process Register

| ID | Process | Capabilities | Roles | Statuses |
|---|---|---|---|---|
| W-01 | Submit facility request | C-01 | R-01 | None |

## BUS-05 Business Rules & Status Lifecycle

| ID | Rule | Owner |
|---|---|---|
| BR-01 | Every request names a location | Alex Owner |

## BUS-06 Data, Reports & Notifications Register

| ID | Name | Classification | Retention | Core |
|---|---|---|---|---|
| REC-01 | Facility request | Internal | 2 years, for trend review | No |

## Assumptions and open questions
No open questions.

## Known limitations

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | No email confirmation | Requester must check the list | Check the list | Alex Owner |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 1.0 | 2026-09-01 | Alex Owner | First version | — |
