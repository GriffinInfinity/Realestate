import unittest

from src.realestate_ops.audit import AuditLog
from src.realestate_ops.audited_intake import audited_intake

class AuditedIntakeTests(unittest.TestCase):
    def test_intake_creates_audit_event(self):
        audit = AuditLog()
        records = [{
            'record_id':'AI-001','organization_or_person':'Example LLC','relationship_type':'Developer',
            'market':'DFW','source':'official','source_date':'2026-09-18',
            'verification_status':'Verified','business_reason':'Verified relationship',
            'potential_service':'Development support','stage':'Qualified','compliance_status':'Clear',
            'dnc_opt_out':False,'next_action':'Research project','next_action_date':'2026-09-21'
        }]
        result = audited_intake(records, audit)
        self.assertEqual(result['accepted'], 1)
        events = audit.for_record('AI-001')
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].event_type, 'pipeline_intake')

if __name__ == '__main__':
    unittest.main()