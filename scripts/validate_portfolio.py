#!/usr/bin/env python3
"""Validate the Takaven portfolio registry and governance files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO_PATH = ROOT / "PORTFOLIO.yaml"

STATUSES = {
    "EXISTING_CORE",
    "REVIVAL_IN_PROGRESS",
    "SHORTLIST_BUILD",
    "SHORTLIST_CONDITIONAL",
    "COMPONENT_ABSORB",
    "HOLD",
    "ARCHIVE",
}
PRIORITIES = {"P0", "P1", "P2", "P3", "P2_MODULE", "P3_MODULE", "HOLD"}
STAGES = {
    "STAGE_0_ASSET_IDENTIFIED",
    "STAGE_1_PRODUCT_DEFINITION",
    "STAGE_2_BUILD_COMPLETION",
    "STAGE_3_PRODUCTION_HARDENING",
    "STAGE_4_MARKET_READY_PREPARATION",
    "STAGE_5_READY_TO_LAUNCH",
}
CONFIDENCE = {"VERIFIED", "INFERRED", "UNVERIFIED"}
REQUIRED_PRODUCT_FILES = {
    "README.md",
    "PRODUCT.md",
    "DESIGN.md",
    "SOURCES.md",
    "EXECUTION.md",
    "DECISIONS.md",
}


def load_registry() -> dict:
    with PORTFOLIO_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def product_folder(product: dict) -> Path:
    return ROOT / "products" / f"{product['id']}-{product['slug']}"


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate_registry(data: dict) -> list[str]:
    errors: list[str] = []
    products = data.get("products", [])
    ids = [product.get("id") for product in products]

    if data.get("portfolio", {}).get("discovery_status") != "PORTFOLIO_DISCOVERY_CLOSED":
        fail("Portfolio discovery status must be PORTFOLIO_DISCOVERY_CLOSED.", errors)

    if len(ids) != len(set(ids)):
        fail("Product IDs must be unique.", errors)

    for product in products:
        pid = product.get("id", "")
        status = product.get("status")
        priority = product.get("priority")
        stage = product.get("lifecycle_stage")

        if not re.fullmatch(r"TKV-[0-9]{3}", pid):
            fail(f"{pid or '<missing>'}: invalid product ID.", errors)
        if status not in STATUSES:
            fail(f"{pid}: invalid status {status!r}.", errors)
        if priority not in PRIORITIES:
            fail(f"{pid}: invalid priority {priority!r}.", errors)
        if stage not in STAGES:
            fail(f"{pid}: invalid lifecycle stage {stage!r}.", errors)
        if product.get("evidence_confidence") not in CONFIDENCE:
            fail(f"{pid}: invalid evidence confidence.", errors)
        if status == "SHORTLIST_CONDITIONAL" and not product.get("condition_to_clear", "").strip():
            fail(f"{pid}: conditional products require condition_to_clear.", errors)
        if status == "COMPONENT_ABSORB" and not product.get("destination_product", "").strip():
            fail(f"{pid}: component products require destination_product.", errors)
        if status == "ARCHIVE" and priority != "HOLD":
            fail(f"{pid}: archived products must use HOLD priority.", errors)

        folder = product_folder(product)
        if not folder.exists():
            fail(f"{pid}: missing product folder {folder.relative_to(ROOT)}.", errors)
            continue
        missing = sorted(file for file in REQUIRED_PRODUCT_FILES if not (folder / file).exists())
        if missing:
            fail(f"{pid}: missing product files: {', '.join(missing)}.", errors)

    for component in data.get("components", []):
        if not component.get("destination_product", "").strip():
            fail(f"Component {component.get('name', '<missing>')}: missing destination_product.", errors)

    return errors


def main() -> int:
    errors = validate_registry(load_registry())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Portfolio validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
