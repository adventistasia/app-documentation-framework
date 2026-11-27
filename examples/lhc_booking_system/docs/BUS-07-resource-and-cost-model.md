---
id: BUS-07
title: Resource & Cost Model
application: LHC Booking System
version: 1.0
status: Accepted
owner: Grace Tan, LHC Manager (Budget holder)
audience: [Budget holder, Management, Business owner, Technical owner]
level: Standard
depth: D
contains: []
related: [BUS-01, ENG-05, ENG-08]
last_reviewed: 2026-09-11
---
# LHC Booking System – Resource & Cost Model

## Purpose

Tells LHC what it takes to deploy and run the LHC Booking System: people and effort, skills, hosting, the domain, running costs, renewals and what retiring it would involve, so the budget holder can fund it and plan for it.

## Scope

Covers every cost and effort line, one-off and recurring. Dependencies and their renewal dates are defined in ENG-05; routine operations tasks (MT) in ENG-08. Amounts are in USD, excluding tax. Internal staff time is costed at the organisation's 2026 charge-back rates: LHC front office USD 25 an hour, LHC management USD 60 an hour, ITS staff USD 40 an hour (ITS developers USD 45 an hour).

## People and effort

| ID | Role | Activity | Covers | Effort per month | Team | Skills needed | Cost per year | Basis | Dependency | Owner |
|---|---|---|---|---|---|---|---|---|---|---|
| COST-01 | LHC Admin (R-03) | Room and rate upkeep, staff roles, queue check, failed-email list, monthly reconciliation and sample audit | MT-01, MT-02, MT-03, MT-04 | 6 hours | LHC Front Office | Booking process, spreadsheet checks | 1,800 | Estimate: time log during the August 2026 pilot | None | Daniel Reyes, LHC Front Office Supervisor |
| COST-02 | ITS Service Desk analyst (R-05) | Triage, access support, urgent removals | Support intake and triage (ENG-08); D-10 | 3 hours | ITS Service Desk | Service desk tool, ENG-08 runbooks | 1,440 | Estimate: ITS average for applications of this size | D-10 | Mark Lim, ITS Service Desk Lead |
| COST-03 | ITS application engineer (R-05) | Patching, dependency upgrades, renewals, secret rotation, restore tests, purge checks, small releases, alert follow-up | MT-05, MT-06, MT-07, MT-08, MT-09, MT-11, MT-12 | 6 hours | ITS Application Team | Python and Django, Azure, PostgreSQL | 2,880 | Estimate: ITS maintenance norm, 0.04 FTE | None | Priya Nair, ITS Application Lead |
| COST-04 | LHC Manager (R-04) | Monthly report review, quarterly access review, yearly budget and rate review | MT-10, MT-13 | 1 hour | LHC Management | None beyond the role | 720 | Estimate | None | Grace Tan, LHC Manager |

## One-off deployment resources

| ID | Item | Effort or cost | When | Basis | Dependency | Owner |
|---|---|---|---|---|---|---|
| COST-05 | Build and test (ITS developer and tester, 400 hours) | 18,000 | 2026-03 to 2026-08 | Actual | None | Priya Nair, ITS Application Lead |
| COST-06 | Room, rate and staff setup data entry (16 hours) | 400 | 2026-08 | Actual | None | Daniel Reyes, LHC Front Office Supervisor |
| COST-07 | Staff training, two 2-hour sessions for 12 people (24 hours) | 600 | 2026-08 | Actual | None | Daniel Reyes, LHC Front Office Supervisor |
| COST-08 | Penetration test (external vendor) and accessibility audit | 3,000 | 2026-08 | Actual: vendor invoice 2,500, ITS accessibility team 500 | None | Priya Nair, ITS Application Lead |
| COST-09 | Early-life support, 4 weeks of extra ITS cover (40 hours) | 1,600 | 2026-09-14 to 2026-10-09 | Estimate | D-10 | Mark Lim, ITS Service Desk Lead |

## Infrastructure and services

