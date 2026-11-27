# Spine Rubrics

These are documentation review criteria for the spine documents: SP-00 Scope Record, SP-01 Glossary, SP-10 Success Measures Register, SP-11 Acceptance Criteria & Verification Register and SP-12 Acceptance & Handover Record. They judge the documents, not the application. Apply them together with the [universal rubric](00_universal_rubric.md). Result values, which criteria apply at each depth, and how the **Critical** and **Full only** flags turn results into a decision are defined only in the [decision rules](04_decision_rules.md). Mechanical cross-document rules (X-xx) are checked by the linter and are not repeated here; a criterion below that touches one asks the reviewer to judge what the linter cannot.

Each document's templates are in `templates/spine/`. "Full only" criteria correspond to the template sections marked *(Full)*.

## SP-00 Scope Record

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| SP-00.1 | Scores with reasons | Every dimension D1–D7 has a score from 0 to 3 and a one-line reason specific to this application that a second scorer could check; the total is correct and the level follows the thresholds. | Yes | No |
| SP-00.2 | Floor rules | Floor rules F1–F3 are each marked as applying or not, consistently with the scores, and the final level reflects them. The final level equals `level` in every front-matter. | Yes | No |
| SP-00.3 | Triggers answered | Every trigger T1–T11 is answered Yes or No with a reason, and each answer is consistent with what the rest of the package describes (for example, T4 is Yes if any record is Personal). | Yes | No |
| SP-00.4 | Item table complete and correct | All 24 items are listed. Each depth matches the depth matrix for the final level after triggers, or is listed as a deviation. Every S item names its parent; every — item has a reason, including the one-line replacement a trigger requires. | Yes | No |
| SP-00.5 | Never-dropped minimum | What success looks like, at least one success measure, criteria for every Must feature, how to run and deploy, and who supports it are all in scope at some depth. | Yes | No |
| SP-00.6 | Deviations justified | Every depth or parent that differs from the matrix is listed with a reason, who agreed and the date. Any lowering is agreed by the business owner. | No | No |
| SP-00.7 | Approval recorded | The business owner and technical owner are named with their decision and date. Nothing is pre-filled. | Yes | No |
| SP-00.8 | Re-scope log kept | The record has been re-scored at each stage gate passed and after each update trigger that adds a role, integration, data type or user group, with a log row for each; lowered levels or depths show the business owner's approval. | No | No |

## SP-01 Glossary

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| SP-01.1 | Home names covered | Every role, status and record name from BUS-04, BUS-05 and BUS-06 appears as a `Term`, spelled exactly as in its home table. | Yes | No |
| SP-01.2 | Clear definitions | Every term has a one-sentence definition in plain language that a new team member, a support person or an agent can understand, and that does not define the term with itself. | Yes | No |
| SP-01.3 | One name per concept | No concept has two terms and no term has two meanings; terms used differently by different teams are resolved or raised as open questions. | No | No |
| SP-01.4 | Synonyms to avoid | Synonyms people actually use are listed for the terms that have them, and the rest of the package does not use those synonyms. | No | No |
| SP-01.5 | Points to home | Every term with a home document gives the document and ID in `Defined in`, and the definition agrees with the home. | No | No |
| SP-01.6 | Technical terms | Specialist and technical terms used in the engineering layer that a newcomer would not know are defined. | No | No |
| SP-01.7 | Abbreviations | Every abbreviation used in the package is expanded. | No | No |

## SP-10 Success Measures Register

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| SP-10.1 | Measures exist at the right number | At least one success measure exists; at Foundation 1–3 in total; at Standard and Full each level L1–L4 has at least one (L4 only when T6 is Yes). | Yes | No |
| SP-10.2 | L1 measures complete | Every L1 measure has a `Baseline` (a value with its date, or "Not measured – capture by <date>" with an owner), a `Target` with a timeframe, a `Source` and a named `Owner`, and links the benefit it measures. | Yes | No |
| SP-10.3 | Precise definitions | Every measure's definition says exactly how the number is calculated (numerator, denominator, filters, time window), so two people would get the same value. | No | No |
| SP-10.4 | Action threshold and frequency | Every measure has a threshold at which the owner must act and a measurement frequency. | No | No |
| SP-10.5 | Benefits measured | Every benefit in BUS-01 has at least one measure that would genuinely show whether the benefit is happening, not a proxy for activity. | No | No |
| SP-10.6 | L2 from acceptance results | L2 measures are based on SP-11 results (for example, pass rate of Must criteria) and defects, with targets. | No | No |
| SP-10.7 | L3 as SLO | Every L3 measure is written as an SLI with an SLO target over a stated window, and ENG-08 monitors it. | No | No |
| SP-10.8 | L4 output checks | When T6 is Yes, every L4 measure links an output check (`OC-xx`), and every core record in BUS-06 is covered by at least one output check, using a suitable check type (invariant, reconciliation, completeness, sample audit, golden data). | Yes | No |
| SP-10.9 | Review arranged | Who reviews which levels, how often and where results are reported is stated, with the date of the first L1 review. | No | No |
| SP-10.10 | Review log | Each L1 review is recorded with values against target and the decision taken. | No | Yes |
| SP-10.11 | Source data quality | Each source's known quality issues and their mitigation are stated. | No | Yes |

