---
id: BUS-09
title: User & Admin Guide
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [End users, Administrators, Support]
level: <Foundation | Standard | Full>
depth: <D | D+>
contains: []
related: [ENG-02, BUS-04, BUS-05, BUS-06, ENG-01, ENG-07, ENG-08]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – User & Admin Guide

> **How to use this template**
> - **Who writes it:** the producer with a representative user and an administrator; support reviews the help and error sections. Agents may draft how-tos from ENG-02 journeys and screens; a real user then follows each one.
> - **When it is due:** Draft at stage 4 (Verify), Accepted at stage 5 (Go-live). Update with every new or changed feature, status, role or error message, and add release notes with every release.
> - **In scope only when T1 is Yes** (people use it through a screen).
> - **Depth S (Foundation):** a section `## BUS-09 User & Admin Guide` in BUS-01 holding a quick start: Getting started (how to get access, the first task in a few numbered steps) and Help (where to get help). Add the Accessibility statement when T11 is Yes.
> - **Depth D (Standard):** everything except sections marked (Full), as one guide.
> - **Depth D+ (Full):** everything, including sections marked (Full).
> - The guide is organised by what the reader is trying to do: get started, do a task, understand, look something up, get help, see what changed. Write in the user's words and never tell a user to do something their role does not allow (check BUS-04).
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

Helps users and administrators of <Application> get started, complete their tasks, understand what they see, look things up, get help and keep up with changes.

## Scope

Covers every user-facing journey in ENG-02 as a how-to task, every user-visible status from BUS-05, and the administration tasks in BUS-04 and ENG-08. It does not cover technical operations (ENG-08) or deployment (ENG-07).

## Getting started

> **Guide:** a tutorial for a first-time user: how to get access, how to sign in, and one complete task from start to finish with what they should see at each step. A new user should succeed on the first try without help.

**Before you start**

| Item | Value |
|---|---|
| Who can use it | <Roles, in user words> |
| How to get access | <Request path; link to BUS-04 Access request> |
| Where to find it | <URL or entry point> |
| Where to get help | <Contact or link; see Help> |

**Your first <task>**

1. <…>
2. <…>
3. <…>

You should now see: <…>

## How-to tasks

> **Guide:** one task per user-facing journey in ENG-02, named by the user's goal ("Submit a booking request"), not the screen. Steps are short, numbered, and in plain words; say what the user should see when it worked. Separate user tasks from admin tasks (next section).

### <Task name>

| Item | Value |
|---|---|
| Related journey | <J-xx> |
| Related process | <W-xx> |
| Required role | <R-xx, in user words> |

**Steps**

1. <…>
2. <…>
3. <…>

**Expected result:** <what the user sees, including the new status>

**Common mistakes:**
- <…>

**If something goes wrong:** <what the user sees, what to do, who to contact>

## Concepts

> **Guide:** explains how the application behaves, so users understand what they see. Explain every user-visible status from BUS-05 in the user's words (BUS-05 `Meaning for users`), why a request can be returned or refused, and how notifications work (when they arrive, from whom, what to do).

### What the statuses mean

| Status | What it means for you | What happens next | Who acts next |
|---|---|---|---|
| <ST-xx Name> | <…> | <…> | <You / staff / automatic> |

### How notifications work

| Notification | When you get it | What to do |
|---|---|---|
| <NTF-xx> | <…> | <…> |

### <Other concept>

<…>

## Reference

> **Guide:** things users look up: field meanings and formats, error messages and what to do about each. Copy messages exactly as the application shows them.

### Fields

| Field | Meaning | Required | Format or example |
|---|---|---|---|
| <…> | <…> | <Yes / No> | <…> |

### Error and warning messages

| Message | What it means | What to do |
|---|---|---|
| "<Exact message text>" | <…> | <…> |

## Admin tasks

> **Guide:** tasks for administrators only, in the same format as how-to tasks, with the required role. Typical tasks: add a user and assign a role, remove access, change setup data, correct a record, run a report. Each must match a permission in BUS-04.

### <Admin task name>

| Item | Value |
|---|---|
| Related capability or process | <C-xx / W-xx> |
| Required role | <R-xx> |

**Steps**

1. <…>
2. <…>

**Expected result:** <…>

**If something goes wrong:** <…>

## FAQ and help

> **Guide:** the questions users actually ask (take them from support tickets after go-live), and the support path: who to contact for which kind of problem, how, and when. The support path must match ENG-08.

| Question | Answer |
|---|---|
| <…> | <…> |

**Getting help**

| Problem | Contact | How | Hours |
|---|---|---|---|
| <Question about the process or a record> | <…> | <…> | <…> |
| <Access problem> | <…> | <…> | <…> |
| <Something is broken> | <…> | <…> | <…> |

## What's new

> **Guide:** release notes in user language, newest first: what changed for the user and what they need to do differently. Link the technical release in ENG-07. Write "First release." for the initial version.

| Version | Date | What changed for you | Release |
|---|---|---|---|
| <…> | <YYYY-MM-DD> | <…> | <ENG-07 release reference> |

## Accessibility statement

> **Guide:** required when T11 is Yes (public-facing), and recommended otherwise. State the target standard (for example WCAG 2.2 AA), how conformance was checked and when, known gaps with workarounds and target dates, and how to report an accessibility problem. Trace to the accessibility NFR in ENG-01. Write "Not required: internal application (T11 No)." if it does not apply.

| Item | Value |
|---|---|
| Target standard | <WCAG 2.2 AA> |
| Requirement | <NFR-xx> |
| How and when checked | <…> |
| Known gaps | <… with workaround and target date> |
| Report a problem | <contact> |

## Supported browsers and devices

> **Guide:** the browsers, versions and devices the application supports, traced to the compatibility NFR in ENG-01. Say what happens on an unsupported one.

| Browser or device | Supported versions | Requirement |
|---|---|---|
| <…> | <…> | <NFR-xx> |

## Keyboard and assistive technology notes (Full)

> **Guide:** keyboard shortcuts, screen-reader notes and any task that needs a different method for assistive technology users.

| Task or area | Keyboard or assistive method | Notes |
|---|---|---|
| <…> | <…> | <…> |

## Training materials (Full)

> **Guide:** training sessions, videos or exercises for each role, with where to find them and who keeps them current.

| Material | For role | Where | Owner | Last updated |
|---|---|---|---|---|
| <…> | <R-xx> | <…> | <Name, role> | <YYYY-MM-DD> |

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | <…> | <…> | <YYYY-MM-DD> | <Open / Closed> |

## Known limitations

> **Guide:** limitations users will notice, with the workaround in user words. Every `LIM-xx` also goes into SP-12. Write "No known limitations." if there are none.

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | <…> | <…> | <… or None> | <…> |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | <YYYY-MM-DD> | <Name> | First draft | — |
