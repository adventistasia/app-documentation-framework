---
id: BUS-01
title: Application Overview & Business Case
application: Stock Count Sheets
version: 1.0
status: Accepted
owner: Morgan Lee, Warehouse manager (business owner)
audience: [Management, Business owner, Support, Engineering, Agents, Everyone]
level: Foundation
depth: D
contains: [SP-00, SP-10, SP-11, SP-12, BUS-02, BUS-03, BUS-04, BUS-05, BUS-06, BUS-09, ENG-02]
related: [ENG-09, ENG-01, ENG-05, ENG-08]
last_reviewed: 2026-09-30
---
# Stock Count Sheets – Application Overview & Business Case

## Purpose

The first page anyone reads about Stock Count Sheets. It explains what the tool does for the warehouse team, why it exists, how success is judged, and who owns and supports it. At Foundation level it also holds the scope decision, success measures, acceptance criteria, handover record and the short business sections listed in `contains`.

## Scope

Covers the business case, ownership and every business and spine item the Scope Record (SP-00, below) places in this file. Everything about building, running and supporting the tool is in ENG-09, the root `AGENTS.md`.

## Application at a glance

Every night the tool imports the stock snapshot that the inventory system exports. Once a month the team lead prints blind count sheets per shelf location, the counters count and write quantities on the sheets, the team lead types the counted quantities in, and the tool produces a variance file that finance uses to adjust stock.

| Item | Value |
|---|---|
| Access point | https://stockcount.apps.internal.example (internal network only) |
| Access method | Company sign-in |
| How to get access | Ask the warehouse manager; see BUS-04 below |
| Hours of use | Monday–Friday 07:00–17:00; heaviest on the last working day of the month (count day) |

## Problem statement

| Item | Description |
|---|---|
| Current situation | The team lead copies the inventory system's spreadsheet into one printed sheet per location, then re-keys the counted quantities and calculates variances by hand. |
| Who is affected | The warehouse team (8 people) and the finance stock accountant. |
| Cost today | About 6 hours of team-lead time per count; finance receives the variances a median of 4 working days after count day and asks for about 6 corrections a month (Jan–Jun 2026, finance month-end close checklist). |

## Benefits

| ID | Benefit | Beneficiary | Measure | Baseline | Target | By when | Benefit owner |
|---|---|---|---|---|---|---|---|
| BEN-01 | Finance gets stock variances the working day after the count | Finance stock accountant | SM-01 | 4 working days (median, Jan–Jun 2026) | ≤ 1 working day | 2026-12-31 | Morgan Lee, Warehouse manager |
| BEN-02 | Fewer re-keying and arithmetic errors in the variances | Warehouse team, finance | SM-02 | 6 corrections a month (average, Jan–Jun 2026) | ≤ 1 correction a month | 2026-12-31 | Morgan Lee, Warehouse manager |

## What success looks like

Finance receives a correct variance file on the working day after every monthly count. The team lead no longer builds count sheets or calculates variances by hand. Counters count from sheets that do not show the expected quantity. When the nightly import fails, the team lead knows before the count starts and the sheets say which day's stock they show.

## Impact if unavailable

| Outage length | Impact | Workaround |
|---|---|---|
| Up to 1 working day, not on count day | None noticeable; the import catches up the next night | None needed |
| On count day, or more than 2 working days around month end | The count is delayed, so finance's stock close is delayed | Old method: print the inventory system's spreadsheet per location and calculate variances in a spreadsheet |

## Strategic fit

Supports the company stock-count policy (every shelf location counted monthly) and finance's month-end close timetable, which expects stock variances within 2 working days.

## Users and stakeholders

| Stakeholder | Description | Main interest | Role |
|---|---|---|---|
| Counters | Six warehouse staff who count shelves | Clear sheets, one per location | R-01 |
| Team lead | Runs the count and enters quantities | Less typing, no arithmetic | R-02 |
| Finance stock accountant | Receives the variance file by email | A correct file on time | None (receives the file, no access) |

## Ownership

| Responsibility | Name and role | Team | Contact |
|---|---|---|---|
| Business owner | Morgan Lee, Warehouse manager | Warehouse | morgan.lee@example.org |
| Support owner | Priya Shah, Warehouse team lead | Warehouse | priya.shah@example.org |
| Technical owner | Tomás Berg, Applications developer | IT applications | tomas.berg@example.org |

## In scope and out of scope

