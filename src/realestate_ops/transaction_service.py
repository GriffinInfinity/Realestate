"""Transactional orchestration for record state plus audit persistence.

The service commits the record only after the audit append succeeds. Repository
implementations may provide stronger atomic transactions later; this boundary
prevents the default in-memory/file-backed flow from silently accepting an
un-audited state change.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Protocol

from .audit import AuditEvent, AuditLog
from .audited_transitions import transition_with_audit

class TransactionalRepository(Protocol):
    def get(self, record_id: str) -> dict | None: ...
    def save(self, record: dict) -> None: ...
    def delete(self, record_id: str) -> None: ...

class TransactionalStateService:
    def __init__(self, repository: TransactionalRepository, audit_log: AuditLog) -> None:
        self.repository = repository
        self.audit_log = audit_log

    def transition(self, record_id: str, target_stage: str, *, actor: str = "pipeline") -> tuple[dict, AuditEvent | None, object]:
        original = self.repository.get(record_id)
        if original is None:
            raise KeyError(f"Unknown record_id: {record_id}")
        candidate = deepcopy(original)
        before = len(self.audit_log.for_record(record_id))
        decision = transition_with_audit(candidate, target_stage, self.audit_log, actor=actor)
        if not decision.allowed:
            return original, None, decision
        event = self.audit_log.for_record(record_id)[before]
        # The transition helper records the audit event before persistence.
        # If record persistence fails, remove the event so observers never see
        # a committed audit for a state that was not committed.
        try:
            self.repository.save(candidate)
        except Exception:
            self.audit_log._events.pop()
            raise
        return candidate, event, decision