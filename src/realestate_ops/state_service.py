"""Persistence boundary for pipeline records and audited stage transitions."""
from __future__ import annotations

from copy import deepcopy
from typing import Protocol

from .audit import AuditEvent
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
    def __init__(self, repository: RecordRepository, audit_store) -> None:
        self.repository = repository
        self.audit_store = audit_store

    def transition(self, record_id: str, target_stage: str, *, actor: str, source: str, timestamp: str):
        record = self.repository.get(record_id)
        if record is None:
            raise KeyError(f"Unknown record_id: {record_id}")
        candidate = deepcopy(record)
        result = transition_with_audit(candidate, target_stage, actor=actor, source=source, timestamp=timestamp)
        if not result.allowed:
            return record, None, result
        self.repository.save(candidate)
        self.audit_store.append(result.audit_event)
        return candidate, result.audit_event, result