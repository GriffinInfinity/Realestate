"""Realestate operating-rule validator.

This module is intentionally dependency-free so it can run in local development,
CI, or a future automation worker.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable
import json
import re


@dataclass
class ValidationIssue:
    record_id: str
    severity: str
    rule_id: str
    message: str
    queue: str | None = None


@dataclass
class ValidationReport:
    checked: int
    issues: list[ValidationIssue] = field(default_factory=list)

    @property
    def valid(self) -> bool:
        return not any(i.severity == "error" for i in self.issues)

    def queues(self) -> dict[str, list[str]]:
        result: dict[str, list[str]] = {}
        for issue in self.issues:
            if issue.queue:
                result.setdefault(issue.queue, []).append(issue.record_id)
        return result

    def to_dict(self) -> dict[str, Any]:
        return {
            "checked": self.checked,
            "valid": self.valid,
            "issues": [i.__dict__ for i in self.issues],
            "queues": self.queues(),
        }


QUALIFIED_STAGES = {"Qualified", "Engaged", "Opportunity", "Active"}
ACTIVE_STAGES = {"Qualified", "Engaged", "Opportunity", "Active"}


def _has(value: Any) -> bool:
    return value is not None and str(value).strip() != ""


def _date_ok(value: Any) -> bool:
    if isinstance(value, date):
        return True
    if not _has(value):
        return False
    try:
        date.fromisoformat(str(value)[:10])
        return True
    except ValueError:
        return False


def validate_record(record: dict[str, Any]) -> list[ValidationIssue]:
    rid = str(record.get("record_id") or record.get("Record ID") or "UNKNOWN")
    issues: list[ValidationIssue] = []

    stage = record.get("stage", record.get("Stage"))
    compliance = record.get("compliance_status", record.get("Compliance Status"))
    dnc = record.get("dnc_opt_out", record.get("DNC / Opt-Out", False))

    if dnc is True or str(dnc).strip().lower() in {"yes", "true", "do not contact"}:
        issues.append(ValidationIssue(rid, "info", "R003",
                                      "Commercial outreach suppressed by DNC/opt-out.",
                                      "suppression"))

    if stage in QUALIFIED_STAGES:
        if not _has(record.get("next_action", record.get("Next Action"))):
            issues.append(ValidationIssue(rid, "error", "R001",
                                          "Qualified/active record is missing a concrete next action.",
                                          "verification"))
        if not _date_ok(record.get("next_action_date", record.get("Next Action Date"))):
            issues.append(ValidationIssue(rid, "error", "R001",
                                          "Qualified/active record is missing a valid next-action date.",
                                          "verification"))

    if compliance == "Review Required":
        issues.append(ValidationIssue(rid, "error", "R002",
                                      "Compliance review is required before advancement or regulated action.",
                                      "compliance"))

    if stage == "Won":
        if not _has(record.get("actual_revenue", record.get("Actual Revenue"))):
            issues.append(ValidationIssue(rid, "error", "R005",
                                          "Won record is missing actual realized revenue.",
                                          "revenue"))
        if not _date_ok(record.get("revenue_date", record.get("Revenue Date"))):
            issues.append(ValidationIssue(rid, "error", "R005",
                                          "Won record is missing a valid revenue date.",
                                          "revenue"))
        if not _has(record.get("revenue_evidence")):
            issues.append(ValidationIssue(rid, "error", "R005",
                                          "Won record is missing revenue evidence.",
                                          "revenue"))

    if record.get("source_requires_refresh") is True:
        issues.append(ValidationIssue(rid, "warning", "R006",
                                      "Source requires re-verification.",
                                      "research"))

    if not _has(record.get("organization_or_person", record.get("Organization / Person"))):
        issues.append(ValidationIssue(rid, "error", "DATA001",
                                      "Identity is missing.",
                                      "verification"))

    if not _has(record.get("business_reason", record.get("Business Reason"))):
        issues.append(ValidationIssue(rid, "error", "DATA002",
                                      "Business reason is missing.",
                                      "verification"))

    return issues


def validate_records(records: Iterable[dict[str, Any]]) -> ValidationReport:
    records = list(records)
    issues: list[ValidationIssue] = []
    seen: set[str] = set()

    for record in records:
        rid = str(record.get("record_id") or record.get("Record ID") or "UNKNOWN")
        if rid in seen:
            issues.append(ValidationIssue(rid, "error", "DATA003",
                                          "Duplicate record ID detected.",
                                          "verification"))
        seen.add(rid)
        issues.extend(validate_record(record))

    return ValidationReport(checked=len(records), issues=issues)


def load_json(path: str | Path) -> list[dict[str, Any]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Expected a JSON array of records.")
    return data


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Validate Realestate pipeline records.")
    parser.add_argument("records", help="Path to a JSON array of pipeline records.")
    parser.add_argument("--output", help="Optional JSON report path.")
    args = parser.parse_args()

    report = validate_records(load_json(args.records))
    payload = json.dumps(report.to_dict(), indent=2)

    if args.output:
        Path(args.output).write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)

    return 0 if report.valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
