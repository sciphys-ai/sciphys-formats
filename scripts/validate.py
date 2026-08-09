#!/usr/bin/env python3
"""Dependency-free checks for schemas and examples."""

from __future__ import annotations

import json
from pathlib import Path


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
                schemas[value["const"]] = path

for path in (ROOT / "examples").glob("*.json"):
    example = read(path)
    if not isinstance(example, dict):
        continue
    version = example.get("schemaVersion")
    if version not in schemas:
        errors.append(f"{path.relative_to(ROOT)}: no schema for {version}")
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
print(f"Validated {len(schemas)} schema identities and all examples.")
