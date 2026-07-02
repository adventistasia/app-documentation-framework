# LHC Booking System Example

This example shows how capabilities and workflows can be documented for the LHC Booking System.

## Capabilities Register Example

| ID | Capability | Description | Outcome | Primary users | Used in workflows |
|---|---|---|---|---|---|
| C01 | Submit booking request | Allows a guest or staff member to submit a room booking request with guest details, stay dates, room needs, and contact information. | A booking request is created and enters the official review process. | Guest, LHC Staff | W01, W02 |
| C02 | Check room availability | Allows staff to see whether rooms are available for requested dates and avoid double-booking. | Staff can determine whether the requested stay can be accommodated. | LHC Staff, LHC Admin | W02, W03, W04 |
| C03 | Review booking request | Allows LHC staff to review completeness, dates, guest details, special requirements, and operational feasibility. | Staff can decide whether the request is ready for confirmation, needs correction, or cannot be accepted. | LHC Staff, LHC Admin | W02, W03 |
| C04 | Confirm booking | Allows authorized staff to approve and confirm a booking. | The guest receives a confirmed booking. | LHC Staff, LHC Admin | W02, W03 |
| C05 | Return or reject request | Allows staff to return incomplete requests or reject requests that cannot be accommodated. | Invalid, incomplete, or unavailable requests are removed from the active confirmation path. | LHC Staff, LHC Admin | W02, W03 |
| C06 | Modify booking | Allows authorized staff to change dates, room assignments, guest details, or booking notes. | Booking records remain accurate when guest or operational needs change. | LHC Staff, LHC Admin | W04 |
| C07 | Cancel booking | Allows authorized users to cancel a booking and release the room allocation. | Canceled bookings no longer occupy room availability. | LHC Staff, LHC Admin | W04 |
| C08 | Manage room records | Allows administrators to add, edit, activate, deactivate, or update room information. | Room inventory stays accurate and usable for booking operations. | LHC Admin | W05 |
| C09 | Manage pricing/rates | Allows authorized users to update room rates or pricing references. | Booking charges and rate references remain current. | LHC Admin | W05, W06 |
| C10 | Assign rooms | Allows staff to assign a specific room to a confirmed booking. | Confirmed guests are linked to actual room assignments. | LHC Staff, LHC Admin | W03, W04 |
| C11 | Track booking status | Allows users to track whether a booking is pending, confirmed, modified, canceled, checked in, completed, or closed. | Staff can monitor where each booking stands in the operational process. | LHC Staff, LHC Admin, ITS Support | W01, W02, W03, W04, W06 |
| C12 | Send notifications | Sends confirmation, status update, cancellation, or action-required messages to guests or staff. | Guests and staff are informed when action is needed or booking status changes. | System, Guest, LHC Staff | W01, W02, W03, W04 |
| C13 | Manage user access and roles | Allows authorized administrators to create accounts, assign roles, change access, or remove access. | Only authorized users can perform booking, administrative, or support actions. | LHC Admin, ITS Support | W07 |
| C14 | Generate booking reports | Produces reports for occupancy, bookings, cancellations, guest stays, or management review. | LHC management receives visibility into booking activity and room usage. | LHC Admin, LHC Management | W06 |
| C15 | Support issue handling | Allows issues to be reported, reviewed, escalated, and resolved by LHC or ITS depending on ownership. | User issues and system problems have a clear resolution path. | LHC Staff, ITS Support | W08 |
| C16 | Maintain audit/history trail | Records important actions such as booking confirmation, modification, cancellation, access changes, and pricing updates. | Important changes can be reviewed for accountability, support, and operational traceability. | LHC Admin, ITS Support | W03, W04, W05, W07, W08 |

## Workflow Register Example

