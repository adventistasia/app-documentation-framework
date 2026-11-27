# Scoping Guide: Deciding What a Project Documents

## Purpose

Not every application needs every document. This guide is the method a team uses to decide, once and in writing, which information its application needs and in how much depth. The result is the **Scope Record (SP-00)**, and the package is reviewed against that record, not against the full standard.

Small projects do the foundational minimum, complex ones do the full standard, and most land in between. Scoping takes under 30 minutes for a small project. A person can run it, or the [scoping agent prompt](agent_prompts/scoping.md) can draft it for the owners to approve.

**The principle:** the full standard is a menu, not a checklist. Only information that answers a real question for a real reader gets written.

## The four steps

1. Score seven dimensions to pick a **level**: Foundation, Standard or Full.
2. Answer eleven **trigger** questions that add or drop specific items.
3. Read each item's **depth** from the matrix: not needed, section, document, or document with extras.
4. Record the result in the **Scope Record** and have the owners approve it.

---

## Step 1. Score the project to pick a level

Score each dimension 0 to 3. Pick the description that best fits; the descriptions matter more than the numbers. Write a one-line reason for each score.

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **D1 Users and reach** | Only the builder | One team, under 20 users | Several teams or departments | Public, customers or external partners |
| **D2 Impact if down or wrong** | Inconvenience | Work slows; a manual workaround is easy | A business process stops, or errors cost money | Safety, legal, financial or reputational harm |
| **D3 Data sensitivity** | No business data | Internal, non-personal data | Personal or confidential data | Special-category personal data, financial or regulated data |
| **D4 Integrations** | None | One or two, simple and one-way (for example, sends email, staff sign-in) | 2 to 4, or one two-way integration | 5 or more, or other systems depend on this one |
| **D5 Process and rule complexity** | Single task | Simple flow, one or two roles, no statuses or approvals | Several roles, statuses or approvals | Many rules, exceptions, approvals or calculations |
| **D6 Team and lifespan** | Throwaway, or under 3 months | One maintainer, under a year | Small team, or handed over to another team | Several teams, multi-year, or maintained mainly by agents |
| **D7 Regulatory and audit exposure** | None | Internal policy only | Internal audit, or contractual obligations | External regulation or certification applies |

| Total | Level | What it means |
|---|---|---|
| 0–7 | **Foundation** | The essentials: what it is, why it exists, how it works at a glance, how to run and support it, and how to tell it is working. |
| 8–15 | **Standard** | The core document set, with brief sections where depth adds little. |
| 16–21 | **Full** | The complete standard, including every section marked Full in the templates. |

### Floor rules

Floor rules stop a low total from hiding a serious risk. Apply them after totalling.

- **F1:** a 3 on D2, D3 or D7 sets the level to at least **Standard**.
- **F2:** a 3 on two or more of D2, D3 and D7 sets the level to **Full**.
- **F3:** a 2 or more on D6 (handover to another team, or maintained by agents) makes ENG-09 Developer & Agent Guide depth **D** at any level.

### Worked checks

| Project | D1 | D2 | D3 | D4 | D5 | D6 | D7 | Total | Floors | Level |
|---|---|---|---|---|---|---|---|---|---|---|
| Small internal tool for one team | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 5 | None | Foundation |
| Public booking system handed to IT support | 3 | 2 | 2 | 1 | 3 | 2 | 1 | 14 | F3 | Standard |
| Payroll export feeding finance and a regulator | 2 | 3 | 3 | 3 | 3 | 2 | 3 | 19 | F2, F3 | Full |

**Calibration:** the thresholds are a starting point. Record every scored project's scores and the level the owners finally agreed in the framework's calibration log ([CHANGELOG.md](CHANGELOG.md), "Calibration"). If two people score the same project and land on different levels, compare reasons dimension by dimension; the disagreement usually sits in one description that needs sharper wording.

---

## Step 2. Answer the triggers

