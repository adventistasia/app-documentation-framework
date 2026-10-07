---
id: SP-01
title: Glossary
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Everyone, Agents]
level: <Foundation | Standard | Full>
depth: D            # D at Full; a section in BUS-01 at Standard; usually not needed at Foundation
contains: []
related: [BUS-04, BUS-05, BUS-06, ENG-04]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Glossary

> **How to use this template**
> - **Who writes it:** the business owner's delegate or the producer, starting from the role, status and record tables; engineers add technical terms. Agents may draft it from the home tables and mark entries inferred.
> - **When it is due:** Draft at stage 1 (Initiate), kept current through the build, Accepted at stage 5 (Go-live).
> - **Depth S (usually Standard):** a section `## SP-01 Glossary` in BUS-01 holding one Terms table with every role, status and record name, and any term teams use differently. Drop Abbreviations if there are none.
> - **Depth D (Full):** everything below. SP-01 has no sections marked (Full).
> - SP-01 is the vocabulary the linter checks names against: every `Name` in the role (BUS-04), status (BUS-05) and record (BUS-06) tables must appear here in the `Term` column, spelled the same way.
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

Defines every role, status, record and specialist term used in the <Application> documentation once, so every document, every screen and every conversation uses the same name for the same thing.

## Scope

Covers business and technical terms used anywhere in the package. Detailed definitions stay in their home documents (roles in BUS-04, statuses in BUS-05, records in BUS-06, entities in ENG-04); this glossary gives the one-sentence meaning and points to them.

## Terms

> **Guide:** one row per term, sorted alphabetically.
> - **Term:** exactly the name used in the home table's `Name` column and in the user interface. Capitalise as the documents do.
> - **Definition:** one plain sentence a new team member, a support person or an agent can understand. Do not define a term with itself.
> - **Synonyms to avoid:** other names people actually use (in email, old systems, the code) that documents must not use. Write "None" if there are none.
> - **Defined in:** the home document and ID, for example `BUS-05 ST-03`. Write "Here" for terms with no other home.
> - Include: every role, status and record name; every term teams use differently; every technical term in the engineering layer a newcomer would not know.
> Prefer: "Confirmed: the booking is accepted and the room is held for the guest." Avoid: "Confirmed: status after confirmation."

| Term | Definition | Synonyms to avoid | Defined in | Category |
|---|---|---|---|---|
| <Term> | <One sentence> | <… or None> | <DOC-ID and ID, or Here> | <Role / Status / Record / Business term / Technical term> |

## Abbreviations

> **Guide:** expand every abbreviation used in the package. If an abbreviation is also a term, define it once in Terms and list it here with a pointer. Write "No abbreviations used." if there are none.

| Abbreviation | Stands for | Meaning or see |
|---|---|---|
| <ABBR> | <Expansion> | <… or Terms: <Term>> |

## Assumptions and open questions

> **Guide:** record terms whose meaning is disputed between teams as open questions until the owner decides.

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | <…> | <…> | <YYYY-MM-DD> | <Open / Closed> |

## Known limitations

> **Guide:** for example, a legacy system that still uses a synonym the glossary says to avoid. Every `LIM-xx` also goes into SP-12. Write "No known limitations." if there are none.

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | <…> | <…> | <… or None> | <…> |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | <YYYY-MM-DD> | <Name> | First draft | — |