| ID | Workflow | Trigger | Main outcome | Main roles | Capabilities used |
|---|---|---|---|---|---|
| W01 | Guest submits booking request | Guest needs accommodation at LHC | Booking request is created and ready for review | Guest, LHC Staff | C01, C11, C12 |
| W02 | LHC reviews booking request | New booking request is submitted | Request is confirmed, returned, or rejected | LHC Staff, LHC Admin | C02, C03, C04, C05, C11, C12 |
| W03 | LHC confirms and assigns room | Request is accepted for accommodation | Guest has a confirmed booking and assigned room | LHC Staff, LHC Admin | C02, C04, C10, C11, C12, C16 |
| W04 | Booking is modified or canceled | Guest or LHC needs to change the booking | Booking is updated, canceled, or room allocation is released | Guest, LHC Staff, LHC Admin | C02, C06, C07, C10, C11, C12, C16 |
| W05 | LHC manages rooms and pricing | Room inventory or pricing changes | Room and rate information stays current | LHC Admin | C08, C09, C16 |
| W06 | LHC reviews booking activity | Management or operations needs visibility | Booking, occupancy, and activity reports are produced | LHC Admin, LHC Management | C09, C11, C14 |
| W07 | Access is created or changed | New staff member, role change, or access removal request | Correct users have correct permissions | LHC Admin, ITS Support | C13, C16 |
| W08 | Support issue is handled | User reports an issue or system problem occurs | Issue is resolved by LHC or escalated to ITS | LHC Staff, LHC Admin, ITS Support | C11, C15, C16 |

## Workflow Detail Example

### W01 - Guest submits booking request

| Step | Actor | Action | Capability used | Status/result | Notes |
|---|---|---|---|---|---|
| 1 | Guest | Navigates to booking entry point and fills in guest details, stay dates, room type, and contact information | C01 | Draft | Guest may arrive via the public website (D01) |
| 2 | System | Validates that required fields are present and formats are correct | C01 | Draft | Incomplete submissions are held on the form; no request is created |
| 3 | System | Creates the booking request and assigns it a request ID | C01 | Pending review | Request enters the review queue |
| 4 | System | Updates booking status to Pending review | C11 | Pending review | Status is visible to LHC Staff and LHC Admin |
| 5 | System | Sends submission acknowledgement notification to guest | C12 | Pending review | Email sent via D04; guest receives confirmation of receipt |

#### Decision points

| Decision | Options | Decision owner | Resulting status/action |
|---|---|---|---|
| Are all required fields present and valid? | Yes → request is created; No → form validation error shown to guest | System | Draft (held) or Pending review (created) |

#### Exceptions and alternate paths

| Exception | Handling | Owner | Escalation path |
|---|---|---|---|
| Email notification fails to send | Request is still created; guest is advised to contact LHC if no acknowledgement is received | System / ITS | ITS support (D04) |
| Guest submits duplicate request for same dates | Staff identifies duplicate during review (W02) and returns or rejects the duplicate | LHC Staff | LHC Admin if unclear |

---

### W02 - LHC reviews booking request

| Step | Actor | Action | Capability used | Status/result | Notes |
|---|---|---|---|---|---|
| 1 | LHC Staff | Opens pending booking request from the review queue | C03 | Pending review | |
| 2 | LHC Staff | Checks room availability for requested dates | C02 | Pending review | Availability checked against current room inventory (D06) |
| 3 | LHC Staff | Reviews guest details, special requirements, and operational feasibility | C03 | Pending review | |
| 4a | LHC Staff / LHC Admin | Confirms the request if complete, available, and feasible | C04 | Confirmed | Proceeds to W03 for room assignment |
| 4b | LHC Staff / LHC Admin | Returns incomplete request to guest for correction | C05 | Returned | Notification sent to guest with details of what is required |
| 4c | LHC Staff / LHC Admin | Rejects request if dates unavailable or request cannot be accommodated | C05 | Rejected | Notification sent to guest explaining rejection |
| 5 | System | Updates booking status to reflect decision | C11 | Confirmed / Returned / Rejected | |
| 6 | System | Sends status notification to guest | C12 | Confirmed / Returned / Rejected | |

