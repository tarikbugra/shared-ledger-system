from sqlalchemy import Column
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.ext.declarative import declarative_base

from monorepo.core.db.models import BaseLedgerEntryModel
from monorepo.healthai.src.api.ledgers.schemas import HealthAILedgerOperation

Base = declarative_base()


class HealthAILedgerEntryModel(BaseLedgerEntryModel):
    __tablename__ = "healthai_ledger_entries"

    operation = Column(SQLAlchemyEnum(HealthAILedgerOperation), nullable=False)
