# Portfolio Decision Log

This log is append-only for material portfolio decisions. Routine status updates belong in `PORTFOLIO.yaml` and generated views.

## 2026-08-20 - Portfolio Discovery Closed

- `PORTFOLIO.yaml` became the canonical registry.
- Portfolio discovery is closed.
- LeaseDesk remains revival in progress.
- HirePass remains P1 / shortlist build with `Talent-Flow` as foundation and controlled consolidation strategy.
- PayrollFlowEngine remains conditional pending product-boundary decision.
- HR Operations Inbox and Attendance & Timesheet Exceptions are retained as TeamFrame components, not independent products.
- VisionForge / AI-DAN remains on hold.

## 2026-08-20 - TeamFrame Removed From Governed Portfolio

- TeamFrame is an active product handled independently by the founder in a separate repository.
- TeamFrame is no longer a product record in this portfolio operating repository.
- `TKV-001` is intentionally not reassigned.
- HR Operations Inbox and Attendance & Timesheet Exceptions remain retained component records only; their destination is the separate TeamFrame repository.

## 2026-08-20 - Bounded Governance Corrections

- `TKV-001` is now explicitly reserved and must not be recycled.
- JSON Schema became the structural validator for `PORTFOLIO.yaml`; Python validation is reserved for cross-record invariants.
- Product source assets now require explicit role, type, locator status and revision fields.
- HirePass remains selected for build, but execution is blocked until `Talent-Flow` has a reproducible locator and pinned revision.
- `DESIGN.md` and `DECISIONS.md` are manual durable records and are no longer generated.
- D2, D3 and D4 design gates require prerequisite approval evidence.
- HirePass's Pass concept is canonically required while detailed terminology remains provisional.
- Retained component records are separated from active independent products in generated views.
