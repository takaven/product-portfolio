# Independent Review Handoff

## Purpose

This repository is intended to be the central operating memory for Takaven product portfolio execution.

## What Was Created

- Canonical registry: `PORTFOLIO.yaml`
- Schema/constants: `schema/portfolio.schema.json`
- Generated human view: `PORTFOLIO.md`
- Product folders for retained governed records except TeamFrame, which is external
- Component and archive registers
- Root governance files
- Issue templates, PR template, CODEOWNERS and validation workflow
- Validation/generation scripts

## Locked Decisions Imported

- Portfolio discovery is closed.
- TeamFrame is external to this repository and handled independently by the founder.
- LeaseDesk is revival in progress.
- HirePass is shortlist build, P1, foundation `Talent-Flow`, controlled consolidation.
- PayrollFlowEngine is conditional pending TeamFrame add-on vs independent control-layer decision.
- HR Operations Inbox and Attendance & Timesheet Exceptions are component records whose destination is the separate TeamFrame repository.
- VisionForge / AI-DAN is on hold.

## Intentionally Incomplete

- No product execution issues were created.
- No product application code was copied or modified.
- No final product UI designs were created.
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

- None currently known for pre-freeze governance hardening.

## Assumptions

- `PORTFOLIO.yaml` uses JSON syntax, which is valid YAML. Structural validation uses the `jsonschema` dependency in `requirements.txt`.
- Empty source repository links mean no safe verified URL was supplied during setup.
- `DESIGN.md` and `DECISIONS.md` are manual durable records; generators must not overwrite them.

## Unverified Items

- `TKV-006` source attribution such as `PassGuard-Pipeline` remains `UNVERIFIED`.
- `TKV-003` primary source `Talent-Flow` remains selected but has `LOCATOR_REQUIRED` until an exact source locator and pinned revision are supplied.
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

This branch records a proposed autonomous-agent model only:

- Hybrid recommendation: GitHub Copilot cloud agent as future Builder Agent, Codex as future Independent Reviewer.
- Autonomy levels 0-3, with release/deploy disabled by default.
- Mandatory human approval points for product scope, design gates, releases, destructive operations, spend and any agent installation or pilot.
- Cross-repository flow for `product-portfolio` issues and product source repository PRs.
- Context bootstrap order for fresh agents without chat history.
- Data and secret safety rules.
- Governance-only pilot definition, not executed.

No autonomous agent has been installed, configured, assigned or piloted. No product execution has started.
