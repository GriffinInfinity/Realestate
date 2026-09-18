import unittest

from src.realestate_ops.contract import normalize_record, validate_contract

class ContractTests(unittest.TestCase):
    def test_normalizes_schema_labels(self):
        record = normalize_record({'Record ID': 'X-1', 'Stage': 'New', 'DNC / Opt-Out': False})
        self.assertEqual(record['record_id'], 'X-1')
        self.assertEqual(record['stage'], 'New')
        self.assertIs(record['dnc_opt_out'], False)

    def test_rejects_missing_required_fields(self):
        errors = validate_contract({'record_id': 'X-2'})
        self.assertIn('missing:market', errors)

    def test_won_requires_evidence(self):
        record = {
            'record_id':'X-3','organization_or_person':'Example','relationship_type':'Developer',
            'market':'DFW','source':'official','source_date':'2026-09-18',
            'verification_status':'Verified','business_reason':'Verified relationship',
            'potential_service':'Development support','stage':'Won','compliance_status':'Clear',
            'dnc_opt_out':False,'actual_revenue':1000,'revenue_date':'2026-09-18'
        }
        self.assertIn('missing:revenue_evidence', validate_contract(record))

if __name__ == '__main__':
    unittest.main()