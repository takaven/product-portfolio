#!/usr/bin/env python3
"""Validate deterministic PORTFOLIO.yaml transitions between base and head.

This validates approval-reference presence. Human review validates whether the
referenced evidence actually authorises the canonical transition.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import validate_portfolio


ROOT = Path(__file__).resolve().parents[1]
SENSITIVE_PRODUCT_FIELDS = {
    "status",
    "priority",
    "lifecycle_stage",
    "product_boundary",
    "exclusions",
    "destination_product",
    "condition_to_clear",
    "current_execution_gate",
    "execution_ready",
}
SENSITIVE_DESIGN_FIELDS = {"design_stage"}
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
APPROVAL_REF_RE = re.compile(
    r"(?:#\d+|https://github\.com/[^/\s]+/[^/\s]+/(?:issues|pull)/\d+|"
    r"(?:^|\s)(?:DECISION-LOG\.md|DECISIONS\.md|products/TKV-[0-9]{3}-[^/\s]+/DECISIONS\.md)"
    r"(?:$|\s|#)|decision:[A-Za-z0-9._/-]+)",
    re.IGNORECASE,
)
PRODUCT_ID_RE = re.compile(r"\bTKV-[0-9]{3}\b", re.IGNORECASE)


def section_body(markdown: str, heading: str) -> str:
    matches = list(SECTION_RE.finditer(markdown))
    for index, match in enumerate(matches):
        if match.group(1).strip().lower() != heading.lower():
            continue
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        return markdown[start:end].strip()
    return ""


def git_show(ref: str, path: str) -> str | None:
    result = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout


def load_json_text(text: str | None) -> dict | None:
    if text is None:
        return None
    return json.loads(text)


def load_event_body(event_path: Path | None) -> str:
    if event_path is None:
        return ""
    with event_path.open(encoding="utf-8") as file:
        event = json.load(file)
    return event.get("pull_request", {}).get("body") or ""


def product_map(data: dict) -> dict[str, dict]:
    return {product["id"]: product for product in data.get("products", [])}


def sensitive_changes(base: dict, head: dict) -> list[str]:
    changes: list[str] = []
    base_products = product_map(base)
    head_products = product_map(head)

    removed = sorted(set(base_products) - set(head_products))
    if removed:
        changes.append(f"removed product records: {', '.join(removed)}")

    added = sorted(set(head_products) - set(base_products))
    if added:
        changes.append(f"added product records: {', '.join(added)}")

    for pid in sorted(set(base_products).intersection(head_products)):
        old = base_products[pid]
        new = head_products[pid]
        for field in sorted(SENSITIVE_PRODUCT_FIELDS):
            if old.get(field) != new.get(field):
                changes.append(f"{pid}: changed {field}")

        old_design = old.get("design_governance", {})
        new_design = new.get("design_governance", {})
        for field in sorted(SENSITIVE_DESIGN_FIELDS):
            if old_design.get(field) != new_design.get(field):
                changes.append(f"{pid}: changed design_governance.{field}")

    return changes


def changed_product_ids(changes: list[str]) -> set[str]:
    return {match.group(0).upper() for change in changes for match in [PRODUCT_ID_RE.search(change)] if match}


def hard_transition_errors(base: dict, head: dict) -> list[str]:
    errors: list[str] = []
    base_products = product_map(base)
    head_products = product_map(head)

    removed = sorted(set(base_products) - set(head_products))
    if removed:
        errors.append(f"Product records must not be removed by automation: {', '.join(removed)}.")

    for pid in sorted(set(base_products).intersection(head_products)):
        old = base_products[pid]
        new = head_products[pid]
        if old.get("execution_ready") is not True and new.get("execution_ready") is True:
            if not validate_portfolio.primary_source_ready(new):
                errors.append(f"{pid}: execution_ready cannot become true without verified primary source locator and pinned revision.")

    return errors


def validate_transition(base: dict | None, head: dict, pr_body: str = "") -> list[str]:
    if base is None:
        return ["Base PORTFOLIO.yaml could not be loaded; transition validation must fail closed."]

    errors = hard_transition_errors(base, head)
    changes = sensitive_changes(base, head)
    if changes:
        declared_product = PRODUCT_ID_RE.search(section_body(pr_body, "Product ID"))
        declared_product_id = declared_product.group(0).upper() if declared_product else ""
        changed_products = changed_product_ids(changes)
        if declared_product_id and any(product_id != declared_product_id for product_id in changed_products):
            errors.append(
                f"Product-scoped PR {declared_product_id} changes canonical state for other products: "
                + ", ".join(sorted(changed_products))
                + "."
            )

        approval = section_body(pr_body, "Governance Approval")
        if not approval or approval.upper() in {"N/A", "NONE"} or not APPROVAL_REF_RE.search(approval):
            errors.append(
                "Sensitive PORTFOLIO.yaml transitions require a concrete Governance Approval reference "
                "(GitHub issue/PR, decision-log reference, product DECISIONS.md reference, or decision:<id>): "
                + "; ".join(changes)
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", default="origin/main")
    parser.add_argument("--head-ref", default="HEAD")
    parser.add_argument("--base-file", type=Path)
    parser.add_argument("--head-file", type=Path)
    parser.add_argument("--event", type=Path)
    args = parser.parse_args()

    if args.base_file:
        try:
            base = json.loads(args.base_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            print(f"ERROR: Base PORTFOLIO.yaml could not be loaded: {error}", file=sys.stderr)
            return 1
    else:
        try:
            base = load_json_text(git_show(args.base_ref, "PORTFOLIO.yaml"))
        except json.JSONDecodeError as error:
            print(f"ERROR: Base PORTFOLIO.yaml could not be parsed: {error}", file=sys.stderr)
            return 1
        if base is None:
            print("ERROR: Base PORTFOLIO.yaml could not be loaded; transition validation must fail closed.", file=sys.stderr)
            return 1

    if args.head_file:
        head = json.loads(args.head_file.read_text(encoding="utf-8"))
    else:
        head = load_json_text(git_show(args.head_ref, "PORTFOLIO.yaml"))
        if head is None:
            print("PORTFOLIO.yaml not found at head; skipping transition validation.")
            return 0

    event_value = os.environ.get("GITHUB_EVENT_PATH", "")
    event_path = args.event or (Path(event_value) if event_value else None)
    errors = validate_transition(base, head, load_event_body(event_path))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Portfolio transition validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
