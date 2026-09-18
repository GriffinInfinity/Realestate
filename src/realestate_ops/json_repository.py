"""Dependency-free JSON repository for canonical pipeline records."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import json

class JsonRecordRepository:
    """Persist one canonical record per JSON object in a single file.

    Writes are atomic at the file level: a temporary file is replaced only
    after the complete serialized collection has been written.
    """
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _load(self) -> dict[str, dict]:
        if not self.path.exists(): return {}
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict): raise ValueError("Repository file must contain an object")
        return {str(k): deepcopy(v) for k,v in raw.items()}

    def get(self, record_id: str) -> dict | None:
        record = self._load().get(record_id)
        return deepcopy(record) if record is not None else None

    def save(self, record: dict) -> None:
        record_id = str(record.get("record_id") or "")
        if not record_id: raise ValueError("record_id is required")
        records = self._load(); records[record_id] = deepcopy(record)
        payload = json.dumps(records, indent=2, ensure_ascii=False) + "\n"
        temp = self.path.with_suffix(self.path.suffix + ".tmp")
        temp.write_text(payload, encoding="utf-8")
        temp.replace(self.path)

    def delete(self, record_id: str) -> None:
        records=self._load()
        if record_id in records:
            del records[record_id]
            temp=self.path.with_suffix(self.path.suffix+".tmp")
            temp.write_text(json.dumps(records,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
            temp.replace(self.path)