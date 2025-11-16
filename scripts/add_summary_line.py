#!/usr/bin/env python3
"""
Add a new summary line to reports.md after the table header.

Usage: add_summary_line.py <reports_md_path> <patches_json_path> <test_name> <report_dir> <status>

Inserts a new row into the reports table after the separator line.
The report_dir should be the directory name (e.g., "2025-11-15_20-49-34").
The test_name is an optional description of the test run.
The patches_json_path is used to extract the list of tested patches.
"""

import json
import re
import sys
from pathlib import Path


def get_tested_patches(patches_json_path: Path) -> str:
    """Get comma-separated list of patch names from patches.json."""
    if not patches_json_path.exists():
        return ""

    try:
        with patches_json_path.open("r", encoding="utf-8") as f:
            patches = json.load(f)

        # Get the keys (package names) as comma-separated list
        patch_names = list(patches.keys())
        return ", ".join(sorted(patch_names)) if patch_names else ""
    except Exception as e:
        print(f"Warning: Could not read patches.json: {e}", file=sys.stderr)
        return ""


def add_summary_line(
    reports_md_path: Path,
    patches_json_path: Path,
    test_name: str,
    report_dir: str,
    status: str,
) -> None:
    """Add a new summary line to reports.md."""

    if not reports_md_path.exists():
        print(f"Error: {reports_md_path} does not exist", file=sys.stderr)
        sys.exit(1)

    # Read the file
    with reports_md_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find the table separator line using regex
    # Matches lines like |---|---| or |-----|------|
    separator_pattern = re.compile(r"^\|[\|\-]+\|$")
    separator_index = None

    for i, line in enumerate(lines):
        if separator_pattern.match(line):
            separator_index = i
            break

    if separator_index is None:
        print("Error: Could not find table separator line", file=sys.stderr)
        sys.exit(1)

    # Create markdown link from report directory name
    # Convert underscores to spaces for display
    display_name = report_dir.replace("_", " ")
    report_link = f"[{display_name}](./results/{report_dir}/report.md)"

    # Use test_name if provided, otherwise use empty string
    test_name_display = test_name if test_name else ""

    # Get tested patches
    patches_tested = get_tested_patches(patches_json_path)

    # Create new row with test name, report link, status, and patches tested
    new_row = f"| {test_name_display} | {report_link} | {status} | {patches_tested} |\n"

    # Insert after separator
    lines.insert(separator_index + 1, new_row)

    # Write back
    with reports_md_path.open("w", encoding="utf-8") as f:
        f.writelines(lines)


def main() -> None:
    """Main entry point."""
    if len(sys.argv) != 6:
        print(
            "Usage: add_summary_line.py <reports_md_path> <patches_json_path> <test_name> <report_dir> <status>",
            file=sys.stderr,
        )
        sys.exit(1)

    reports_md_path = Path(sys.argv[1])
    patches_json_path = Path(sys.argv[2])
    test_name = sys.argv[3]
    report_dir = sys.argv[4]
    status = sys.argv[5]

    try:
        add_summary_line(
            reports_md_path, patches_json_path, test_name, report_dir, status
        )
        print(f"✓ Updated {reports_md_path}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
