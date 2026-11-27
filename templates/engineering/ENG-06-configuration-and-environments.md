---
id: ENG-06
title: Configuration & Environments
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Engineering, Technical operators, Agents]
level: <Foundation | Standard | Full>
depth: <D | D+>
contains: []
related: [ENG-03, ENG-05, ENG-07, ENG-08, ENG-09]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Configuration & Environments

> **How to use this template**
> - **Who writes it:** the technical owner or lead engineer. An agent may draft from environment files, infrastructure code and the configuration loader; mark drafted content as inferred until confirmed.
> - **When it is due:** Draft by stage 3 (Build); Accepted by stage 5 (Go-live).
> - **Depth S** (section `## ENG-06 Configuration & Environments` in ENG-09, the default at Foundation and Standard): the environments table, and the secrets table with locations and owners. List configuration items and feature flags only if there are any that an operator would change. Keep every linked column (the linter checks them; other columns may be left out) and use level-3 subheadings named after this template's sections, so the section can later be promoted to its own file without restructuring.
> - **Depth D (Standard):** every section.
> - **Depth D+ (Full):** the same as D. No section is marked (Full), and the depth matrix never sets this item to D+.
> - **Never write a secret value** (password, key, token, connection string with credentials) in this or any document. Record where it is stored and who owns it.
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

<Two to four sentences. Example: "Lists the environments <Application> runs in and the configuration, secrets and feature flags it reads, so operators and agents can run, configure and promote it without guessing. Secret values are never recorded; only where they are kept.">

## Scope

<Example: "Covers all environments from local development to production. How code moves between environments is in ENG-07; where each container runs is in ENG-03; local setup commands are in ENG-09.">

## Environments

> **Guide:** One row per environment, including local development if it is shared or scripted. **Data** must say whether it holds real data; an environment with real personal data needs the same access control as production.

| ID | Environment | Purpose | URL | Data | Access | Hosting | Deployed from |
|---|---|---|---|---|---|---|---|
| ENV-01 | <Development> | <Shared integration testing> | <https://dev.example.org> | <Synthetic / Copy of production, masked / Real> | <Engineering team via SSO> | <Platform, account or project> | <main branch, on merge> |

## Configuration items

> **Guide:** Every setting the application reads at start-up or run time that is not a secret. **Value source** says where each environment's value comes from (environment variable, configuration file path, parameter store key), not the value itself when it differs per environment. **Who may change** names a role; changing production configuration is a change under ENG-08 Change management.

| ID | Name | Purpose | Default | Value source per environment | Who may change | Restart needed |
|---|---|---|---|---|---|---|
| CFG-01 | <APP_BASE_URL> | <Public base URL used in emails> | <http://localhost:3000> | <ENV-01: pipeline variable; ENV-03: parameter store /app/prod/base_url> | <Technical owner> | <Yes / No> |

## Secrets

> **Guide:** Name and location only. **Stored in** is the vault, secret manager or pipeline secret store and the key path. **Rotation** gives the interval and how it is done (or a runbook entry). Rotation dates that must not be missed also go in the ENG-08 maintenance calendar.

| ID | Name | Purpose | Stored in | Used by | Rotation | Owner | Last rotated |
|---|---|---|---|---|---|---|---|
| SEC-01 | <DATABASE_URL> | <Database connection for the API> | <Secret manager: /app/prod/db_url> | <CMP-02> | <Every 90 days; RB-05> | <Named person> | <YYYY-MM-DD> |

## Feature flags

> **Guide:** Every flag is temporary unless stated. **Removal criteria** says when the flag and its dead code path are deleted; a flag with no removal criteria becomes permanent configuration and should be listed as a configuration item instead. Write "No feature flags." if there are none.

| ID | Flag | Purpose | Owner | Default | State per environment | Removal criteria | Added |
|---|---|---|---|---|---|---|---|
| FLAG-01 | <new_review_screen> | <Gradual rollout of the redesigned review screen> | <Product owner> | <Off> | <ENV-01 On; ENV-03 Off> | <Remove 2 weeks after 100% rollout with no Sev1–Sev2 incidents> | <YYYY-MM-DD> |

## Promotion and parity

> **Guide:** How a configuration change reaches each environment, and the known differences between environments that can make something pass in test and fail in production.

<How configuration changes are made and promoted, e.g. "Pull request to infrastructure repository; applied by pipeline; production requires technical owner approval".>

| Difference | Environments | Why | Risk |
|---|---|---|---|
| <Email sending disabled; messages captured instead> | <ENV-01, ENV-02> | <Avoid emailing real users> | <Email templates not tested end to end before production> |

## Assumptions and open questions

| ID | Assumption or question | Owner | Due | Status |
|---|---|---|---|---|
| Q-01 | <…> | <…> | <YYYY-MM-DD> | <Open / Closed> |

## Known limitations

| ID | Limitation | Impact | Workaround | Owner |
|---|---|---|---|---|
| LIM-01 | <…> | <…> | <…, or None> | <…> |

## Change log

| Version | Date | Author | Summary | Approved by |
|---|---|---|---|---|
| 0.1 | <YYYY-MM-DD> | <Name> | First draft | — |
