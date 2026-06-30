# Verifier and Control Agent Rules

## Purpose

This document defines deterministic pass/fail checks that automated verifier or control agents can apply after a review agent produces an audit result.

The review agent evaluates quality. The verifier agent determines whether the artifact or package passes the control gate.

## Inputs expected by verifier

For each artifact:

- Artifact content
- Artifact type or document ID
- Audit result
- Universal rubric results
- Artifact-specific rubric results
- Bug/Risk/Idea findings
- Required fixes
- Conditional acceptance items
- Related artifacts needed for coherence checks

## Artifact pass/fail control rules

### Automatic fail conditions

Fail the artifact if any of these are true:

1. Artifact is missing.
2. Artifact type does not match expected document.
3. Application identity is missing.
4. Owner is missing.
5. Purpose is missing.
6. Required structure is substantially missing.
7. A critical universal criterion is marked Fail.
8. A critical artifact-specific criterion is marked Fail.
9. Any high-severity Bug remains open.
10. Any high-severity Risk has no mitigation, acceptance, or owner.
11. Artifact contradicts a previously accepted artifact.
12. Artifact claims accepted/complete status while required acceptance evidence is missing.

### Conditional pass conditions

Allow Accept with Conditions only if all are true:

1. No automatic fail condition exists.
2. Remaining Bugs are low or medium severity.
3. Remaining Risks have owners and mitigation or explicit acceptance.
4. Conditional items are listed.
5. Conditional items have owners or are assigned to the handover/open items list.
6. The artifact remains operationally usable despite the conditions.

### Full pass conditions

Accept the artifact only if all are true:

1. All required universal criteria pass.
2. All required artifact-specific criteria pass.
3. No open high or medium Bugs.
4. No unmitigated high or medium Risks.
5. Cross-document references are valid.
6. No required fixes remain.
7. Acceptance owner is named.

## Cross-document verification rules

| Rule ID | Verification rule | Fail condition |
|---|---|---|
| X-01 | Every capability maps to at least one workflow or is marked administrative/support only. | Capability exists but has no workflow mapping or classification. |
| X-02 | Every workflow maps to at least one capability. | Workflow cannot be traced to system capability. |
| X-03 | Every workflow role exists in Roles and Access Matrix. | Undefined role appears in workflow. |
| X-04 | Every status used in workflows exists in Status Lifecycle. | Undefined status appears. |
| X-05 | Every status transition used in workflows is allowed in Status Lifecycle. | Workflow uses unauthorized transition. |
| X-06 | Every major business rule references an owner. | Rule has no owner or authority. |
| X-07 | Every report has audience, purpose, owner, and data source. | Report is vague or unowned. |
| X-08 | Every notification has trigger, recipient, purpose, and expected action. | Notification is incomplete. |
| X-09 | Every critical dependency has owner, impact, criticality, support path, and affected workflow/capability. | Critical dependency is incomplete. |
| X-10 | Every support category has owner and escalation path. | Support issue cannot be routed. |
| X-11 | Every high risk has control, owner, and mitigation or formal acceptance. | High risk is unmanaged. |
| X-12 | Every known limitation appears in Acceptance and Handover Record. | Limitation is hidden from handover. |
| X-13 | Role names are consistent across capabilities, workflows, access matrix, support guide, and user guide. | Same role appears under inconsistent names without mapping. |
| X-14 | Application name, owner, URL/access point, and status are consistent across all artifacts. | Identity inconsistency exists. |
| X-15 | Support Guide references Dependencies Register for dependency checks. | Support cannot troubleshoot dependency failure. |

## Package-level pass/fail rules

### Package automatic fail

Fail the package if any of these are true:

1. Required artifact is missing.
2. DOC-01, DOC-02, DOC-03, DOC-04, DOC-05, DOC-07, DOC-08, or DOC-11 is Rejected or Revise and Resubmit.
3. Capabilities and workflows are not traceable.
4. Roles and access are not defined.
5. Support model is missing or unowned.
6. Critical dependencies are missing or unowned.
7. Known limitations are not disclosed in handover.
8. Business owner or support owner acceptance is missing from handover.

### Package conditional pass

Accept with Conditions only if:

1. All required artifacts exist.
2. Core operational artifacts are at least Accept with Conditions.
3. Open conditions are documented in the Handover Record.
4. No high-severity unresolved Bugs remain.
5. No high-severity unmanaged Risks remain.
6. Business owner and support owner accept the conditions.

### Package full pass

Accept the package only if:

1. All required artifacts are Accept.
2. All cross-document verification rules pass.
3. No required fixes remain.
4. Handover record contains final sign-off.
5. Support ownership, dependencies, limitations, and accepted scope are clear.
