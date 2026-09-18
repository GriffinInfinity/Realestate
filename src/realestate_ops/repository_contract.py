"""Shared repository protocol and contract helpers."""
from __future__ import annotations
from copy import deepcopy
from typing import Protocol

class RecordRepository(Protocol):
    def get(self, record_id: str) -> dict | None: ...
    def save(self, record: dict) -> None: ...
    def delete(self, record_id: str) -> None: ...

class RepositoryContractMixin:
    """Behavioral checks usable by every repository implementation."""
    def contract_round_trip(self, record: dict) -> None:
        record_id=record["record_id"]
        self.save(deepcopy(record))
        loaded=self.get(record_id)
        assert loaded == record
        loaded["__mutation_test__"]=True
        assert self.get(record_id) == record
        self.delete(record_id)
        assert self.get(record_id) is None

def assert_repository_contract(factory) -> None:
    repo=factory()
    record={"record_id":"CONTRACT-001","stage":"New","verification_status":"Verified"}
    RepositoryContractMixin.contract_round_trip(repo,record)