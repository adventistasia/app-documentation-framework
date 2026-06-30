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
