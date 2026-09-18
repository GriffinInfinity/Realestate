# Durable Pipeline Repository

The operations engine now supports a dependency-free JSON repository for canonical pipeline records.

## Boundary

`JsonRecordRepository` implements the repository contract used by the state service:

- `get(record_id)`
- `save(record)`
- `delete(record_id)`

Records are keyed by canonical `record_id`. Reads return defensive copies so callers cannot mutate persisted state accidentally.

## Write safety

Writes serialize the complete record collection to a temporary file and replace the target file only after serialization succeeds. This reduces the risk of leaving a partially written repository file after an application error.

## Production path

The JSON repository is a local operational adapter, not the final multi-user datastore. The repository abstraction allows a transactional SQL implementation to be introduced later without rewriting validation, transition, audit, or business logic.

## Next gate

Before introducing external systems, add repository contract tests shared by in-memory and JSON implementations, then add startup/recovery validation and a migration format/version field.
