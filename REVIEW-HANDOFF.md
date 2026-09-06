# Independent Review Handoff

## Purpose

This repository is intended to be the central operating memory for Takaven product portfolio execution.

## Product Repository Architecture

`takaven/product-portfolio` is the control plane only. It contains canonical portfolio records, product governance, decisions, execution gates, source locators and generated operating views. Product application source code does not live in this repository.

Standalone Takaven products should normally have one dedicated source repository per product. This keeps deployment, CI/test history, secrets, databases/storage, release history, sanitisation, permissions and agent execution context separated, which is especially important for HR/payroll products that may handle sensitive data.

LeaseDesk's actual source repository is `isudally/leasedesk-demo` on `main` at `c36c26f4d12b64f2a66239f47d23d46bbf50eebd`. HirePass's actual source repository is `takaven/hirepass` on `main` at `bc444c2f69cd1fc62359b8ee7fef49392971a619`. TeamFrame's actual application source repository is `takaven/teamframe` on `main` at `73c3e2df701b8484632d3335ca4861c4f2ccb8a7`, and its commercial-site source repository is `takaven/teamframe-site` on `main` at `34192eb663bdef5186032234e39f7d8d76969414`. Files under `products/` are governance/documentation records only; there is no duplicate application source in the control repository.

Future standalone products such as PayrollFlowEngine should receive separate source repositories if activated as standalone products. Long-term Takaven organisation repository normalisation, such as moving LeaseDesk to `takaven/leasedesk`, is deferred and no LeaseDesk migration, rename or new repository creation is currently authorised.

## What Was Created

- Canonical registry: `PORTFOLIO.yaml`
- Schema/constants: `schema/portfolio.schema.json`
- Generated human view: `PORTFOLIO.md`
- Product folders for retained governed records, including TeamFrame as `TKV-001`
- Component and archive registers
- Root governance files
- Issue templates, PR template, CODEOWNERS and validation workflow
- Validation/generation scripts

## Locked Decisions Imported

- Portfolio discovery is closed.
- LeaseDesk, HirePass and TeamFrame are active Takaven commercial products in the immediate launch focus.
- LeaseDesk is source-locked and brand-locked. Product/release work is complete, but LeaseDesk is not deployed or released.
- HirePass is source-locked and brand-locked. Product/code work, Signature Pass, Candidate Pass, Manager Pass and HR Pass Control are accepted, but HirePass is not deployed or released.
- TeamFrame is source-locked and brand-locked as an established product with a separate commercial-site repository.
- PayrollFlowEngine is conditional pending TeamFrame add-on vs independent control-layer decision.
- HR Operations Inbox and Attendance & Timesheet Exceptions are component records whose destination is TeamFrame.
- VisionForge / AI-DAN is on hold.

## Intentionally Incomplete

- No new product execution issue is open from this handoff.
- No product application code was copied or modified.
- LeaseDesk source execution has completed in the separate source repository; no product source code lives in this control repository.
- Final product visual harmonisation is intentionally deferred to a later portfolio-wide UI alignment programme.
- GitHub branch protection has been applied to `main` while the repository is public.

## Automation Created

- Portfolio registry validation.
- JSON Schema validation of `PORTFOLIO.yaml`.
- Cross-record invariant validation for orphan folders, reserved IDs and execution-ready source locators.
- Generated portfolio view staleness check.
- Generated product docs staleness check for generated files only.
- Basic Markdown/internal link check.
- Validation failure-case tests.

## GitHub Settings Successfully Applied

- Repository created as private: `takaven/product-portfolio`
- Default branch pushed as `main`
- Portfolio Validation workflow created and first push run completed successfully
- Branch protection on `main` requiring pull requests and the `validate` status check, with admin enforcement enabled

## Settings Not Applied

- GitHub Team upgrade is deferred.
- Repository visibility remains public for now.

## Assumptions

- `PORTFOLIO.yaml` uses JSON syntax, which is valid YAML. Structural validation uses the `jsonschema` dependency in `requirements.txt`.
- Empty source repository links mean no safe verified URL was supplied during setup.
- `DESIGN.md` and `DECISIONS.md` are manual durable records; generators must not overwrite them.

## Unverified Items

- `TKV-006` source attribution such as `PassGuard-Pipeline` remains `UNVERIFIED`.
- LeaseDesk, HirePass and TeamFrame source baselines are verified and pinned in `PORTFOLIO.yaml`.
- Repository visibility is currently public. If the repository is made private again under a plan that does not support private-repo branch protection, `main` protection and required checks must be reverified before autonomous product execution.

## Manual Actions Required

- Reverify `main` protection after any repository visibility or GitHub base-plan change.

## Product Repository Safety Confirmation

No product repositories, exports, demo applications, databases or uploaded assets should be modified by this setup.

## Phase 1 Operating Model Hardening

This branch adds bounded governance hardening only:

- Canonical gate, authority and design-governance metadata in `PORTFOLIO.yaml`.
- Generated operating dashboard in `DASHBOARD.md`.
- Schema and validation checks for design-system version drift and D1-D4 gate progression.
- Issue and PR template fields for final endpoint, review classification and authority evidence.
- Conservative autonomous-agent guidance in `AUTONOMOUS-AGENTS.md`.
- Deferred automation candidates in `PHASE-2-AUTOMATION-CANDIDATES.md`.

No product execution, product source modification, autonomous-agent installation, deployment or execution issue creation is authorised by this phase.

