---
id: ENG-05
title: Integrations & Dependencies Register
application: <Application name>
version: 0.1
status: Draft
owner: <Named person and role>
audience: [Engineering, Support, Business owner, Agents]
level: <Foundation | Standard | Full>
depth: <D | D+>
contains: []
related: [BUS-02, BUS-07, BUS-08, ENG-03, ENG-04, ENG-06, ENG-08]
last_reviewed: <YYYY-MM-DD>
---
# <Application> – Integrations & Dependencies Register

> **How to use this template**
> - **Who writes it:** the technical owner, with the support owner and business owner for owners, impact and workarounds. An agent may draft from configuration, client libraries and infrastructure files; mark drafted content as inferred until confirmed.
> - **When it is due:** Draft by stage 3 (Build); Accepted by stage 4 (Verify).
> - **Depth S** (section `## ENG-05 Integrations & Dependencies Register` in ENG-09): the dependency register with its linked columns (ID, Dependency, Type, Owner, Criticality, Impact, Support path, Workaround, Runbook, Cost) and, when T5 is Yes, one interface row per integration. Keep every linked column (the linter checks them; other columns may be left out) and use level-3 subheadings named after this template's sections, so the section can later be promoted to its own file without restructuring.
> - **Depth D (Standard):** every section except those marked (Full).
> - **Depth D+ (Full):** every section, including (Full).
> - This document replaces DOC-07 Application Dependencies Register; its columns are kept.
> - Delete this block and every `> **Guide:**` block before review, and replace every `<…>`.

## Purpose

<Two to four sentences. Example: "Lists everything <Application> relies on and everything that relies on it, with owners, impact if unavailable, support paths and workarounds, and the contract for every data exchange. Support uses it during incidents; engineers use it when changing an integration; owners use it for renewals and costs.">

## Scope

<Example: "Covers systems, services, accounts, data, people, vendors and funding the application depends on, and downstream systems that depend on it. Runbook entries are in ENG-08, cost lines in BUS-07, connection settings and secret locations in ENG-06.">

## Dependency types

> **Guide:** Use exactly one of these values in the `Type` column (X-20).

| Type | Use for | Examples |
|---|---|---|
| Hosting | Website, platform, servers, containers, database service | Cloud platform, shared web hosting |
| Domain | Domain names, DNS, certificates | Registrar, DNS provider, TLS certificate |
| Email | Sending or receiving email and messages | Email delivery service, SMS gateway |
| Identity | Sign-in, user accounts, directory | Single sign-on provider, directory service |
| Integration | Another system the application exchanges data with; needs an interface entry | Finance system, partner API, file feed |
| Data | Business data the application uses but does not own | Reference lists, master data |
| Vendor | Third-party product or service provider not covered above | Reporting tool, payment provider support |
| Network | Connectivity, VPN, firewall rules | Office network, VPN to partner |
| People | A team or person whose work the application needs | Data steward, operations team |
| Process | A business or support process the application relies on | Access approval process, month-end close |
| Funding | Budget, subscription or contract that keeps it running | Annual licence, hosting budget |

## Dependency register

> **Guide:**
> - **Criticality:** High (a Must capability stops), Medium (degraded, workaround exists), Low (inconvenience).
> - **Impact:** what users and the business experience if it is unavailable, not the technical error.
> - **Support path:** who to contact and how (team, queue, phone, contract reference).
> - **Workaround:** what the business does meanwhile, or `None` stated explicitly.
> - **Runbook:** the ENG-08 runbook entry (RB IDs). Every High dependency needs one (X-21).
> - **Cost:** Yes when it costs money; it then needs a BUS-07 cost line (X-24).
> - **Renewal:** the next renewal or expiry date; it must match the BUS-07 licence and subscription line and the ENG-08 maintenance calendar.
> - **Capabilities affected:** must agree with the `Dependencies` column of BUS-02 (every High dependency is listed there by at least one capability, X-09).
> - **Direction:** Upstream (the application relies on it) or Downstream (it relies on the application).

| ID | Dependency | Type | Purpose | Owner | Criticality | Impact | Support path | Capabilities affected | Workaround | Runbook | Cost | Renewal | Direction | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D-01 | <Email delivery service> | <Email> | <Sends notifications> | <Named person or team> | <High / Medium / Low> | <Requesters get no acknowledgement; staff not alerted> | <Vendor support portal, contract ref; internal: platform team> | <C-01, C-04> | <Staff phone requesters from the queue, or None> | <RB-01, or None> | <Yes / No> | <YYYY-MM-DD, or None> | <Upstream / Downstream> | <…> |

## Interfaces

> **Guide:** Required when T5 is Yes. One row per data exchange with another system: every dependency of type Integration has at least one (X-20). Never write a secret, password or token; name the secret by its ENG-06 `SEC` ID.
> - **Endpoint or location:** base URL, queue or folder, non-secret.
> - **Data exchanged:** ENG-04 entities (ENT IDs) and, briefly, which fields.
> - **Error and retry behaviour:** what happens on timeout, rejection or bad data, how many retries over what time, and where failures surface (ALR ID).
> - **Contract:** link to the OpenAPI document, schema, file specification or agreement.

| ID | Dependency | Direction | Protocol | Endpoint or location | Data exchanged | Trigger / frequency | Authentication | Error and retry behaviour | Contract | Other-side owner |
|---|---|---|---|---|---|---|---|---|---|---|
| INT-01 | <D-03> | <In / Out> | <REST / SOAP / file / SFTP / email / SSO / message queue> | <https://api.example.org/v2, or /exports/daily/> | <ENT-01: id, status, dates> | <On submit / nightly 02:00 / on demand> | <OAuth client credentials, SEC-02> | <3 retries with backoff over 15 min; then ALR-03> | <Link to schema or agreement> | <Team, contact> |

## Downstream consumers

> **Guide:** Systems, reports or teams that rely on this application. They are dependencies with Direction Downstream. Operators need to know whom to warn before maintenance and during an outage.

| Dependency | What they consume | Impact on them if this application fails | How they are told | Contact |
|---|---|---|---|---|
| <D-04> | <Daily export of confirmed records (INT-02)> | <Their monthly report is incomplete> | <Email to their support list; see ENG-08 Communication> | <Team, contact> |

## Interface details (Full)

> **Guide:** For integrations where a change on either side could break the other: versioning, limits and guarantees.

| Interface | Version and change policy | Rate limits | Idempotency | Ordering and duplicates | Service level from the other side | Test environment |
|---|---|---|---|---|---|---|
| <INT-01> | <v2; 90 days' notice of breaking change> | <100 requests/min> | <Idempotency key per request> | <…> | <99.9%, support hours> | <Sandbox URL, ENV-02> |

## Exit and substitution (Full)

> **Guide:** For High dependencies on a vendor or external platform: what it would take to replace it, and how data is recovered if the contract ends.

| Dependency | Data held by the vendor | How to export | Alternatives | Notice period | Effort to switch |
|---|---|---|---|---|---|
| <D-01> | <Delivery logs only> | <API export> | <…> | <30 days> | <2 person-days> |

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
