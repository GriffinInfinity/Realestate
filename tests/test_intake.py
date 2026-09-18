import unittest

from src.realestate_ops.intake import intake

class IntakeTests(unittest.TestCase):
    def test_valid_records_enter_operational_validation(self):
        records = [{
            'record_id':'I-001','organization_or_person':'Example LLC','relationship_type':'Developer',
            'market':'DFW','source':'official','source_date':'2026-09-18',
            'verification_status':'Verified','business_reason':'Verified development relationship',
            'potential_service':'Development support','stage':'Qualified','compliance_status':'Clear',
            'dnc_opt_out':False,'next_action':'Research current project','next_action_date':'2026-09-21'
        }]
        result = intake(records)
        self.assertEqual(result['accepted'], 1)
        self.assertEqual(result['quarantined'], 0)
        self.assertTrue(result['operational_report']['valid'])

    def test_invalid_records_are_quarantined(self):
        result = intake([{'record_id':'I-002','stage':'Qualified'}])
        self.assertEqual(result['accepted'], 0)
        self.assertEqual(result['quarantined'], 1)
        self.assertIn('I-002', result['contract_errors'])

if __name__ == '__main__':
    unittest.main()