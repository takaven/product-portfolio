# Takaven Product Portfolio

This is the central operating repository for the Takaven product portfolio.

Takaven is the parent software portfolio for revived and governed product work including LeaseDesk, HirePass and selected retained components. This repository is not a product application. It is the source of truth for what this portfolio repository governs, what has already been decided, where each retained record stands and what execution step is authorised next.

TeamFrame is an active product handled independently by the founder in a separate repository. It is referenced here only where retained components may later be absorbed into TeamFrame.

## Current Products

The canonical registry is `PORTFOLIO.yaml`. The generated human-readable product and component view is `PORTFOLIO.md`. The generated operating snapshot is `DASHBOARD.md`.

## Active Queue

See `PORTFOLIO.md`. Do not manually maintain product status, priority or queue summaries in this README.

## Where Agents Start

1. Read `AGENTS.md`.
2. Read `PORTFOLIO.yaml`.
3. Read `DASHBOARD.md` for current blockers and execution readiness.
4. Read `GITHUB-AUTOMATION.md`.
5. Read `AUTONOMOUS-AGENTS.md` when agent operation or review is involved.
6. Read the relevant folder under `products/`.
7. Read the active GitHub issue.
8. Inspect actual source assets before execution.

## Governance Lock

Portfolio discovery is closed. Do not reopen broad product discovery, change product scope, alter product status, or start a new execution phase unless an authorised GitHub issue explicitly allows it.

No product repositories, including TeamFrame, may be modified from this setup repository.

## Operating State

Product-Portfolio Setup is 3/3 complete. Autonomous Agent Enablement is 2/2 complete. The Copilot Builder pilot and Independent Reviewer model have been validated for governance-only work.

`product-portfolio` is intentionally public and protected for now. GitHub Team and a private protected repository posture are deferred unless real product execution creates a material confidentiality or enforcement need.

## Current Programme State

- Governance is enabled and frozen for product execution. Discovery is closed.
- `TKV-002 LeaseDesk` is 8/8 complete. Product code is ready for a founder production-release decision, but LeaseDesk is not deployed, released or commercially live.
- LeaseDesk source of truth is `isudally/leasedesk-demo` on `main` at `d2ce8e988f2d8726fde3dc7e3529e84e0d27db78`.
- LeaseDesk production release still requires founder approval and deployment prerequisites: production PostgreSQL, production secrets, durable document storage, backups, HTTPS/TLS, runtime/domain configuration, host/port compatibility, health/readiness access and final fictional-data smoke testing.
- LeaseDesk final visual harmonisation is intentionally deferred. Do not reopen LeaseDesk implementation for cosmetic polish before the portfolio-wide UI alignment phase unless a material usability defect appears.
- `TKV-003 HirePass` is the next P1 product priority. Before execution, verify the authoritative `Talent-Flow` source locator, pinned baseline, sanitisation/secrets status and governed boundary. Preserve Candidate Pass, Manager Pass and secure external hiring workflow; do not turn HirePass into a generic ATS.
- `TKV-004 PayrollFlowEngine` remains P2 / conditional. Its boundary is Payroll Change Control / Payroll Document Intelligence, not full payroll software. The standalone versus TeamFrame add-on decision remains unresolved.
- TeamFrame remains external and founder-managed in a separate repository.

## Portfolio-Wide UI Strategy

Final visual alignment is deferred until the selected products are complete. The later portfolio-wide UI phase should align typography, spacing, component styling, forms, tables, navigation, status patterns, responsive behaviour, Takaven brand use, iconography and visual polish.

Products should belong to one Takaven family without becoming visually identical:

- TeamFrame: calm, structured, spacious.
- HirePass: sharper, pass-centric, identity/status-driven.
- LeaseDesk: operational, property-oriented, controlled density.
- PayrollFlowEngine: precise, analytical, audit/control-oriented.

## Automation Boundary

Automation may validate canonical state, regenerate views, and support bounded issue execution. It must not approve product boundaries, advance design gates, create execution issues, deploy products, or modify external product repositories without explicit governance authority.

Autonomous-agent operation is enabled only inside authorised issues and pull requests. Product execution is never authorised by repository documentation alone.

## Governance Freeze

The current governance architecture is sufficient for first-product execution. Future governance infrastructure changes require a material defect observed during product execution, a repeated manual-friction pattern, a material security or permission issue, or a platform behaviour change affecting controls.

Theoretical improvement, additional automation possibility, cleaner architecture preference or cosmetic documentation refinement are not sufficient reasons by themselves.
