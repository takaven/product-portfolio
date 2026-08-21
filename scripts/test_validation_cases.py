#!/usr/bin/env python3
"""Failure-case tests for portfolio governance validation."""

from __future__ import annotations

import copy
import json
import tempfile
from pathlib import Path

import generate_portfolio
import generate_dashboard
import generate_product_docs
import validate_portfolio


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PRODUCT_FILES = {
    "README.md",
    "PRODUCT.md",
    "DESIGN.md",
    "SOURCES.md",
    "EXECUTION.md",
    "DECISIONS.md",
}


def load_registry() -> dict:
    with (ROOT / "PORTFOLIO.yaml").open(encoding="utf-8") as file:
        return json.load(file)


def make_root(data: dict) -> Path:
    temp = Path(tempfile.mkdtemp())
    products_dir = temp / "products"
    products_dir.mkdir()
    for product in data["products"]:
        folder = products_dir / f"{product['id']}-{product['slug']}"
        folder.mkdir()
        for filename in REQUIRED_PRODUCT_FILES:
            (folder / filename).write_text(f"# {filename}\n", encoding="utf-8")
    return temp


def assert_fails(name: str, data: dict, expected: str, root: Path | None = None) -> None:
    errors = validate_portfolio.validate_registry(data, root or make_root(data))
    if not any(expected in error for error in errors):
        raise AssertionError(f"{name} did not fail with {expected!r}. Errors: {errors}")


def test_invalid_status(base: dict) -> None:
    data = copy.deepcopy(base)
    data["products"][0]["status"] = "BAD_STATUS"
    assert_fails("invalid status", data, "BAD_STATUS")


def test_conditional_without_condition(base: dict) -> None:
    data = copy.deepcopy(base)
    product = next(item for item in data["products"] if item["status"] == "SHORTLIST_CONDITIONAL")
    product["condition_to_clear"] = ""
    assert_fails("conditional with empty condition", data, "condition_to_clear")

    data = copy.deepcopy(base)
    product = next(item for item in data["products"] if item["status"] == "SHORTLIST_CONDITIONAL")
    del product["condition_to_clear"]
    assert_fails("conditional with omitted condition", data, "condition_to_clear")


def test_component_without_destination(base: dict) -> None:
    data = copy.deepcopy(base)
    product = next(item for item in data["products"] if item["status"] == "COMPONENT_ABSORB")
    product["destination_product"] = ""
    assert_fails("component with empty destination", data, "destination_product")

    data = copy.deepcopy(base)
    product = next(item for item in data["products"] if item["status"] == "COMPONENT_ABSORB")
    del product["destination_product"]
    assert_fails("component with omitted destination", data, "destination_product")


def test_orphan_product_folder(base: dict) -> None:
    data = copy.deepcopy(base)
    root = make_root(data)
    orphan = root / "products" / "TKV-999-orphan"
    orphan.mkdir()
    for filename in REQUIRED_PRODUCT_FILES:
        (orphan / filename).write_text("# orphan\n", encoding="utf-8")
    assert_fails("orphan product folder", data, "Orphan product folder", root)


def test_duplicate_or_reused_permanent_id(base: dict) -> None:
    data = copy.deepcopy(base)
    data["products"][0]["id"] = "TKV-001"
    assert_fails("reserved ID", data, "Reserved product IDs")

    data = copy.deepcopy(base)
    data["products"][1]["id"] = data["products"][0]["id"]
    assert_fails("duplicate ID", data, "Product IDs must be unique")


def test_execution_ready_without_source_locator(base: dict) -> None:
    data = copy.deepcopy(base)
    product = next(item for item in data["products"] if item["id"] == "TKV-003")
    product["execution_ready"] = True
    assert_fails("execution-ready without locator", data, "verified primary source locator")


def test_execution_ready_local_source_requires_pinned_revision(base: dict) -> None:
    data = copy.deepcopy(base)
    product = next(item for item in data["products"] if item["id"] == "TKV-003")
    source = next(item for item in product["source_assets"] if item["role"] == "PRIMARY")
    product["execution_ready"] = True
    source["source_type"] = "REPLIT_EXPORT_OR_LOCAL_ASSET"
    source["locator_status"] = "VERIFIED"
    source["evidence_confidence"] = "VERIFIED"
    source["local_or_replit_locator"] = "C:/verified/local/Talent-Flow"
    source["repository_url"] = ""
    source["pinned_commit_sha"] = ""
    assert_fails("execution-ready local source without pinned revision", data, "verified primary source locator")