**In scope:** import the nightly stock snapshot, generate count sheets, record counted quantities, export the variance file (C-01 to C-04).

**Out of scope:** adjusting stock in the inventory system (finance does this), cycle counts during the month, barcode scanning (LIM-01), sending the file to finance automatically (Q-01).

## Key non-functional commitments

| Commitment | Requirement |
|---|---|
| Available Monday–Friday 07:00–17:00, 99% of the time each month | NFR-01 |
| Count sheets for the whole warehouse ready in 20 seconds or less | NFR-02 |
| Only the team lead can enter counts or export variances | NFR-03 |
| Back within 1 working day after a failure, losing at most the last 24 hours of entries | NFR-04, NFR-05 |

## Resources and costs summary

T8 is No: the tool runs on the IT department's shared internal web hosting platform (D-02), funded centrally by IT. It takes about 2 hours a month of Tomás Berg's time and about 1 hour a month of the team lead's time to type counts. No licences.

## Documentation package

| Document | Depth | Where |
|---|---|---|
| BUS-01 Application Overview & Business Case | D | This file |
| SP-00, SP-10, SP-11, SP-12 | S | Sections in this file |
| BUS-02, BUS-03, BUS-04, BUS-05, BUS-06, BUS-09, ENG-02 | S | Sections in this file |
| ENG-09 Developer & Agent Guide | D | Root `AGENTS.md` |
| ENG-01, ENG-03, ENG-04, ENG-05, ENG-06, ENG-07, ENG-08 | S | Sections in `AGENTS.md` |

## SP-00 Scope Record

### Scores

| Dimension | Score (0–3) | Reason |
|---|---|---|
| D1 Users and reach | 1 | One warehouse team of 8 people |
| D2 Impact if down or wrong | 1 | Count slows; the old spreadsheet method is an easy workaround |
| D3 Data sensitivity | 1 | Internal stock quantities and unit costs; no personal data |
| D4 Integrations | 1 | One simple inbound file from the inventory system |
| D5 Process and rule complexity | 1 | One monthly flow, two roles, no statuses or approvals |
| D6 Team and lifespan | 1 | One maintainer (Tomás Berg) |
| D7 Regulatory and audit exposure | 1 | Internal stock-count policy only |
| **Total** | 7 | 0–7 Foundation |

**Floor rules applied:** None (no 3 on D2, D3 or D7; D6 below 2). **Final level:** Foundation.

### Triggers

| Trigger | Question | Answer | Reason |
|---|---|---|---|
| T1 | Do people use it through a screen? | Yes | Team lead and counters use web pages |
| T2 | Is there more than one role or permission level? | Yes | Counters (R-01) and team lead (R-02) |
| T3 | Do records move through statuses or approvals? | No | A count line is either entered or not; no approvals |
| T4 | Does it store personal or confidential data? | No | No personal or confidential data |
| T5 | Does it exchange data with other systems? | Yes | Imports the inventory system's nightly CSV export (INT-01) |
| T6 | Does it produce outputs others rely on? | Yes | Finance adjusts stock from the variance file (REP-02) |
| T7 | Does it run scheduled or background jobs? | Yes | Nightly import at 02:30 |
| T8 | Does it cost anything beyond an existing shared platform? | No | Runs on the shared internal web hosting platform, funded by IT |
| T9 | Does a non-technical person own it or approve its results? | Yes | The warehouse manager owns it |
| T10 | Will a different team or AI agents build or maintain it? | No | Built and maintained by the same developer; no handover planned |
| T11 | Is it public-facing? | No | Internal network only |

### Items