## Phase 2 GitHub Automation

This branch adds deterministic read-only GitHub automation only:

- PR governance metadata validation for canonical Product ID, required sections and work-item reference format.
- Sensitive `PORTFOLIO.yaml` transition validation for concrete approval-reference presence.
- Read-only workflow permissions.
- Automation failure-case tests.
- `GITHUB-AUTOMATION.md` as the operating description for implemented and deferred controls.

It deliberately does not add automatic issue closure, labels, stale bots, autonomous agent assignment, deployments or product execution.

CI does not prove work-item authorisation or approval substance. Human/governance review remains responsible for those judgments.

## Phase 3 Autonomous Agent Integration Design

This phase recorded the autonomous-agent model:

- Hybrid recommendation: GitHub Copilot cloud agent as future Builder Agent, Codex as future Independent Reviewer.
- Autonomy levels 0-3, with release/deploy disabled by default.
- Mandatory human approval points for product scope, design gates, releases, destructive operations, spend and any agent installation or pilot.
- Cross-repository flow for `product-portfolio` issues and product source repository PRs.
- Context bootstrap order for fresh agents without chat history.
- Data and secret safety rules.
- Governance-only pilot definition.

## Autonomous Agent Enablement Closure

Autonomous Agent Enablement is 2/2 complete.

- Copilot Builder pilot: VALIDATED for governance-only work.
- Independent Reviewer model: VALIDATED.
- Governance hardening: COMPLETE.
- Current operating loop: authorised issue -> Builder -> CI -> independent review where required -> bounded correction -> human merge -> hard stop.
- `product-portfolio` currently remains PUBLIC + protected.
- Copilot Pro is active.
- GitHub Team is deferred unless real product execution creates a material confidentiality or enforcement need.

Governance is frozen for first-product execution. Future governance infrastructure changes require a material defect observed during product execution, repeated manual friction, a material security or permission issue, or a platform behaviour change affecting controls. Theoretical improvements, extra automation possibilities, cleaner architecture preferences and cosmetic documentation refinement are not sufficient reasons by themselves.

## Current Product Handover

### LeaseDesk

- Product record: `TKV-002`
- Source repository: `isudally/leasedesk-demo`
- Final source `main` SHA: `c36c26f4d12b64f2a66239f47d23d46bbf50eebd`
- Source closeout: `isudally/leasedesk-demo#6`, Issue `#5`
- Control closeout: Issue `#21`, PR `#22`, merge SHA `86e3330b05a58e61423ca457b056e446b7361367`
- Programme state: Phase 1/4 COMPLETE, Phase 2/4 COMPLETE, Phase 3/4 COMPLETE, Phase 4/4 COMPLETE, Gates 8/8 COMPLETE, Gate 6 slices 5/5 COMPLETE, Gate 7 PASS, Gate 8 PASS.
- Current gate: product code ready for production release; production deployment/release requires founder approval.
- Not done: production deployment, release, infrastructure provisioning, DNS, production secrets, production database, durable document storage/backups, and final production smoke test.
- UI decision: final branding is applied; production deployment remains a separate founder/customer-delivery decision.

### HirePass

- Product record: `TKV-003`
- Source repository: `takaven/hirepass`
- Final source `main` SHA: `bc444c2f69cd1fc62359b8ee7fef49392971a619`
- Programme state: product/code programme COMPLETE through Gate 8/8; Signature Pass ACHIEVED; final release-quality cleanup COMPLETE; visual signature acceptance ACHIEVED; final branding applied.
- Current gate: commercial launch preparation; production deployment/release requires founder/customer-delivery approval.
- Not done: production deployment, release, infrastructure provisioning, DNS, production secrets, production database, durable upload storage/backups, final production smoke test and post-execution repository visibility closeout.
- Boundary: secure external hiring workflow centred on Candidate Pass, Manager Pass and HR Pass Control; do not turn HirePass into a generic ATS.

### TeamFrame

- Product record: `TKV-001`
- Application repository: `takaven/teamframe`
- Application source `main` SHA: `73c3e2df701b8484632d3335ca4861c4f2ccb8a7`
- Commercial-site repository: `takaven/teamframe-site`
- Commercial-site source `main` SHA: `34192eb663bdef5186032234e39f7d8d76969414`
- Programme state: established product; source locked; brand locked; commercial site locked.
- Current gate: commercial launch preparation; customer deployment remains controlled per customer.
- Not done: walkthrough destination, customer deployment, production release actions and any cross-product integration.

### Commercial Launch Preparation

- Immediate commercial focus: LeaseDesk, HirePass and TeamFrame.
- Remaining founder/commercial decisions: LeaseDesk pricing/package, HirePass pricing/package, TeamFrame walkthrough destination, Takaven-level commercial website, deployment per actual sale/customer and sales/outreach.
- External proof and testimonials are classified as an early commercial objective, not a product-level launch blocker.
- The independent TeamFrame pricing concern is classified as monitor after first sales; approved pricing remains unchanged.
- HirePass is focused on hiring handoffs before employment. TeamFrame is focused on ongoing people operations after an organisation needs structured employee and HR administration. Any integration remains a future separate decision.
- `TKV-004 PayrollFlowEngine` remains P2 / conditional. The exact condition is deciding TeamFrame add-on versus independent Takaven control-layer product. It is Payroll Change Control / Payroll Document Intelligence, not full payroll software.

No product deployment or next-product execution is authorised by this handoff.
