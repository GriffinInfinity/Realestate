"""Persistence boundary for pipeline records and audited stage transitions."""
from __future__ import annotations

from copy import deepcopy
from typing import Protocol

from .audit import AuditEvent, AuditLog
from .audited_transitions import transition_with_audit

class RecordRepository(Protocol):
    def get(self, record_id: str) -> dict | None: ...
    def save(self, record: dict) -> None: ...

class InMemoryRecordRepository:
    def __init__(self, records: list[dict] | None = None) -> None:
        self._records = {r["record_id"]: deepcopy(r) for r in (records or [])}
    def get(self, record_id: str) -> dict | None:
        record = self._records.get(record_id)
        return deepcopy(record) if record is not None else None
    def save(self, record: dict) -> None:
        self._records[record["record_id"]] = deepcopy(record)

class PipelineStateService:
    def __init__(self, repository: RecordRepository, audit_log: AuditLog) -> None:
        self.repository = repository
        self.audit_log = audit_log

    def transition(self, record_id: str, target_stage: str, *, actor: str = "pipeline") -> tuple[dict, AuditEvent | None, object]:
        record = self.repository.get(record_id)
        if record is None:
            raise KeyError(f"Unknown record_id: {record_id}")
        candidate = deepcopy(record)
        before = len(self.audit_log.for_record(record_id))
        decision = transition_with_audit(candidate, target_stage, self.audit_log, actor=actor)
        if not decision.allowed:
            return record, None, decision
        candidate["stage"] = target_stage
        self.repository.save(candidate)
        event = self.audit_log.for_record(record_id)[before]
        return candidate, event, decision