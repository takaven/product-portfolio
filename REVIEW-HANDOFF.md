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
- GitHub branch protection may require manual verification depending on permissions.

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

## Settings Not Applied

- Branch protection on `main` was not applied. GitHub returned a plan/permission restriction for branch protection on a private repository.
- Required status checks were not enforced through branch protection for the same reason.

## Assumptions

- `PORTFOLIO.yaml` uses JSON syntax, which is valid YAML. Structural validation uses the `jsonschema` dependency in `requirements.txt`.
- Empty source repository links mean no safe verified URL was supplied during setup.
- `DESIGN.md` and `DECISIONS.md` are manual durable records; generators must not overwrite them.

## Unverified Items

- `TKV-006` source attribution such as `PassGuard-Pipeline` remains `UNVERIFIED`.
- `TKV-003` primary source `Talent-Flow` remains selected but has `LOCATOR_REQUIRED` until an exact source locator and pinned revision are supplied.
- GitHub branch protection and required checks are unverified until applied and confirmed after repository creation.

## Manual Actions Required

- Enable branch protection for `main` if the GitHub organisation/account plan allows it later.
- When branch protection is available, require pull requests and the `validate` status check from the Portfolio Validation workflow.

## Product Repository Safety Confirmation

No product repositories, exports, demo applications, databases or uploaded assets should be modified by this setup.
