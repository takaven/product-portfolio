#!/usr/bin/env python3
"""Validate the Takaven portfolio registry and governance files."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO_PATH = ROOT / "PORTFOLIO.yaml"
SCHEMA_PATH = ROOT / "schema" / "portfolio.schema.json"
REQUIRED_PRODUCT_FILES = {
    "README.md",
    "PRODUCT.md",
    "DESIGN.md",
    "SOURCES.md",
    "EXECUTION.md",
    "DECISIONS.md",
}
MANUAL_PRODUCT_FILES = {"DESIGN.md", "DECISIONS.md"}


def load_registry() -> dict:
    with PORTFOLIO_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def load_schema() -> dict:
    with SCHEMA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def product_folder(product: dict, root: Path = ROOT) -> Path:
    return root / "products" / f"{product['id']}-{product['slug']}"


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate_schema(data: dict, schema: dict | None = None) -> list[str]:
    schema = schema or load_schema()
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda error: list(error.path))
    return [
        f"schema {'/'.join(str(part) for part in error.path) or '<root>'}: {error.message}"
        for error in errors
    ]


def primary_source_ready(product: dict) -> bool:
    for source in product.get("source_assets", []):
        if source.get("role") != "PRIMARY":
            continue
        if source.get("locator_status") != "VERIFIED":
            continue
        if source.get("repository_url") and source.get("pinned_commit_sha"):
            return True
        if source.get("local_or_replit_locator") and source.get("pinned_commit_sha"):
            return True
        if source.get("local_or_replit_locator") and source.get("source_type") == "REPLIT_EXPORT_OR_LOCAL_ASSET":
            return True
    return False


def validate_cross_record_invariants(data: dict, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    products = data.get("products", [])
    ids = [product.get("id") for product in products]
    reserved_ids = {item.get("id") for item in data.get("portfolio", {}).get("reserved_product_ids", [])}

    if data.get("portfolio", {}).get("discovery_status") != "PORTFOLIO_DISCOVERY_CLOSED":
        fail("Portfolio discovery status must be PORTFOLIO_DISCOVERY_CLOSED.", errors)

    if len(ids) != len(set(ids)):
        fail("Product IDs must be unique.", errors)

    reused_reserved = sorted(set(ids).intersection(reserved_ids))
    if reused_reserved:
        fail(f"Reserved product IDs must not be reused: {', '.join(reused_reserved)}.", errors)

    products_dir = root / "products"
    canonical_folders = {f"{product['id']}-{product['slug']}" for product in products}
    if products_dir.exists():
        for folder in products_dir.iterdir():
            if folder.is_dir() and folder.name.startswith("TKV-") and folder.name not in canonical_folders:
                fail(f"Orphan product folder is not represented in PORTFOLIO.yaml: products/{folder.name}.", errors)

    for product in products:
        pid = product.get("id", "")
        status = product.get("status")

        if status == "ARCHIVE" and product.get("priority") != "HOLD":
            fail(f"{pid}: archived products must use HOLD priority.", errors)
        if product.get("execution_ready") is True and not primary_source_ready(product):
            fail(f"{pid}: execution-ready products require a verified primary source locator and revision.", errors)

        folder = product_folder(product, root)
        if not folder.exists():
            fail(f"{pid}: missing product folder {folder.relative_to(root)}.", errors)
            continue
        missing = sorted(file for file in REQUIRED_PRODUCT_FILES if not (folder / file).exists())
        if missing:
            fail(f"{pid}: missing product files: {', '.join(missing)}.", errors)
        for filename in MANUAL_PRODUCT_FILES:
            text = (folder / filename).read_text(encoding="utf-8")
            if "GENERATED FROM PORTFOLIO.yaml" in text:
                fail(f"{pid}: {filename} must be manually maintained, not generated.", errors)

    for component in data.get("components", []):
        if not component.get("destination_product", "").strip():
            fail(f"Component {component.get('name', '<missing>')}: missing destination_product.", errors)

    return errors


def validate_registry(data: dict, root: Path = ROOT) -> list[str]:
    return validate_schema(data) + validate_cross_record_invariants(data, root)


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
