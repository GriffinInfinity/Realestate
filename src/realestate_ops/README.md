# Realestate Operations Engine

## Purpose
Small, dependency-free Python components for validating pipeline data and generating operator queues.

## Current components

- `src/realestate_ops/validator.py` — validates pipeline records against core operating rules.
- `src/realestate_ops/daily_report.py` — converts validator output into a prioritized daily operating report.
- `config/operating_rules.yaml` — machine-readable operating rules.
- `examples/pipeline_records.json` — example validator input.

## Local usage

Run the validator:

```powershell
python src/realestate_ops/validator.py examples/pipeline_records.json --output validation-report.json
```

The validator exits with code 0 when no error-level issues are found and code 1 when errors exist.

## Design principle

These components are deliberately dependency-light and read-only with respect to source records. They identify work; they do not silently modify business records, bypass compliance gates, or turn estimates into revenue.
