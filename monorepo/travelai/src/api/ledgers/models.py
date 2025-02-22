from sqlalchemy import Column
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.ext.declarative import declarative_base

from monorepo.core.db.models import BaseLedgerEntryModel
from monorepo.travelai.src.api.ledgers.schemas import TravelAILedgerOperation


class TravelAILedgerEntryModel(BaseLedgerEntryModel):
    __tablename__ = "travelai_ledger_entries"
    __table_args__ = {"schema": "travelai"}

    operation = Column(SQLAlchemyEnum(TravelAILedgerOperation), nullable=False)
