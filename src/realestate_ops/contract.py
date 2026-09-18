"""Contract validation and normalization helpers.

Keeps integration-specific field mapping separate from operating rules.
"""

from __future__ import annotations

from typing import Any

STAGES = {"New", "Qualified", "Engaged", "Opportunity", "Active", "Won", "Nurture", "Disqualified"}
VERIFICATION = {"Unverified", "Partially Verified", "Verified", "Needs Review"}
COMPLIANCE = {"Clear", "Review Required", "Blocked"}

REQUIRED = {
    "record_id", "organization_or_person", "relationship_type", "market",
    "source", "source_date", "verification_status", "business_reason",
    "potential_service", "stage", "compliance_status", "dnc_opt_out",
}

def normalize_record(raw: dict[str, Any]) -> dict[str, Any]:
    aliases = {
        "Record ID": "record_id",
        "Organization / Person": "organization_or_person",
        "Relationship Type": "relationship_type",
        "Market": "market",
        "Source": "source",
        "Source Date": "source_date",
        "Verification Status": "verification_status",
        "Business Reason": "business_reason",
        "Potential Service": "potential_service",
        "Stage": "stage",
        "Compliance Status": "compliance_status",
        "DNC / Opt-Out": "dnc_opt_out",
        "Next Action": "next_action",
        "Next Action Date": "next_action_date",
        "Estimated Value": "estimated_value",
        "Estimate Basis": "estimate_basis",
        "Actual Revenue": "actual_revenue",
        "Revenue Date": "revenue_date",
    }
    result: dict[str, Any] = {}
    for key, value in raw.items():
        result[aliases.get(key, key)] = value
    return result

def validate_contract(record: dict[str, Any]) -> list[str]:
    record = normalize_record(record)
    errors: list[str] = []
    missing = sorted(k for k in REQUIRED if not record.get(k) and record.get(k) is not False)
    errors.extend(f"missing:{key}" for key in missing)
    if record.get("stage") not in STAGES:
        errors.append("invalid:stage")
    if record.get("verification_status") not in VERIFICATION:
        errors.append("invalid:verification_status")
    if record.get("compliance_status") not in COMPLIANCE:
        errors.append("invalid:compliance_status")
    if record.get("stage") in {"Qualified", "Engaged", "Opportunity", "Active"}:
        if not record.get("next_action"):
            errors.append("missing:next_action")
        if not record.get("next_action_date"):
            errors.append("missing:next_action_date")
    if record.get("stage") == "Won":
        for key in ("actual_revenue", "revenue_date", "revenue_evidence"):
            if not record.get(key):
                errors.append(f"missing:{key}")
    return errors