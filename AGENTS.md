# AGENTS.md

This repository governs Takaven product portfolio execution. It is a control repository, not a product application.

## Required Reading Order

Before acting, every agent must read:

1. `PORTFOLIO.yaml`
2. The relevant folder under `products/`
3. The active GitHub issue
4. The actual source repository or source asset named in the issue

## Canonical Source

`PORTFOLIO.yaml` is authoritative for product ID, name, status, priority, lifecycle stage, source hierarchy, product boundary, exclusions, TeamFrame relationship, current execution gate, component/archive state and conditions.

Markdown files may explain context but must not introduce conflicting canonical state. If a conflict is found, stop that update, report the conflict and do not guess.

## Execution Rules

- Never reopen portfolio discovery unless explicitly authorised.
- Never silently change product boundaries.
- Never change canonical portfolio state for implementation convenience.
- Never start the next execution phase automatically.
- Stop at the GitHub issue acceptance gate.
- Work through pull requests rather than direct default-branch changes.
- Update canonical state only when the issue authorises it.
- Record material decisions in the relevant `DECISIONS.md` and root `DECISION-LOG.md`.
- Distinguish `VERIFIED`, `INFERRED` and `UNVERIFIED` claims.

## Safety Rules

Do not copy real candidate, employee, payroll, tenant, property, uploaded-document, credential or environment data into this repository.

Do not modify product repositories from this repository. That includes TeamFrame, LeaseDesk, Talent-Flow, HirePass source variants, PayrollFlowEngine, Replit exports, demo apps, databases, deployment configuration and uploaded assets.

## Product-Specific Guardrails

- TeamFrame is handled separately by the founder. No TeamFrame execution issue should be created from this setup.
- LeaseDesk is revival in progress and should not be treated as a disposable validation app.
- HirePass is the next build target but no product execution is authorised by this repository setup.
- PayrollFlowEngine is conditional and must not become a full payroll system.
- HR Operations Inbox and Attendance & Timesheet Exceptions are components/modules for TeamFrame, not independent product workstreams.
- VisionForge / AI-DAN is on hold.
