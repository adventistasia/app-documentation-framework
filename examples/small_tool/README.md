# Example: a Foundation package (Stock Count Sheets)

This folder is a complete, illustrative Foundation-level documentation package for an invented internal tool. Everything in it (the tool, the people, the hosts, the commands, the test results and the sign-offs) is made up to show the shape of a good package. It describes no real organisation or system.

## The tool

**Stock Count Sheets** is a small web page used by one warehouse team of about 8 people. Every night it imports the inventory system's CSV export. Once a month the team lead prints blind count sheets per shelf location, the counters count, the team lead types in the counted quantities, and the tool exports a variance CSV that finance uses to adjust stock. It holds no personal data.

## Why it is Foundation

The Scope Record (the `## SP-00 Scope Record` section of `docs/README.md`) scores it 1 on every dimension: one team, an easy manual workaround, internal non-personal data, one simple inbound file, one monthly flow with two roles, one maintainer and an internal stock-count policy. The total is 7, the top of the Foundation band (0–7). No floor rule applies.

The triggers then add a few items the Foundation matrix would otherwise leave out or keep minimal:

| Trigger | Answer | Effect in this package |
|---|---|---|
| T1 screens | Yes | BUS-09 quick start and ENG-02 journeys, both as sections |
| T2 two roles | Yes | BUS-04 as a section (counter and team lead) |
| T3 statuses | No | BUS-05 holds rules only, with no lifecycle |
| T5 data exchange | Yes | An interface row (INT-01) for the nightly CSV |
| T6 outputs others rely on | Yes | An L4 measure (SM-03) linked to an output check (OC-01) |
| T7 scheduled job | Yes | Job monitoring, an alert and a runbook entry in ENG-08 |
| T8 cost | No | No BUS-07; one line in BUS-01 names the shared platform |
| T10 other team or agents | No | No ENG-10 Decision Log |

## How the two files map to the 24 items

A Foundation package is two files ([scoping guide](../../03_scoping_guide.md#depth-matrix)):

| File | Document | Sections it holds (depth S) |
|---|---|---|
| `docs/README.md` | BUS-01 Application Overview & Business Case | SP-00, SP-10, SP-11, SP-12, BUS-02, BUS-03, BUS-04, BUS-05, BUS-06, BUS-09, ENG-02 |
| `AGENTS.md` | ENG-09 Developer & Agent Guide | ENG-01, ENG-03, ENG-04, ENG-05, ENG-06, ENG-07, ENG-08 |

That is 20 items. The other four (SP-01, BUS-07, BUS-08 and ENG-10) are set to — in the Scope Record, each with a one-line reason. ENG-02 sits in BUS-01 because its default parent, BUS-03, is itself a section.

## What to look for

- **Every outcome question is answered at a glance.** B1 and S1 are answered by Benefits and What success looks like. B2 by the Problem statement and Impact if unavailable. B3 by BUS-02 and BUS-03. B4 by the Resources and costs summary and ENG-05. E1, E2 and E6 by ENG-03, ENG-04 and ENG-05. E3 by ENG-01 and BUS-05. E4 by the commands, ENG-06, ENG-07 and ENG-08. E5 by ENG-02 and BUS-09. S2 by SP-10 and the output checks. S3 by SP-11 and SP-12.
- **The success chain is linked by ID.** BEN-01 → SM-01 → C-04 → FR-04 → AC-07 → OC-01 → SM-03.
- **Sections keep the linked columns** of their templates (`Processes`, `Capabilities`, `Roles`, `Verifies`, `Records` and the others), so each can be promoted to its own file later without restructuring.
- **Acceptance is honest.** All 12 Must criteria have a result with evidence. The deploy, rollback and restore were dry-run by someone who did not write them. The three owners recorded their own decisions.

## Checking it

```text
python3 tools/doclint.py package examples/small_tool --today 2026-10-07
```

The linter reports no findings. The framework self-check (`python3 tools/doclint.py framework .`) lints this package too.

A deliberately flawed copy of this package, with its expected review results, is in [examples/review_training/](../review_training/README.md).