| Item | Depth | Parent | Reason |
|---|---|---|---|
| SP-00 Scope Record | S | BUS-01 | Matrix |
| SP-01 Glossary | — | — | One team with one vocabulary; names are defined in the tables of this file |
| SP-10 Success Measures Register | S | BUS-01 | Matrix; L4 added by T6 |
| SP-11 Acceptance Criteria & Verification Register | S | BUS-01 | Matrix |
| SP-12 Acceptance & Handover Record | S | BUS-01 | Matrix |
| BUS-01 Application Overview & Business Case | D | — | Matrix |
| BUS-02 Capabilities Register | S | BUS-01 | Matrix |
| BUS-03 Business Process Register | S | BUS-01 | Matrix |
| BUS-04 Roles & Access Matrix | S | BUS-01 | T2 Yes |
| BUS-05 Business Rules & Status Lifecycle | S | BUS-01 | Matrix; T3 No, so rules only and no lifecycle |
| BUS-06 Data, Reports & Notifications Register | S | BUS-01 | Matrix; T4 No: "No personal or confidential data." |
| BUS-07 Resource & Cost Model | — | — | T8 No: shared internal web hosting platform, named in BUS-01 Resources and costs summary |
| BUS-08 Risk & Controls Register | — | — | Matrix: limitations are held in BUS-01 Known limitations |
| BUS-09 User & Admin Guide | S | BUS-01 | T1 Yes: quick start |
| ENG-01 Requirements Specification | S | ENG-09 | Matrix |
| ENG-02 User Journeys | S | BUS-01 | T1 Yes; BUS-01 because BUS-03 is itself S |
| ENG-03 Architecture & Design | S | ENG-09 | Matrix; T4 and T11 No, so one-line security statement |
| ENG-04 Data Model | S | ENG-09 | Matrix |
| ENG-05 Integrations & Dependencies Register | S | ENG-09 | Matrix; T5 Yes adds the interface |
| ENG-06 Configuration & Environments | S | ENG-09 | Matrix |
| ENG-07 Deployment & Release Guide | S | ENG-09 | Matrix |
| ENG-08 Operations & Support Runbook | S | ENG-09 | Matrix; T6 adds output checks, T7 job monitoring |
| ENG-09 Developer & Agent Guide | D | — | Matrix: root `AGENTS.md` |
| ENG-10 Decision Log | — | — | T10 No: same maintainer throughout |

No deviations from the depth matrix.

### Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Business owner | Morgan Lee, Warehouse manager | Approved | 2026-08-04 |
| Technical owner | Tomás Berg, Applications developer | Approved | 2026-08-04 |

Re-scored at go-live review on 2026-09-30: no change (approved by Morgan Lee).

## SP-10 Success Measures Register

| ID | Level | Measure | Definition | Source | Baseline | Target | Threshold for action | Frequency | Owner | Links |
|---|---|---|---|---|---|---|---|---|---|---|
| SM-01 | L1 | Days to variance file | Working days from count day to the date finance logs the variance file as received | Finance month-end close checklist, "Stock variances received" date | 4 working days (median of Jan–Jun 2026 counts) | ≤ 1 working day by 2026-12-31 | > 2 working days in any month | Monthly, reviewed quarterly | Morgan Lee, Warehouse manager | BEN-01, C-04 |
| SM-02 | L1 | Variance corrections | Correction requests finance raises against the month's variance file | Finance stock query log, filtered to "count variance" | 6 a month (average of Jan–Jun 2026) | ≤ 1 a month by 2026-12-31 | ≥ 3 in any month | Monthly, reviewed quarterly | Morgan Lee, Warehouse manager | BEN-02, C-03 |
| SM-03 | L4 | Variance file mismatches | Mismatches OC-01 reports for the month's file before it is sent | OC-01 result, kept with the sent file | Not measured – capture at the 2026-10-30 count (Priya Shah) | 0 every month | ≥ 1: do not send the file | Monthly, each count | Priya Shah, Warehouse team lead | OC-01, C-04 |

First L1 review: 2026-12-15, by Morgan Lee.

## SP-11 Acceptance Criteria & Verification Register

Roles: R-01 Counter, R-02 Team lead. All criteria were run in ENV-02 Test with a copy of the 2026-09-15 export (3,812 lines, 420 locations).

