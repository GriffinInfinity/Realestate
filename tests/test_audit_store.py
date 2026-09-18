import tempfile
import unittest
from pathlib import Path

from src.realestate_ops.audit import AuditEvent
from src.realestate_ops.audit_store import JsonlAuditStore

class AuditStoreTests(unittest.TestCase):
    def test_events_survive_reload(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'audit.jsonl'
            store=JsonlAuditStore(path)
            event=AuditEvent('S-001','created','R-001','2026-09-18T00:00:00+00:00','test','unit')
            store.append(event)
            reloaded=JsonlAuditStore(path)
            self.assertEqual(reloaded.events(),[event])

    def test_duplicate_event_is_rejected_after_reload(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'audit.jsonl'
            store=JsonlAuditStore(path)
            event=AuditEvent('S-002','created','R-002','2026-09-18T00:00:00+00:00','test','unit')
            store.append(event)
            with self.assertRaises(ValueError):
                JsonlAuditStore(path).append(event)

if __name__ == '__main__':
    unittest.main()