## SP-11 Acceptance Criteria & Verification Register

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| SP-11.1 | Coverage | Every Must functional requirement and every NFR has at least one criterion; every business rule and every transition has at least one positive and one negative criterion. At Foundation, every Must feature (and every transition when T3 is Yes) is covered. | Yes | No |
| SP-11.2 | Well-formed Given/When/Then | Each criterion gives the starting state and the actor by role, one action or event, and an observable outcome with concrete values; a third party could say Pass or Fail without asking the author. | Yes | No |
| SP-11.3 | One behaviour each | Each criterion tests one behaviour, and contains no implementation detail unless that detail is the requirement. | No | No |
| SP-11.4 | Verification method | Every criterion has a `Method` (Automated test, Manual test, Inspection, Demonstration or Measurement) that can actually show its outcome. | Yes | No |
| SP-11.5 | Evidence for results | Every result other than Not run has evidence that can be followed (test ID, path or link), who verified it and the date. No result is recorded that did not happen. | Yes | No |
| SP-11.6 | Priority inherited | Each criterion's priority matches the requirement, rule or transition it verifies. | No | No |
| SP-11.7 | Waivers and failures honest | Every Waived criterion names its approver and reason; every Fail has a defect or follow-up reference and an owner. | No | No |
| SP-11.8 | Summary matches | The results summary counts match the register and the date and environment of the last run are stated. | No | No |
| SP-11.9 | Traceability matrix | Every requirement, rule, transition and Must journey is shown with its criteria and combined result, with no gaps. | No | Yes |
| SP-11.10 | Re-verification | Which criteria are re-run after go-live, when, how and by whom is stated. | No | Yes |

## SP-12 Acceptance & Handover Record

| ID | Criterion | Pass condition | Critical | Full only |
|---|---|---|---|---|
| SP-12.1 | Delivered scope | What was delivered is listed by capability or process ID, with the evidence that each was accepted. | No | No |
| SP-12.2 | Deferred scope | Deferred items and open issues are listed with reason, owner and target, or the record says explicitly that nothing was deferred. | No | No |
| SP-12.3 | Acceptance results honest | Counts match SP-11. The record is not Accepted while any Must criterion is Not run or Fail, unless an owner has waived it, named with a date. | Yes | No |
| SP-12.4 | Success baseline | Each success measure shows whether its baseline is captured, missing baselines have a capture date, and the date and owner of the first L1 review are given. | No | No |
| SP-12.5 | Dry-run evidence | A deploy, a rollback and a restore have each been performed from the documents by someone who did not write them, with date, environment, result and evidence. | Yes | No |
| SP-12.6 | Accepted areas | Acceptance of the business processes, the roles and access model (definitions, permissions, request, removal) and the support model (intake, escalation, routine tasks, dependency support) is recorded with who accepted each. | No | No |
| SP-12.7 | Known limitations consolidated | Every known limitation raised anywhere in the package is listed with where it was raised, its impact and workaround, and who accepted it. | Yes | No |
| SP-12.8 | Accepted risks | Every High risk in BUS-08, and every Medium risk accepted rather than mitigated, is listed with its residual risk, who accepted it and when it is reviewed again. | No | No |
| SP-12.9 | Conditions owned | Every condition and open item has an ID, an owner, a target date and the owner who agreed to go live with it open. | No | No |
| SP-12.10 | Ownership after handover | A named person, team and support path is given for business ownership, business support, technical support, hosting, access administration, data ownership, releases and success-measure reporting, and they match BUS-01 and ENG-08. | Yes | No |
| SP-12.11 | Sign-off | The business owner, support owner and technical owner decisions are recorded by those people with dates. Nothing is pre-filled, and `status` is Accepted only when all three have accepted. | Yes | No |
| SP-12.12 | Early-life support | The early-life support period, arrangements, exit criteria and post-go-live review date are stated. | No | Yes |

## Mapping from the 2026-06-30 criteria

The 2026-06-30 release had no spine documents except DOC-11. SP-00, SP-01, SP-10 and SP-11 are new.

| Old ID | New ID |
|---|---|
| AH-01 Delivered scope | SP-12.1 |
| AH-02 Deferred scope | SP-12.2 |
| AH-03 Accepted workflows | Merged into SP-12.6 (business processes accepted) |
| AH-04 Accepted access model | Merged into SP-12.6 |
| AH-05 Accepted support model | Split: acceptance into SP-12.6, ownership into SP-12.10 |
| AH-06 Known limitations | SP-12.7 (accepted risks now also SP-12.8) |
| AH-07 Operational readiness | Replaced by SP-12.5 (dry-run evidence) and SP-12.6 |
| AH-08 Sign-off | SP-12.11 |
