# Conventions

This file is the single source for how application documentation is stored, named, identified and laid out. Templates, rubrics, review rules, agent prompts and the linter all follow it. If another file appears to disagree with this one, this file wins and the other file has a bug.

## 1. Where documentation lives

- An application's documentation lives **in the application's own code repository**, under `/docs`, as markdown files with YAML front-matter (docs-as-code). It is versioned, reviewed and merged with the code it describes.
- Put a short `AGENTS.md` at the repository root. It is either the full ENG-09 Developer & Agent Guide (Foundation level) or a pointer to it (Standard and Full).
- Business readers who do not use the repository read a generated site or PDF built from `/docs`. The markdown stays the source; nobody edits the generated copy.
- ENG-10 may keep one file per decision under `docs/decisions/ADR-001-<title>.md`. These files have no front-matter; they belong to ENG-10, and every ADR ID is defined in the ENG-10 decision index table, which links each file.
- Never store secret values (passwords, keys, tokens, connection strings) in documentation. Record *where* a secret is stored and who owns it.

Typical layouts:

```text
Foundation                         Standard / Full
repo/                              repo/
  AGENTS.md        (ENG-09)          AGENTS.md                       (points to ENG-09)
  docs/                              docs/
    README.md      (BUS-01)            SP-00-scope-record.md
                                       BUS-01-overview-and-business-case.md
                                       BUS-02-capabilities-register.md
                                       ...
                                       ENG-09-developer-and-agent-guide.md
                                       decisions/ADR-001-<title>.md    (optional: one file per ADR)
```

## 2. Document IDs and file names

Every document has a fixed **document ID** from the [document set register](01_document_set_register.md): `SP-00` to `SP-12` (spine), `BUS-01` to `BUS-09` (business layer), `ENG-01` to `ENG-10` (engineering layer).

- File name: `<DOC-ID>-<kebab-title>.md`, for example `BUS-02-capabilities-register.md`.
- Two allowed exceptions, both used mainly at Foundation level: BUS-01 may be `docs/README.md`, and ENG-09 may be the root `AGENTS.md`.
- A document is identified by the `id` in its front-matter, not by its file name.

### Items held as sections (depth S)

When the Scope Record sets an item to depth **S** (see the [scoping guide](03_scoping_guide.md)), it has no file of its own. It is a section inside a parent document:

- The section heading is `## <DOC-ID> <Title>`, where `<Title>` is the document's title in the [document set register](01_document_set_register.md), for example `## ENG-06 Configuration & Environments` or `## SP-10 Success Measures Register`.
- Inside an S section use level-3 headings and below, because the section ends at the next level-2 heading.
- The parent's front-matter lists it under `contains`.
- The section uses the core tables of that item's template, keeping every linked column (§6) and dropping other columns that add nothing, so it can be promoted to its own file without restructuring. It does not repeat the front-matter or standard sections; the parent's apply.

## 3. Front-matter

Every document file starts with this block. All keys are required; use `[]` for an empty list.

```yaml
---
id: BUS-02                      # document ID
title: Capabilities Register
application: <application name, identical in every document>
version: 1.0                    # 0.x while drafting; 1.0 at first acceptance; raise the minor number for each later accepted change
status: Draft                   # Draft | In Review | Accepted | Superseded
owner: <named person and role>  # accountable for the content
audience: [Business owner, Support, Engineering, Agents]
level: Standard                 # Foundation | Standard | Full (from the Scope Record)
depth: D                        # D | D+ (from the Scope Record; S items have no file)
contains: []                    # IDs of S-depth items held as sections in this file
related: [BUS-03, BUS-04, ENG-01, SP-11]   # document IDs only
last_reviewed: 2026-10-06       # ISO date
---
```

Rules:

- `related` and `contains` hold document IDs only. Each must exist in the package as a file or as a section (checked by the linter).
- `status: Accepted` requires a matching approval entry in the change log and, for the package, in SP-12. A document must never claim Accepted without that evidence.
- `level` is the same in every document of a package.