| ID | Verifies | Criterion | Method | Evidence | Priority | Result | Verified by | Date | Approver |
|---|---|---|---|---|---|---|---|---|---|
| AC-01 | FR-01, BR-01 | Given a valid export file `stock_20260915.csv` with 3,812 data rows in the import folder, when the nightly import runs, then the stock snapshot is replaced, the import log reads "3812 rows read, 3812 rows loaded" and every sheet header reads "Stock as at 15 Sep 2026". | Automated test | T-01 `tests/test_import.py::test_valid_file` | Must | Pass | Tomás Berg | 2026-09-18 | |
| AC-02 | BR-01 | Given the snapshot from 14 Sep 2026 is loaded and the new file lacks the `location` column, when the nightly import runs, then the file is rejected, the log reads "Rejected: missing column location", ALR-01 is sent, and sheet headers still read "Stock as at 14 Sep 2026". | Automated test | T-02 `tests/test_import.py::test_missing_column` | Must | Pass | Tomás Berg | 2026-09-18 | |
| AC-03 | FR-02, BR-02, J-01 | Given a loaded snapshot with 420 locations and R-02 signed in, when R-02 selects month 2026-09 and Print count sheets, then one printable document opens with one sheet per location in location-code order, each line showing SKU, description, unit and an empty Counted box, and no system quantity on any page. | Manual test | T-03 `tests/manual/print_sheets.md`; screenshots in the UAT folder | Must | Pass | Priya Shah | 2026-09-22 | |
| AC-04 | BR-02, NFR-03 | Given R-01 is signed in, when R-01 opens the Enter counts page or the Variance page by its address, then the message "This page is for team leads" is shown and no system quantity or entry field is displayed. | Automated test | T-04 `tests/test_access.py` | Must | Pass | Tomás Berg | 2026-09-18 | |
| AC-05 | FR-03, BR-03, J-02 | Given R-02 is on Enter counts for location A-01-03, month 2026-09, when R-02 enters 12 for SKU 100245 and saves, then the line shows Counted 12 with R-02's name and the save time. | Automated test | T-05 `tests/test_counts.py::test_save` | Must | Pass | Tomás Berg | 2026-09-18 | |
| AC-06 | BR-03 | Given the same empty line, when R-02 enters -1 or 2.5 and saves, then the message "Enter a whole number of 0 or more" is shown and the line stays empty. | Automated test | T-06 `tests/test_counts.py::test_invalid` | Must | Pass | Tomás Berg | 2026-09-18 | |
| AC-07 | FR-04, J-02 | Given month 2026-09 where SKU 100245 at A-01-03 has system quantity 40, counted 37 and unit cost 2.50, when R-02 selects Export variance, then the CSV has one row per sheet line and that row shows System 40, Counted 37, Variance -3, Variance value -7.50. | Automated test | T-07 `tests/test_export.py::test_variance_row` | Must | Pass | Tomás Berg | 2026-09-18 | |
| AC-08 | BR-04 | Given a sheet line with no counted quantity, when R-02 exports the variance file, then that row shows Counted empty, Status "Not counted" and Variance empty. | Automated test | T-08 `tests/test_export.py::test_not_counted` | Must | Pass | Tomás Berg | 2026-09-18 | |
| AC-09 | BR-04 | Given a sheet line counted as 0 with system quantity 5, when R-02 exports the variance file, then that row shows Counted 0, Status "Counted" and Variance -5 (it is not reported as Not counted). | Automated test | T-09 `tests/test_export.py::test_zero_count` | Must | Pass | Tomás Berg | 2026-09-18 | |
| AC-10 | NFR-01 | Given the platform uptime monitor polls `/healthz` every minute, when availability for 1–29 Sep 2026, Monday–Friday 07:00–17:00, is calculated, then at least 99% of polls succeeded. | Measurement | Uptime report, 1–29 Sep 2026 (99.8%) | Must | Pass | Tomás Berg | 2026-09-30 | |
| AC-11 | NFR-02 | Given 420 locations and 3,812 lines in ENV-02, when R-02 selects Print count sheets five times, then the slowest of the five documents is ready in 20 s or less. | Measurement | Timing log in the UAT folder (slowest 6.4 s) | Must | Pass | Priya Shah | 2026-09-22 | |
| AC-12 | NFR-04, NFR-05 | Given last night's platform backup of ENV-01, when a platform engineer restores it into ENV-02 following ENG-08 Backup and restore, then the tool is usable within 1 working day and the restored counts include every line saved before the backup time. | Demonstration | Restore record 2026-09-22 (2 h 10 min; counts to 01:00 present) | Must | Pass | Jun Park | 2026-09-22 | |

## SP-12 Acceptance & Handover Record

### Acceptance results

Must: 12 total · 12 Pass · 0 Fail · 0 Waived · 0 Not run (SP-11 as above, last run 2026-09-30). Nothing deferred.

### Dry-run evidence

| Procedure | Followed document | Performed by | Date | Environment | Result | Evidence |
|---|---|---|---|---|---|---|
| Deploy | ENG-07 Deployment steps | Jun Park, Platform engineer | 2026-09-22 | ENV-02 | Succeeded | Pipeline run 1187 |
| Rollback | ENG-07 Rollback | Jun Park, Platform engineer | 2026-09-22 | ENV-02 | Succeeded | Pipeline run 1188 |
| Restore | ENG-08 Backup and restore | Jun Park, Platform engineer | 2026-09-22 | ENV-02 | Succeeded | Restore record (AC-12) |

