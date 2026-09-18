"""Repository contract tests for in-memory and JSON adapters."""
import tempfile, unittest
from pathlib import Path
from src.realestate_ops.json_repository import JsonRecordRepository
from src.realestate_ops.state_service import InMemoryRecordRepository
from src.realestate_ops.repository_contract import RepositoryContractMixin

class RepositoryContractTests(unittest.TestCase):
    def exercise(self, repo):
        record={"record_id":"CONTRACT-001","stage":"New","verification_status":"Verified"}
        repo.save(record)
        self.assertEqual(repo.get("CONTRACT-001"),record)
        loaded=repo.get("CONTRACT-001"); loaded["stage"]="Mutated"
        self.assertEqual(repo.get("CONTRACT-001"),record)
        self.assertIsNone(repo.get("missing"))
        repo.delete("CONTRACT-001")
        self.assertIsNone(repo.get("CONTRACT-001"))

    def test_memory_adapter_contract(self):
        self.exercise(InMemoryRecordRepository())

    def test_json_adapter_contract(self):
        with tempfile.TemporaryDirectory() as d:
            self.exercise(JsonRecordRepository(Path(d)/"records.json"))

if __name__ == "__main__": unittest.main()