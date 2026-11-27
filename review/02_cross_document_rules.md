# Cross-Document Rules

These rules check that the documents in a package agree with each other. Each rule is tagged:

- **Mechanical:** an exact check on IDs, columns and front-matter. The [linter](05_linter_spec.md) runs it, and its output is authoritative. A reviewer does not re-judge a mechanical rule; they copy the linter's findings.
- **Judgment:** needs a reader. The review agent or human reviewer applies it.

Each rule belongs to exactly one gate in [03_package_gates.md](03_package_gates.md). Column names in "Check" are the linked columns defined in [conventions §6](../02_conventions.md#6-linked-columns).

A rule whose subject is out of scope (the Scope Record sets the item to —) passes automatically. A rule that needs a document held only as an S section is checked against that section.

Severity of a failure is set by [04_decision_rules.md §4](../rubrics/04_decision_rules.md#4-severity); the column below gives the usual severity as guidance for the linter.

| Rule | Check | Type | Usual severity | Gate |
|---|---|---|---|---|
| X-01 | Every capability (`C`) lists at least one process in `Processes`, or says `Admin/support only`. | Mechanical | Medium | G3 |
| X-02 | Capability↔process links are two-way: if `C-xx` lists `W-yy`, then `W-yy` lists `C-xx` in `Capabilities`, and the reverse. Every process lists at least one capability. | Mechanical | High | G3 |
| X-03 | Every role ID used in any `Roles` column exists in BUS-04 (or the R-01 line in BUS-01 when T2 is No). Only role IDs or `Automated` appear in `Roles` columns. | Mechanical | High | G3 |
| X-04 | Every status ID used anywhere exists in the BUS-05 status table. | Mechanical | High | G3 |
| X-05 | Every transition's `From` and `To` are defined statuses; every transition ID used in journeys or application acceptance criteria exists in BUS-05. | Mechanical | High | G3 |
| X-06 | Every business rule (`BR`) has an `Owner`. | Mechanical | Medium | G4 |
| X-07 | Every report (`REP`) has `Audience`, `Purpose`, `Owner` and `Source`. | Mechanical | Medium | G4 |
| X-08 | Every notification (`NTF`) has `Trigger`, `Recipient`, `Purpose` and `Expected action`. | Mechanical | Medium | G4 |
| X-09 | Every dependency (`D`) has `Owner`, `Criticality`, `Impact` and `Support path`; every High dependency has a `Workaround` (or `None`) and is listed in the `Dependencies` column of at least one capability; a dependency's `Capabilities affected` agrees with the capabilities that list it. | Mechanical | High | G6 |
| X-10 | Every support category in ENG-08 has an owner and an escalation path, and a support person could route a real issue using it. | Judgment | Medium | G6 |
| X-11 | Every High risk (`RISK`) has `Control` and `Owner`, and either a mitigation or a recorded formal acceptance. | Mechanical | High | G4 |
| X-12 | Every known limitation (`LIM`) raised in any document appears in SP-12. | Mechanical | High | G8 |
| X-13 | When SP-01 is in scope, every role, status and record name from its home table appears as a term in SP-01; prose elsewhere uses those names, not synonyms SP-01 says to avoid. | Mechanical (terms present) | Medium | G4 |
| X-14 | `application` and `level` are identical in every front-matter; the access point and owners named in BUS-01 match those in ENG-06, ENG-08 and SP-12. | Mechanical (front-matter) and Judgment (owners) | Medium | G1 |
| X-15 | The ENG-08 triage table references dependencies by `D` ID in its `Dependencies` column. | Mechanical | Medium | G6 |
| X-16 | Process↔journey links are two-way (`W` `Journeys` ↔ `J` `Processes`); every journey lists at least one process. | Mechanical | Medium | G3 |
| X-17 | Every record (`REC`) has `Classification` and `Retention`; Personal and Special-category records have a purpose; every entity (`ENT`) lists at least one record, and every record is stored by at least one entity when ENG-04 is in scope. | Mechanical | High | G4 |
| X-18 | Every functional requirement (`FR`) lists at least one capability; every capability not marked `Admin/support only` is covered by at least one FR when ENG-01 is at depth D or D+. | Mechanical | Medium | G3 |
| X-19 | Coverage: every Must FR, every NFR, every business rule and every transition is in the `Verifies` column of at least one application acceptance criterion; every NFR has a `Target`; every application acceptance criterion has a `Method`. | Mechanical | High | G7 |
| X-20 | Every interface (`INT`) names a defined dependency; every dependency of `Type` Integration has at least one interface. | Mechanical | High | G5 |
| X-21 | Every alert (`ALR`) names at least one runbook entry; every High dependency names a runbook entry in `Runbook`. | Mechanical | High | G6 |
| X-22 | At least one success measure exists. Every L1 measure has `Baseline`, `Target`, `Source` and `Owner`; every benefit names a measure in `Measure`. | Mechanical | High | G7 |
| X-23 | When T6 is Yes: every record with `Core` = Yes is in the `Records` column of at least one output check; every output check has `Procedure`, `Frequency` and `Owner`; every L4 measure links to an output check. | Mechanical | High | G7 |
| X-24 | Every dependency with `Cost` = Yes appears in the `Dependency` column of a BUS-07 cost line. | Mechanical | Medium | G2 |
| X-25 | Every file has complete, valid front-matter; every `related` and `contains` ID resolves; every content ID matches its format and is defined exactly once. | Mechanical | High | G1 |
| X-26 | SP-12 is not `Accepted` while any Must application acceptance criterion has `Result` Not run or Fail; every Waived criterion names its approver. | Mechanical | High | G8 |
| X-27 | Every Scope Record item at depth S, D or D+ exists as a section or file; every item at — has a reason; no document exists that the Scope Record marks —; the never-dropped minimum is present. | Mechanical | High | G1 |
| X-28 | No document's `last_reviewed` is older than the review interval for its level. | Mechanical | Low | G1 |
| X-29 | The architecture, data model and integrations agree: every integration in ENG-05 appears in the ENG-03 context view, every container that stores data maps to entities in ENG-04, and the runtime view's steps match the journeys. | Judgment | Medium | G5 |
| X-30 | The application acceptance criteria are well formed: observable and binary, concrete values, one behaviour each, actor and starting state given, and both a positive and a negative criterion for each rule and transition. | Judgment | High | G7 |
