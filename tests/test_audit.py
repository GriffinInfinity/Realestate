import unittest

from src.realestate_ops.audit import AuditLog

class AuditTests(unittest.TestCase):
    def test_events_are_append_only_and_traceable(self):
        log = AuditLog()
        event = log.record('E-001', 'stage_changed', 'R-001', 'operator', 'pipeline', 'New', 'Qualified')
        self.assertEqual(log.for_record('R-001'), [event])
        self.assertEqual(len(log.export()), 1)

    def test_duplicate_event_ids_are_rejected(self):
        log = AuditLog()
        log.record('E-002', 'created', 'R-002', 'operator', 'import')
        with self.assertRaises(ValueError):
            log.record('E-002', 'updated', 'R-002', 'operator', 'pipeline')

if __name__ == '__main__':
    unittest.main()