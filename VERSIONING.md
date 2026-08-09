# Versioning and compatibility

Schema identifiers contain a contract version, for example `sciphys.measurement.v0.1`.

- `v0.x` is experimental. Breaking changes are allowed only with migration notes and retained examples of the previous version.
- `v1` and later are stable. Optional additive fields remain compatible; removing, renaming, changing meaning, tightening accepted values, or changing units requires a new major version.
- Published schema files are immutable. Corrections that change validation behavior create a new version.
- Implementations should reject unknown major versions and preserve unknown namespaced extension fields when round-tripping.

A proposal affecting more than one repository requires an RFC in `sciphys-os`. Every release includes conformance examples, a change log, and a migration path.
