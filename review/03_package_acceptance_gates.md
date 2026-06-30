# Package Acceptance Gates

## Gate 1 - Completeness

The package passes Gate 1 when:

- All required artifacts are present.
- Missing optional artifacts are identified as not applicable or deferred.
- Every artifact has metadata: title, application name, version/date, owner, status.

Fail if:

- A required artifact is missing.
- The package does not identify the application clearly.
- Document versions or ownership are absent.

## Gate 2 - Business understanding

The package passes Gate 2 when:

- Application purpose and business value are clear.
- Users and stakeholders are identified.
- In-scope and out-of-scope functions are clear.
- Operational impact is documented.

Fail if:

- The reader cannot explain what the application does or why it exists.
- Ownership is missing.
- Impact of unavailability is not documented.

## Gate 3 - Capability and workflow traceability

The package passes Gate 3 when:

- Capabilities describe what the system can do.
- Each capability has an outcome.
- Workflows describe how the system is used.
- Capabilities and workflows map to each other.
- Roles and statuses used in workflows are defined.

Fail if:

- Capabilities are just UI features.
- Workflows are missing triggers, outcomes, or roles.
- Capabilities and workflows do not trace.

## Gate 4 - Governance and control

The package passes Gate 4 when:

- Business rules are documented and owned.
- Status lifecycle is defined.
- Access roles and sensitive permissions are documented.
- Data, reports, and notifications have owners and purposes.
- Risks and controls are documented for major issues.

Fail if:

- Rules are vague or unowned.
- Access is unclear.
- Sensitive data is not identified.
- Reports or notifications lack purpose or owner.

## Gate 5 - Support readiness

The package passes Gate 5 when:

- Support ownership is clear.
- Issue intake, triage, escalation, and routine operations are documented.
- Critical dependencies have owners, support paths, and impact statements.
- Known limitations and workarounds are documented.

Fail if:

- Users cannot know where to get help.
- Support team cannot triage issues.
- Dependency failures have no support path.

## Gate 6 - Handover readiness

The package passes Gate 6 when:

- Delivered and deferred scope are recorded.
- Accepted workflows are listed.
- Roles/access model and support model are accepted.
- Known limitations and accepted risks are disclosed.
- Business owner, support owner, and technical/application owner acceptance are recorded.

Fail if:

- Acceptance record is missing.
- Known limitations are hidden.
- Handover does not identify owners.
