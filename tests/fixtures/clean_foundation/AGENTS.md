---
id: ENG-09
title: Developer & Agent Guide
application: Sample Request Tracker
version: 1.0
status: Draft
owner: Sam Dev, Technical owner
audience: [Engineering, Agents]
level: Foundation
depth: D
contains: [ENG-01, ENG-03, ENG-04, ENG-05, ENG-06, ENG-07, ENG-08]
related: [BUS-01]
last_reviewed: 2026-09-01
---
# Sample Request Tracker – Developer & Agent Guide

## Purpose
Tells a developer or agent how the application is built, run and supported.

## Scope
Engineering at Foundation level; the business view is in BUS-01.

## ENG-01 Requirements Specification

| ID | Requirement | Capabilities | Priority |
|---|---|---|---|
| FR-01 | Store a submitted request | C-01 | Must |

| ID | Requirement | Target | Priority |
|---|---|---|---|
| NFR-01 | List performance | p95 under 2 s with 500 requests | Must |

## ENG-03 Architecture & Design
One web form writing to one database table (CMP-01).

| ID | Component | Purpose |
|---|---|---|
| CMP-01 | Form app | Collects and lists requests |

## ENG-04 Data Model

| ID | Entity | Records |
|---|---|---|
| ENT-01 | request | REC-01 |

## ENG-05 Integrations & Dependencies Register

> **Guide:** template guidance like this is skipped, so W-99 here is not a reference.
> It runs to the end of the blockquote: | ID | X-1 |

| ID | Dependency | Type | Owner | Criticality | Impact | Support path | Capabilities affected | Workaround | Runbook | Cost |
|---|---|---|---|---|---|---|---|---|---|---|
| D-01 | Team platform | Hosting | Platform team | Medium | Form unavailable | Platform help desk | C-01 | Email requests | None | No |

## ENG-06 Configuration & Environments
One environment; no secrets beyond the platform login.

## ENG-07 Deployment & Release Guide
Deploy by publishing the form from the platform console.

## ENG-08 Operations & Support Runbook
Supported by Sam Dev (sam@example.org). Backups are taken nightly by the platform.

## Assumptions and open questions
No open questions.

## Known limitations
No known limitations beyond LIM-01 in BUS-01.

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 1.0 | 2026-09-01 | Sam Dev | First version | — |
