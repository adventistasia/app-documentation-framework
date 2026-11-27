# Review training: a package with known defects

This folder tests whether a review agent (or a human reviewer, or the linter) catches defects that are known in advance. It holds a copy of the [Stock Count Sheets Foundation example](../small_tool/README.md) with defects planted in it, and the results a correct review should produce. Everything in it is invented and illustrative.

## Contents

| Path | What it is |
|---|---|
| `stock_count_flawed/docs/README.md` | BUS-01 with its S sections, with defects planted |
| `stock_count_flawed/AGENTS.md` | ENG-09 with its S sections, with defects planted |
| `stock_count_flawed/expected_findings.json` | The exact `(rule, severity)` list the linter must report for this package |
| `expected_audit_result.md` | The answer key: every planted defect, then a full package audit result in the [audit result template](../../review/01_audit_result_template.md) layout, with evidence, severities, document decisions, gate results and the package decision |

The planted defects are listed **only** in `expected_audit_result.md`. Some can be found mechanically and some need judgment. This README deliberately does not say which or how many, so it can be shown to the reviewer under test.

## How to use it

**To test a review agent:**

1. Give the agent the [reviewer prompt](../../agent_prompts/reviewer.md), the framework, and the `stock_count_flawed/` folder as the package under review. Do not give it `expected_audit_result.md`, and do not tell it the package is flawed.
2. Compare its audit result with `expected_audit_result.md`:
   - Did it find every planted defect, with true evidence?
   - Did it give the severity the [decision rules](../../rubrics/04_decision_rules.md#4-severity) require?
   - Did it reach the same document decisions, gate results and package decision?
3. Extra findings are fine when their evidence is true. A finding without evidence, or with false evidence, counts against the agent.

**To test the linter:**

```text
python3 tools/doclint.py package examples/review_training/stock_count_flawed --today 2026-10-07 --format json
```

Compare the `(rule, severity)` pairs in the output with `stock_count_flawed/expected_findings.json`. The framework self-check (`python3 tools/doclint.py framework .`) does this comparison automatically for every package under `examples/review_training/`, and fails when the two differ in either direction.

## Changing the package

When a template, rule or linter check changes, update the flawed package, `expected_findings.json` and `expected_audit_result.md` together. Keep the defects the linter cannot see. They are the point of the exercise, because they test what a reviewer adds beyond the linter.
