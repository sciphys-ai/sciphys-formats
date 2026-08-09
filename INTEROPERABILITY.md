# Interoperability

SciPhys contracts wrap rather than replace established scientific formats.

Priority mappings include NeXus/HDF5 for experimental data, NOMAD Metainfo for materials archives, CIF for structures, JCAMP-DX for spectra, OME-compatible metadata for microscopy, and RO-Crate for portable research objects.

A mapping contribution must include:

1. source and target versions;
2. bidirectional field mapping;
3. explicit unit conversions;
4. fields that are lossy, ambiguous, or unmapped;
5. at least one redistributable conformance example;
6. round-trip tests where the source format permits them;
7. provenance showing which adapter and mapping version ran.

Vendor-specific fields belong under namespaced `extensions` until a scientifically meaningful common field is accepted. Similar field names are not evidence of equivalent meaning.