The level sets the baseline. Triggers then adjust individual items, because the right set depends on what the application *is*, not only on how big it is.

- A **Yes** adds the item at least at section depth (S), even at Foundation.
- A **No** removes the item, or the part named, and its review criteria. Record the one-line replacement shown.

| Trigger question | If Yes | If No |
|---|---|---|
| **T1** Do people use it through a screen (not only through an API or a job)? | ENG-02 User Journeys and BUS-09 User & Admin Guide in scope | Drop both |
| **T2** Is there more than one role or permission level? | BUS-04 Roles & Access in scope | One line in BUS-01 stating who has access, with a single R-01 role |
| **T3** Do records move through statuses or approvals? | Lifecycle part of BUS-05; an AC for each transition | Drop the lifecycle part of BUS-05 |
| **T4** Does it store personal or confidential data? | Classification, purpose and retention in BUS-06; Security section and threat-model summary in ENG-03 | One line: "No personal or confidential data." |
| **T5** Does it exchange data with other systems? | Interface (INT) entries in ENG-05 | ENG-05 lists platform dependencies only |
| **T6** Does it produce outputs others rely on (reports, exports, calculations, notifications)? | L4 output checks in SP-10 and ENG-08 | Drop L4 |
| **T7** Does it run scheduled or background jobs? | Job monitoring and failure runbook entries in ENG-08 | One line: "No scheduled jobs." |
| **T8** Does it cost anything beyond an existing shared platform (licences, hosting, staff time)? | BUS-07 Resource & Cost Model in scope | One line in BUS-01 naming the shared platform |
| **T9** Does a non-technical person own it or approve its results? | Plain-language BUS-01 and L1 measures in SP-10 written for that owner | Owner sections may be brief |
| **T10** Will a different team or AI agents build or maintain it? | ENG-09 at depth D; ENG-10 Decision Log in scope | ENG-09 may be a short README |
| **T11** Is it public-facing? | Accessibility statement in BUS-09; Security section and threat-model summary in ENG-03 | Drop |

---

## Step 3. Read the depth of each item

| Depth | Meaning | What gets reviewed |
|---|---|---|
| **—** | Not needed. One line in the Scope Record says why. Nothing is written. | Nothing. Absence is not a finding. |
| **S** | Section. A few lines or a short table inside a parent document, headed `## <DOC-ID> <Title>`. | That item's **critical** criteria only. |
| **D** | Document. Its own file with the template's core sections. | All criteria not marked Full only. |
| **D+** | Document with extras: the template sections marked *(Full)*. | All criteria, including Full only. |

### Depth matrix

The **Parent** column says where an S item goes. A Scope Record may name a different parent, with a reason.

