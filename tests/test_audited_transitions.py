import unittest

from src.realestate_ops.audit import AuditLog
from src.realestate_ops.audited_transitions import transition_with_audit

class AuditedTransitionTests(unittest.TestCase):
    def test_allowed_transition_is_audited(self):
        record={'record_id':'AT-001','stage':'New','verification_status':'Verified','compliance_status':'Clear'}
        audit=AuditLog()
        decision=transition_with_audit(record,'Qualified',audit)
        self.assertTrue(decision.allowed)
        event=audit.for_record('AT-001')[0]
        self.assertEqual(event.event_type,'stage_changed')
        self.assertEqual(event.previous_value,'New')
        self.assertEqual(event.new_value,'Qualified')

    def test_rejected_transition_creates_no_event(self):
        record={'record_id':'AT-002','stage':'New','verification_status':'Partially Verified','compliance_status':'Clear'}
        audit=AuditLog()
        decision=transition_with_audit(record,'Qualified',audit)
        self.assertFalse(decision.allowed)
        self.assertEqual(audit.for_record('AT-002'),[])

if __name__ == '__main__':
    unittest.main()