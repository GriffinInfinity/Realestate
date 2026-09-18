"""Repository contract is the single dependency for state-service storage."""
from .repository_contract import RecordRepository
from .state_service import InMemoryRecordRepository

__all__ = ["RecordRepository", "InMemoryRecordRepository"]