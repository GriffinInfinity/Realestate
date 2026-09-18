"""Transactional orchestration for record state plus audit persistence."""
from __future__ import annotations
from copy import deepcopy
from typing import Protocol
from .audit import AuditEvent, AuditLog
from .audit_transaction import AuditTransaction
from .audited_transitions import transition_with_audit

class TransactionalRepository(Protocol):
    def get(self, record_id: str) -> dict | None: ...
    def save(self, record: dict) -> None: ...
    def delete(self, record_id: str) -> None: ...

class TransactionalStateService:
    def __init__(self, repository: TransactionalRepository, audit_log: AuditLog) -> None:
        self.repository, self.audit_log = repository, audit_log
    def transition(self, record_id: str, target_stage: str, *, actor: str = "pipeline") -> tuple[dict, AuditEvent | None, object]:
        original=self.repository.get(record_id)
        if original is None: raise KeyError(f"Unknown record_id: {record_id}")
        candidate=deepcopy(original)
        tx=AuditTransaction(self.audit_log,record_id)
        decision=transition_with_audit(candidate,target_stage,self.audit_log,actor=actor)
        if not decision.allowed: return original,None,decision
        event=tx.events_added()[0]
        try: self.repository.save(candidate)
        except Exception:
            tx.rollback()
            raise
        return candidate,event,decision