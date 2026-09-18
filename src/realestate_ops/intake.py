"""End-to-end pipeline intake service.

Normalizes external records, validates the canonical contract, then applies
the operating validator. It is read-only with respect to source systems.
"""

from __future__ import annotations

from typing import Any

from .contract import normalize_record, validate_contract
from .validator import validate_records

def intake(records: list[dict[str, Any]]) -> dict[str, Any]:
    normalized = [normalize_record(r) for r in records]
    contract_errors: dict[str, list[str]] = {}
    accepted: list[dict[str, Any]] = []
    quarantined: list[dict[str, Any]] = []

    for record in normalized:
        rid = str(record.get("record_id", "UNKNOWN"))
        errors = validate_contract(record)
        if errors:
            contract_errors[rid] = errors
            quarantined.append(record)
        else:
            accepted.append(record)

    operational_report = validate_records(accepted).to_dict()
    return {
        "accepted": len(accepted),
        "quarantined": len(quarantined),
        "contract_errors": contract_errors,
        "operational_report": operational_report,
        "records": accepted,
    }