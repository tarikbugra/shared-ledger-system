from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseLedgerEntryModel(Base):
    """Base Ledger Entry Model."""

    __tablename__ = "ledger_entries"
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, nullable=False)
    nonce = Column(String, nullable=False, unique=True)
    owner_id = Column(String, nullable=False)
    created_on = Column(DateTime, default=datetime.now())
