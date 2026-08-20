#!/usr/bin/env python3
"""Generate human-readable portfolio views from PORTFOLIO.yaml."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO_PATH = ROOT / "PORTFOLIO.yaml"
OUTPUT_PATH = ROOT / "PORTFOLIO.md"


def load_registry() -> dict:
    with PORTFOLIO_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def row(values: list[str]) -> str:
    return "| " + " | ".join(value.replace("\n", " ") for value in values) + " |"


def render(data: dict) -> str:
    portfolio = data["portfolio"]
    products = data["products"]
    active = [p for p in products if p["priority"] in {"P0", "P1"}]
    queue = sorted(products, key=lambda p: p["priority"])

    lines: list[str] = [
        "<!-- GENERATED FROM PORTFOLIO.yaml. DO NOT EDIT DIRECTLY. -->",
        "",
        "# Takaven Product Portfolio",
        "",
        f"**Discovery status:** `{portfolio['discovery_status']}`",
        "",
        "Takaven is a software portfolio for revived and active products with bounded execution gates. This repository is the operating memory for portfolio decisions, source hierarchy, product boundaries and authorised next steps.",
        "",
        "## External Products",
        "",
    ]
    external_products = portfolio.get("external_products", [])
    if external_products:
        lines.extend(
            [
                row(["Product", "Relationship", "Governance Rule"]),
                row(["-------", "------------", "---------------"]),
            ]
        )
        for item in external_products:
            lines.append(row([item["name"], item["relationship"], item["governance_rule"]]))
        lines.append("")
    else:
        lines.extend(["No external products recorded.", ""])

    lines.extend(
        [
        "## Operating Principle",
        "",
        f"> {portfolio['operating_principle']}",
        "",
        "## Current Products",
        "",
        row(["ID", "Product", "Category", "Status", "Priority", "Execution Gate"]),
        row(["--", "-------", "--------", "------", "--------", "--------------"]),
        ]
    )
    for product in products:
        lines.append(
            row(
                [
                    product["id"],
                    product["name"],
                    product["category"],
                    f"`{product['status']}`",
                    f"`{product['priority']}`",
                    product["current_execution_gate"],
                ]
            )
        )

    lines.extend(
        [
            "",
            "## Active Queue",
            "",
            row(["Priority", "Products"]),
            row(["--------", "--------"]),
        ]
    )
    priorities = ["P0", "P1", "P2", "P3", "P2_MODULE", "P3_MODULE", "HOLD"]
    for priority in priorities:
        names = [p["name"] for p in queue if p["priority"] == priority]
        if names:
            lines.append(row([f"`{priority}`", ", ".join(names)]))

    lines.extend(
        [
            "",
            "## Components",
            "",
            row(["Component", "Destination", "Reuse Instruction"]),
            row(["---------", "-----------", "-----------------"]),
        ]
    )
    for component in data.get("components", []):
        lines.append(row([component["name"], component["destination_product"], component["reuse_instruction"]]))

    lines.extend(
        [
            "",
            "## New Product Policy",
            "",
            "Portfolio discovery is closed. New products may enter only when:",
            "",
        ]
    )
    for item in portfolio["new_product_policy"]:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## Where Agents Start",
            "",
            "1. Read `AGENTS.md`.",
            "2. Read `PORTFOLIO.yaml`.",
            "3. Read the relevant folder under `products/`.",
            "4. Read the active GitHub issue.",
            "5. Inspect actual source assets before execution.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated output is stale.")
    args = parser.parse_args()

    rendered = render(load_registry())
    if args.check:
        existing = OUTPUT_PATH.read_text(encoding="utf-8") if OUTPUT_PATH.exists() else ""
        if existing != rendered:
            print("PORTFOLIO.md is stale. Run scripts/generate_portfolio.py.", flush=True)
            return 1
        print("Generated portfolio view is current.")
        return 0

    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"Generated {OUTPUT_PATH.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
