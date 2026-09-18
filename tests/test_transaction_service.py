import unittest
from src.realestate_ops.audit import AuditLog
from src.realestate_ops.transaction_service import TransactionalStateService

class Repo:
    def __init__(self, record, fail=False): self.record=dict(record); self.fail=fail
    def get(self, record_id): return dict(self.record) if self.record.get('record_id')==record_id else None
    def save(self, record):
        if self.fail: raise RuntimeError('persistence failure')
        self.record=dict(record)
    def delete(self, record_id): self.record={}

class TransactionServiceTests(unittest.TestCase):
    def base(self): return {'record_id':'R-200','stage':'New','verification_status':'Verified','compliance_status':'Clear'}
    def test_success_commits_both(self):
        repo=Repo(self.base()); log=AuditLog(); service=TransactionalStateService(repo,log)
        record,event,decision=service.transition('R-200','Qualified')
        self.assertTrue(decision.allowed); self.assertEqual(record['stage'],'Qualified'); self.assertEqual(repo.record['stage'],'Qualified'); self.assertEqual(len(log.for_record('R-200')),1)
    def test_persistence_failure_rolls_back_audit(self):
        repo=Repo(self.base(),fail=True); log=AuditLog(); service=TransactionalStateService(repo,log)
        with self.assertRaises(RuntimeError): service.transition('R-200','Qualified')
        self.assertEqual(repo.record['stage'],'New'); self.assertEqual(log.for_record('R-200'),[])
    def test_rejection_has_no_side_effects(self):
        repo=Repo(self.base()); log=AuditLog(); service=TransactionalStateService(repo,log)
        record,event,decision=service.transition('R-200','Opportunity')
        self.assertFalse(decision.allowed); self.assertIsNone(event); self.assertEqual(record['stage'],'New'); self.assertEqual(log.for_record('R-200'),[])
if __name__ == '__main__': unittest.main()