#!/usr/bin/env python3
"""
Extract packages to test from uv.lock file based on config.json rules.

Usage: extract_packages_to_test.py <uv_lock_path> <config.json> <variables.sh> [previous_report_dir]

Extracts package names from uv.lock that match the regex patterns in config.json
and don't match exclude patterns, then outputs them to variables.sh.

If previous_report_dir is provided, packages with successful test results in that
report will be moved to done_packages instead of packages.
"""

import json
import re
import sys
from pathlib import Path


def package_matches(package_name: str, regexes: list[str]) -> bool:
    """Check if package name matches any of the given regex patterns."""
    for pattern in regexes:
        # Add anchors to ensure full string match
        full_pattern = f"^{pattern}$"
        if re.fullmatch(full_pattern, package_name):
            return True
    return False


def extract_packages_from_uv_lock(uv_lock_path: Path) -> list[str]:
    """Extract all package names from uv.lock file."""
    packages: list[str] = []

    with uv_lock_path.open("r") as f:
        for line in f:
            line = line.strip()
            if line.startswith('name = "'):
                # Extract package name from: name = "package-name"
                package_name = line[8:-1]  # Remove 'name = "' and trailing '"'
                packages.append(package_name)

    return packages


def filter_packages(packages: list[str], config_path: Path) -> list[str]:
    """Filter packages based on config.json rules."""

    # Load config
    with config_path.open("r") as f:
        config = json.load(f)

    filtered_packages: list[str] = []

    for package_name in packages:
        matched = False

        # Check each repository configuration
        for repo in config.get("repositories", []):
            package_regexes = repo.get("package-regexes", [])
            exclude_package_regexes = repo.get("exclude-package-regexes", [])

            # Check if package matches any include regex
            if not package_matches(package_name, package_regexes):
                continue

            # Check if package matches any exclude regex
            if package_matches(package_name, exclude_package_regexes):
                print(f"⏭️  Excluding {package_name} (matches exclude pattern)")
                matched = False
                break

            matched = True
            break

        if matched:
            filtered_packages.append(package_name)

    return filtered_packages


def check_previous_results(
    packages: list[str], previous_report_dir: Path | None
) -> tuple[list[str], list[str]]:
    """
    Split packages into those to test and those already done.

    Returns:
        Tuple of (packages_to_test, done_packages)
    """
    if not previous_report_dir or not previous_report_dir.exists():
        return packages, []

    packages_to_test: list[str] = []
    done_packages: list[str] = []

    for package in packages:
        summary_file = (
            previous_report_dir / "packages" / package / "result-summary.json"
        )

        if summary_file.exists():
            try:
                with summary_file.open("r") as f:
                    summary = json.load(f)

                # Check if tests were successful
                original = summary.get("original_tests_outcome")
                patched = summary.get("patched_tests_outcome")

                if patched is not None:
                    is_success = patched == "success"
                else:
                    is_success = original == "success"

                if is_success:
                    print(f"✓ {package} already passed in previous report")
                    done_packages.append(package)
                else:
                    packages_to_test.append(package)
            except (json.JSONDecodeError, KeyError) as e:
                print(f"⚠️  Could not read previous result for {package}: {e}")
                packages_to_test.append(package)
        else:
            packages_to_test.append(package)

    return packages_to_test, done_packages


def extract_packages(
    uv_lock_path: Path,
    config_path: Path,
    output_path: Path,
    previous_report_dir: Path | None = None,
) -> None:
    """Extract and filter packages, then write to variables.sh."""

    # Extract all packages from uv.lock
    all_packages = extract_packages_from_uv_lock(uv_lock_path)
    print(f"Found {len(all_packages)} packages in uv.lock")

    # Filter based on config
    filtered_packages = filter_packages(all_packages, config_path)
    print(f"Filtered to {len(filtered_packages)} packages")

    # Check previous results if provided
    packages_to_test, done_packages = check_previous_results(
        filtered_packages, previous_report_dir
    )

    # Sort for consistency
    packages_to_test.sort()
    done_packages.sort()

    # Write to variables.sh as JSON arrays
    packages_json = json.dumps(packages_to_test)
    done_packages_json = json.dumps(done_packages)

    with output_path.open("w") as f:
        f.write(f"packages='{packages_json}'\n")
        f.write(f"done_packages='{done_packages_json}'\n")

    print(f"\n✓ {len(packages_to_test)} packages to test")
    if packages_to_test:
        print(f"To test: {', '.join(packages_to_test)}")

    if done_packages:
        print(f"\n✓ {len(done_packages)} packages already completed")
        print(f"Done: {', '.join(done_packages)}")


if __name__ == "__main__":
    if len(sys.argv) not in (4, 5):
        print(
            "Usage: extract_packages_to_test.py <uv_lock_path> <config.json> <variables.sh> [previous_report_dir]",
            file=sys.stderr,
        )
        sys.exit(1)

    uv_lock_path = Path(sys.argv[1])
    config_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])
    previous_report_dir = Path(sys.argv[4]) if len(sys.argv) == 5 else None

    try:
        extract_packages(uv_lock_path, config_path, output_path, previous_report_dir)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
