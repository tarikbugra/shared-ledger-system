import enum
from sqlalchemy import Column
from src.monorepo.core.db.models import LedgerEntry
from src.travelai.src.api.ledgers.schemas import TravelAppLedgerOperation


class TravelAILedgerEntryModel(LedgerEntry):
    __tablename__ = "ledger_entries"

    operation = Column(enum.Enum(TravelAppLedgerOperation), nullable=False)
