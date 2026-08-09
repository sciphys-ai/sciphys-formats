# SciPhys Formats

[![Validate schemas](https://github.com/sciphys-ai/sciphys-formats/actions/workflows/validate.yml/badge.svg)](https://github.com/sciphys-ai/sciphys-formats/actions/workflows/validate.yml)

Versioned, vendor-neutral contracts for experimental measurements and scientific evidence.

SciPhys Formats lets instruments, analysis tools, agents, notebooks, archives, and hosted products exchange data without sharing an implementation. It complements established scientific formats: original bytes remain authoritative while SciPhys records portable metadata, provenance, results, claims, and review.

## Contracts

| Contract | Status | Purpose |
|---|---|---|
| [`sciphysdata.v0.schema.json`](schemas/sciphysdata.v0.schema.json) | legacy draft | Early measurement envelope; retained for compatibility |
| [`measurement.v0.1.schema.json`](schemas/measurement.v0.1.schema.json) | experimental | Vendor-neutral sample, instrument, acquisition, and raw-file metadata |
| [`evidence-bundle.v0.1.schema.json`](schemas/evidence-bundle.v0.1.schema.json) | experimental | Provenance graph, scientific claims, artifacts, and expert review |

Examples under [`examples/`](examples/) are CI-checked for schema identity and referential integrity. Experimental schemas may change through RFCs; stable schemas follow the compatibility rules in [VERSIONING.md](VERSIONING.md).

## Design rules

- Preserve original instrument files and hash them with SHA-256.
- Keep acquisition metadata separate from analysis outputs.
- Represent quantities with explicit values and units.
- Separate observations, derived results, interpretations, and hypotheses.
- Link every scientific claim to evidence nodes.
- Record processes, parameters, implementations, versions, and review decisions.
- Put unmapped vendor metadata in namespaced extensions instead of discarding it.
- Never imply that a confidence number alone establishes scientific validity.

## Ecosystem

- [sciphys-os](https://github.com/sciphys-ai/sciphys-os) implements the runtime and agent Skills.
- [sciphys-bench](https://github.com/sciphys-ai/sciphys-bench) uses versioned contracts for evaluation artifacts.
- [sciphys-recipes](https://github.com/sciphys-ai/sciphys-recipes) demonstrates end-to-end interoperable workflows.

Read [INTEROPERABILITY.md](INTEROPERABILITY.md) before proposing a mapping, and [CONTRIBUTING.md](CONTRIBUTING.md) before submitting data examples.

Code and schemas are Apache-2.0. Example data must declare compatible redistribution terms.
