#!/usr/bin/env python3
"""Validate DocuFlow configuration files and GitHub Actions security rules.

Checks performed:
  1. Required project files exist.
  2. YAML, JSON and TOML configuration files parse.
  3. Every page referenced in mkdocs.yml `nav` exists, and every page in docs/ is in `nav`.
  4. Workflows declare permissions, avoid pull_request_target and pin actions to commit SHAs.
  5. Issue forms contain the keys GitHub requires.

Usage: python scripts/check_config.py
Requires PyYAML (installed with MkDocs). Python 3.11+ is needed for tomllib.
"""

from __future__ import annotations

import json
import re
import sys
import tomllib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)
    print(f"  FAIL  {message}")


def ok(message: str) -> None:
    print(f"  ok    {message}")


class TolerantLoader(yaml.SafeLoader):
    """Load mkdocs.yml, which uses !ENV and !!python/name tags that SafeLoader rejects."""


def _ignore_tag(loader: yaml.Loader, tag_suffix: str, node: yaml.Node):
    if isinstance(node, yaml.ScalarNode):
        return loader.construct_scalar(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    return loader.construct_mapping(node)


TolerantLoader.add_multi_constructor("!", _ignore_tag)
TolerantLoader.add_multi_constructor("tag:yaml.org,2002:python/", _ignore_tag)


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.load(handle, Loader=TolerantLoader)  # noqa: S506 - loader is a SafeLoader subclass


REQUIRED_FILES = [
    "mkdocs.yml",
    "requirements.txt",
    ".markdownlint.json",
    "lychee.toml",
    ".gitignore",
    "LICENSE",
    "CONTRIBUTING.md",
    "README.md",
    "docs/index.md",
    "docs/assets/css/docuflow.css",
    "docs/assets/js/docuflow.js",
    ".github/workflows/docs-validation.yml",
    ".github/workflows/deploy-docs.yml",
    ".github/workflows/pr-quality.yml",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/documentation_request.yml",
    ".github/pull_request_template.md",
]


def check_required_files() -> None:
    print("Required files")
    missing = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    for name in missing:
        fail(f"missing {name}")
    if not missing:
        ok(f"all {len(REQUIRED_FILES)} required files exist")


def check_config_syntax() -> None:
    print("Configuration syntax")
    try:
        json.loads((ROOT / ".markdownlint.json").read_text(encoding="utf-8"))
        ok(".markdownlint.json is valid JSON")
    except (OSError, json.JSONDecodeError) as exc:
        fail(f".markdownlint.json: {exc}")
    try:
        tomllib.loads((ROOT / "lychee.toml").read_text(encoding="utf-8"))
        ok("lychee.toml is valid TOML")
    except (OSError, tomllib.TOMLDecodeError) as exc:
        fail(f"lychee.toml: {exc}")
    yaml_files = [ROOT / "mkdocs.yml", *sorted((ROOT / ".github").rglob("*.yml"))]
    for path in yaml_files:
        try:
            load_yaml(path)
            ok(f"{path.relative_to(ROOT)} is valid YAML")
        except (OSError, yaml.YAMLError) as exc:
            fail(f"{path.relative_to(ROOT)}: {exc}")


def nav_paths(node) -> list[str]:
    """Return every Markdown path referenced in the nav tree."""
    found: list[str] = []
    if isinstance(node, str):
        if node.endswith(".md"):
            found.append(node)
    elif isinstance(node, list):
        for item in node:
            found.extend(nav_paths(item))
    elif isinstance(node, dict):
        for value in node.values():
            found.extend(nav_paths(value))
    return found


def check_navigation() -> None:
    print("Navigation")
    config = load_yaml(ROOT / "mkdocs.yml")
    referenced = nav_paths(config.get("nav", []))
    if not referenced:
        fail("mkdocs.yml has no nav entries")
        return
    docs = ROOT / "docs"
    problems = 0
    for rel in referenced:
        if not (docs / rel).is_file():
            fail(f"nav points to missing file docs/{rel}")
            problems += 1
    on_disk = {p.relative_to(docs).as_posix() for p in docs.rglob("*.md")}
    for rel in sorted(on_disk - set(referenced)):
        fail(f"docs/{rel} exists but is not in nav")
        problems += 1
    duplicates = {rel for rel in referenced if referenced.count(rel) > 1}
    for rel in sorted(duplicates):
        fail(f"{rel} appears more than once in nav")
        problems += 1
    if not problems:
        ok(f"{len(referenced)} nav entries match the files in docs/")


SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")


def iter_steps(workflow: dict):
    for job_name, job in (workflow.get("jobs") or {}).items():
        for step in job.get("steps") or []:
            yield job_name, step
        if "uses" in job:  # reusable workflow call
            yield job_name, job


def check_workflows() -> None:
    print("Workflow security")
    for path in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
        name = path.relative_to(ROOT).as_posix()
        workflow = load_yaml(path)
        triggers = workflow.get("on", workflow.get(True))  # PyYAML reads the key `on` as True
        if not triggers:
            fail(f"{name}: no triggers defined")
        if isinstance(triggers, dict) and "pull_request_target" in triggers:
            fail(f"{name}: pull_request_target is not allowed")
        if "permissions" not in workflow:
            fail(f"{name}: top-level `permissions` is missing")
        pinned = 0
        for job_name, step in iter_steps(workflow):
            uses = step.get("uses")
            if not uses or uses.startswith("./"):
                continue
            _, _, ref = uses.partition("@")
            if SHA_PATTERN.match(ref):
                pinned += 1
            else:
                fail(f"{name}: job '{job_name}' uses '{uses}' without a full commit SHA")
        for job_name, job in (workflow.get("jobs") or {}).items():
            if "timeout-minutes" not in job:
                fail(f"{name}: job '{job_name}' has no timeout-minutes")
        if not [e for e in errors if e.startswith(name)]:
            ok(f"{name}: permissions set, {pinned} action(s) pinned, timeouts set")


def check_issue_forms() -> None:
    print("Issue forms")
    for path in sorted((ROOT / ".github" / "ISSUE_TEMPLATE").glob("*.yml")):
        form = load_yaml(path)
        name = path.relative_to(ROOT).as_posix()
        missing = [key for key in ("name", "description", "body") if key not in form]
        if missing:
            fail(f"{name}: missing keys {', '.join(missing)}")
            continue
        ids = [item.get("id") for item in form["body"] if item.get("id")]
        if len(ids) != len(set(ids)):
            fail(f"{name}: duplicate field ids")
        else:
            ok(f"{name}: {len(form['body'])} form elements")


def main() -> int:
    check_required_files()
    check_config_syntax()
    if not errors:
        check_navigation()
        check_workflows()
        check_issue_forms()
    print()
    if errors:
        print(f"{len(errors)} problem(s) found.")
        return 1
    print("Configuration checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
