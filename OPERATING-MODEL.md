# Takaven Operating Model

The portfolio operating hierarchy is:

> Portfolio repository -> product source-of-truth -> bounded GitHub issue -> agent execution -> pull request -> automated checks -> status/register update

## Source of Truth

`PORTFOLIO.yaml` is the canonical machine-readable register. Generated views such as `PORTFOLIO.md` must be regenerated from it.

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

## Frontend Governance

No full frontend rollout may begin before visual foundation and critical screens are approved through gates D1-D4.