def test_execution_ready_local_source_with_pinned_revision_passes(base: dict) -> None:
    data = copy.deepcopy(base)
    product = next(item for item in data["products"] if item["id"] == "TKV-003")
    source = next(item for item in product["source_assets"] if item["role"] == "PRIMARY")
    product["execution_ready"] = True
    source["source_type"] = "REPLIT_EXPORT_OR_LOCAL_ASSET"
    source["locator_status"] = "VERIFIED"
    source["evidence_confidence"] = "VERIFIED"
    source["local_or_replit_locator"] = "C:/verified/local/Talent-Flow"
    source["repository_url"] = ""
    source["pinned_commit_sha"] = "sha256:example-local-export-hash"
    errors = validate_portfolio.validate_registry(data, make_root(data))
    if errors:
        raise AssertionError(f"execution-ready local source with pinned revision should pass. Errors: {errors}")


def test_design_system_version_must_match(base: dict) -> None:
    data = copy.deepcopy(base)
    data["products"][0]["design_governance"]["design_system_version"] = "unknown-design-system"
    assert_fails("unknown design-system version", data, "current portfolio design system version")


def test_design_gate_progression_requires_references(base: dict) -> None:
    data = copy.deepcopy(base)
    product = next(item for item in data["products"] if item["status"] != "COMPONENT_ABSORB")
    product["design_governance"]["design_stage"] = "D4_AUTHORISED"
    assert_fails("D4 without prior design approvals", data, "approved D1 reference")


def test_component_design_stage_not_applicable(base: dict) -> None:
    data = copy.deepcopy(base)
    product = next(item for item in data["products"] if item["status"] == "COMPONENT_ABSORB")
    product["design_governance"]["design_stage"] = "NOT_STARTED"
    assert_fails("component with active design stage", data, "NOT_APPLICABLE")


def test_stale_generated_portfolio(base: dict) -> None:
    rendered = generate_portfolio.render(base)
    if rendered == "# stale\n":
        raise AssertionError("stale portfolio fixture unexpectedly matched generated output")


def test_stale_generated_dashboard(base: dict) -> None:
    rendered = generate_dashboard.render(base)
    if rendered == "# stale\n":
        raise AssertionError("stale dashboard fixture unexpectedly matched generated output")


def test_active_queue_excludes_hold_and_components(base: dict) -> None:
    rendered = generate_dashboard.render(base)
    active_queue = rendered.split("## Active Execution Queue", 1)[1].split("## Source Locator Health", 1)[0]
    if "TKV-005" in active_queue or "TKV-006" in active_queue or "TKV-007" in active_queue:
        raise AssertionError("Active execution queue must exclude component and HOLD records.")


def test_design_and_decisions_not_generated() -> None:
    forbidden = {"DESIGN.md", "DECISIONS.md"}
    generated = set(generate_product_docs.DOCS)
    overlap = forbidden.intersection(generated)
    if overlap:
        raise AssertionError(f"Manual docs must not be generated: {sorted(overlap)}")


def main() -> int:
    base = load_registry()
    tests = [
        test_invalid_status,
        test_conditional_without_condition,
        test_component_without_destination,
        test_orphan_product_folder,
        test_duplicate_or_reused_permanent_id,
        test_execution_ready_without_source_locator,
        test_execution_ready_local_source_requires_pinned_revision,
        test_execution_ready_local_source_with_pinned_revision_passes,
        test_design_system_version_must_match,
        test_design_gate_progression_requires_references,
        test_component_design_stage_not_applicable,
        test_stale_generated_portfolio,
        test_stale_generated_dashboard,
        test_active_queue_excludes_hold_and_components,
    ]
    for test in tests:
        test(copy.deepcopy(base))
    test_design_and_decisions_not_generated()
    print("Validation failure-case tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
