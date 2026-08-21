# Autonomous Agent Options

This repository may later use autonomous coding agents for bounded work. No autonomous agent integration is installed or configured by this document.

## Position

Autonomous agents are suitable for narrow, reviewable tasks once the source locator, issue scope, acceptance gate and validation checks are clear.

They are not suitable for:

- reopening product discovery;
- changing product boundaries;
- approving design gates;
- deciding commercial positioning;
- deploying products;
- modifying source repositories without an authorised execution issue.

## GitHub Copilot Coding Agent

Official documentation indicates GitHub Copilot coding agent can work from assigned issues, create branches and pull requests, and run in an ephemeral GitHub Actions-powered environment.

References:

- [About Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)
- [Use Copilot coding agent on GitHub](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-on-github)
- [Copilot coding agent access management](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/access-management)
- [Customise the Copilot coding agent environment](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment)

Suggested use here: later pilot on one low-risk repository-governance issue after this operating model is reviewed.

Do not enable broad automation from this repository until issue templates, CI and review flow have proven stable.

## OpenAI Codex Cloud

Official documentation indicates OpenAI Codex cloud runs coding tasks in isolated cloud environments, can be started from connected tools such as GitHub, and supports reviewing summaries/diffs before opening a pull request.

References:

- [Codex cloud tasks](https://learn.chatgpt.com/docs/cloud)
- [OpenAI Codex in GitHub](https://docs.github.com/en/copilot/concepts/agents/openai-codex)

Suggested use here: bounded implementation or audit tasks where a human can review the pull request before merge.

## Third-Party GitHub Agents

Third-party agents should not be added until this repository has a clear need that GitHub Copilot coding agent or OpenAI Codex cloud cannot cover.

Any third-party agent must be reviewed for repository permissions, data exposure, audit logs, branch behaviour and secret access before installation.

## Minimum Activation Criteria

Before any autonomous agent receives portfolio work:

- the issue has a finite final endpoint;
- `PORTFOLIO.yaml` identifies the product and gate;
- the source locator and revision are verified where source code is involved;
- the agent is limited to the authorised repository and files;
- CI validates generated views and governance checks;
- the pull request is human-reviewed before merge.