| Item | Foundation | Standard | Full | Parent when S | Triggers that change it |
|---|---|---|---|---|---|
| SP-00 Scope Record | S | D | D | BUS-01 | — |
| SP-01 Glossary | — | S | D | BUS-01 | Add at S if teams use different names for the same thing |
| SP-10 Success Measures | S (1–3 measures) | D | D+ | BUS-01 | T6, T9 |
| SP-11 Acceptance Criteria & Verification | S (Must features only) | D | D+ | BUS-01 | T3 |
| SP-12 Acceptance & Handover Record | S (sign-off checklist) | D | D+ | BUS-01 | — |
| BUS-01 Overview & Business Case | D (brief) | D | D+ | — | T9 |
| BUS-02 Capabilities | S | D | D+ | BUS-01 | — |
| BUS-03 Business Processes | S | D | D+ | BUS-01 | — |
| BUS-04 Roles & Access | — | D | D+ | BUS-01 | T2 |
| BUS-05 Rules & Status Lifecycle | S | D | D | BUS-01 | T3 |
| BUS-06 Data, Reports & Notifications | S | D | D+ | BUS-01 | T4, T6 |
| BUS-07 Resource & Cost | S | D | D+ | BUS-01 | T8 |
| BUS-08 Risk & Controls | — (limitations in BUS-01) | D | D+ | BUS-01 | — |
| BUS-09 User & Admin Guide | S (quick start) | D | D+ | BUS-01 | T1, T11 |
| ENG-01 Requirements | S (Must features, key NFRs) | D | D+ | ENG-09 | — |
| ENG-02 User Journeys | — | S | D | BUS-03 (BUS-01 when BUS-03 is itself S) | T1 |
| ENG-03 Architecture & Design | S (one diagram, stack) | D | D+ | ENG-09 | T4, T11 |
| ENG-04 Data Model | S (entity list) | D | D+ | ENG-09 | — |
| ENG-05 Integrations & Dependencies | S (list with owners) | D | D+ | ENG-09 | T5 |
| ENG-06 Configuration & Environments | S | S | D | ENG-09 | — |
| ENG-07 Deployment & Release | S | D | D+ | ENG-09 | — |
| ENG-08 Operations & Support Runbook | S (who supports, backups, health check) | D | D+ | ENG-09 | T6, T7 |
| ENG-09 Developer & Agent Guide | D (root `AGENTS.md`) | D | D | — | F3, T10 |
| ENG-10 Decision Log | — | D (light ADRs) | D | ENG-09 | T10 |

A **Foundation** package is therefore two files: `docs/README.md` (BUS-01, holding its S sections) and the root `AGENTS.md` (ENG-09, holding its S sections). It still answers every business, engineering and success question in the [documentation model](00_documentation_model.md), at a glance rather than in depth.

### Never dropped, at any level

These five things are always in scope. No trigger, deviation or approval removes them.

1. **What success looks like** (section in BUS-01).
2. **At least one success measure** with baseline, target, source and owner (SP-10).
3. **Application acceptance criteria for every Must feature** (SP-11).
4. **How to run and deploy it** (ENG-07, or its section in ENG-09).
5. **Who supports it**, and how to reach them (ENG-08, or its section).

---

## Step 4. Record the decision in the Scope Record

Use [templates/spine/SP-00-scope-record.md](templates/spine/SP-00-scope-record.md). It holds:

| Section | Content |
|---|---|
| Scores | D1–D7 with a one-line reason each, the total and the resulting level |
| Floor rules applied | F1, F2, F3, or "None" |
| Triggers | T1–T11 answers, each with a one-line reason |
| Item table | Every item with its depth (—, S, D, D+), its parent for S items, and a reason for every — |
| Deviations | Any item set differently from the matrix, with the reason and who agreed |
| Approval | Business owner and technical owner, with date |
| Re-scope log | Date, what changed, new level or depths, who approved |

## Rules that keep scoping honest

1. **Review against scope.** Reviewers and the verifier check the package against the Scope Record. An item marked — is not a finding, as long as its reason is recorded.
2. **Depth sets the rubric.** S items are judged on that item's critical criteria only; D items on all criteria not marked Full only; D+ items on all criteria.
3. **Re-scope when the project changes.** Re-score at each stage gate (see the [documentation model](00_documentation_model.md#stages)) and whenever an update trigger adds a role, integration, data type or user group. Raising a level or depth needs no approval. Lowering one needs the business owner's approval, recorded in the re-scope log.
4. **Write what answers a question.** A register with one or two rows becomes a sentence, unless its items carry IDs other documents link to; then a one- or two-row table is the short form. A section with nothing to say becomes one line.
5. **Reference instead of repeating.** Link to the other document by ID rather than copying it.
6. **Draft from what exists.** Where code, tickets or designs already hold the information, an agent drafts from them (see the [reverse producer prompt](agent_prompts/producer_reverse.md)) and people review rather than write from scratch.
7. **Promote, don't rewrite.** An S section uses the same tables as its template, so it can be lifted into its own file without restructuring when the level or depth goes up.
