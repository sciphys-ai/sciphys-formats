#!/usr/bin/env python3
"""Validate SciPhys examples against their JSON Schemas and graph invariants."""

from __future__ import annotations

import json
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as error:
    raise SystemExit("Install validation dependencies with: python -m pip install -r requirements-dev.txt") from error


ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def read(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{path.relative_to(ROOT)}: {error}")
        return None


schemas = {}
for path in (ROOT / "schemas").glob("*.json"):
    schema = read(path)
    if isinstance(schema, dict):
        if "$id" not in schema or "$schema" not in schema:
            errors.append(f"{path.relative_to(ROOT)}: missing $id or $schema")
        for value in schema.get("properties", {}).values():
            if isinstance(value, dict) and "const" in value:
                schemas[value["const"]] = (path, schema)

for path in (ROOT / "examples").glob("*.json"):
    example = read(path)
    if not isinstance(example, dict):
        continue
    version = example.get("schemaVersion")
    if version not in schemas:
        errors.append(f"{path.relative_to(ROOT)}: no schema for {version}")
    else:
        _, schema = schemas[version]
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for error in sorted(validator.iter_errors(example), key=lambda item: list(item.absolute_path)):
            location = ".".join(str(part) for part in error.absolute_path) or "$"
            errors.append(f"{path.relative_to(ROOT)}:{location}: {error.message}")
    if version == "sciphys.evidence-bundle.v0.1":
        node_ids = {node.get("id") for node in example.get("nodes", [])}
        for edge in example.get("edges", []):
            if edge.get("from") not in node_ids or edge.get("to") not in node_ids:
                errors.append(f"{path.relative_to(ROOT)}: dangling edge")
        for claim in example.get("claims", []):
            if not claim.get("evidenceRefs") or not set(claim["evidenceRefs"]).issubset(node_ids):
                errors.append(f"{path.relative_to(ROOT)}: dangling or empty claim evidence")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)
print(f"Validated {len(schemas)} JSON Schemas and all examples.")
