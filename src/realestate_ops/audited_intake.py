"""Audited pipeline intake wrapper.

Adds audit events around contract intake without changing the underlying
validator semantics.
"""

from __future__ import annotations

from typing import Any

from .audit import AuditLog
from .intake import intake

def audited_intake(records: list[dict[str, Any]], audit: AuditLog, actor: str = "pipeline") -> dict[str, Any]:
    result = intake(records)
    for record in records:
        rid = str(record.get("record_id") or record.get("Record ID") or "UNKNOWN")
        audit.record(
            event_id=f"intake:{rid}",
            event_type="pipeline_intake",
            record_id=rid,
            actor=actor,
            source="intake",
            metadata={
                "accepted": rid not in result["contract_errors"],
                "contract_errors": result["contract_errors"].get(rid, []),
            },
        )
    return result