### Success baseline

SM-01 and SM-02 baselines captured from finance records for Jan–Jun 2026; SM-03 is captured at the first live count on 2026-10-30. First L1 review 2026-12-15 by Morgan Lee.

### Consolidated known limitations

| Limitation | Description | Raised in | Impact | Workaround | Accepted by | Date |
|---|---|---|---|---|---|---|
| LIM-01 | No barcode scanning; counts are typed from paper | BUS-01 | About 1 hour of typing a month | None | Morgan Lee, Warehouse manager | 2026-09-30 |
| LIM-02 | Stock moved between the 02:00 export and the count is not in the snapshot | ENG-09 | Variances for lines picked on count morning | No picking from a location until it is counted | Morgan Lee, Warehouse manager | 2026-09-30 |

### Support and operations ownership after handover

| Responsibility | Owner | Team | Contact or support path | From |
|---|---|---|---|---|
| Business ownership, data ownership and success-measure reporting | Morgan Lee, Warehouse manager | Warehouse | morgan.lee@example.org | 2026-10-01 |
| Access administration | Morgan Lee approves; IT service desk changes group membership | Warehouse, IT | morgan.lee@example.org | 2026-10-01 |
| Business and process support | Priya Shah, Warehouse team lead | Warehouse | In person or priya.shah@example.org | 2026-10-01 |
| Technical support, incidents and releases | Tomás Berg, Applications developer | IT applications | IT service desk queue "Stock Count Sheets" | 2026-10-01 |
| Hosting and backups | Jun Park, Platform engineer | IT platform | IT service desk queue "Web hosting platform" | 2026-10-01 |

### Final decisions

| Owner | Role | Decision | Date | Conditions | Notes |
|---|---|---|---|---|---|
| Morgan Lee | Business owner | Accept | 2026-09-30 | None | |
| Priya Shah | Support owner | Accept | 2026-09-30 | None | |
| Tomás Berg | Technical owner | Accept | 2026-09-30 | None | |

## BUS-02 Capabilities Register

| ID | Name | Outcome | Roles | Processes | Dependencies | Automated | Criticality |
|---|---|---|---|---|---|---|---|
| C-01 | Import nightly stock snapshot | The latest expected quantities are ready before the first shift | Automated, R-02 | W-01 | D-01, D-02 | Yes, nightly; R-02 can re-run it | High |
| C-02 | Generate count sheets | One blind count sheet per shelf location, ready to print | R-01, R-02 | W-01 | D-02, D-03 | No | High |
| C-03 | Record counted quantities | Every counted line is stored once, by location | R-02 | W-01 | D-02, D-03 | No | High |
| C-04 | Export variance file | Finance gets a file of system, counted and variance quantities and values | R-02 | W-01 | D-02, D-03 | No | High |

## BUS-03 Business Process Register

| ID | Name | Trigger | Outcome | Owner | Roles | Capabilities | Statuses | Journeys | Manual steps outside the system |
|---|---|---|---|---|---|---|---|---|---|
| W-01 | Run the monthly stock count | Last working day of the month (count day) | Finance has a checked variance file by the next working day | Morgan Lee | R-01, R-02 | C-01, C-02, C-03, C-04 | None | J-01, J-02 | Counting shelves, recounting large variances, emailing the file to finance |

1. Before the first shift the team lead checks the sheets show today's date (C-01) and prints them (C-02).
2. Counters count each location and write quantities on the sheet; picking from a location waits until it is counted (LIM-02).
3. The team lead recounts any line that differs by more than 10 units from what they expect, then types the counts in (C-03).
4. The team lead runs OC-01, exports the variance file (C-04) and emails it to the finance stock accountant.

## BUS-04 Roles & Access Matrix

| ID | Name | Description | Typical users | Role owner | Access approver |
|---|---|---|---|---|---|
| R-01 | Counter | Views and prints count sheets | Warehouse staff | Morgan Lee | Morgan Lee, Warehouse manager |
| R-02 | Team lead | Runs the count: prints sheets, enters counts, exports variances, re-runs the import | Warehouse team lead and deputy | Morgan Lee | Morgan Lee, Warehouse manager |

| Role | View and print sheets | Enter counts | Export variance file | Re-run import |
|---|---|---|---|---|
| R-01 | Yes | No | No | No |
| R-02 | Yes | Yes | Yes | Yes |

