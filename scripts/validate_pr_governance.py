#!/usr/bin/env python3
"""Validate pull request governance metadata from the GitHub event payload."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCT_ID_RE = re.compile(r"\b(?:TKV-[0-9]{3}|N/A)\b", re.IGNORECASE)
ISSUE_REF_RE = re.compile(r"(?:#\d+|https://github\.com/[^/\s]+/[^/\s]+/issues/\d+)", re.IGNORECASE)
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
PRODUCT_FOLDER_RE = re.compile(r"^products/(TKV-[0-9]{3})-")
REQUIRED_SECTIONS = [
    "Product ID",
    "Issue / Execution Gate",
    "Final Endpoint",
    "What Changed",
    "What Was Intentionally Not Changed",
]


def load_event(path: Path) -> dict:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def section_body(markdown: str, heading: str) -> str:
    matches = list(SECTION_RE.finditer(markdown))
    for index, match in enumerate(matches):
        if match.group(1).strip().lower() != heading.lower():
            continue
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        return markdown[start:end].strip()
    return ""


def changed_files_from_git(base_ref: str) -> list[str]:
    subprocess.run(["git", "fetch", "--no-tags", "origin", base_ref], cwd=ROOT, check=True, stdout=subprocess.PIPE)
    result = subprocess.run(
        ["git", "diff", "--name-only", f"origin/{base_ref}...HEAD"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    return [line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()]


def validate_pr(event: dict, changed_files: list[str]) -> list[str]:
    pull_request = event.get("pull_request")
    if not pull_request:
        return []

    errors: list[str] = []
    body = pull_request.get("body") or ""
    head_repo = pull_request.get("head", {}).get("repo", {}).get("full_name")
    base_repo = pull_request.get("base", {}).get("repo", {}).get("full_name")

    if head_repo and base_repo and head_repo != base_repo:
        errors.append("Cross-repository pull requests are not authorised for portfolio automation.")

    missing = [heading for heading in REQUIRED_SECTIONS if not section_body(body, heading)]
    if missing:
        errors.append(f"PR body is missing required governance section content: {', '.join(missing)}.")

    product_section = section_body(body, "Product ID")
    product_match = PRODUCT_ID_RE.search(product_section)
    product_id = product_match.group(0).upper() if product_match else ""
    if not product_id:
        errors.append("PR Product ID must be a canonical TKV-000 value or N/A for repository-only governance work.")

    issue_section = section_body(body, "Issue / Execution Gate")
    if product_id and product_id != "N/A" and not ISSUE_REF_RE.search(issue_section):
        errors.append("Product-scoped PRs must reference the authorised GitHub issue in Issue / Execution Gate.")

    changed_product_ids = sorted(
        {match.group(1) for path in changed_files for match in [PRODUCT_FOLDER_RE.match(path)] if match}
    )
    if product_id.startswith("TKV-") and any(item != product_id for item in changed_product_ids):
        errors.append(
            f"Product-scoped PR {product_id} changes other product folders: {', '.join(changed_product_ids)}."
        )

    if "PORTFOLIO.yaml" in changed_files:
        canonical_section = section_body(body, "Canonical Source Updated?")
        if "PORTFOLIO.yaml" not in canonical_section:
            errors.append("PRs changing PORTFOLIO.yaml must explicitly acknowledge canonical source update.")

    if any(path.startswith(".github/workflows/") for path in changed_files):
        changed = section_body(body, "What Changed") + "\n" + section_body(body, "Why")
        if "permissions" not in changed.lower():
            errors.append("PRs changing GitHub workflows must mention permissions in What Changed or Why.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", type=Path, default=None, help="GitHub event JSON path.")
    parser.add_argument("--changed-files", nargs="*", default=None, help="Override changed file list for tests.")
    args = parser.parse_args()

    event_value = os.environ.get("GITHUB_EVENT_PATH", "")
    event_path = args.event or (Path(event_value) if event_value else None)
    if event_path is None:
        print("No GitHub event path supplied; skipping PR governance validation.")
        return 0

    event = load_event(event_path)
    if args.changed_files is not None:
        changed_files = args.changed_files
    else:
        base_ref = event.get("pull_request", {}).get("base", {}).get("ref", "main")
        changed_files = changed_files_from_git(base_ref)

    errors = validate_pr(event, [path.replace("\\", "/") for path in changed_files])
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("PR governance metadata validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