#### Decision points

| Decision | Options | Decision owner | Resulting status/action |
|---|---|---|---|
| Is the room available for requested dates? | Yes → proceed to feasibility review; No → reject or offer alternate dates | LHC Staff | Rejection or alternate offer |
| Is the request complete and feasible? | Complete and feasible → confirm; Incomplete → return; Not feasible → reject | LHC Staff / LHC Admin | Confirmed, Returned, or Rejected |

#### Exceptions and alternate paths

| Exception | Handling | Owner | Escalation path |
|---|---|---|---|
| Request has conflicting or unclear dates | Returned to guest for clarification | LHC Staff | LHC Admin if unresolved |
| Guest does not respond to a returned request | Request remains in Returned status; LHC may close after a defined period | LHC Admin | LHC management |

---

### W03 - LHC confirms and assigns room

| Step | Actor | Action | Capability used | Status/result | Notes |
|---|---|---|---|---|---|
| 1 | LHC Staff / LHC Admin | Opens confirmed booking and verifies room availability for assigned dates | C02, C04 | Confirmed | |
| 2 | LHC Staff / LHC Admin | Assigns a specific room to the confirmed booking | C10 | Room assigned | Room assignment recorded in booking record |
| 3 | System | Updates booking status to reflect room assignment | C11 | Room assigned | |
| 4 | System | Records the assignment action in the audit trail | C16 | Room assigned | |
| 5 | System | Sends booking confirmation with room details to guest | C12 | Room assigned | Email sent via D04 |

#### Decision points

| Decision | Options | Decision owner | Resulting status/action |
|---|---|---|---|
| Is the preferred room available for assignment? | Yes → assign; No → assign alternate room or return to review | LHC Staff / LHC Admin | Room assigned or return to W02 |

#### Exceptions and alternate paths

| Exception | Handling | Owner | Escalation path |
|---|---|---|---|
| No suitable room is available at assignment stage | Booking is returned to review; guest is notified | LHC Admin | LHC management |
| Guest requests a specific room type not available | LHC offers alternate option or rejects if no alternative | LHC Staff | LHC Admin |

---

### W04 - Booking is modified or canceled

| Step | Actor | Action | Capability used | Status/result | Notes |
|---|---|---|---|---|---|
| 1 | Guest / LHC Staff / LHC Admin | Submits or requests a change to an existing confirmed booking | C06 / C07 | Modification requested / Cancellation requested | Guests may request via phone or email outside the system |
| 2 | LHC Staff / LHC Admin | Verifies the request and checks availability if dates are changing | C02 | — | |
| 3a | LHC Staff / LHC Admin | Modifies booking dates, room assignment, or guest details | C06, C10 | Modified | |
| 3b | LHC Staff / LHC Admin | Cancels booking and releases room allocation | C07 | Canceled | Room becomes available for other bookings |
| 4 | System | Updates booking status | C11 | Modified / Canceled | |
| 5 | System | Records the change in the audit trail | C16 | Modified / Canceled | |
| 6 | System | Sends notification to guest confirming the change or cancellation | C12 | Modified / Canceled | |

#### Decision points

| Decision | Options | Decision owner | Resulting status/action |
|---|---|---|---|
| Is the new date range available? | Yes → proceed with modification; No → advise guest of unavailability | LHC Staff / LHC Admin | Modified or no change |
| Is the request a modification or cancellation? | Modification → update booking; Cancellation → cancel and release room | LHC Staff / LHC Admin | Modified or Canceled |

#### Exceptions and alternate paths

| Exception | Handling | Owner | Escalation path |
|---|---|---|---|
| Modification conflicts with another booking | Offer alternate dates or cancel if no option available | LHC Staff | LHC Admin |
| Guest requests cancellation after check-in | Handled as an operational decision outside normal workflow | LHC Admin | LHC management |

