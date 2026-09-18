import tempfile, unittest
from pathlib import Path
from src.realestate_ops.json_repository import JsonRecordRepository

class JsonRepositoryTests(unittest.TestCase):
    def test_save_reload_and_delete(self):
        with tempfile.TemporaryDirectory() as d:
            repo=JsonRecordRepository(Path(d)/'records.json')
            record={'record_id':'R-300','stage':'New','name':'Test'}
            repo.save(record)
            record['name']='mutated'
            self.assertEqual(repo.get('R-300')['name'],'Test')
            self.assertEqual(repo.get('missing'),None)
            repo.delete('R-300')
            self.assertIsNone(repo.get('R-300'))
    def test_missing_record_id_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError): JsonRecordRepository(Path(d)/'records.json').save({'stage':'New'})
if __name__ == '__main__': unittest.main()