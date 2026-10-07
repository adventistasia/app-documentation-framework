# Decision Rules

This file is the **only** place where review decisions, result scales, severity and the use of critical criteria are defined. Rubrics, gates, the audit template, the review process and agent prompts refer to it and never restate its conditions.

## 1. Criterion results

Each criterion in the [universal rubric](00_universal_rubric.md) and the artifact rubrics gets one result.

| Result | Meaning |
|---|---|
| **Pass** | Satisfied, with evidence the reviewer can point to. |
| **Partial** | Partly satisfied: a gap, an ambiguity or weak evidence. |
| **Fail** | Missing, contradicted or unusable. |
| **Not in scope** | The Scope Record sets this item or section to —, or the criterion is Full only and the item's depth is not D+. Cite the Scope Record line. |
| **Not applicable** | The criterion cannot apply to this application, with a one-line reason (for example, "no reports produced"). |

## 2. Which criteria apply

Depth comes from the Scope Record (SP-00).

| Item depth | Universal criteria | Artifact criteria |
|---|---|---|
| — | None | None |
| **S** (section in a parent) | Applied to the parent file, not to the section | The item's **Critical = Yes** criteria only |
| **D** | All | All with **Full only = No** |
| **D+** | All | All |

An S item has no status or decision of its own. Its criterion results and findings count toward the decision on the parent file.

## 3. Critical criteria

- A criterion is critical when its rubric row says **Critical = Yes**. Every artifact rubric marks at least two.
- The critical universal criteria are U-01 Identity, U-02 Purpose, U-04 Required structure, U-07 Traceability, U-08 Usability for its readers, U-10 Ownership and U-12 Acceptance readiness. They are marked in the universal rubric table.

## 4. Severity

Every Bug and Risk finding carries a severity from this table.

| Severity | A Bug is this severe when… | A Risk is this severe when… |
|---|---|---|
| **High** | A reader following the document would make a wrong operational, access, data or acceptance decision; or a critical criterion cannot pass; or the document contradicts another Accepted document; or it claims acceptance, completeness or a test result without evidence. | It is likely to cause a service outage, a data or privacy breach, financial loss, or a failed handover if not addressed. |
| **Medium** | The document is usable but incomplete or ambiguous in a way that needs follow-up with the author. | It could cause delay, rework or support confusion, and a workaround exists. |
| **Low** | Cosmetic, formatting or wording, with no effect on any decision. A Stale document (past its review interval) with no other issue is Low. | Minor inconvenience; unlikely to happen. |

Ideas carry a **Value** (High / Medium / Low) instead of a severity and never affect a decision.

## 5. Document decision

Apply the first row whose conditions are all true, reading from the top.

| Decision | All of these are true |
|---|---|
| **Reject** | Any one of: it is the wrong document; it cannot be used by its readers; it contradicts an Accepted document or the Scope Record; it claims acceptance, completeness or a test result without evidence; it hides a known limitation, an owner or a support path. |
| **Accept** | Every applicable critical criterion is Pass · no more than three Partial results, all on non-critical criteria, each with a logged fix · no open High or Medium Bug · every High or Medium Risk is mitigated or formally accepted by a named owner · every applicable cross-document rule passes · the accepting owner is named. |
| **Accept with Conditions** | No applicable critical criterion is Fail (a critical Partial is allowed only as a condition) · no open High Bug · every High Risk is mitigated or formally accepted · each remaining Medium Bug, Medium Risk and critical Partial is a condition with an owner, a target date and a `COND-xx` entry in SP-12 open items · the accepting owner has agreed to the conditions · the document remains usable for its readers. |
| **Revise and Resubmit** | None of the above. |

## 6. Package decision

The package decision is computed from the [package gates](../review/03_package_gates.md); it is never decided separately.

First, give each gate a result. A gate contains cross-document rules and documents, as listed in [03_package_gates.md](../review/03_package_gates.md). Rules and documents that are out of scope are ignored.

| Gate result | When |
|---|---|
| **Pass** | Every rule in the gate passes, and every document in the gate is Accept. |
| **Conditional** | Every failed rule in the gate is Medium or Low and logged as a `COND-xx` condition in SP-12, and every document in the gate is Accept or Accept with Conditions. |
| **Fail** | Anything else, including any High rule failure or any document at Revise and Resubmit or Reject. |

Then:

| Package decision | When |
|---|---|
| **Accept** | Every gate result is Pass. |
| **Accept with Conditions** | Every gate result is Pass or Conditional, no rule in G1 Completeness, G3 Traceability or G8 Handover has failed, and the business owner and support owner have agreed to the conditions recorded in SP-12. |
| **Revise and Resubmit** | Any gate result is Fail, or any rule in G1, G3 or G8 has failed. |

A package is never Rejected as a whole; individual documents are.

## 7. Evidence

Every Bug and Risk cites evidence: a quote, a table row, an ID, a linter output line, or the absence of something required ("No access removal process found in BUS-04"). A finding without evidence is not counted.

## 8. Honesty rules for producers

These are Reject conditions when broken, whoever the producer is:

- Unknown but required details are written `TBD` with an owner and a `Q-xx` entry. They are never invented.
- No sign-off, approval, test result or measurement is recorded unless it happened, with who and when.
- Content an agent inferred from code or other material is marked as inferred until a person confirms it.
- Limitations are never hidden: each appears in its document and in SP-12.
