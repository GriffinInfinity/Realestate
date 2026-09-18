"""Pipeline stage transition guard.

Validates allowed state changes and returns a structured decision before a
record is mutated. It is intentionally side-effect free.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

STAGE_ORDER = ["New", "Qualified", "Engaged", "Opportunity", "Active", "Won"]

ALLOWED = {
    "New": {"Qualified", "Nurture", "Disqualified"},
    "Qualified": {"Engaged", "Nurture", "Disqualified"},
    "Engaged": {"Opportunity", "Nurture", "Disqualified"},
    "Opportunity": {"Active", "Nurture", "Disqualified"},
    "Active": {"Won", "Nurture", "Disqualified"},
    "Won": set(),
    "Nurture": {"Qualified", "Engaged", "Disqualified"},
    "Disqualified": {"New"},
}

@dataclass(frozen=True)
class TransitionDecision:
    allowed: bool
    from_stage: str
    to_stage: str
    reasons: tuple[str, ...] = ()

def can_transition(record: dict[str, Any], to_stage: str) -> TransitionDecision:
    current = str(record.get("stage", ""))
    if current not in ALLOWED:
        return TransitionDecision(False, current, to_stage, ("invalid_current_stage",))
    if to_stage not in ALLOWED:
        return TransitionDecision(False, current, to_stage, ("invalid_target_stage",))
    if to_stage not in ALLOWED[current]:
        return TransitionDecision(False, current, to_stage, ("transition_not_allowed",))
    if to_stage == "Qualified" and record.get("verification_status") != "Verified":
        return TransitionDecision(False, current, to_stage, ("verification_required",))
    if to_stage in {"Opportunity", "Active"} and record.get("compliance_status") != "Clear":
        return TransitionDecision(False, current, to_stage, ("compliance_clearance_required",))
    if to_stage == "Won":
        missing = [k for k in ("actual_revenue", "revenue_date", "revenue_evidence") if not record.get(k)]
        if missing:
            return TransitionDecision(False, current, to_stage, tuple(f"missing:{k}" for k in missing))
    return TransitionDecision(True, current, to_stage)