#!/usr/bin/env python3
"""Generate the portfolio operating dashboard from PORTFOLIO.yaml."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO_PATH = ROOT / "PORTFOLIO.yaml"
OUTPUT_PATH = ROOT / "DASHBOARD.md"


def load_registry() -> dict:
    with PORTFOLIO_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def row(values: list[str]) -> str:
    return "| " + " | ".join(value.replace("\n", " ") for value in values) + " |"


def primary_source_status(product: dict) -> str:
    for source in product.get("source_assets", []):
        if source.get("role") == "PRIMARY":
            return f"{source.get('name', '-')}: `{source.get('locator_status', '-')}` / `{source.get('evidence_confidence', '-')}`"
    return "No primary source recorded"


def render(data: dict) -> str:
    portfolio = data["portfolio"]
    products = data["products"]
    independent = [p for p in products if p["status"] != "COMPONENT_ABSORB"]
    components = [p for p in products if p["status"] == "COMPONENT_ABSORB"]
    active_queue = [p for p in independent if p["priority"] != "HOLD"]
    blocked = [p for p in products if not p.get("execution_ready")]

    status_counts = Counter(p["status"] for p in products)
    source_counts = Counter(
        source["locator_status"]
        for product in products
        for source in product.get("source_assets", [])
    )

    lines: list[str] = [
        "<!-- GENERATED FROM PORTFOLIO.yaml. DO NOT EDIT DIRECTLY. -->",
        "",
        "# Takaven Portfolio Dashboard",
        "",
        "This generated dashboard is the operating snapshot for portfolio execution readiness.",
        "",
        "## Control Snapshot",
        "",
        row(["Control", "Value"]),
        row(["-------", "-----"]),
        row(["Discovery status", f"`{portfolio['discovery_status']}`"]),
        row(["Gate model", f"`{portfolio['gate_model']['model_version']}`"]),
        row(["Design system", f"`{portfolio['design_system']['current_version']}`"]),
        row(["No automatic next phase", f"`{str(portfolio['gate_model']['no_automatic_next_phase']).lower()}`"]),
        "",
        "## Active Execution Queue",
        "",
        row(["Priority", "ID", "Product", "Status", "Stage", "Execution Ready", "Current Gate"]),
        row(["--------", "--", "-------", "------", "-----", "---------------", "------------"]),
    ]
    for product in sorted(active_queue, key=lambda item: item["priority"]):
        lines.append(
            row(
                [
                    f"`{product['priority']}`",
                    product["id"],
                    product["name"],
                    f"`{product['status']}`",
                    f"`{product['lifecycle_stage']}`",
                    f"`{str(product.get('execution_ready', False)).lower()}`",
                    product["current_execution_gate"],
                ]
            )
        )

    lines.extend(
        [
            "",
            "## Source Locator Health",
            "",
            row(["ID", "Product", "Primary Source Status"]),
            row(["--", "-------", "---------------------"]),
        ]
    )
    for product in products:
        lines.append(row([product["id"], product["name"], primary_source_status(product)]))

    lines.extend(
        [
            "",
            "## Design Gate Status",
            "",
            row(["ID", "Product", "Design Stage", "Design System", "Visual Profile"]),
            row(["--", "-------", "------------", "-------------", "--------------"]),
        ]
    )
    for product in products:
        design = product["design_governance"]
        lines.append(
            row(
                [
                    product["id"],
                    product["name"],
                    f"`{design['design_stage']}`",
                    f"`{design['design_system_version']}`",
                    design["visual_profile_version"],
                ]
            )
        )

    lines.extend(
        [
            "",
            "## Retained Components",
            "",
            "These records are not independent execution workstreams.",
            "",
            row(["ID", "Component", "Destination", "Execution Gate"]),
            row(["--", "---------", "-----------", "--------------"]),
        ]
    )
    for product in components:
        lines.append(
            row(
                [
                    product["id"],
                    product["name"],
                    product.get("destination_product", ""),
                    product["current_execution_gate"],
                ]
            )
        )

    lines.extend(
        [
            "",
            "## Blocker Snapshot",
            "",
            row(["ID", "Product", "Blocking State"]),
            row(["--", "-------", "--------------"]),
        ]
    )
    for product in blocked:
        reason = product["current_execution_gate"]
        if product["status"] == "SHORTLIST_CONDITIONAL":
            reason = product.get("condition_to_clear") or reason
        lines.append(row([product["id"], product["name"], reason]))

    lines.extend(
        [
            "",
            "## Summary Counts",
            "",
            row(["Metric", "Result"]),
            row(["------", "-----:"]),
            row(["Product records", str(len(products))]),
            row(["Active queue records", str(len(active_queue))]),
            row(["Component records", str(len(components))]),
            row(["Execution blocked records", str(len(blocked))]),
        ]
    )
    for status, count in sorted(status_counts.items()):
        lines.append(row([f"Status `{status}`", str(count)]))
    for locator_status, count in sorted(source_counts.items()):
        lines.append(row([f"Source locator `{locator_status}`", str(count)]))

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated output is stale.")
    args = parser.parse_args()

    rendered = render(load_registry())
    if args.check:
        existing = OUTPUT_PATH.read_text(encoding="utf-8") if OUTPUT_PATH.exists() else ""
        if existing != rendered:
            print("DASHBOARD.md is stale. Run scripts/generate_dashboard.py.", flush=True)
            return 1
        print("Generated dashboard is current.")
        return 0

    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"Generated {OUTPUT_PATH.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
