# Review Process

## Purpose

This process says who reviews application documentation, when, in what order, and what each step produces. The criteria themselves live elsewhere: the [universal rubric](../rubrics/00_universal_rubric.md), the artifact rubrics ([business](../rubrics/01_business_rubrics.md), [engineering](../rubrics/02_engineering_rubrics.md), [spine](../rubrics/03_spine_rubrics.md)), the [cross-document rules](02_cross_document_rules.md), the [package gates](03_package_gates.md) and the [decision rules](../rubrics/04_decision_rules.md).

## Roles

| Role | Does | Never does |
|---|---|---|
| Producer (person or agent) | Drafts and updates documents from people, code and existing material | Reviews its own output; records sign-offs or results that did not happen |
| Linter | Checks the mechanical cross-document rules exactly | Judges quality |
| Reviewer (person or agent) | Applies the rubrics and judgment rules; writes findings with evidence | Edits the document under review |
| Verifier (person or agent) | Applies the decision rules and gates to the review results; returns a decision | Re-reviews content or changes the rules |
| Business, support and technical owners | Confirm accuracy, agree conditions, sign off | Delegate sign-off to an agent |

## When reviews happen

Reviews follow the [stages](../00_documentation_model.md#stages), not one big review at the end.

| Event | What is reviewed | Decision needed |
|---|---|---|
| End of each stage | Every document due Accepted at that stage | Document decisions; the stage passes when they are Accept or Accept with Conditions |
| Go-live | The whole package against the Scope Record | Package decision |
| Any pull request that changes behaviour | The documents named by the [update triggers](../00_documentation_model.md#update-triggers) | The pull request reviewer confirms the listed documents were updated; the linter must show no new High or Medium findings |
| Review interval passes (Stale) | The stale document | Re-review; update `last_reviewed` and the change log |
| Re-scope | SP-00 and any document whose depth went up | Document decisions for the changed items |

## Review steps for a document

1. **Load scope.** Read SP-00 to find the document's depth and any items marked — or S. Out-of-scope criteria are recorded as Not in scope. If there is no Scope Record (for example, auditing documentation written before this framework), review at depth D and say so in the audit result.
2. **Run the linter** on the whole package. Copy its findings for this document into the audit result. They are authoritative for mechanical rules.
3. **Structure and rubric pass.** Apply the universal rubric (for files) and the artifact rubric (for the document's depth) criterion by criterion, with evidence.
4. **Coherence pass.** Read the related documents named in front-matter. Apply the judgment cross-document rules that touch this document. Look for contradictions the linter cannot see (a role that exists but whose permissions contradict a journey, a runbook that would not work).
5. **Readers' test.** Ask the questions the document must answer (from the [register](../01_document_set_register.md)) as its intended reader would. Any question the document cannot answer is a finding.
6. **Write the audit result** using the [audit result template](01_audit_result_template.md), classify findings as Bug, Risk or Idea with severity and evidence, and recommend a decision under the decision rules.
7. **Verify.** The verifier checks the audit result against the decision rules and issues the decision. Where the reviewer's recommendation and the rules disagree, the rules win and the verifier says why.
8. **Close.** Fixes go back to the producer. Conditions get `COND-xx` entries in SP-12 with owner and date. The owner records approval in the document's change log.

## Package review

After every document in scope has a decision:

1. Run the linter on the package.
2. Give each gate a result and compute the package decision, both as defined in the [decision rules](../rubrics/04_decision_rules.md#6-package-decision).
3. Confirm the three evidence checks in the gates table: approved Scope Record, dry-run of deploy, rollback and restore, and recorded owner decisions.

## Finding types

| Type | Meaning | Example |
|---|---|---|
| **Bug** | Something in the documentation is incorrect, inconsistent, missing or unusable. | Process W-04 uses role R-06, which BUS-04 does not define. |
| **Risk** | Something that may cause an operational, governance, support or acceptance failure. | High dependency D-04 has no runbook entry, so an outage would be handled ad hoc. |
| **Idea** | A non-blocking improvement. | Add a Mermaid state diagram to BUS-05. |

Severity is defined in the [decision rules](../rubrics/04_decision_rules.md#4-severity). Every Bug and Risk cites evidence.

## Framework feedback

If a reviewer finds that the framework itself has a blind spot (a criterion that misses a real problem, or a template that forces busywork), they note it in the optional **Framework feedback** section of the audit result. It never affects the decision. Framework changes go through this repository's pull requests and [CHANGELOG.md](../CHANGELOG.md).
