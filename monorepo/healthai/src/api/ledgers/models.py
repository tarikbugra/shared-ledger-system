from sqlalchemy import Column
from sqlalchemy import Enum as SQLAlchemyEnum

from monorepo.core.db.models import BaseLedgerEntryModel
from monorepo.healthai.src.api.ledgers.schemas import HealthAILedgerOperation


class HealthAILedgerEntryModel(BaseLedgerEntryModel):
    """Health AI Ledger Entry Model."""

    __tablename__ = "healthai_ledger_entries"
    __table_args__ = {"schema": "healthai"}

    operation = Column(SQLAlchemyEnum(HealthAILedgerOperation), nullable=False)
