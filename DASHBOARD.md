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
| `P0` | TKV-002 | LeaseDesk | `REVIVAL_IN_PROGRESS` | `STAGE_4_MARKET_READY_PREPARATION` | `true` | Gate 4/8 D2 critical screens approved; next LeaseDesk work requires explicit Gate 5/8 D3 authorisation. |
| `P1` | TKV-003 | HirePass | `SHORTLIST_BUILD` | `STAGE_2_BUILD_COMPLETION` | `false` | BLOCKED - verify Talent-Flow source locator and pinned revision before Phase 1 sanitisation and foundation extraction. |
| `P2` | TKV-004 | PayrollFlowEngine | `SHORTLIST_CONDITIONAL` | `STAGE_1_PRODUCT_DEFINITION` | `false` | Resolve product boundary decision. |

## Source Locator Health

| ID | Product | Primary Source Status |
| -- | ------- | --------------------- |
| TKV-002 | LeaseDesk | leasedesk-demo: `VERIFIED` / `VERIFIED` |
| TKV-003 | HirePass | Talent-Flow: `LOCATOR_REQUIRED` / `UNVERIFIED` |
| TKV-004 | PayrollFlowEngine | PayrollFlowEngine source assets: `LOCATOR_REQUIRED` / `VERIFIED` |
| TKV-005 | HR Operations Inbox | No primary source recorded |
| TKV-006 | Attendance & Timesheet Exceptions | No primary source recorded |
| TKV-007 | VisionForge / AI-DAN | VisionForge / AI-DAN assets: `LOCATOR_REQUIRED` / `VERIFIED` |

## Design Gate Status

| ID | Product | Design Stage | Design System | Visual Profile |
| -- | ------- | ------------ | ------------- | -------------- |
| TKV-002 | LeaseDesk | `D2_APPROVED` | `takaven-design-system-v1` | leasedesk-visual-profile-v0 |
| TKV-003 | HirePass | `NOT_STARTED` | `takaven-design-system-v1` | hirepass-visual-profile-v0 |
| TKV-004 | PayrollFlowEngine | `NOT_STARTED` | `takaven-design-system-v1` | payrollflowengine-visual-profile-v0 |
| TKV-005 | HR Operations Inbox | `NOT_APPLICABLE` | `takaven-design-system-v1` | hr-operations-inbox-visual-profile-v0 |
| TKV-006 | Attendance & Timesheet Exceptions | `NOT_APPLICABLE` | `takaven-design-system-v1` | attendance-exceptions-visual-profile-v0 |
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
| TKV-003 | HirePass | BLOCKED - verify Talent-Flow source locator and pinned revision before Phase 1 sanitisation and foundation extraction. |
| TKV-004 | PayrollFlowEngine | Decide TeamFrame add-on vs independent Takaven control-layer product. |
| TKV-005 | HR Operations Inbox | Only execute inside authorised TeamFrame work in the separate TeamFrame repository. |
| TKV-006 | Attendance & Timesheet Exceptions | Only execute inside authorised TeamFrame work in the separate TeamFrame repository after source confirmation. |
| TKV-007 | VisionForge / AI-DAN | No execution scheduled. |

## Summary Counts

| Metric | Result |
| ------ | -----: |
| Product records | 6 |
| Active queue records | 3 |
| Component records | 2 |
| Execution blocked records | 5 |
| Status `COMPONENT_ABSORB` | 2 |
| Status `HOLD` | 1 |
| Status `REVIVAL_IN_PROGRESS` | 1 |
| Status `SHORTLIST_BUILD` | 1 |
| Status `SHORTLIST_CONDITIONAL` | 1 |
| Source locator `LOCATOR_REQUIRED` | 4 |
| Source locator `UNVERIFIED` | 9 |
| Source locator `VERIFIED` | 1 |
