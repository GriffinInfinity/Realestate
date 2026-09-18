"""Append-only audit event model and in-memory event store.

The store is deliberately small and dependency-free. A database adapter can
replace it later without changing event semantics.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any

@dataclass(frozen=True)
class AuditEvent:
    event_id: str
    event_type: str
    record_id: str
    timestamp: str
    actor: str
    source: str
    previous_value: Any = None
    new_value: Any = None
    metadata: dict[str, Any] | None = None

class AuditLog:
    def __init__(self) -> None:
        self._events: list[AuditEvent] = []

    def append(self, event: AuditEvent) -> None:
        if any(e.event_id == event.event_id for e in self._events):
            raise ValueError(f"Duplicate event_id: {event.event_id}")
        self._events.append(event)

    def record(self, event_id: str, event_type: str, record_id: str, actor: str, source: str, previous_value: Any = None, new_value: Any = None, metadata: dict[str, Any] | None = None) -> AuditEvent:
        event = AuditEvent(event_id, event_type, record_id, datetime.now(timezone.utc).isoformat(), actor, source, previous_value, new_value, metadata)
        self.append(event)
        return event

    def for_record(self, record_id: str) -> list[AuditEvent]:
        return [e for e in self._events if e.record_id == record_id]

    def export(self) -> list[dict[str, Any]]:
        return [asdict(e) for e in self._events]