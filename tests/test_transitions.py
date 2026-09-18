import unittest

from src.realestate_ops.transitions import can_transition

class TransitionTests(unittest.TestCase):
    def base(self):
        return {'stage':'New','verification_status':'Verified','compliance_status':'Clear'}

    def test_new_to_qualified_requires_verification(self):
        record=self.base(); record['verification_status']='Partially Verified'
        d=can_transition(record,'Qualified')
        self.assertFalse(d.allowed)
        self.assertIn('verification_required',d.reasons)

    def test_qualified_to_engaged_allowed(self):
        record=self.base(); record['stage']='Qualified'
        self.assertTrue(can_transition(record,'Engaged').allowed)

    def test_opportunity_requires_clear_compliance(self):
        record=self.base(); record['stage']='Engaged'; record['compliance_status']='Review Required'
        d=can_transition(record,'Opportunity')
        self.assertFalse(d.allowed)
        self.assertIn('compliance_clearance_required',d.reasons)

    def test_active_to_won_requires_revenue_evidence(self):
        record=self.base(); record['stage']='Active'
        d=can_transition(record,'Won')
        self.assertFalse(d.allowed)
        self.assertIn('missing:actual_revenue',d.reasons)

    def test_new_cannot_jump_to_won(self):
        record=self.base(); record.update({'actual_revenue':100,'revenue_date':'2026-09-18','revenue_evidence':'receipt'})
        self.assertFalse(can_transition(record,'Won').allowed)

if __name__ == '__main__':
    unittest.main()