#!/usr/bin/env python3
"""Generate product orientation documents from PORTFOLIO.yaml."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO_PATH = ROOT / "PORTFOLIO.yaml"
PRODUCTS_DIR = ROOT / "products"


def load_registry() -> dict:
    with PORTFOLIO_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def product_dir(product: dict) -> Path:
    return PRODUCTS_DIR / f"{product['id']}-{product['slug']}"


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- None recorded."


def component_warning(product: dict) -> str:
    if product["status"] != "COMPONENT_ABSORB":
        return ""
    return (
        "\n## Component Warning\n\n"
        "This is a retained component/module record, not an independent product workstream. "
        "Do not create standalone execution issues unless a Portfolio Governance Change updates the canonical registry.\n"
    )


def readme(product: dict) -> str:
    return f"""<!-- GENERATED FROM PORTFOLIO.yaml. DO NOT EDIT STRUCTURED STATE DIRECTLY. -->
# {product['id']} - {product['name']}

{product['product_promise']}

## Orientation

- Category: `{product['category']}`
- Status: `{product['status']}`
- Priority: `{product['priority']}`
- Lifecycle stage: `{product['lifecycle_stage']}`
- Current execution gate: {product['current_execution_gate']}
- Evidence confidence: `{product['evidence_confidence']}`

## Important Warning

Canonical state lives in `../../PORTFOLIO.yaml`. If this folder and the registry disagree, stop and report the conflict.
{component_warning(product)}
## Start Here

1. Read `../../AGENTS.md`.
2. Read `../../PORTFOLIO.yaml`.
3. Read this folder's product documents.
4. Read the authorised GitHub issue.
5. Inspect actual source assets before execution.
"""


def product_md(product: dict) -> str:
    return f"""# Product Definition

Canonical state lives in `../../PORTFOLIO.yaml`.

## Promise

{product['product_promise']}

## Buyer

{product['primary_buyer']}

## Problem

{product['problem']}

## Product Boundary

{bullet(product['product_boundary'])}

## Explicit Exclusions

{bullet(product['exclusions'])}

## Relationship To TeamFrame

{product['teamframe_relationship']}

## Remarks

{product['important_remarks']}
"""


def design_md(product: dict) -> str:
    return f"""# Design Notes

Use `../../DESIGN-SYSTEM.md` as the portfolio-level design governance source.

## Product Direction

{product['name']} should follow its product boundary and avoid borrowing patterns that imply excluded scope.

## Frontend Gate Rule

No full frontend rollout before D1-D3 are approved.

## Current State

No final product design is created by this operating-repository setup.
"""


def sources_md(product: dict) -> str:
    lines = [
        "# Source Assets",
        "",
        "This file records safe source metadata only. Do not copy source code, real records, uploads, secrets or raw audit exports into this repository.",
        "",
        "| Source | Classification | Confidence | Remarks |",
        "| ------ | -------------- | ---------- | ------- |",
    ]
    for source in product["source_assets"]:
        lines.append(
            f"| {source['name']} | {source['classification']} | `{source['evidence_confidence']}` | {source['remarks']} |"
        )
    if product.get("source_repository_links"):
        lines.extend(["", "## Repository Links", ""])
        for link in product["source_repository_links"]:
            lines.append(f"- {link}")
    else:
        lines.extend(["", "## Repository Links", "", "No safe verified repository links recorded during setup."])
    return "\n".join(lines) + "\n"


def execution_md(product: dict) -> str:
    return f"""# Execution

Canonical execution state lives in `../../PORTFOLIO.yaml`.

## Current Gate

{product['current_execution_gate']}

## Condition To Clear

{product.get('condition_to_clear') or 'None.'}

## Destination Product

{product.get('destination_product') or 'Not applicable.'}

## Prohibited During Unauthorised Work

- Do not modify product source repositories.
- Do not change product boundary.
- Do not create execution issues unless explicitly authorised.
- Do not copy sensitive data into this repository.
"""


def decisions_md(product: dict) -> str:
    return f"""# Decisions

Append only material decisions for {product['name']}.

## 2026-08-20 - Initial Portfolio Record

- Status: `{product['status']}`
- Priority: `{product['priority']}`
- Current execution gate: {product['current_execution_gate']}
- Evidence confidence: `{product['evidence_confidence']}`
"""


DOCS = {
    "README.md": readme,
    "PRODUCT.md": product_md,
    "DESIGN.md": design_md,
    "SOURCES.md": sources_md,
    "EXECUTION.md": execution_md,
    "DECISIONS.md": decisions_md,
}


def generate(check: bool) -> int:
    data = load_registry()
    stale: list[str] = []
    for product in data["products"]:
        folder = product_dir(product)
        folder.mkdir(parents=True, exist_ok=True)
        for filename, renderer in DOCS.items():
            path = folder / filename
            rendered = renderer(product)
            if check:
                existing = path.read_text(encoding="utf-8") if path.exists() else ""
                if existing != rendered:
                    stale.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(rendered, encoding="utf-8", newline="\n")

    if stale:
        print("Product docs are stale:")
        for item in stale:
            print(f"- {item}")
        return 1
    print("Product docs are current." if check else "Generated product docs.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    return generate(parser.parse_args().check)


if __name__ == "__main__":
    raise SystemExit(main())