## 4. Standard document layout

Every template, and therefore every document, has this shape:

```markdown
---
(front-matter)
---
# <Application> – <Title>

## Purpose
Why this document exists and what decision or operation it supports. Two to four sentences.

## Scope
What this document covers and what it leaves to other documents (by ID).

## <Body sections>
Specific to the document type. See its template.

## Assumptions and open questions
| ID | Assumption or question | Owner | Due | Status |

## Known limitations
| ID | Limitation | Impact | Workaround | Owner |

## Change log
| Version | Date | Author | Summary | Approved by |
```

- If a standard section has nothing to say, write one line, for example "No known limitations." Do not delete the heading.
- Every limitation gets a `LIM-xx` ID and must also appear in SP-12 (X-12).
- Every open question gets a `Q-xx` ID.

## 5. Content IDs

IDs make cross-document links checkable by a script. They are fixed-format, unique within the application, and **never reused** after an item is deleted (mark it "Retired" instead).

Format: an uppercase prefix, a hyphen and a zero-padded number. Two digits unless shown otherwise (`C-01` … `C-99`, then `C-100`).

| Prefix | Item | Defined in (home) | Example |
|---|---|---|---|
| `BEN` | Benefit | BUS-01 | BEN-01 |
| `C` | Capability | BUS-02 | C-01 |
| `W` | Business process (workflow) | BUS-03 | W-01 |
| `R` | Role | BUS-04 | R-01 |
| `BR` | Business rule | BUS-05 | BR-01 |
| `ST` | Status | BUS-05 | ST-01 |
| `TR` | Status transition | BUS-05 | TR-01 |
| `REC` | Business record | BUS-06 | REC-01 |
| `REP` | Report, export or dashboard | BUS-06 | REP-01 |
| `NTF` | Notification | BUS-06 | NTF-01 |
| `COST` | Cost or effort line | BUS-07 | COST-01 |
| `RISK` | Risk | BUS-08 | RISK-01 |
| `FR` | Functional requirement | ENG-01 | FR-01 |
| `NFR` | Non-functional requirement | ENG-01 | NFR-01 |
| `J` | User journey | ENG-02 | J-01 |
| `CMP` | Component or container | ENG-03 | CMP-01 |
| `ENT` | Data entity | ENG-04 | ENT-01 |
| `D` | Dependency | ENG-05 | D-01 |
| `INT` | Interface (integration contract) | ENG-05 | INT-01 |
| `ENV` | Environment | ENG-06 | ENV-01 |
| `CFG` | Configuration item | ENG-06 | CFG-01 |
| `SEC` | Secret (location, never value) | ENG-06 | SEC-01 |
| `FLAG` | Feature flag | ENG-06 | FLAG-01 |
| `ALR` | Alert | ENG-08 | ALR-01 |
| `RB` | Runbook entry | ENG-08 | RB-01 |
| `OC` | Output check (L4) | ENG-08 | OC-01 |
| `MT` | Maintenance task | ENG-08 | MT-01 |
| `ADR` | Decision record (three digits) | ENG-10 | ADR-001 |
| `SM` | Success measure | SP-10 | SM-01 |
| `AC` | Application acceptance criterion | SP-11 | AC-01 |
| `T` | Test (automated or manual script) | SP-11 (referenced) | T-01 |
| `COND` | Acceptance condition or open handover item | SP-12 | COND-01 |
| `LIM` | Known limitation | Raised in any document, listed in SP-12 | LIM-01 |
| `Q` | Assumption or open question | Any document | Q-01 |

Rules:

