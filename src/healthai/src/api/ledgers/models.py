import enum
from sqlalchemy import Column
from src.monorepo.core.db.models import LedgerEntry
from src.healthai.src.api.ledgers.schemas import HealthAppLedgerOperation


class HealthAILedgerEntryModel(LedgerEntry):
    __tablename__ = "ledger_entries"

    operation = Column(enum.Enum(HealthAppLedgerOperation), nullable=False)
