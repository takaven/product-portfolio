<!-- GENERATED FROM PORTFOLIO.yaml. DO NOT EDIT DIRECTLY. -->

# Takaven Portfolio Dashboard

This generated dashboard is the operating snapshot for portfolio execution readiness.

## Control Snapshot

| Control | Value |
| ------- | ----- |
| Discovery status | `PORTFOLIO_DISCOVERY_CLOSED` |
| Gate model | `phase1-governance-v1` |
| Design system | `takaven-design-system-v1` |
| No automatic next phase | `true` |

## Active Execution Queue

| Priority | ID | Product | Status | Stage | Execution Ready | Current Gate |
| -------- | -- | ------- | ------ | ----- | --------------- | ------------ |
| `P0` | TKV-002 | LeaseDesk | `EXISTING_CORE` | `STAGE_5_READY_TO_LAUNCH` | `true` | Commercial launch preparation; production deployment/release remains founder/customer-delivery controlled. |
| `P1` | TKV-003 | HirePass | `EXISTING_CORE` | `STAGE_5_READY_TO_LAUNCH` | `true` | Commercial launch preparation; production deployment/release remains founder/customer-delivery controlled. |
| `P1` | TKV-001 | TeamFrame | `EXISTING_CORE` | `STAGE_5_READY_TO_LAUNCH` | `true` | Commercial launch preparation; customer deployment remains controlled per customer and requires founder/customer-delivery approval. |
| `P2` | TKV-004 | PayrollFlowEngine | `SHORTLIST_CONDITIONAL` | `STAGE_1_PRODUCT_DEFINITION` | `false` | Future/conditional. Resolve product boundary decision after LeaseDesk, HirePass and TeamFrame commercial launch preparation unless explicitly authorised earlier. |

## Source Locator Health

| ID | Product | Primary Source Status |
| -- | ------- | --------------------- |
| TKV-002 | LeaseDesk | leasedesk-demo: `VERIFIED` / `VERIFIED` |
| TKV-003 | HirePass | hirepass: `VERIFIED` / `VERIFIED` |
| TKV-001 | TeamFrame | teamframe: `VERIFIED` / `VERIFIED` |
| TKV-005 | HR Operations Inbox | No primary source recorded |
| TKV-006 | Attendance & Timesheet Exceptions | No primary source recorded |
| TKV-004 | PayrollFlowEngine | PayrollFlowEngine source assets: `LOCATOR_REQUIRED` / `VERIFIED` |
| TKV-007 | VisionForge / AI-DAN | VisionForge / AI-DAN assets: `LOCATOR_REQUIRED` / `VERIFIED` |

## Design Gate Status

| ID | Product | Design Stage | Design System | Visual Profile |
| -- | ------- | ------------ | ------------- | -------------- |
| TKV-002 | LeaseDesk | `D4_AUTHORISED` | `takaven-design-system-v1` | leasedesk-visual-profile-v1 |
| TKV-003 | HirePass | `D4_AUTHORISED` | `takaven-design-system-v1` | hirepass-visual-profile-v1 |
| TKV-001 | TeamFrame | `D4_AUTHORISED` | `takaven-design-system-v1` | teamframe-visual-profile-v1 |
| TKV-005 | HR Operations Inbox | `NOT_APPLICABLE` | `takaven-design-system-v1` | hr-operations-inbox-visual-profile-v0 |
| TKV-006 | Attendance & Timesheet Exceptions | `NOT_APPLICABLE` | `takaven-design-system-v1` | attendance-exceptions-visual-profile-v0 |
| TKV-004 | PayrollFlowEngine | `NOT_STARTED` | `takaven-design-system-v1` | payrollflowengine-visual-profile-v0 |
| TKV-007 | VisionForge / AI-DAN | `NOT_STARTED` | `takaven-design-system-v1` | visionforge-visual-profile-v0 |

## Retained Components

These records are not independent execution workstreams.

| ID | Component | Destination | Execution Gate |
| -- | --------- | ----------- | -------------- |
| TKV-005 | HR Operations Inbox | TeamFrame | Only execute inside authorised TeamFrame work in the separate TeamFrame repository. |
| TKV-006 | Attendance & Timesheet Exceptions | TeamFrame | Only execute inside authorised TeamFrame work in the separate TeamFrame repository after source confirmation. |

## Blocker Snapshot

| ID | Product | Blocking State |
| -- | ------- | -------------- |
| TKV-005 | HR Operations Inbox | Only execute inside authorised TeamFrame work in the separate TeamFrame repository. |
| TKV-006 | Attendance & Timesheet Exceptions | Only execute inside authorised TeamFrame work in the separate TeamFrame repository after source confirmation. |
| TKV-004 | PayrollFlowEngine | Decide TeamFrame add-on vs independent Takaven control-layer product. |
| TKV-007 | VisionForge / AI-DAN | No execution scheduled. |

## Summary Counts

| Metric | Result |
| ------ | -----: |
| Product records | 7 |
| Active queue records | 4 |
| Component records | 2 |
| Execution blocked records | 4 |
| Status `COMPONENT_ABSORB` | 2 |
| Status `EXISTING_CORE` | 3 |
| Status `HOLD` | 1 |
| Status `SHORTLIST_CONDITIONAL` | 1 |
| Source locator `LOCATOR_REQUIRED` | 3 |
| Source locator `UNVERIFIED` | 9 |
| Source locator `VERIFIED` | 5 |