| ID | Item | Sizing | Environments | Monthly cost | Annual cost | Basis | Dependency | Owner |
|---|---|---|---|---|---|---|---|---|
| COST-10 | Azure App Service (web, worker, nightly job) | Production B2; test B1 | ENV-02, ENV-03 | 68 | 816 | Quote: Azure pricing calculator, 2026-05-12 | D-02 | Priya Nair, ITS Application Lead |
| COST-11 | Azure Database for PostgreSQL Flexible Server | Production B1ms, 32 GB, 35-day geo-redundant backup; test B1ms | ENV-02, ENV-03 | 55 | 660 | Quote: Azure pricing calculator, 2026-05-12 | D-02 | Priya Nair, ITS Application Lead |
| COST-12 | Application Insights, Log Analytics and Key Vault | 2 GB logs a month, 90-day retention | ENV-02, ENV-03 | 17 | 204 | Actual: August 2026 bill | D-02 | Priya Nair, ITS Application Lead |

The TLS certificate is an App Service managed certificate and costs nothing. Email (D-04) and single sign-on (D-05) are covered by the organisation's existing M365 and Entra ID licences.

## Licences and subscriptions

| ID | Item | Cost | Billing cycle | Renewal date | Notice period | Basis | Dependency | Owner |
|---|---|---|---|---|---|---|---|---|
| COST-13 | Domain booking.lhc.example.org (under the organisation's registrar account) | 20 | Annual | 2027-03-31 | Renew at least 30 days before | Actual | D-03 | Kevin Ho, ITS Network and M365 Administrator |

## Running cost summary

| Cost group | Monthly | Annual | Main assumptions |
|---|---|---|---|
| People and effort | 570 | 6,840 | Effort as in COST-01 to COST-04 at 2026 charge-back rates; no major incidents |
| Infrastructure and services | 140 | 1,680 | Sizing as in COST-10 to COST-12; one production and one test environment |
| Licences and subscriptions | 2 | 20 | Domain only |
| **Total recurring** | 712 | 8,540 | |
| One-off (deployment) | — | 23,600 | COST-05 to COST-09, spent in 2026 |

## Scaling assumptions

| Driver | Current | Expected | Effect on cost | Cost lines affected |
|---|---|---|---|---|
| Booking requests | About 45 a week | Up to 100 a week if LHC opens its annex in 2027 | Database storage stays under 32 GB; App Service may need B3 (about 55 a month more) above 30 concurrent users | COST-10, COST-11 |
| Notification emails | About 300 a month | About 700 a month | None: within the M365 tenant limits | None |
| Incidents and support calls | About 4 a month during the pilot | About 2 a month after early-life support | Service desk effort | COST-02 |
| Charge-back rates | 2026 rates | Reviewed each July | Every people line | COST-01, COST-02, COST-03, COST-04 |

## Funding and ownership

| Item | Value |
|---|---|
| Budget holder | Grace Tan, LHC Manager |
| Cost centre or budget line | LHC operations, line "Guest booking services" |
| Funding period | Financial year 2026–27 (July to June), renewed yearly |
| Next budget review | 2027-05-31 |

## End of life

- Export bookings, rooms and rates to spreadsheets, and keep them for the rest of their BUS-06 retention periods (7 years for anonymised bookings and rates) in the LHC records store; delete personal data that is past its 2-year period first.
- Tell guests with future Confirmed bookings and LHC Finance at least 60 days ahead, and switch the LHC website link (D-01) to the replacement.
- Remove the Azure resources, the Entra ID application registration and the noreply mailbox; let the domain lapse at its next renewal.
- Effort: about 24 hours of ITS time and 8 hours of LHC Admin time.

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-04 | ITS charge-back rates for 2027–28 are not yet published; people costs will be updated when they are. | Priya Nair, ITS Application Lead | 2027-05-31 | Open |

## Known limitations

No known limitations.

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | 2026-02-23 | Priya Nair | Initial estimate at stage 1 | — |
| 0.2 | 2026-05-12 | Priya Nair | Azure quotes added | — |
| 1.0 | 2026-09-11 | Priya Nair | Accepted at go-live with actual one-off costs and pilot effort figures | Grace Tan, LHC Manager, 2026-09-11 |
