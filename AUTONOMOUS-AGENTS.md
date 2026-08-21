# Autonomous Agent Operating Model

Phase 3/3 and Autonomous Agent Enablement Phase 2/2 are complete. This document records the frozen autonomous-agent operating model for Takaven.

## Position

Autonomous agents may be useful only inside bounded GitHub issues with clear acceptance gates, source locators, PR review and CI. The goal is not maximum autonomy. The goal is useful autonomy that preserves portfolio governance, source pinning, design gates, auditability and least privilege.

No product execution is authorised by this document.

## Programme State

- Product-Portfolio Setup Programme: 3/3 COMPLETE.
- Autonomous Agent Enablement: 2/2 COMPLETE.
- Copilot Builder pilot: VALIDATED for governance-only work.
- Independent Reviewer model: VALIDATED.
- Governance hardening: COMPLETE.
- Current operating loop: authorised issue -> Builder -> CI -> independent review where required -> bounded correction -> human merge -> hard stop.
- Product execution requires separate explicit authorisation.

Current platform posture:

- `product-portfolio`: PUBLIC + protected.
- Copilot Pro: active.
- GitHub Team: deferred.
- Private protected posture may be reconsidered only if real product execution creates a material confidentiality or enforcement need.

## Governance Freeze

The current governance architecture is considered sufficient for first-product execution. Future governance changes require at least one of:

- a material defect observed during product execution;
- a repeated manual-friction pattern;
- a material security or permission issue;
- a platform behaviour change affecting controls.

The following are not sufficient reasons by themselves:

- theoretical improvement;
- additional automation possibility;
- cleaner architecture preference;
- cosmetic documentation refinement.

## Official Evidence Reviewed

The current recommendation is based on official vendor documentation reviewed during Phase 3:

