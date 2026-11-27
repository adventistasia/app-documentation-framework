# Linter Specification

## Purpose

Most cross-document rules are ID lookups. A script checks them exactly and the same way every time, so review agents spend their effort on judgment. The linter runs **before** any review; its findings are authoritative for every rule tagged Mechanical in [02_cross_document_rules.md](02_cross_document_rules.md).

The reference implementation is [tools/doclint.py](../tools/doclint.py): Python 3.9 or later, standard library only.

## Usage

```text
python3 tools/doclint.py package <repo-root> [--docs docs] [--today YYYY-MM-DD] [--format text|json]
python3 tools/doclint.py framework <framework-root>
```

- `package` lints one application's documentation: every `.md` file under `<repo-root>/<docs>` plus `<repo-root>/AGENTS.md` if it exists. Files without front-matter are ignored, except that a front-matter-less `AGENTS.md` is accepted as a pointer file.
- `framework` lints this framework repository itself (section 6).
- Exit code `0` when there are no High or Medium findings, `1` when there are, `2` on a usage or parse error.

## 1. Reading the package

1. **Front-matter:** the YAML block between the first two `---` lines. Only the simple forms used in [conventions §3](../02_conventions.md#3-front-matter) need to be parsed: `key: value` and `key: [a, b]`. Text after `#` is a comment.
2. **Documents and sections:** each file is the document named by its `id`. Inside a file, a level-2 heading of the form `## <DOC-ID> <Title>` starts an **S section** for that document ID, which runs until the next level-2 heading. Everything else belongs to the file's own document.
3. **Code and guidance:** fenced code blocks are skipped entirely, and so are blockquotes beginning `> **Guide:**` or `> **How to use this template**`.
4. **Tables:** GitHub-style pipe tables. The first row is the header. Cells are trimmed. A cell's ID list is every ID token in it.
5. **ID tokens:** `\b(BEN|C|W|R|BR|ST|TR|REC|REP|NTF|COST|RISK|FR|NFR|J|CMP|ENT|D|INT|ENV|CFG|SEC|FLAG|ALR|RB|OC|MT|SM|AC|T|COND|LIM|Q)-\d{2,}\b` and `\bADR-\d{3,}\b`. Document IDs are `\b(SP|BUS|ENG)-\d{2}\b`.
6. **Definitions:** a table whose first header cell is `ID` defines the ID in the first cell of each row. Its rows are the **items** of that prefix; other cells are read by header name using the linked columns in [conventions §6](../02_conventions.md#6-linked-columns). Header matching is exact after trimming and ignores case.
7. **References:** every ID token anywhere else (prose, other cells) is a reference.

## 2. Reading the Scope Record

SP-00, as a file or as a section, must contain these tables. Columns are matched by header name; other columns are allowed (the template adds `Question` to the Triggers table).

| Table | Header row |
|---|---|
| Triggers | `Trigger` · `Answer` · `Reason` (Trigger cells are `T1` … `T11`; Answer is `Yes` or `No`) |
| Items | `Item` · `Depth` · `Parent` · `Reason` (Item cells start with a document ID; Depth is `—`, `-`, `S`, `D` or `D+`) |

The level is read from the SP-00 front-matter, or the parent's when SP-00 is a section.

## 3. Checks

Each check reports findings tagged with the rule it implements. Usual severity is from the rule table.

| Check | Rules | What is checked |
|---|---|---|
| Front-matter | X-25, X-14 | All keys present; `status` in Draft / In Review / Accepted / Superseded; `level` in Foundation / Standard / Full; `depth` in D / D+; `related` and `contains` entries are document IDs that exist as a file or section; `application` and `level` identical across files. |
| Standard sections | X-25 | Each file has level-2 headings Purpose, Scope, Assumptions and open questions, Known limitations, Change log. (`AGENTS.md` pointer files are exempt.) |
| IDs | X-25 | Every defined ID matches its format; no ID is defined twice; every referenced ID is defined somewhere (reported per reference, once per ID per file). `T-xx` references are exempt from "must be defined" (tests live in code). |
| Scope | X-27 | Every item at S has a section `## <ID>` in its parent (or any file); every item at D or D+ has a file with that `id`; every item at — has a non-empty Reason and no file or section; every one of the 24 document IDs appears in the Items table; the never-dropped minimum is present (a "What success looks like" heading in BUS-01, at least one `SM`, at least one `AC`, ENG-07 not —, ENG-08 not —). |
| Capabilities and processes | X-01, X-02 | As in the rule table. |
| Roles, statuses, transitions | X-03, X-04, X-05 | Every `R`, `ST`, `TR` referenced is defined; `Roles` cells contain only R IDs or `Automated`; transition `From` and `To` are defined statuses. |
| Rules, reports, notifications | X-06, X-07, X-08 | Named columns are present and non-empty (and not `TBD` without a `Q-xx` in the same row). |
| Dependencies | X-09, X-15, X-20, X-21, X-24 | As in the rule table. |
| Risks | X-11 | High risks (any of `Severity`, `Rating` or `Risk level` = High) have non-empty `Control` and `Owner`. |
| Limitations | X-12 | Every `LIM` defined or referenced outside SP-12 appears in a `Limitation` cell of SP-12's "Consolidated known limitations" table. |
| Glossary | X-13 | When SP-01 is in scope, the name in the `Name` column of every `R`, `ST` and `REC` row appears in an SP-01 table cell under `Term`. |
| Journeys | X-16 | As in the rule table. |
| Records and entities | X-17 | As in the rule table. |
| Requirements and coverage | X-18, X-19 | As in the rule table. Must is read from `Priority`. |
| Success measures | X-22, X-23 | As in the rule table. `Level` cells start with `L1` … `L4`. T6 is read from the Scope Record. |
| Handover | X-26 | If SP-12 front-matter `status` is Accepted, no Must `AC` has `Result` Not run or Fail; Waived rows mention an approver (any non-empty `Approver`, `Waived by` or `Verified by` cell). |
| Staleness | X-28 | `last_reviewed` older than 12 / 6 / 3 months for Foundation / Standard / Full, compared with `--today`. |

Rules out of scope pass silently: a check whose home document is — in the Scope Record is skipped, and so are checks gated by a trigger answered No (T3 for transitions, T5 for interfaces, T6 for output checks, T1 for journeys).

## 4. Output

Text output is a markdown table in the [audit result](01_audit_result_template.md) findings format, so it can be pasted into a review:

```text
| ID | Rule | Severity | Location | Finding |
|---|---|---|---|---|
| A-BUG-01 | X-02 | High | BUS-02-capabilities-register.md:14 | C-03 lists W-03, but W-03 does not list C-03 in Capabilities. |
```

followed by a summary line: `Linter: <n> High · <n> Medium · <n> Low · rules checked: X-01, X-02, …`.

JSON output is a list of objects with keys `id`, `rule`, `severity`, `file`, `line`, `message`.

## 5. Limits

The linter checks structure, not meaning. It cannot tell whether a capability is described well, whether a criterion is testable, or whether a runbook would work. Those are judgment rules and rubric criteria for the reviewer.

## 6. Framework self-check

`framework` mode lints this repository so the framework obeys its own rules:

| Check | Fails when |
|---|---|
| Template front-matter | A template under `templates/` lacks a front-matter key from conventions §3. |
| Template sections | A template lacks one of the five standard sections. |
| Template related | A template's `related` lists something other than a valid document ID. |
| Rubric coverage | A document ID in the register has no rubric section, or a rubric row lacks a Critical or Full only value, or a rubric has fewer than two Critical = Yes rows. |
| Example names | `LHC` or `ITS` (whole word, case-sensitive) appears outside `examples/`, `CHANGELOG.md` and `releases/`. |
| Consolidated guide | `consolidated_guide.md` differs from what `build/build_consolidated.py` would produce, or the manifest misses a markdown file. |
| Examples | Each package under `examples/` (a folder containing `docs/`) lints with no High or Medium findings, except packages under `examples/review_training/`, whose findings must equal their `expected_findings.json`. |