- **Definition:** an ID is defined where it is the first cell of a table row whose first column header is `ID`. Each ID is defined exactly once in the package. Everywhere else it is a reference.
- **References** use the bare ID (`C-03`, `ST-02`). In tables, list several IDs separated by commas.
- **Names vs IDs:** tables refer to roles, statuses, capabilities and so on by ID. Prose may use the name, and the name must be exactly the one in the home table and in SP-01 Glossary.
- Document IDs (`SP-`, `BUS-`, `ENG-`) are never used as content IDs.
- Rubric criterion IDs (section 7) and audit finding IDs (section 8) are not content IDs and never appear inside an application's `/docs`.

## 6. Linked columns

The linter finds the tables that hold links by their header text, so these headers must be used exactly as written. A template may add other columns freely.

| Table (first column `ID`, prefix) | Column header | Holds | Checked by |
|---|---|---|---|
| Capabilities (`C`) | `Processes` | W IDs, or `Admin/support only` | X-01, X-02 |
| Capabilities (`C`) | `Roles` | R IDs | X-03 |
| Capabilities (`C`) | `Dependencies` | D IDs, or `None` | X-09 |
| Processes (`W`) | `Capabilities` | C IDs | X-01, X-02 |
| Processes (`W`) | `Roles` | R IDs | X-03 |
| Processes (`W`) | `Statuses` | ST IDs, or `None` | X-04 |
| Processes (`W`) | `Journeys` | J IDs, or `None` | X-16 |
| Rules (`BR`) | `Owner` | Person or role | X-06 |
| Transitions (`TR`) | `From`, `To` | ST IDs | X-05 |
| Transitions (`TR`) | `Roles` | R IDs, or `Automated` | X-03 |
| Records (`REC`) | `Core` | Yes / No (a core record needs an output check when T6 applies) | X-23 |
| Records (`REC`) | `Classification` | Public / Internal / Confidential / Personal / Special-category | X-17 |
| Records (`REC`) | `Retention` | Period and rationale | X-17 |
| Reports (`REP`) | `Audience`, `Purpose`, `Owner`, `Source` | Text | X-07 |
| Notifications (`NTF`) | `Trigger`, `Recipient`, `Purpose`, `Expected action` | Text | X-08 |
| Cost lines (`COST`, every table holding COST rows) | `Dependency` | D ID, or `None` | X-24 |
| Risks (`RISK`) | `Owner`, `Control` | Text | X-11 |
| Functional requirements (`FR`) | `Capabilities` | C IDs | X-18 |
| Functional / non-functional requirements (`FR`, `NFR`) | `Priority` | Must / Should / Could / Won't | X-19 |
| Non-functional requirements (`NFR`) | `Target` | Measurable target | X-19 |
| Journeys (`J`) | `Processes` | W IDs | X-16 |
| Journeys (`J`) | `Roles` | R IDs | X-03 |
| Journeys (`J`) | `Transitions` | TR IDs, or `None` | X-05 |
| Entities (`ENT`) | `Records` | REC IDs | X-17 |
| Entities (`ENT`) | `Classification` | As for records | X-17 |
| Dependencies (`D`) | `Type` | Hosting / Domain / Email / Identity / Integration / Data / Vendor / Network / People / Process / Funding | X-20 |
| Dependencies (`D`) | `Criticality` | High / Medium / Low | X-09, X-21 |
| Dependencies (`D`) | `Owner`, `Impact`, `Support path`, `Workaround` | Text (`None` allowed for Workaround) | X-09 |
| Dependencies (`D`) | `Capabilities affected` | C IDs; must agree with the capabilities that list this dependency in `Dependencies` | X-09 |
| Dependencies (`D`) | `Runbook` | RB IDs, or `None` | X-21 |
| Dependencies (`D`) | `Cost` | Yes / No | X-24 |
| Interfaces (`INT`) | `Dependency` | D ID | X-20 |
| Output checks (`OC`) | `Procedure`, `Frequency`, `Owner` | Text | X-23 |
| Alerts (`ALR`) | `Runbook` | RB IDs | X-21 |
| Triage categories (ENG-08) | `Dependencies` | D IDs, or `None` | X-15 |
| Output checks (`OC`) | `Records` | REC IDs | X-23 |
| Success measures (`SM`) | `Level` | L1 / L2 / L3 / L4 | X-22 |
| Success measures (`SM`) | `Baseline`, `Target`, `Source`, `Owner` | Text | X-22 |
| Success measures (`SM`) | `Links` | BEN, C, OC IDs | X-22, X-23 |
| Acceptance criteria (`AC`) | `Verifies` | FR, NFR, BR, J or TR IDs | X-19 |
| Acceptance criteria (`AC`) | `Method` | Automated test / Manual test / Inspection / Demonstration / Measurement | X-19 |
| Acceptance criteria (`AC`) | `Priority`, `Result` | Must/Should/Could; Not run / Pass / Fail / Waived | X-26 |
| Benefits (`BEN`) | `Measure` | SM IDs | X-22 |
| Capabilities, processes, roles, statuses, records, notifications (`C`, `W`, `R`, `ST`, `REC`, `NTF`) | `Name` | The exact name used in prose and in SP-01 | X-13 |
| Glossary (SP-01, first column `Term`) | `Term` | The defined term | X-13 |
| Risks (`RISK`) | `Severity` | High / Medium / Low | X-11 |
| Acceptance criteria (`AC`) | `Approver` | Who waived it, when `Result` is Waived | X-26 |
| Scope Record triggers (SP-00, first column `Trigger`) | `Trigger`, `Answer`, `Reason` | T1–T11; Yes / No | X-27 |
| Scope Record items (SP-00, first column `Item`) | `Item`, `Depth`, `Parent`, `Reason` | Document ID and title; — / S / D / D+ | X-27 |
| Known limitations (`LIM`) | — | Defined in each document's Known limitations section (first column `ID`); listed in SP-12's "Consolidated known limitations" table, whose first column header is `Limitation` | X-12 |

