# Universal Documentation Rubric

Apply this rubric to every artifact in the documentation set.

## Result scale

| Result | Meaning |
|---|---|
| Pass | Criterion is satisfied with clear evidence. |
| Partial | Criterion is partly satisfied but has gaps, ambiguity, or weak evidence. |
| Fail | Criterion is missing, contradicted, or unusable. |
| Not Applicable | Criterion does not apply and the reason is documented. |

## Universal criteria

| ID | Criterion | Pass condition | Fail condition |
|---|---|---|---|
| U-01 | Identity | Document has title, application name, version/date, status, owner, and intended audience. | Missing identity fields or unclear artifact scope. |
| U-02 | Purpose | Document clearly states why it exists and what decision or operation it supports. | Purpose is missing or generic. |
| U-03 | Scope | In-scope and out-of-scope content are clear where relevant. | Reader cannot tell what is covered. |
| U-04 | Required structure | Required sections and tables are present. | Required sections are missing. |
| U-05 | Specificity | Uses actual names, roles, workflows, statuses, reports, dependencies, owners, or placeholders explicitly marked TBD. | Uses vague language without owners or specific references. |
| U-06 | Plain language | Understandable by business, operational, support, and governance readers; unexplained technical terms are avoided. | Reads like technical implementation notes only. |
| U-07 | Traceability | References related artifacts, IDs, roles, workflows, capabilities, dependencies, or risks as needed. | Cannot be connected to the rest of the package. |
| U-08 | Operational usability | A reader can use the document to operate, support, govern, or accept the application. | Document is informational only and not actionable. |
| U-09 | Risk and limitation visibility | Assumptions, limitations, gaps, exceptions, and risks are visible. | Gaps are hidden or falsely implied as complete. |
| U-10 | Ownership and accountability | Owners, approvers, or responsible roles are identified for the artifact content and major decisions. | No clear accountable owner. |
| U-11 | Consistency | Terms, role names, statuses, IDs, and scope are consistent with related documents. | Contradicts other artifacts or uses inconsistent names. |
| U-12 | Acceptance readiness | Document can be reviewed and signed off by the correct owner. | No acceptance state, owner, or review path. |

## Minimum scoring guidance

For artifact acceptance:

- No Fail on U-01, U-02, U-04, U-07, U-08, U-10, or U-12.
- Partial results must have required fixes or conditional acceptance items.
- A document with more than three Partial results should normally be Revise and Resubmit.
