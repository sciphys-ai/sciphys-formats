# Contributing to SciPhys Formats

Open an issue or RFC before changing a shared field's meaning. A schema pull request should include the scientific use case, schema changes, valid and invalid examples, compatibility impact, migration notes, and the source format or ontology being mapped.

Run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

Do not add private lab metadata or third-party files without explicit redistribution rights. Hash or omit instrument serial numbers and personal identifiers. Synthetic examples must be labeled synthetic and name their generator.

Reviewers assess semantic correctness separately from JSON Schema validity. A file passing validation does not prove that units, calibration, or scientific meaning are correct.
