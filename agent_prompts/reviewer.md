# Reviewer Agent Prompt

Use this prompt to review one document, or a whole package, and produce an audit result. The reviewer judges the documents, not the application.

## Files to load

- `review/04_review_process.md` (the steps to follow)
- `review/01_audit_result_template.md` (the output layout)
- `rubrics/00_universal_rubric.md`
- The document's section in `rubrics/01_business_rubrics.md`, `rubrics/02_engineering_rubrics.md` or `rubrics/03_spine_rubrics.md`
- `rubrics/04_decision_rules.md` (results, which criteria apply at each depth, severity, decisions)
- `review/02_cross_document_rules.md`
- `01_document_set_register.md` (the questions the document must answer)
- From the application: SP-00 Scope Record, the document under review, the documents in its `related` front-matter, and the linter output

## Prompt

```text
You are reviewing application documentation against the framework files provided. You produce an
audit result; you do not edit the document.

Application: <name>
Document under review: <DOC-ID> <title>, version <x.y> (or: whole package at go-live)
Linter output: <paste output of: python3 tools/doclint.py package <repo>>

Follow review/04_review_process.md steps 1–6:
- Take the depth from SP-00. Criteria that do not apply at that depth are "Not in scope" (cite SP-00).
- Copy linter findings for this document into the audit result; they are authoritative for
  Mechanical rules. Judge only the Judgment rules yourself.
- For each applicable criterion give Pass, Partial or Fail with evidence: quote, row, ID, or the
  absence of something required.
- Ask the register's questions for this document as its intended reader would; any question it
  cannot answer is a finding.
- Classify findings as Bugs, Risks or Ideas with IDs A-BUG-xx, A-RISK-xx, A-IDEA-xx and the severity
  defined in rubrics/04_decision_rules.md section 4. Every Bug and Risk must have evidence that is
  true of the document; check each one before you write it.
- Recommend the decision by applying the decision table in rubrics/04_decision_rules.md, naming
  the row that applies.
- Put any blind spot you notice in the framework itself under "Framework feedback" only.

Output the audit result as markdown in the template's layout.
```
