from sqlalchemy import Column, Integer, String, DateTime, Enum, func
from sqlalchemy.ext.declarative import declarative_base
from src.monorepo.core.ledgers.schemas import BaseLedgerOperation

Base = declarative_base()


class LedgerEntry(Base):
    __tablename__ = "ledger_entries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    operation = Column(Enum(BaseLedgerOperation), nullable=False)
    amount = Column(Integer, nullable=False)
    nonce = Column(String, unique=True, nullable=False)
    owner_id = Column(String, nullable=False)
    created_on = Column(DateTime, server_default=func.now(), nullable=False)
