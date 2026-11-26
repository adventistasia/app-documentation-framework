# Task Review Rubric

Use this rubric to assess a task brief or coding-agent instruction **before implementation begins**. It checks whether the request is specific, grounded in project decisions, bounded, and verifiable. It evaluates the instructions, not the agent's code or the eventual feature.

## Review scale

| Result | Meaning |
|---|---|
| Pass | The task gives enough specific information to satisfy the criterion and verify it. |
| Partial | The criterion is addressed, but important detail, traceability, or verification is missing. |
| Fail | The criterion is missing, contradictory, or too vague to guide the work safely. |
| Not Applicable | The criterion genuinely does not apply; the reviewer explains why. |

Do not use Not Applicable to hide missing information. If applicability is unclear, mark Partial and ask.

## Criteria

| ID | Criterion | Pass condition |
|---|---|---|
| TR-01 | Source of truth | The task identifies the authoritative requirements, design rules, or existing behavior. It states which source takes precedence if sources conflict. References are precise enough for the agent to find. |
| TR-02 | Intended outcome | The task describes one main user or system outcome. The result can be observed without relying on phrases such as “make it better” or “handle it properly.” |
| TR-03 | Acceptance criteria | Completion is described as observable conditions. Criteria cover the expected success path and relevant refusal, failure, or unchanged-state outcomes. Each criterion is specific enough to pass or fail. |
| TR-04 | Scope and boundaries | The task names the behavior or area in scope and what must remain out of scope. It states whether the agent may investigate, edit, run commands, change tests, or take external actions. |
| TR-05 | Relevant edge cases and invariants | The task calls out applicable roles and permissions, dates, existing data, state transitions, side effects, and failure cases. It does not need irrelevant cases, but exclusions should be justified when they could otherwise be expected. |
| TR-06 | Verification mapping | Every acceptance criterion maps to evidence: a named or discoverable automated test, a test to add, or a specific human review. The task does not treat an agent's assertion or a green unrelated test as proof. |
| TR-07 | Assumptions and decisions | Known assumptions are explicit. Conflicts or unresolved product/business decisions are identified, and the agent is told to stop and ask rather than invent a rule. |
| TR-08 | Completion and handoff | The task says what the agent must report: files or areas changed, checks actually run and their exact results, remaining gaps, and risks or decisions needing a person. |

## Readiness decision

A task is **Ready** when:

- TR-01, TR-02, TR-03, TR-04, and TR-06 are Pass.
- TR-05, TR-07, and TR-08 are Pass or justified Not Applicable.
- There is no unresolved decision that would change the implementation or its acceptance criteria.

A task is **Revise** when one or more criteria are Partial but can be made clear with edits or answers.

A task is **Not Ready** when a critical criterion is Fail, the task contains conflicting instructions, or implementation depends on an unresolved decision.

Do not average away a critical gap. A high number of Pass results cannot compensate for missing source authority, untestable acceptance criteria, unclear scope, or no verification plan.

## Evaluator instructions

Use the prompt below to review a proposed task. Provide evidence from the task and linked project sources. Do not fill gaps by guessing or start implementation.

```text
You are reviewing a proposed task brief for an AI coding agent.

Use the Task Review Rubric at:
rubrics/03_task_review_rubric.md

Review the task brief at:
[PATH OR LINK TO TASK FILE]

Project or repository:
[NAME OR PATH]

Read the task and any linked authoritative requirements needed to assess it. Evaluate the instructions before implementation begins. Do not implement, edit files, or run commands that change project state.

For each rubric criterion TR-01 through TR-08:
- Return Pass, Partial, Fail, or Not Applicable.
- Cite the exact task text or project source that supports your result.
- For Partial or Fail, state the missing detail and the smallest question or edit needed to resolve it.
- For Not Applicable, explain why it genuinely does not apply.

Then return:
1. Readiness decision: Ready, Revise, or Not Ready.
2. Blocking questions that need a person to answer.
3. A criterion-to-verification map showing how each acceptance criterion can be checked.
4. Suggested edits to the task brief. Do not silently rewrite uncertain business rules.

Do not mark a task Ready if its acceptance criteria cannot be verified or if a required business decision is unresolved.
```

## Project-specific traceability

For RMS Cares tasks, cite the applicable rule in the agreed organization-model design and the reference page describing current behavior. Map each acceptance criterion to a focused test or named human review. If the design and current implementation differ, identify that as a gap to validate; do not assume the implementation is the intended behavior.

For other projects, use their equivalent authoritative specifications, current-behavior documentation, and verification sources.

## Example invocation

```text
Assess `tasks/coverage-group-preview.md` using
`rubrics/03_task_review_rubric.md`. Read the linked RMS Cares design
rules and current reference documentation. Return the rubric results and
readiness decision. Do not edit code.
```
