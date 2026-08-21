#!/usr/bin/env python3
"""Failure-case tests for Phase 2 GitHub automation controls."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import validate_portfolio_transitions
import validate_pr_governance


ROOT = Path(__file__).resolve().parents[1]


def load_registry() -> dict:
    with (ROOT / "PORTFOLIO.yaml").open(encoding="utf-8") as file:
        return json.load(file)


def pr_event(body: str, head_repo: str = "takaven/product-portfolio", base_repo: str = "takaven/product-portfolio") -> dict:
    return {
        "pull_request": {
            "body": body,
            "head": {"repo": {"full_name": head_repo}},
            "base": {"ref": "main", "repo": {"full_name": base_repo}},
        }
    }


def governance_body(product_id: str = "N/A", issue: str = "Repository governance work") -> str:
    return f"""## Product ID

{product_id}

## Issue / Execution Gate

{issue}

## Review Classification

MATERIAL

## Final Endpoint

Stop after validation passes.

## What Changed

Updated automation and permissions checks.

## Why

Reduce manual governance administration.

## What Was Intentionally Not Changed

No product execution.

## Canonical Source Updated?

PORTFOLIO.yaml not changed.

## Governance Approval

decision:phase-2-automation
"""


def assert_pr_fails(name: str, event: dict, changed_files: list[str], expected: str) -> None:
    errors = validate_pr_governance.validate_pr(event, changed_files)
    if not any(expected in error for error in errors):
        raise AssertionError(f"{name} did not fail with {expected!r}. Errors: {errors}")


def assert_transition_fails(name: str, base: dict, head: dict, body: str, expected: str) -> None:
    errors = validate_portfolio_transitions.validate_transition(base, head, body)
    if not any(expected in error for error in errors):
        raise AssertionError(f"{name} did not fail with {expected!r}. Errors: {errors}")


def test_canonical_product_id_passes() -> None:
    errors = validate_pr_governance.validate_pr(
        pr_event(governance_body("TKV-003", "#42")),
        ["products/TKV-003-hirepass/README.md"],
    )
    if errors:
        raise AssertionError(f"canonical product ID should pass. Errors: {errors}")


def test_na_product_id_passes_for_governance_pr() -> None:
    errors = validate_pr_governance.validate_pr(
        pr_event(governance_body("N/A")),
        ["GITHUB-AUTOMATION.md"],
    )
    if errors:
        raise AssertionError(f"N/A product ID should pass for governance PR. Errors: {errors}")


def test_unknown_product_id_fails() -> None:
    assert_pr_fails(
        "unknown product ID",
        pr_event(governance_body("TKV-999", "#42")),
        ["products/TKV-999-fake/README.md"],
        "not recorded in canonical PORTFOLIO.yaml",
    )


def test_product_pr_requires_authorised_issue_reference() -> None:
    body = governance_body("TKV-003", "No issue reference here")
    assert_pr_fails(
        "product PR without work-item reference",
        pr_event(body),
        ["products/TKV-003-hirepass/README.md"],
        "work-item reference",
    )


def test_product_pr_rejects_malformed_work_item_reference() -> None:
    body = governance_body("TKV-003", "issue forty two")
    assert_pr_fails(
        "product PR with malformed work-item reference",
        pr_event(body),
        ["products/TKV-003-hirepass/README.md"],
        "work-item reference",
    )


def test_product_pr_cannot_change_other_product_folder() -> None:
    body = governance_body("TKV-003", "#42")
    assert_pr_fails(
        "product PR changes other product folder",
        pr_event(body),
        ["products/TKV-004-payrollflowengine/README.md"],
        "changes other product folders",
    )


def test_portfolio_change_requires_canonical_acknowledgement() -> None:
    body = governance_body("N/A").replace("PORTFOLIO.yaml not changed.", "")
    assert_pr_fails(
        "portfolio change without canonical acknowledgement",
        pr_event(body),
        ["PORTFOLIO.yaml"],
        "canonical source update",
    )


def test_workflow_change_requires_permissions_note() -> None:
    body = governance_body("N/A").replace("Updated automation and permissions checks.", "Updated automation checks.")
    assert_pr_fails(
        "workflow change without permissions note",
        pr_event(body),
        [".github/workflows/portfolio-validation.yml"],
        "permissions",
    )


def test_cross_repository_pr_rejected() -> None:
    body = governance_body("N/A")
    assert_pr_fails(
        "cross repository PR",
        pr_event(body, head_repo="someone/product-portfolio"),
        ["README.md"],
        "Cross-repository",
    )


def test_sensitive_transition_requires_governance_approval(base: dict) -> None:
    head = copy.deepcopy(base)
    product = next(item for item in head["products"] if item["id"] == "TKV-007")
    product["status"] = "SHORTLIST_BUILD"
    assert_transition_fails(
        "sensitive status transition without approval",
        base,
        head,
        governance_body("N/A").replace("decision:phase-2-automation", ""),
        "Governance Approval",
    )


def test_sensitive_transition_rejects_arbitrary_approval_prose(base: dict) -> None:
    head = copy.deepcopy(base)
    product = next(item for item in head["products"] if item["id"] == "TKV-007")
    product["status"] = "SHORTLIST_BUILD"
    assert_transition_fails(
        "sensitive status transition with arbitrary approval prose",
        base,
        head,
        governance_body("N/A").replace("decision:phase-2-automation", "I approve this myself"),
        "Governance Approval",
    )


def test_execution_ready_transition_requires_source_evidence(base: dict) -> None:
    head = copy.deepcopy(base)
    product = next(item for item in head["products"] if item["id"] == "TKV-003")
    product["execution_ready"] = True
    assert_transition_fails(
        "execution ready transition without source evidence",
        base,
        head,
        governance_body("TKV-003", "#42"),
        "execution_ready cannot become true",
    )


def test_sensitive_transition_with_governance_approval_passes(base: dict) -> None:
    head = copy.deepcopy(base)
    product = next(item for item in head["products"] if item["id"] == "TKV-004")
    product["condition_to_clear"] = "Founder chose independent Takaven control-layer product."
    errors = validate_portfolio_transitions.validate_transition(base, head, governance_body("N/A"))
    if errors:
        raise AssertionError(f"governance-approved sensitive transition should pass. Errors: {errors}")


def test_missing_base_portfolio_fails_closed(base: dict) -> None:
    errors = validate_portfolio_transitions.validate_transition(None, base, governance_body("N/A"))
    if not any("Base PORTFOLIO.yaml" in error for error in errors):
        raise AssertionError(f"missing base portfolio should fail closed. Errors: {errors}")


def test_pr_governance_happy_path() -> None:
    errors = validate_pr_governance.validate_pr(pr_event(governance_body("TKV-003", "#42")), ["products/TKV-003-hirepass/README.md"])
    if errors:
        raise AssertionError(f"valid product PR metadata should pass. Errors: {errors}")


def main() -> int:
    base = load_registry()
    tests_without_base = [
        test_canonical_product_id_passes,
        test_na_product_id_passes_for_governance_pr,
        test_unknown_product_id_fails,
        test_product_pr_requires_authorised_issue_reference,
        test_product_pr_rejects_malformed_work_item_reference,
        test_product_pr_cannot_change_other_product_folder,
        test_portfolio_change_requires_canonical_acknowledgement,
        test_workflow_change_requires_permissions_note,
        test_cross_repository_pr_rejected,
        test_pr_governance_happy_path,
    ]
    for test in tests_without_base:
        test()

    tests_with_base = [
        test_sensitive_transition_requires_governance_approval,
        test_sensitive_transition_rejects_arbitrary_approval_prose,
        test_execution_ready_transition_requires_source_evidence,
        test_sensitive_transition_with_governance_approval_passes,
        test_missing_base_portfolio_fails_closed,
    ]
    for test in tests_with_base:
        test(copy.deepcopy(base))

    print("Automation governance tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