---

### W05 - LHC manages rooms and pricing

| Step | Actor | Action | Capability used | Status/result | Notes |
|---|---|---|---|---|---|
| 1 | LHC Admin | Identifies need to add, edit, or deactivate a room record or update pricing | C08 / C09 | — | Triggered by operational change or management decision |
| 2 | LHC Admin | Makes the required changes to room inventory or pricing/rate data | C08 / C09 | Updated | Changes take effect immediately for new booking checks |
| 3 | System | Records the change in the audit trail | C16 | Updated | |

#### Decision points

| Decision | Options | Decision owner | Resulting status/action |
|---|---|---|---|
| Is the room being deactivated or permanently removed? | Deactivated → room hidden from availability; Removed → record archived | LHC Admin | Room status updated |

#### Exceptions and alternate paths

| Exception | Handling | Owner | Escalation path |
|---|---|---|---|
| Room deactivation conflicts with an existing booking | Existing booking must be reassigned or canceled before deactivation | LHC Admin | LHC management |
| Pricing update affects confirmed bookings | Existing bookings retain previously agreed rates; only new bookings use updated rates | LHC Admin | LHC management |

---

### W06 - LHC reviews booking activity

| Step | Actor | Action | Capability used | Status/result | Notes |
|---|---|---|---|---|---|
| 1 | LHC Admin / LHC Management | Identifies reporting need (occupancy, bookings, cancellations, guest stays) | C14 | — | Triggered by management review cycle or ad hoc request |
| 2 | LHC Admin | Selects report type and filters (date range, room type, status) | C14 | — | |
| 3 | System | Generates and displays the requested report | C14 | Report produced | |
| 4 | LHC Admin / LHC Management | Reviews report and identifies any actions required | C09, C11 | — | May trigger W04 (modification/cancellation) or W05 (pricing update) |

#### Decision points

| Decision | Options | Decision owner | Resulting status/action |
|---|---|---|---|
| Does the report identify issues requiring action? | Yes → initiate relevant workflow; No → review complete | LHC Admin / LHC Management | Action initiated or none required |

#### Exceptions and alternate paths

| Exception | Handling | Owner | Escalation path |
|---|---|---|---|
| Report data is incomplete or inaccurate | Reported as an issue and escalated to ITS (W08) | LHC Admin | ITS Support |

---

### W07 - Access is created or changed

| Step | Actor | Action | Capability used | Status/result | Notes |
|---|---|---|---|---|---|
| 1 | LHC Admin / ITS Support | Receives request to create, modify, or remove user access | C13 | — | Triggered by onboarding, role change, or offboarding |
| 2 | LHC Admin | Verifies the request against the approved roles and access matrix | C13 | — | |
| 3 | LHC Admin / ITS Support | Creates account, assigns role, updates access, or removes access | C13 | Access updated | |
| 4 | System | Records the access change in the audit trail | C16 | Access updated | |

#### Decision points

| Decision | Options | Decision owner | Resulting status/action |
|---|---|---|---|
| Is the requested role approved for the user? | Yes → proceed; No → escalate to LHC management for approval | LHC Admin | Access granted or escalated |

#### Exceptions and alternate paths

| Exception | Handling | Owner | Escalation path |
|---|---|---|---|
| Urgent access removal (e.g. staff departure) | Access removed immediately; formal record updated afterwards | LHC Admin / ITS Support | LHC management |
| Role not defined in the access matrix | Access not granted until role is formally defined and approved | LHC Admin | LHC management |

---

### W08 - Support issue is handled

