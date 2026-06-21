# SciPhys Formats

Open schemas for AI-native experimental science data.

SciPhys Formats defines a shared language for samples, instruments,
measurements, analysis results, provenance, and expert feedback. The goal is to
make raw experimental data searchable, auditable, and reusable across labs,
notebooks, AI systems, and hosted workspaces.

## Why It Matters

AI for science needs more than files. It needs context:

- who measured the sample;
- what project and material system the data belongs to;
- how the sample was prepared;
- which instrument and settings were used;
- which analysis version produced the result;
- what an expert accepted, rejected, or corrected.

This repository is the public schema layer for that context.

## Current Scope

- `schemas/sciphysdata.v0.schema.json`: draft JSON Schema for experimental
  measurements and expert feedback.
- `examples/xrd-measurement.example.json`: minimal XRD measurement example.

The schema is intentionally small in v0. It will expand as real parser,
benchmark, and lab workflow cases demand it.

## Design Principles

- Evidence is a first-class object.
- Provenance must travel with the result.
- Expert feedback should be structured, not trapped in comments.
- Public examples must not expose private lab data.
- Schemas should be useful outside the hosted SciPhys product.

## Related Repositories

- [sciphys-os](https://github.com/sciphys-ai/sciphys-os): parsers and analysis primitives.
- [sciphys-bench](https://github.com/sciphys-ai/sciphys-bench): benchmark specifications and public cases.
- [sciphys-recipes](https://github.com/sciphys-ai/sciphys-recipes): reproducible workflows.

## License

Apache-2.0.
