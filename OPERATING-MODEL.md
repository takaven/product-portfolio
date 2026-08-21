# Takaven Operating Model

The portfolio operating hierarchy is:

> Portfolio repository -> product source-of-truth -> bounded GitHub issue -> agent execution -> pull request -> automated checks -> status/register update

## Source of Truth

`PORTFOLIO.yaml` is the canonical machine-readable register for products and component records governed by this repository. Generated views such as `PORTFOLIO.md` must be regenerated from it.

TeamFrame is handled outside this repository. References to TeamFrame exist only to identify external destination context for retained components.

`DASHBOARD.md` is generated from `PORTFOLIO.yaml` and exists only as an operating snapshot. If it disagrees with `PORTFOLIO.yaml`, regenerate it rather than editing it by hand.

## Execution Flow

1. A bounded GitHub issue defines the authorised work.
2. The agent reads this repository's governance files.
3. The agent reads the relevant product folder.
4. The agent inspects the actual source assets.
5. The agent works only within the issue scope.
6. The agent opens a pull request.
7. CI validates the portfolio registry and generated views.
8. Status or decision updates are made only where authorised.

## Portfolio Discovery

Portfolio discovery is closed. New products may enter the register only under the policy recorded in `PORTFOLIO.yaml`.

## Gate Model

The Phase 1 gate model uses the existing canonical fields rather than introducing a second workflow system:

- `status`
- `priority`
- `lifecycle_stage`
- `execution_ready`
- `current_execution_gate`

Every execution or review issue must define a finite final endpoint. The agent stops there even when the next useful step is obvious.

Review findings use four classifications:

- `BLOCKING`: prevents merge or execution gate clearance.
- `MATERIAL`: should be corrected before the current phase is accepted.
- `NON_BLOCKING`: record or defer; does not trigger another correction loop by itself.
- `COSMETIC`: improve only when already in scope.

Only `BLOCKING` and `MATERIAL` findings require correction loops. Previously passed review areas remain closed unless a regression, new evidence or explicit governance reopening occurs.

## Authority Model

Agents may inspect authorised source assets, create working branches, modify authorised files, run checks, fix in-scope CI defects, prepare pull requests and update generated views.

Founder or governance approval is required for product boundary changes, commercial positioning changes, product activation/archive, D1-D3 design approval, D4 full frontend authorisation, Takaven master brand changes, production deployment/release and significant external-service spend.

Builder, Independent Reviewer and Governance Reviewer should be treated as separate roles. An implementation agent must not self-approve material governance changes.

## Frontend Governance

No full frontend rollout may begin before visual foundation and critical screens are approved through gates D1-D4.

Design gate status is recorded per product in `PORTFOLIO.yaml`. Components absorbed into TeamFrame use `NOT_APPLICABLE` in this repository because TeamFrame is governed separately.

## Loop Prevention

This repository should prevent repeated rediscovery and endless correction cycles. Future work should begin from the active issue and dashboard, not from a broad product search. Correction passes should name the specific defect class and final endpoint. Once a gate passes, it stays passed unless a concrete regression or authorised governance change reopens it.

## GitHub Automation

Phase 2 GitHub automation is documented in `GITHUB-AUTOMATION.md`.

The automation layer is limited to deterministic repository administration checks:

- PR metadata and work-item reference traceability.
- Sensitive canonical transition detection.
- Generated-view freshness.
- Existing registry/schema/product-folder validation.

It must remain read-only unless a later governance phase explicitly authorises a narrow write operation. CI validates reference format and metadata structure; human review validates authorisation substance. Merge never starts the next product phase automatically.