- GitHub Copilot cloud agent can research a repository, create a plan, make changes on a branch, run tests in an ephemeral GitHub Actions-powered environment, and optionally open a pull request. It is available for paid Copilot plans and can work in GitHub-hosted repositories unless disabled. Source: [GitHub Copilot cloud agent overview](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent).
- GitHub Copilot cloud agent can be started from GitHub, assigned to issues, and can raise a pull request and request review. Source: [Using Copilot cloud agent on GitHub](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-on-github).
- GitHub Copilot cloud agent access depends on plan and repository policy. Business and Enterprise administrators must enable it; Pro, Pro+ and Max accounts have it enabled by default unless a repository is opted out. Source: [Managing access to GitHub Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/access-management).
- GitHub Copilot cloud agent environment setup can be customised through setup steps, but this repository does not configure that yet. Source: [Configure the Copilot cloud agent environment](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment).
- Codex code review can review GitHub pull request diffs, follow repository guidance and post review feedback focused on serious issues. Source: [Review GitHub pull requests with Codex](https://learn.chatgpt.com/docs/third-party/github).
- Codex GitHub Action can automate Codex feedback in CI, but examples require additional write permissions to post PR comments. This remains deferred. Source: [Codex GitHub Action](https://learn.chatgpt.com/docs/github-action).
- Codex reads `AGENTS.md` files before work and can use repository-specific instructions. Source: [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

## Vendor Assessment

| Option | GitHub Fit | Private Repo | Issue to PR | Permissions | Auditability | Recommendation |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| GitHub Copilot cloud agent | High | Supported on GitHub repos where enabled | Strong | Requires repo write access for branches/PRs; no default-branch write should be granted | High through GitHub branches, commits, PRs and logs | Primary Builder candidate after review and pilot |
| OpenAI Codex cloud / GitHub workflows | Medium | Supported where GitHub connection is configured | Partial, depending on workflow | Good for review; CI comment posting needs write permissions if automated | High for PR reviews and GitHub Action logs | Primary Independent Reviewer candidate; secondary Builder only where GitHub-native Copilot is insufficient |
| Third-party GitHub agents | Unknown until individually reviewed | Unknown | Unknown | Often broader or app-specific | Varies | Do not install unless Copilot/Codex cannot cover a concrete need |

## Recommended Model

Use a hybrid model:

1. GitHub Copilot cloud agent is the preferred future Builder Agent for bounded implementation issues because it is GitHub-native, issue-driven, branch/PR-oriented and visible in the normal GitHub review flow.
2. Codex is the preferred Independent Reviewer for high-signal PR review because it can follow `AGENTS.md` and review PR diffs without becoming the builder of record.
3. Product governance remains in this repository, CI and human review. No agent may approve its own material work.

Do not grant new agent permissions, enable new repositories or start product execution unless a bounded issue explicitly authorises that action.

## Autonomy Levels

| Level | Name | Permitted Actions | Default Status |
| --- | --- | --- | --- |
| 0 | Read-only review | Inspect issue, docs, source and PR; report findings only | Allowed when assigned |
| 1 | PR preparation | Create branch, edit authorised files, run checks, open draft PR | Allowed only after issue authorisation and agent enablement |
| 2 | Iterative PR maintenance | Respond to CI and `BLOCKING` or `MATERIAL` reviewer findings within the same issue scope | Allowed only within an existing authorised PR |
| 3 | Release/deploy | Deploy, release, migrate production data or change live services | Disabled by default |

## Mandatory Human Approval Points

Human/founder/governance approval remains mandatory for:

- activating a new product;
- changing product boundary;
- changing commercial positioning;
- clearing conditional status;
- D1 UX principles approval;
- D2 critical screens approval;
- D3 component primitives approval;
- D4 full frontend implementation authorisation;
- Takaven master brand changes;
- production deployment or release;
- destructive data or schema operations;
- material external spend;
- granting a new agent integration or repository permission;
- starting any pilot.

Routine implementation inside an already authorised issue should not require repeated approval unless it hits one of these gates.

## Cross-Repository Flow

The recommended cross-repository model is:

`product-portfolio issue -> source repo execution -> source repo PR -> independent review -> merge -> product-portfolio governance update, if authorised`

Rules:

1. The control issue lives in `takaven/product-portfolio` when the work is governance, source-resolution, gate approval or portfolio-state related.
2. Product implementation issues should live in the product source repository once that repository is pinned and governed.
3. Every product source issue or PR must carry the Product ID, execution gate, source locator and final endpoint copied from the controlling portfolio record or issue.
4. Implementation PRs belong in the source repository. Canonical portfolio updates belong in `product-portfolio`.
5. If an agent cannot safely access both the control repo and source repo, split the work: one issue/PR for product-source changes and a separate governance PR for canonical updates.
6. Because GitHub Copilot cloud agent can only make changes in the selected repository for a task, do not assign it a cross-repository implementation task that requires edits in both repositories.

## Context Bootstrap

A fresh autonomous agent must reconstruct context in this order:

1. Root `AGENTS.md`
2. `PORTFOLIO.yaml`
3. `DASHBOARD.md`
4. `GITHUB-AUTOMATION.md`
5. This `AUTONOMOUS-AGENTS.md`
6. Relevant product folder under `products/`
7. Active GitHub issue
8. Exact source repository or source asset named by the issue
9. Pinned baseline revision or export hash
10. Product-specific `DESIGN.md` and `DECISIONS.md`
11. Relevant previous PR or review evidence linked from the issue

If any required source locator, pinned revision, prerequisite design approval or governance reference is missing, the agent must stop and report the blocker.

## Permission Model

Minimum permissions:

- Builder Agent: write access only to the specific repository for branch and PR creation; no direct default-branch write; no deployment permission; no production secrets; no billing/admin access; no organisation-wide write access.
- Independent Reviewer: read or review permission where practical; if automated comments are later enabled, restrict write permission to PR comments only.
- Governance Layer: existing read-only CI checks remain authoritative. Any future write automation must be separately reviewed and approved.

## Data and Secret Safety

Agents may identify the existence and category of sensitive material, but must not copy values or records into issues, PRs, logs or this repository.

Sensitive categories include:

- `.env` files and credentials;
- API keys and tokens;
- candidate, employee, payroll, tenant or property records;
- uploaded CVs, passports, visas, contracts and private documents;
- production databases or storage buckets.

If a source contains unsanitised sensitive data and the task requires sharing, external review, migration or public logs, stop at the sanitisation gate. Do not continue by redacting ad hoc in a PR description.

A cloud autonomous Builder must not be granted access to a source repository containing unsanitised real candidate, employee, payroll, tenant, financial, identity-document or similarly sensitive operational data unless a separately approved data-processing or security decision explicitly authorises that access. The normal path is to sanitise or isolate the source first, verify the safe source, and only then grant Builder access.

## Review Loop

Default flow:

1. Human creates or approves a bounded issue.
2. Builder prepares a branch and draft PR.
3. Human approves the GitHub Actions workflow run if GitHub requires approval for the agent-created or agent-updated PR.
4. CI runs deterministic checks.
5. Independent Reviewer reviews the PR.
6. Builder fixes `BLOCKING` and `MATERIAL` findings within scope.
7. Focused re-review checks only the corrected findings and regressions.
8. Human/governance merges when satisfied.

For Copilot-created or Copilot-updated PRs, GitHub Actions may require a human to approve workflow runs before CI executes. This is a GitHub safety gate and does not constitute product execution, design approval, agent installation or authorisation of the next phase.

Passed findings remain closed. Cosmetic findings do not force another correction loop. Merge does not begin the next phase.

## Concurrency Rules

- One active Builder PR per product and execution gate.
- One active design gate per product at a time.
- Do not run redesign and implementation branches simultaneously for the same surface.
- Do not assign two agents to the same issue unless one is explicitly Builder and the other is Reviewer.
- If two branches touch the same canonical product record, pause one until the other merges or closes.
- Product-source changes and portfolio-governance changes should be split unless a single authorised issue explicitly permits both.

## Governance-Only Pilot

Validated pilot:

> One governance-only issue in `product-portfolio` asked an agent to make a bounded documentation wording correction in `AUTONOMOUS-AGENTS.md`, open a draft PR, pass existing CI, respond to an independent reviewer correction, and stop before merge.

Pilot acceptance checks:

- issue assignment works;
- agent reads `AGENTS.md`;
- branch and draft PR are created;
- PR template is completed;
- CI runs, after human workflow approval if GitHub requires it;
- reviewer correction loop is bounded;
- no product source repository is accessed or modified;
- no next issue or phase starts automatically.

The pilot validated the operating loop for governance-only work. It does not authorise product execution.

## Explicit Prohibitions

Autonomous agents must not automatically:

- begin the next phase;
- expand product scope;
- change product status, priority or boundary unless the issue explicitly authorises the canonical change;
- approve design gates;
- redesign after D-gate approval;
- deploy or release;
- add external integrations;
- access production secrets;
- alter sensitive source data;
- create product execution issues from this repository without authorisation.
