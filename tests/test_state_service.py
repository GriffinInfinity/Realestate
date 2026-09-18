import unittest

from src.realestate_ops.audit import AuditLog
from src.realestate_ops.state_service import InMemoryRecordRepository, PipelineStateService

class StateServiceTests(unittest.TestCase):
    def make_service(self):
        record={"record_id":"R-100","stage":"New","verification_status":"Verified","compliance_status":"Clear"}
        repo=InMemoryRecordRepository([record])
        log=AuditLog()
        return PipelineStateService(repo,log),repo,log

    def test_allowed_transition_persists_and_audits(self):
        service,repo,log=self.make_service()
        updated,event,decision=service.transition("R-100","Qualified",actor="test")
        self.assertTrue(decision.allowed)
        self.assertEqual(updated["stage"],"Qualified")
        self.assertEqual(repo.get("R-100")["stage"],"Qualified")
        self.assertEqual(event.event_type,"stage_changed")
        self.assertEqual(len(log.for_record("R-100")),1)

    def test_rejected_transition_has_no_persistence_or_audit(self):
        service,repo,log=self.make_service()
        updated,event,decision=service.transition("R-100","Opportunity")
        self.assertFalse(decision.allowed)
        self.assertIsNone(event)
        self.assertEqual(updated["stage"],"New")
        self.assertEqual(repo.get("R-100")["stage"],"New")
        self.assertEqual(log.for_record("R-100"),[])

    def test_missing_record_fails_explicitly(self):
        service,_,_=self.make_service()
        with self.assertRaises(KeyError): service.transition("missing","Qualified")

if __name__ == '__main__': unittest.main()