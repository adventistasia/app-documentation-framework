# Universal Documentation Review Rubric

Apply these criteria to every document **file** in a package. Sections held at depth S inside a parent are covered by the parent's universal review; they are judged only on their own critical artifact criteria. Result values, which criteria apply at each depth, and how results turn into a decision are defined in [04_decision_rules.md](04_decision_rules.md).

These are documentation review criteria: they judge the document, not the application.

| ID | Criterion | Pass condition | Fail condition | Critical |
|---|---|---|---|---|
| U-01 | Identity | Front-matter is complete and valid as defined in [conventions §3](../02_conventions.md#3-front-matter): id, title, application, version, status, owner, audience, level, depth, contains, related, last_reviewed. | A key is missing or invalid, or the document cannot be identified. | Yes |
| U-02 | Purpose | The Purpose section says why the document exists and what decision or operation it supports, specific to this application. | Purpose is missing or generic boilerplate. | Yes |
| U-03 | Scope | The Scope section says what is covered and which other documents (by ID) cover the rest. | The reader cannot tell what is covered. | No |
| U-04 | Required structure | The standard sections (Purpose, Scope, Assumptions and open questions, Known limitations, Change log) and the template's core body sections for its depth are present; empty ones say so in one line. | A required section is missing. | Yes |
| U-05 | Specificity | Uses real names, IDs, values and owners, or `TBD` with an owner and a `Q-xx` entry. Numbers have units and timeframes. | Vague wording ("fast", "the team", "as needed") stands in for facts. | No |
| U-06 | Language for its readers | Business and spine documents are plain language a manager or support person can follow. Engineering documents may be technical, and every specialist term is in SP-01 Glossary. | The intended readers could not follow it. | No |
| U-07 | Traceability | Links to related items by ID as the template requires, and every ID referenced exists. | It cannot be connected to the rest of the package, or references IDs that do not exist. | Yes |
| U-08 | Usable for its readers | A reader in the stated audience can use it to do their job: decide, build, operate, support, use or accept. | It is informational only; a reader would still have to ask the author. | Yes |
| U-09 | Limitations and unknowns visible | Assumptions, open questions and known limitations are listed with IDs; inferred content is marked as inferred. | Gaps are hidden, or the document implies completeness it does not have. | No |
| U-10 | Ownership | The document owner and the owners of its major items (rules, records, dependencies, risks, measures) are named. | No accountable owner for the document or its major items. | Yes |
| U-11 | Consistency | Names, statuses, roles and IDs match their home documents and SP-01; nothing contradicts another document. | Contradicts another document, or uses names inconsistently. | No |
| U-12 | Acceptance readiness | The status is honest, the change log records every version, and the approver of an Accepted version is named with a date. | No status or review path, or status Accepted without a recorded approval. | Yes |
| U-13 | Says it once | Content held in another document is linked by ID, not copied. | Material is duplicated so that the two copies can drift. | No |
