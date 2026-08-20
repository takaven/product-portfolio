<!-- GENERATED FROM PORTFOLIO.yaml. DO NOT EDIT DIRECTLY. -->

# Takaven Product Portfolio

**Discovery status:** `PORTFOLIO_DISCOVERY_CLOSED`

Takaven is a software portfolio for revived and active products with bounded execution gates. This repository is the operating memory for portfolio decisions, source hierarchy, product boundaries and authorised next steps.

## External Products

| Product | Relationship | Governance Rule |
| ------- | ------------ | --------------- |
| TeamFrame | active product handled independently by the founder in a separate repository | TeamFrame is not part of this portfolio operating repository and must not be modified or executed from here. |

## Operating Principle

> Portfolio repository -> product source-of-truth -> bounded GitHub issue -> agent execution -> pull request -> automated checks -> status/register update

## Current Products

| ID | Product | Category | Status | Priority | Execution Gate |
| -- | ------- | -------- | ------ | -------- | -------------- |
| TKV-002 | LeaseDesk | Property Operations | `REVIVAL_IN_PROGRESS` | `P0` | Commercial-product completion after validation/demo readiness. |
| TKV-003 | HirePass | Recruitment Workflow | `SHORTLIST_BUILD` | `P1` | Phase 1 - sanitisation and foundation extraction. |
| TKV-004 | PayrollFlowEngine | Payroll Operations / Document Intelligence | `SHORTLIST_CONDITIONAL` | `P2` | Resolve product boundary decision. |
| TKV-005 | HR Operations Inbox | HR Workflow | `COMPONENT_ABSORB` | `P2_MODULE` | Only execute inside authorised TeamFrame work in the separate TeamFrame repository. |
| TKV-006 | Attendance & Timesheet Exceptions | HR Operations | `COMPONENT_ABSORB` | `P3_MODULE` | Only execute inside authorised TeamFrame work in the separate TeamFrame repository after source confirmation. |
| TKV-007 | VisionForge / AI-DAN | AI Developer Tools | `HOLD` | `HOLD` | No execution scheduled. |

## Active Queue

| Priority | Products |
| -------- | -------- |
| `P0` | LeaseDesk |
| `P1` | HirePass |
| `P2` | PayrollFlowEngine |
| `P2_MODULE` | HR Operations Inbox |
| `P3_MODULE` | Attendance & Timesheet Exceptions |
| `HOLD` | VisionForge / AI-DAN |

## Components

| Component | Destination | Reuse Instruction |
| --------- | ----------- | ----------------- |
| Candidate Pass workflow | HirePass | Reuse workflow concepts; harden token security and document access before production. |
| Manager Pass workflow | HirePass | Reuse flow; centralise permissions, expiry and audit logging. |
| JWT auth and audit scaffolding | HirePass | Port patterns only after replacing unsafe defaults and adding tenant isolation. |
| HR Operations Inbox | TeamFrame | Absorb into TeamFrame only through authorised TeamFrame module work. |
| Attendance and timesheet exceptions | TeamFrame | Keep as component; do not treat as standalone product. |

## New Product Policy

Portfolio discovery is closed. New products may enter only when:

- genuinely new source assets are discovered
- Takaven intentionally creates a new product
- materially new evidence justifies reopening an archived lineage

## Where Agents Start

1. Read `AGENTS.md`.
2. Read `PORTFOLIO.yaml`.
3. Read the relevant folder under `products/`.
4. Read the active GitHub issue.
5. Inspect actual source assets before execution.
