---
id: ENG-10
title: Decision Log
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Engineering, Agents, Future maintainers]
level: <Foundation | Standard | Full>
depth: <D | D+>
contains: []
related: [ENG-01, ENG-03, ENG-09, BUS-08]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Decision Log

> **How to use this template**
> - **Who writes it:** whoever makes the decision (engineer, technical owner or agent proposing it), approved by the deciders named in the record. Kept current during the build, not written at the end.
> - **When it is due:** Draft by stage 3 (Build), with ADRs added as decisions are made; Accepted by stage 5 (Go-live). In scope when trigger T10 is Yes, and at Standard and Full.
> - **Depth S** (section `## ENG-10 Decision Log` in ENG-09): the ADR index and, for each decision, a short record with context, decision, alternatives and consequences in a few lines.
> - **Depth D (Standard):** every section. At Standard, "light" ADRs of five to ten lines each are enough.
> - **Depth D+ (Full):** the same as D. No section is marked (Full), and the depth matrix never sets this item to D+.
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

<Two to four sentences. Example: "Records the significant technical and product decisions for <Application> as architecture decision records (ADRs): what was decided, why, what was rejected and what follows. It exists so that nobody, human or agent, undoes a deliberate choice without knowing why it was made.">

## Scope

<Example: "Covers decisions about technology, structure, data, security, hosting and deliberate omissions. Requirements and constraints imposed from outside are in ENG-01; the resulting design is described in ENG-03.">

## When to write an ADR

> **Guide:** Write an ADR for every choice an agent or a new engineer might otherwise "fix". If a reasonable person could look at the code and think "this is wrong, I'll change it", and it is deliberate, it needs an ADR. Typical cases:
> - Framework, language, data store and hosting choices.
> - Authentication and authorisation approach.
> - Deliberate omissions ("no caching", "no soft delete", "no mobile app").
> - A pattern that looks inefficient or odd but is intended (for example a denormalised table, a synchronous call, a manual step).
> - A trade-off between two NFRs (see ENG-03 Quality goals).
> - Anything that reverses or replaces an earlier ADR.
>
> Do not write an ADR for choices that follow directly from the coding conventions in ENG-09.

## Decision index

> **Guide:** One row per ADR, oldest first; IDs use three digits and are never reused. **Status:** Proposed (under discussion) · Accepted (in force) · Superseded by ADR-xxx (replaced; keep the old record, never delete it). A rejected proposal stays in the index with status `Rejected` so the discussion is not repeated.

| ID | Title | Status | Date | Deciders |
|---|---|---|---|---|
| ADR-001 | <Use a relational database for all business records> | <Proposed / Accepted / Superseded by ADR-00x / Rejected> | <YYYY-MM-DD> | <Names and roles> |

## Decision records

> **Guide:** Repeat this block for each ADR in the index. Write it so someone joining in two years understands the situation without asking. Keep it short: context and decision in a few sentences each. Alternatives must be real options that were considered, each with why it was not chosen. Consequences include the bad ones.
>
> **One file per ADR (optional):** a team may instead keep each record as `docs/decisions/ADR-001-<kebab-title>.md`, starting with `# ADR-001 <Title>` and using the same headings below. The index table in this document still defines every ADR ID and must link each file.

### ADR-001 <Title>

- **Status:** <Proposed / Accepted / Superseded by ADR-00x / Rejected>
- **Date:** <YYYY-MM-DD>
- **Deciders:** <Names and roles>

**Context**

<The problem or force that required a decision: requirement, constraint, incident or cost. Link IDs, e.g. NFR-02, RISK-03.>

**Decision**

<What was decided, stated as a rule someone can follow: "We will … ".>

**Alternatives considered**

| Option | Advantages | Disadvantages | Why not chosen |
|---|---|---|---|
| <Option A> | <…> | <…> | <…> |
| <Option B> | <…> | <…> | <…> |

**Consequences**

- Positive: <…>
- Negative: <…, including what becomes harder>
- Follow-up: <Work this creates, e.g. "Add runbook entry for failover (ENG-08)".>

**Links:** <ENG-03 section, requirements, risks, pull requests, the ADR this supersedes or is superseded by>

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