**Access request:** the person asks Morgan Lee, who emails the IT service desk to add them to directory group `stockcount-counters` (R-01) or `stockcount-leads` (R-02); done within 1 working day. **Removal:** leavers are removed automatically when their company account is closed; for a role change or urgent removal Morgan Lee asks the service desk to remove the group membership, done within 4 working hours and confirmed by reply email.

## BUS-05 Business Rules & Status Lifecycle

T3 is No: there are no statuses or transitions.

| ID | Rule | Applies to | Blocking | Owner | Processes | Capabilities |
|---|---|---|---|---|---|---|
| BR-01 | If an import file lacks a required column (`sku`, `location`, `description`, `unit`, `quantity`, `unit_cost`) or has no data rows, reject it and keep the previous snapshot | REC-01 | Yes | Tomás Berg, Technical owner | W-01 | C-01 |
| BR-02 | Count sheets and every page open to R-01 never show the system quantity (blind count) | REP-01 | Yes | Morgan Lee, Business owner | W-01 | C-02 |
| BR-03 | A counted quantity must be a whole number of 0 or more | REC-02 | Yes | Morgan Lee, Business owner | W-01 | C-03 |
| BR-04 | A line with no counted quantity is exported as "Not counted", never as 0 | REP-02 | Yes | Morgan Lee, Business owner | W-01 | C-04 |

## BUS-06 Data, Reports & Notifications Register

No personal or confidential data.

| ID | Name | Description | Core | Classification | Purpose | Retention | Owner |
|---|---|---|---|---|---|---|---|
| REC-01 | Stock snapshot | Expected quantity and unit cost per SKU and location, from the nightly import | Yes | Internal | Expected quantities for sheets and variances | 400 days, so last year's count can be compared; older snapshots deleted by the nightly job | Morgan Lee |
| REC-02 | Stock count | Counted quantity per SKU and location per month, with who entered it | Yes | Internal | Counted quantities for the variance file | 24 months; finance keeps the official record; older counts deleted by the nightly job | Morgan Lee |

| ID | Name | Purpose | Audience | Frequency | Format | Source | Owner | Official record |
|---|---|---|---|---|---|---|---|---|
| REP-01 | Monthly count sheets | Blind sheets the counters write on | Counters (R-01) | Monthly | Printable page | REC-01 | Priya Shah | No |
| REP-02 | Variance file | Finance adjusts stock from it | Finance stock accountant | Monthly | CSV | REC-01, REC-02 | Priya Shah | Yes, once sent to finance |

No notifications to users; a failed import raises operator alert ALR-01 (ENG-08).

## BUS-09 User & Admin Guide

**Getting started:** ask Morgan Lee for access (BUS-04), then open https://stockcount.apps.internal.example and sign in with your company account.

**Count day (team lead, R-02):**
1. Open the home page and check the banner reads "Stock as at" today's date. If it shows an older date, call Tomás Berg before printing.
2. Select **Print count sheets**, choose the month and print. You see one sheet per location.
3. After counting, open **Enter counts**, choose a location and type each counted quantity; leave a line empty if it was not counted.
4. Select **Check variance file**; it must say "OK". Then select **Export variance** and email the file to the finance stock accountant.

**Help:** questions about the count go to Priya Shah; anything that looks broken goes to the IT service desk queue "Stock Count Sheets" (ENG-08).

## ENG-02 User Journeys

| ID | Journey | Roles | Goal | Entry point | Processes | Requirements | Transitions | Exit state |
|---|---|---|---|---|---|---|---|---|
| J-01 | Print the month's count sheets | R-01, R-02 | Have a blind sheet for every location | Home page, Print count sheets | W-01 | FR-02 | None | Printable document open; if the import failed, a banner shows the snapshot date |
| J-02 | Enter counts and export variances | R-02 | Send finance a checked variance file | Home page, Enter counts | W-01 | FR-03, FR-04 | None | Variance CSV downloaded; an invalid quantity shows a message and is not saved |

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | Should the variance file go to finance automatically instead of by email? | Morgan Lee | 2027-01-31 | Open |

## Known limitations

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | No barcode scanning; counts are typed from paper | About 1 hour of typing a month | None | Morgan Lee |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-08-04 | Tomás Berg | First draft with Scope Record | — |
| 0.9 | 2026-09-23 | Tomás Berg | Acceptance results and dry runs added | — |
| 1.0 | 2026-09-30 | Tomás Berg | Accepted at go-live review | Morgan Lee, Warehouse manager, 2026-09-30 |
