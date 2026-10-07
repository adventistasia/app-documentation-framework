# Application Documentation Framework

A standard that teams and AI agents follow while they build and run applications, so that every application ends up with documentation that serves both the business and the engineers who build and operate it.

## What this framework is

This repository is a **guide to documenting an application**, not documentation of any application. It does three things:

1. **It tells teams what to document, and how much.** A short [scoping method](03_scoping_guide.md) decides which documents a project needs and at what depth, so small projects write two files and complex ones the full set. Nobody writes documents nobody needs.
2. **It requires every application's documentation to say how success is judged:** what success looks like, success measures at four levels, and **application acceptance criteria** that operators use to check whether the application and its output are right.
3. **It supplies documentation review criteria** (rubrics, cross-document rules, gates and a linter) that judge whether the *documents* are good enough.

"Application acceptance criteria" judge the application. "Documentation review criteria" judge the documents. The framework never uses the bare phrase "acceptance criteria", because mixing them up is how documentation ends up approved while the application is never tested against anything.

## What the resulting documentation lets people answer

| Business readers | Engineering readers (engineers, operators, AI agents) | Both |
|---|---|---|
| **B1** What the application contributes to the business | **E1** Technical design and architecture | **S1** What success looks like |
| **B2** Why it matters | **E2** How it works end to end | **S2** Success measures: business outcome, product acceptance, operational health, output correctness |
| **B3** What capabilities it enables | **E3** Functional and non-functional requirements | **S3** Testable application acceptance criteria |
| **B4** What it takes to deploy and run: people, effort, infrastructure, licences, cost | **E4** What it takes to deploy, operate and maintain it | |
| | **E5** User flows and journeys | |
| | **E6** Interfaces with other applications and systems | |

The [documentation model](00_documentation_model.md) explains how the documents answer these and how they link into one **success chain**, from a business benefit down to the daily check that proves the output is right.

## Where application documentation lives

In the application's own code repository, under `/docs`, as markdown with front-matter, versioned and reviewed with the code. A root `AGENTS.md` is what AI agents read first. Business readers get a generated site or PDF. See [conventions](02_conventions.md).

## How to start

| Step | Do this | Using |
|---|---|---|
| 1 | Score the project and record the scope (under 30 minutes for a small project) | [Scoping guide](03_scoping_guide.md), [SP-00 template](templates/spine/SP-00-scope-record.md), [scoping prompt](agent_prompts/scoping.md) |
| 2 | Write the documents in scope, stage by stage as the application is built | [Document register](01_document_set_register.md), [templates](templates/), [forward](agent_prompts/producer_forward.md) or [reverse](agent_prompts/producer_reverse.md) producer prompt |
| 3 | Lint the package | `python3 tools/doclint.py package <app-repo>` ([spec](review/05_linter_spec.md)) |
| 4 | Review documents and the package | [Review process](review/04_review_process.md), [rubrics](rubrics/), [reviewer](agent_prompts/reviewer.md) and [verifier](agent_prompts/verifier.md) prompts |
| 5 | Keep it true: update the listed documents in the same pull request as each change | [Update triggers](00_documentation_model.md#update-triggers) |

To see what good looks like, read a worked example:

- [examples/small_tool/](examples/small_tool/): a Foundation package in two files.
- [examples/lhc_booking_system/](examples/lhc_booking_system/): a Standard package for a public booking system, starting with its Scope Record.
- [examples/review_training/](examples/review_training/): deliberately flawed documents with the audit result a reviewer should produce.

## Files

```text
README.md                         this file
00_documentation_model.md         outcomes, layers, success chain, traceability, stages, update triggers, cadence
01_document_set_register.md       every document: purpose, readers, due stage, how to produce, questions to answer
02_conventions.md                 storage, file names, front-matter, layout, IDs, linked columns, writing style
03_scoping_guide.md               levels, floor rules, triggers, depth matrix, never-dropped minimum, Scope Record
templates/
  spine/                          SP-00 Scope Record · SP-01 Glossary · SP-10 Success Measures ·
                                  SP-11 Acceptance Criteria & Verification · SP-12 Acceptance & Handover
  business/                       BUS-01 … BUS-09
  engineering/                    ENG-01 … ENG-10
rubrics/
  00_universal_rubric.md          criteria for every document file
  01_business_rubrics.md          criteria per business document
  02_engineering_rubrics.md       criteria per engineering document
  03_spine_rubrics.md             criteria per spine document
  04_decision_rules.md            the only place decisions, severity and critical criteria are defined
review/
  01_audit_result_template.md     review output
  02_cross_document_rules.md      X-rules, each Mechanical or Judgment, each in one gate
  03_package_gates.md             G1–G8
  04_review_process.md            who reviews what, when, in which order
  05_linter_spec.md               what the linter checks
agent_prompts/                    scoping, producer (forward and reverse), reviewer, verifier
examples/                         worked packages and review-training material
tools/doclint.py                  the linter (Python 3, no dependencies)
build/                            manifest and script that generate consolidated_guide.md
consolidated_guide.md             every source file in one document, for agents with small contexts (generated; do not edit)
CHANGELOG.md                      framework versions, mapping from the 2026-06-30 release, calibration log
releases/                         archived releases
```

## Working on the framework itself

- Change a rule in the one file that owns it; other files link to it.
- After any change, run:

  ```text
  python3 build/build_consolidated.py
  python3 tools/doclint.py framework .
  python3 -m unittest discover -s tests
  ```

- Record the change in [CHANGELOG.md](CHANGELOG.md).
