# Audit Result: <Application> – <DOC-ID> <Title>

> **Guide:** one audit result per document review, or one per package review (then section 3 lists every document). Store it outside `/docs`, for example in the pull request or `docs/reviews/`. Findings use the Bug / Risk / Idea format and IDs `A-BUG-xx`, `A-RISK-xx`, `A-IDEA-xx` ([conventions §8](../02_conventions.md#8-review-finding-ids)). Results and decisions follow [rubrics/04_decision_rules.md](../rubrics/04_decision_rules.md); do not invent other categories.

## 1. Review scope

| Field | Value |
|---|---|
| Application | |
| Document reviewed | <DOC-ID> <Title>, version <x.y> |
| Depth in Scope Record | S / D / D+ (SP-00 version <x.y>) |
| Review type | Stage <n> review / Go-live package review / Change review / Stale re-review |
| Reviewer | <name or agent and run reference> |
| Date | |
| Related documents read | <DOC-IDs and versions> |
| Linter run | `python3 tools/doclint.py package <path>` on <commit or date> |

## 2. Rubric summary

Universal: <n> Pass · <n> Partial · <n> Fail · <n> Not in scope or not applicable
Artifact: <n> Pass · <n> Partial · <n> Fail · <n> Not in scope or not applicable
Critical criteria not passing: <n> (<IDs>)
Open findings: <n> High · <n> Medium · <n> Low

## 3. Universal rubric results

> **Guide:** for an S-depth item, write "Covered by the parent's review" and skip to section 4.

| ID | Criterion | Result | Evidence |
|---|---|---|---|
| U-01 | Identity | | |
| U-02 | Purpose | | |
| U-03 | Scope | | |
| U-04 | Required structure | | |
| U-05 | Specificity | | |
| U-06 | Language for its readers | | |
| U-07 | Traceability | | |
| U-08 | Usable for its readers | | |
| U-09 | Limitations and unknowns visible | | |
| U-10 | Ownership | | |
| U-11 | Consistency | | |
| U-12 | Acceptance readiness | | |
| U-13 | Says it once | | |

## 4. Artifact rubric results

| ID | Criterion | Critical | Result | Evidence |
|---|---|---|---|---|
| <DOC-ID>.1 | | Yes / No | | |

## 5. Cross-document rules

> **Guide:** copy mechanical results from the linter; judge only the Judgment rules.

| Rule | Type | Result | Evidence |
|---|---|---|---|
| X-xx | Mechanical / Judgment | Pass / Fail / Not in scope | |

## 6. Findings

Severity definitions: [decision rules §4](../rubrics/04_decision_rules.md#4-severity).

### Bugs

| ID | Finding | Severity | Evidence | Required action |
|---|---|---|---|---|
| A-BUG-01 | | High / Medium / Low | | |

### Risks

| ID | Finding | Severity | Evidence | Mitigation or required action |
|---|---|---|---|---|
| A-RISK-01 | | High / Medium / Low | | |

### Ideas

| ID | Finding | Value | Evidence | Suggested action |
|---|---|---|---|---|
| A-IDEA-01 | | High / Medium / Low | | |

## 7. Required fixes

| Finding | Fix | Owner |
|---|---|---|
| | | |

## 8. Proposed conditions

> **Guide:** only for Accept with Conditions. Each condition becomes a `COND-xx` row in SP-12 with owner, target date and the accepting owner's agreement.

| Finding | Condition | Owner | Target date |
|---|---|---|---|
| | | | |

## 9. Decision

Decision: **Accept / Accept with Conditions / Revise and Resubmit / Reject**

Decision rule applied: <row of the decision table in rubrics/04_decision_rules.md §5 or §6, and why it applies>

Next action: <who does what next>

## 10. Framework feedback (optional, never affects the decision)

<Blind spots in the framework noticed during this review.>
