---
id: BUS-06
title: Data, Reports & Notifications Register
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Data owner, Compliance, Business owner, Support, Engineering]
level: <Foundation | Standard | Full>
depth: <D | D+>
contains: []
related: [BUS-03, BUS-05, BUS-08, ENG-04, ENG-08, SP-10]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Data, Reports & Notifications Register

> **How to use this template**
> - **Who writes it:** the producer with the data owner; the compliance or privacy contact confirms classification, purpose and retention for personal data. Engineers map each record to its entities in ENG-04.
> - **When it is due:** Draft at stage 2 (Define), Accepted at stage 4 (Verify). Update with every new record, report, export or notification, and every change in classification or retention.
> - **Depth S (Foundation):** a section `## BUS-06 Data, Reports & Notifications Register` in BUS-01 holding the Records table (keep `Core`, `Classification`, `Purpose`, `Retention`). Reports and notifications may be one line each if there are only one or two; otherwise keep their tables with the linked columns.
> - **Depth D (Standard):** everything except sections marked (Full).
> - **Depth D+ (Full):** everything, including sections marked (Full).
> - **When T4 is No**, write one line under Records: "No personal or confidential data." and still classify each record.
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

Lists the business records <Application> holds, how each is classified and kept, and the reports, exports and notifications it produces, so the data owner, compliance and support know what data exists, why, for how long, and who relies on each output.

## Scope

Covers business records (`REC-xx`), reports, exports and dashboards (`REP-xx`), and notifications (`NTF-xx`). The technical entities and fields that store records are in ENG-04; statuses of records in BUS-05; output checks that confirm reports and records are correct in ENG-08 and SP-10 (L4).

## Records

> **Guide:**
> - **Name:** the exact name used in prose and in SP-01. **Required fields:** the business fields that must be present for the record to be valid.
> - **Core:** Yes when the business relies on the record being right (it drives decisions, money or reports). When T6 is Yes, every core record needs at least one output check in ENG-08.
> - **Classification:** Public / Internal / Confidential / Personal / Special-category (health, beliefs, biometrics and similar). Use the most sensitive field's class.
> - **Purpose:** for Personal and Special-category records, why the data is held and the lawful basis or policy that allows it. Write "—" for other records.
> - **Retention:** the period and the rationale ("7 years after the booking date: finance policy"). **Disposal:** how it is deleted or anonymised at the end, and by whom.
> Prefer: "Personal · Purpose: to contact the guest about their booking (contract) · Retention: 2 years after checkout, privacy policy section 4". Avoid: "Sensitive: Yes".

| ID | Name | Description | Required fields | Core | Classification | Purpose | Retention | Disposal | Owner | Processes |
|---|---|---|---|---|---|---|---|---|---|---|
| REC-01 | <Record name> | <…> | <…> | <Yes / No> | <Public / Internal / Confidential / Personal / Special-category> | <Purpose and lawful basis, or —> | <Period and rationale> | <Method and who> | <Name, role> | <W-xx> |

## Reports, exports and dashboards

> **Guide:** one row per report, export or dashboard others use. **Source:** the records (`REC-xx`) or system it is built from. **Official record:** Yes when the report itself is kept as evidence (for audit, finance or regulation). Reports others rely on need an output check in ENG-08 when T6 is Yes.

| ID | Name | Purpose | Audience | Frequency | Format | Source | Owner | Official record |
|---|---|---|---|---|---|---|---|---|
| REP-01 | <…> | <Decision or task it supports> | <Who reads it> | <…> | <Screen / PDF / spreadsheet / file feed> | <REC-xx or system> | <Name, role> | <Yes / No> |

## Notifications

> **Guide:** one row per message the application sends. **Trigger:** the event that sends it, usually a transition (`TR-xx`) or a schedule. **Expected action:** what the recipient should do, or "None, information only". Notifications that others rely on need a completeness check when T6 is Yes.

| ID | Name | Trigger | Recipient | Purpose | Expected action | Channel | Processes | Owner |
|---|---|---|---|---|---|---|---|---|
| NTF-01 | <…> | <TR-xx or event> | <R-xx or external party> | <…> | <…> | <Email / In-app / SMS / Chat> | <W-xx> | <Name, role> |

## Data subject requests (Full)

> **Guide:** required at Full level when there are Personal or Special-category records. Say how a person's request to see, correct, export or delete their data is received, who handles it, how it is carried out in the application, and the time limit.

| Request type | Received through | Handled by | How it is done | Time limit |
|---|---|---|---|---|
| <Access / Correction / Erasure / Export> | <…> | <Name, role> | <…> | <…> |

## Report lineage (Full)

> **Guide:** for each official or core report, the path from source records to the figures shown: filters, calculations and cut-off times, so a reconciliation can be designed and a disputed number traced.

| Report | Source records | Filters and calculations | Cut-off | Reconciled by |
|---|---|---|---|---|
| <REP-xx> | <REC-xx> | <…> | <…> | <OC-xx> |

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | <…> | <…> | <YYYY-MM-DD> | <Open / Closed> |

## Known limitations

> **Guide:** for example, a retention period not yet enforced automatically. Every `LIM-xx` also goes into SP-12. Write "No known limitations." if there are none.

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | <…> | <…> | <… or None> | <…> |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | <YYYY-MM-DD> | <Name> | First draft | — |
