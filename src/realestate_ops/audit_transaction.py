"""Explicit audit-log rollback API.

Keeps transactional orchestration independent of the AuditLog internals.
"""
from __future__ import annotations

from dataclasses import dataclass

from .audit import AuditEvent, AuditLog

@dataclass(frozen=True)
class AuditCheckpoint:
    record_id: str
    event_count: int

class AuditTransaction:
    def __init__(self, audit_log: AuditLog, record_id: str) -> None:
        self.audit_log = audit_log
        self.checkpoint = AuditCheckpoint(record_id, len(audit_log.for_record(record_id)))

    def events_added(self) -> list[AuditEvent]:
        return self.audit_log.for_record(self.checkpoint.record_id)[self.checkpoint.event_count:]

    def rollback(self) -> None:
        self.audit_log.rollback_to(self.checkpoint)