# Takaven Product Portfolio

This is the central operating repository for the Takaven product portfolio.

Takaven is the parent software portfolio for active and revived products including TeamFrame, LeaseDesk, HirePass and selected retained components. This repository is not a product application. It is the source of truth for what Takaven is building, what has already been decided, where each product stands and what execution step is authorised next.

## Current Products

The canonical registry is `PORTFOLIO.yaml`. The generated human-readable view is `PORTFOLIO.md`.

- `TKV-001` - TeamFrame: existing core product.
- `TKV-002` - LeaseDesk: revival in progress.
- `TKV-003` - HirePass: next shortlisted build.
- `TKV-004` - PayrollFlowEngine: conditional shortlist.
- `TKV-005` - HR Operations Inbox: component to absorb into TeamFrame.
- `TKV-006` - Attendance & Timesheet Exceptions: component to absorb into TeamFrame.
- `TKV-007` - VisionForge / AI-DAN: hold.

## Active Queue

- `P0`: TeamFrame, LeaseDesk
- `P1`: HirePass
- `P2`: PayrollFlowEngine
- `P2_MODULE`: HR Operations Inbox
- `P3_MODULE`: Attendance & Timesheet Exceptions
- `HOLD`: VisionForge / AI-DAN

## Where Agents Start

1. Read `AGENTS.md`.
2. Read `PORTFOLIO.yaml`.
3. Read the relevant folder under `products/`.
4. Read the active GitHub issue.
5. Inspect actual source assets before execution.

## Governance Lock

Portfolio discovery is closed. Do not reopen broad product discovery, change product scope, alter product status, or start a new execution phase unless an authorised GitHub issue explicitly allows it.

No product repositories may be modified from this setup repository.
