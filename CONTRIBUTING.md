# Contributing

All changes should arrive through pull requests.

## Before Opening a Pull Request

- Confirm the change is authorised by a GitHub issue.
- Confirm the issue names the product ID and execution gate.
- Read `AGENTS.md`, `PORTFOLIO.yaml` and the relevant product folder.
- Keep sensitive data out of this repository.
- Regenerate `PORTFOLIO.md` if `PORTFOLIO.yaml` changed.
- Run:

```bash
python scripts/validate_portfolio.py
python scripts/generate_portfolio.py --check
python scripts/check_docs.py
```

## Scope Changes

Product status, priority, boundary, canonical source and archive/component state may not be changed through ordinary implementation work. Use the Portfolio Governance Change issue template.
