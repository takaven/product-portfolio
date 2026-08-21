# GitHub Automation

Phase 2/3 adds deterministic GitHub administration checks only. It does not configure autonomous agents, close issues automatically, apply labels, deploy products or make product decisions.

## Implemented Controls

| Automation | Classification | Reason |
| ---------- | -------------- | ------ |
| Work-item reference presence | `IMPLEMENT_NOW` | Product-scoped PRs must include a concrete work-item reference so human review can trace execution. |
| Gate metadata validation | `IMPLEMENT_NOW` | PR body must include product ID, execution gate, final endpoint, change summary and exclusions. |
| Duplicate active work prevention | `DOCUMENT_ONLY` | Reliable duplicate detection needs GitHub issue state and labels; premature automation would be noisy. |
| Automatic close-on-merge | `DOCUMENT_ONLY` | Safe only after issue linkage and label discipline are proven; merge must not start the next gate. |
| Labels | `DOCUMENT_ONLY` | Useful later, but not required for deterministic CI checks. Avoid label sprawl first. |
| Dashboard freshness | `IMPLEMENT_NOW` | Existing generated-view staleness checks remain the safest approach. Actions must not silently commit generated files. |
| Stale work | `DOCUMENT_ONLY` | Long-running product work is not automatically stale; simple time rules would create false positives. |
| Governance transition validation | `IMPLEMENT_NOW` | Sensitive canonical transitions require concrete approval-reference evidence and hard source-readiness checks. |

## Workflow

1. A bounded GitHub issue or work item authorises work.
2. A branch is created for that issue.
3. The PR uses the repository template.
4. Product-scoped PRs include a concrete work-item reference.
5. CI validates registry state, generated views, product docs, PR metadata, reference format and canonical transitions.
6. Human review decides whether the referenced work item actually authorises the PR and whether the PR satisfies it.
7. Merge closes only the submitted work. It does not start the next gate.

## Effective Permissions

`Portfolio Validation` uses:

- `contents: read`
- `pull-requests: read`

No write permission is granted. No secrets are required.

## Fail-Safe Behaviour

Automation blocks or reports when:

- required PR metadata is missing;
- product-scoped PRs do not include a concrete work-item reference;
- a product-scoped PR changes another product folder;
- a workflow change omits a permissions note;
- a cross-repository PR is opened;
- sensitive `PORTFOLIO.yaml` transitions lack concrete governance approval-reference evidence;
- `execution_ready` becomes true without verified source locator and pinned revision;
- generated views are stale.

Automation does not:

- decide whether a product should be built;
- approve a design gate;
- approve commercial positioning;
- deploy or release software;
- close issues automatically;
- assign autonomous agents.

## Machine vs Human Validation

Machine validation verifies:

- reference presence and format;
- canonical Product ID;
- required metadata sections;
- sensitive canonical transition detection;
- source-readiness evidence;
- generated-view freshness.

Human/governance review verifies:

- whether the referenced work item actually authorises the PR;
- whether governance approval evidence substantively authorises a canonical transition;
- whether subjective design, product and commercial judgments are acceptable.
