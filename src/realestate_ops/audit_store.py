"""Durable JSON-lines audit event store.

Provides a simple append-only persistence boundary for audit events without
requiring a database dependency. A database implementation can later satisfy
the same conceptual interface.
"""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
import json
from typing import Iterable

from .audit import AuditEvent

class JsonlAuditStore:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, event: AuditEvent) -> None:
        existing_ids = {e.event_id for e in self.events()}
        if event.event_id in existing_ids:
            raise ValueError(f"Duplicate event_id: {event.event_id}")
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(event), ensure_ascii=False) + "\n")

    def append_many(self, events: Iterable[AuditEvent]) -> None:
        for event in events:
            self.append(event)

    def events(self) -> list[AuditEvent]:
        if not self.path.exists():
            return []
        result = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                result.append(AuditEvent(**json.loads(line)))
        return result

    def for_record(self, record_id: str) -> list[AuditEvent]:
        return [e for e in self.events() if e.record_id == record_id]