| Step | Actor | Action | Capability used | Status/result | Notes |
|---|---|---|---|---|---|
| 1 | LHC Staff / LHC Admin | User reports an issue (booking error, access problem, system error) | C15 | Issue reported | |
| 2 | LHC Staff / LHC Admin | Reviews the issue and determines if it is an operational or technical matter | C11, C15 | Under review | |
| 3a | LHC Admin | Resolves operational issues (booking corrections, access adjustments) | C15 | Resolved | |
| 3b | LHC Admin | Escalates technical or system issues to ITS Support | C15 | Escalated | |
| 4a | System | Records operational resolution in the audit trail (follows 3a) | C16 | Resolved | |
| 4b | ITS Support | Investigates and resolves technical issue (follows 3b) | C15 | Resolved | |
| 5 | System | Records escalation outcome in the audit trail (follows 4b) | C16 | Resolved | |

#### Decision points

| Decision | Options | Decision owner | Resulting status/action |
|---|---|---|---|
| Is the issue operational or technical? | Operational → LHC Admin resolves; Technical → escalate to ITS | LHC Admin | Resolved or Escalated |

#### Exceptions and alternate paths

| Exception | Handling | Owner | Escalation path |
|---|---|---|---|
| ITS cannot reproduce the issue | LHC Admin provides additional evidence; ITS re-investigates | LHC Admin / ITS Support | ITS management |
| Issue recurs after resolution | Treated as a new issue; root cause investigation initiated | LHC Admin / ITS Support | LHC management / ITS management |

---

## Example Application Dependencies Register

| ID | Dependency | Type | Purpose | Owner | Impact if unavailable | Support path |
|---|---|---|---|---|---|---|
| D01 | Public website / landing page | Website | Directs guests to booking information and booking entry point. | LHC / ITS | Guests may not find the booking service. | ITS support |
| D02 | Booking application hosting | Application platform | Runs the guest booking system. | ITS | Booking system becomes unavailable. | ITS / hosting provider |
| D03 | Application domain | Domain/DNS | Provides public access to the booking system URL. | ITS | Users cannot access the application by URL. | ITS / DNS administrator |
| D04 | Email service | Communication | Sends booking confirmations, status updates, and staff notifications. | ITS / M365 Admin | Guests and staff may not receive booking updates. | ITS support |
| D05 | Staff user accounts | Identity/access | Allows LHC staff and admins to log in. | LHC Admin / ITS | Staff cannot process bookings. | LHC Admin, then ITS |
| D06 | Room inventory data | Business data | Provides available rooms, room types, and capacity. | LHC Admin | Staff may assign incorrect or unavailable rooms. | LHC Admin |
| D07 | Pricing/rate data | Business data | Provides room rates or pricing references. | LHC Admin / Management | Incorrect pricing may be used. | LHC Admin / Management |
| D08 | Internet connectivity | Infrastructure | Allows guests and staff to access the system. | User site / ITS | Users may not be able to access the system. | Local IT / ISP |
| D09 | LHC booking staff | Operational dependency | Reviews, confirms, modifies, and cancels bookings. | LHC | Requests may remain unprocessed. | LHC management |
| D10 | ITS support process | Support dependency | Handles technical issues, access issues, and escalations. | ITS | Issues may not be resolved consistently. | ITS helpdesk |

## Example Audit Finding

```markdown
### Bugs

| ID | Finding | Severity | Evidence | Required action |
|---|---|---|---|---|
| BUG-01 | Role names are not normalized across capabilities and workflows. | Medium | Capabilities use Support while workflows use ITS Support. | Use the same role names as the Roles and Access Matrix. |

### Risks

| ID | Finding | Severity | Evidence | Required action |
|---|---|---|---|---|
| RISK-01 | Email dependency affects notifications but is not mapped to affected capabilities. | Medium | D04 exists but C12 does not reference dependency D04. | Link D04 to C12 and related workflows W01-W04. |

### Ideas

| ID | Finding | Value | Evidence | Suggested action |
|---|---|---|---|---|
| IDEA-01 | Add criticality to capabilities. | Medium | Capabilities do not yet show launch-critical functions. | Add Criticality column to Capabilities Register. |
```
