# Package Gates

The package is judged through eight gates. Each gate is a named set of cross-document rules and documents. Every cross-document rule and every document belongs to exactly one gate. How a gate result (Pass, Conditional, Fail) and the package decision are computed is defined only in [rubrics/04_decision_rules.md §6](../rubrics/04_decision_rules.md#6-package-decision).

Items the Scope Record marks — are left out of their gate. Items held as S sections count through their critical criteria.

| Gate | What it shows | Cross-document rules | Documents (judged by their own rubric) | Also checks |
|---|---|---|---|---|
| **G1 Completeness** | The package is what the Scope Record says it is. | X-14, X-25, X-27, X-28 | SP-00 | The Scope Record is approved by the business owner and technical owner. |
| **G2 Business understanding** | A business reader can answer B1–B4. | X-24 | BUS-01, BUS-07 | BUS-01 has "What success looks like". |
| **G3 Capability and journey traceability** | What the system does, how it is used and what it must do all line up. | X-01, X-02, X-03, X-04, X-05, X-16, X-18 | BUS-02, BUS-03, ENG-01, ENG-02 | — |
| **G4 Governance and control** | Rules, access, data and risk are defined and owned. | X-06, X-07, X-08, X-11, X-13, X-17 | SP-01, BUS-04, BUS-05, BUS-06, BUS-08 | — |
| **G5 Engineering readiness** | An engineer or agent can understand how the system is built and change it safely (E1, E2, E6). | X-20, X-29 | ENG-03, ENG-04, ENG-05, ENG-06, ENG-09, ENG-10 | — |
| **G6 Operational readiness** | It can be deployed, run, supported and recovered (E4). | X-09, X-10, X-15, X-21 | ENG-07, ENG-08, BUS-09 | A deploy, a rollback and a restore have been dry-run from the documents, with evidence in SP-12. |
| **G7 Success measurability** | Success can be measured and the application objectively accepted (S1–S3). | X-19, X-22, X-23, X-30 | SP-10, SP-11 | — |
| **G8 Handover** | Acceptance is honest and ownership is clear after go-live. | X-12, X-26 | SP-12 | Business owner, support owner and technical owner decisions are recorded. |

## Checks that are not cross-document rules

The "Also checks" column holds three package checks that need evidence rather than a table lookup. Each is judged by the verifier as Pass or Fail and counts as a High rule in its gate when it fails.

## Order of work

1. Run the linter. Its findings fill the mechanical rules.
2. Review each document in scope against its rubric.
3. Apply the judgment rules.
4. Give each gate a result, then compute the package decision.
