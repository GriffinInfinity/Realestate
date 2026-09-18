"""Audited stage transition service.

Combines the side-effect-free transition guard with the append-only audit log.
The caller remains responsible for persisting the changed record.
"""

from __future__ import annotations

from typing import Any

from .audit import AuditLog
from .transitions import TransitionDecision, can_transition

def transition_with_audit(record: dict[str, Any], to_stage: str, audit: AuditLog, actor: str = "pipeline") -> TransitionDecision:
    decision = can_transition(record, to_stage)
    if not decision.allowed:
        return decision

    record_id = str(record.get("record_id") or record.get("Record ID") or "UNKNOWN")
    current = decision.from_stage
    audit.record(
        event_id=f"stage:{record_id}:{current}:{to_stage}",
        event_type="stage_changed",
        record_id=record_id,
        actor=actor,
        source="transition_guard",
        previous_value=current,
        new_value=to_stage,
    )
    return decision