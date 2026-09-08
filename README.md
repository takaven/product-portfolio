# Takaven Product Portfolio

This is the central operating repository for the Takaven product portfolio.

Takaven is the parent software portfolio for active commercial product work including LeaseDesk, HirePass, TeamFrame and selected retained components. This repository is not a product application. It is the source of truth for what this portfolio repository governs, what has already been decided, where each retained record stands and what execution step is authorised next.

TeamFrame is an active Takaven commercial product. Its application and commercial website live in separate source repositories; this control repository records only portfolio state, source baselines and governance context.

## Current Products

The canonical registry is `PORTFOLIO.yaml`. The generated human-readable product and component view is `PORTFOLIO.md`. The generated operating snapshot is `DASHBOARD.md`.

## Repository Architecture

`takaven/product-portfolio` is the Takaven control plane. It records portfolio governance, product status, boundaries, priorities, decisions, source locators, execution gates, design governance, handover notes and generated operating views.

It is not an application monorepo and must not contain copies of product source code. Standalone Takaven products should use one dedicated source repository per product unless a later explicit founder/product architecture decision changes that topology.

Current examples: `isudally/leasedesk-demo` is the authoritative LeaseDesk application source repository, `takaven/hirepass` is the authoritative HirePass application source repository, `takaven/teamframe` is the authoritative TeamFrame application source repository and `takaven/teamframe-site` is the authoritative TeamFrame commercial-site source repository. The files under `products/` are governance and documentation records only, not product implementations.

This separation preserves independent deployment, CI/test history, secrets and environment boundaries, database/storage boundaries, release histories, sanitisation controls, agent execution context and future licensing, sale, transfer or spin-out options. Future Takaven organisation normalisation such as `takaven/leasedesk`, `takaven/hirepass` or `takaven/payrollflowengine` is deferred until there is a material operational reason; do not migrate or rename `isudally/leasedesk-demo` merely for tidiness.

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

No product repositories may be modified from this setup repository unless a separate authorised issue explicitly names that source repository and work boundary.

## Operating State

Product-Portfolio Setup is 3/3 complete. Autonomous Agent Enablement is 2/2 complete. The Copilot Builder pilot and Independent Reviewer model have been validated for governance-only work.

`product-portfolio` is intentionally public and protected for now. GitHub Team and a private protected repository posture are deferred unless real product execution creates a material confidentiality or enforcement need.

## Current Programme State

- Governance is enabled and frozen for product execution. Discovery is closed.
- `TKV-001 TeamFrame` is source-locked and brand-locked. TeamFrame is an active commercial product; customer deployment remains controlled per customer.
- `TKV-002 LeaseDesk` is source-locked and brand-locked. Product/release work is complete, but LeaseDesk is not deployed or released.
- LeaseDesk source of truth is `isudally/leasedesk-demo` on `main` at `ce0d8969966cbbab3c6ee2f0718ef3a64a2f0f69`.
- `TKV-003 HirePass` is source-locked and brand-locked. Product/code work, Signature Pass, Candidate Pass, Manager Pass and HR Pass Control are accepted, but HirePass is not deployed or released.
- HirePass source of truth is `takaven/hirepass` on `main` at `7a45f1af75b7182c7a51daa8a1efe26ff9ba8d6a`.
- `TKV-004 PayrollFlowEngine` remains P2 / conditional. Its boundary is Payroll Change Control / Payroll Document Intelligence, not full payroll software. The standalone versus TeamFrame add-on decision remains unresolved.
- The approved Takaven commercial model is one-off product purchase with customer-paid/customer-controlled infrastructure where practical. Post-handover support and future change requests are optional and quoted separately; no monthly software subscription, mandatory maintenance or annual software licence is approved.
- LeaseDesk public offer is `LeaseDesk + Setup` at `US$2,950` one-off. HirePass public offer is `HirePass + Setup` at `US$3,450` one-off. TeamFrame preserves `US$1,950` software-only and `from US$3,450` with setup.
- LeaseDesk `from US$5,450` and HirePass `from US$6,450` custom-work anchors are internal quoting anchors only, not second public product tiers or technical capacity limits.
- The next programme phase is `COMMERCIAL LAUNCH PREPARATION`: Takaven commercial website, TeamFrame walkthrough destination, sales/demo preparation, deployment per actual sale/customer and sales/outreach.
- The final independent adversarial launch review found no product-level blockers. Accepted pre-outreach corrections are operational/commercial readiness items only; product development remains closed.

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
