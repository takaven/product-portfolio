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

## Automation Boundary

Automation may validate canonical state, regenerate views, and support bounded issue execution. It must not approve product boundaries, advance design gates, create execution issues, deploy products, or modify external product repositories without explicit governance authority.

Autonomous-agent operation is enabled only inside authorised issues and pull requests. Product execution is never authorised by repository documentation alone.

## Governance Freeze

The current governance architecture is sufficient for first-product execution. Future governance infrastructure changes require a material defect observed during product execution, a repeated manual-friction pattern, a material security or permission issue, or a platform behaviour change affecting controls.

Theoretical improvement, additional automation possibility, cleaner architecture preference or cosmetic documentation refinement are not sufficient reasons by themselves.
