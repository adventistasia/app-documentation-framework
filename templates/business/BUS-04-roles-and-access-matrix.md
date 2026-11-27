---
id: BUS-04
title: Roles & Access Matrix
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Business owner, Access approvers, Support, Auditors, Engineering]
level: <Foundation | Standard | Full>
depth: <D | D+>
contains: []
related: [BUS-02, BUS-03, BUS-05, ENG-03, ENG-08, SP-01]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Roles & Access Matrix

> **How to use this template**
> - **Who writes it:** the producer with the business owner and the access approvers; the support owner confirms the request and removal steps. Engineers confirm the permissions match the authorisation model in ENG-03.
> - **When it is due:** Draft at stage 2 (Define), Accepted at stage 4 (Verify). Update with every new role or permission.
> - **In scope only when T2 is Yes** (more than one role or permission level). When T2 is No, BUS-01 defines a single `R-01` role in one line instead.
> - **Depth S:** a section `## BUS-04 Roles & Access Matrix` in BUS-01 holding the Roles table, the Permissions matrix, and one line each for who approves access and how it is removed.
> - **Depth D (Standard):** everything except sections marked (Full).
> - **Depth D+ (Full):** everything, including sections marked (Full).
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

Defines each role in <Application>, what it may do, who approves access to it, and how access is requested, removed and reviewed, so access decisions and audits can be made from this document.

## Scope

Covers every role (`R-xx`) used anywhere in the package: in capabilities, processes, journeys and transitions. How authentication and authorisation are built is in ENG-03; how support handles access requests day to day is in ENG-08.

## Roles

> **Guide:** one row per role. **Name** is the exact name used in prose, in the user interface and in SP-01. A role is a set of permissions and responsibilities, not a person or a team. Never include "System": automated actions are marked `Automated` in BUS-02, BUS-03 and BUS-05.

| ID | Name | Description | Typical users | Role owner | Access approver |
|---|---|---|---|---|---|
| R-01 | <Role name> | <What this role is for, in plain words> | <Job titles or groups> | <Name, role> | <Name, role> |

## Permissions matrix

> **Guide:** one row per role, Yes or No per action. Adjust the action columns to the application; keep them in business words. Where a permission is limited (for example, "only their own requests"), write the limit instead of Yes.

| Role | View | Create | Update | Approve / confirm | Return / reject | Cancel / delete | Manage setup | Manage users and roles | Generate reports | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| <R-xx> | <Yes / No / limit> | <…> | <…> | <…> | <…> | <…> | <…> | <…> | <…> | <…> |

> **Guide:** optionally add a capability view: one row per capability (`C-xx`) with the roles allowed to use it. It must agree with the `Roles` column in BUS-02.

## Access request

> **Guide:** numbered steps from "a person needs access" to "access works", naming who requests, who approves (the access approver from the Roles table) and who grants, with the expected time.

1. <…>
2. <…>
3. <…>

## Access removal

> **Guide:** numbered steps for routine removal (leaver, role change) and for **urgent removal** (suspected misuse, dismissal), with who triggers it, who performs it and how quickly. Say how removal is confirmed.

**Routine removal:**
1. <…>
2. <…>

**Urgent removal:**
1. <…>
2. <…>

## Periodic access review

> **Guide:** who reviews the list of users and roles, how often, what they check, and where the evidence is kept.

| Item | Value |
|---|---|
| Reviewer | <Name, role> |
| Frequency | <Quarterly / every 6 months> |
| What is checked | <Every user still needs their role; no leavers; sensitive roles justified> |
| Evidence kept in | <…> |

## Sensitive permissions and segregation

> **Guide:** list permissions that could cause harm if misused (administration, approval, export of personal data, deletion) and role combinations one person must not hold (for example, "submit and approve the same request"), with the control and its owner. Link risks in BUS-08.

| Permission or combination | Risk | Control | Owner |
|---|---|---|---|
| <…> | <…> | <…> | <Name, role> |

## Segregation of duties matrix (Full)

> **Guide:** a role-by-role grid marking which pairs of roles must not be held by the same person, and how the application or the process enforces it.

| Role | <R-01> | <R-02> | Enforced by |
|---|---|---|---|
| <R-01> | — | <Conflict / OK> | <Application check / periodic review> |

## Access review log (Full)

> **Guide:** record each completed access review.

| Date | Reviewer | Users reviewed | Changes made | Evidence |
|---|---|---|---|---|
| <YYYY-MM-DD> | <Name, role> | <n> | <…> | <link> |

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | <…> | <…> | <YYYY-MM-DD> | <Open / Closed> |

## Known limitations

> **Guide:** for example, a permission the application cannot restrict as finely as the business wants. Every `LIM-xx` also goes into SP-12. Write "No known limitations." if there are none.

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | <…> | <…> | <… or None> | <…> |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | <YYYY-MM-DD> | <Name> | First draft | — |