## 7. Rubric criterion IDs

- Universal criteria: `U-01` to `U-13`.
- Artifact criteria: `<DOC-ID>.<n>`, for example `BUS-02.4` is criterion 4 for the Capabilities Register.
- Each artifact rubric row has two flags: **Critical** (Yes/No) and **Full only** (Yes/No). How they are used is set in [rubrics/04_decision_rules.md](rubrics/04_decision_rules.md).

## 8. Review finding IDs

Audit results (produced by review agents, stored outside `/docs`, for example in the pull request or `docs/reviews/`) number their findings `A-BUG-01`, `A-RISK-01`, `A-IDEA-01`. The `A-` prefix keeps them apart from risks in the application's own BUS-08 register.

## 9. Writing style

- **Business layer and spine:** plain language for a manager, process owner or support person. Use business verbs. Prefer *Submit booking request* to *Submit button*, *Review booking request* to *Admin page*, *Generate monthly report* to *Excel export button*, *Manage access and roles* to *User table*, *Send notifications* to *Email API*.
- **Engineering layer:** technical language is expected, but every term a newcomer would not know is defined in SP-01 Glossary.
- **Unknowns:** write `TBD` with an owner and a `Q-xx` entry. Never invent a value, an owner, a sign-off or a test result.
- **Inferences:** when an agent derives content from code or other material instead of from a person, mark it `Inferred from <path or source>; confirm with <owner>` until confirmed.
- **Say it once:** if something is stated in another document, link to it by ID instead of copying it.
- **Write what answers a question:** a table with one or two rows becomes a sentence, unless its rows carry IDs that other documents link to (an ID is defined only in a table), in which case keep a short table; a section with nothing to say becomes one line ("No scheduled jobs.").
- **Diagrams:** use Mermaid in markdown so diagrams are versioned and diffable. Every diagram has a one-sentence caption saying what it shows.
- **Dates:** ISO format (`2026-10-06`). **Numbers:** include units and timeframes ("p95 ≤ 2 s at 50 concurrent users", not "fast").
- **Names:** generic files in this framework never use the names of a real application or organisation; those appear only under `examples/`.
