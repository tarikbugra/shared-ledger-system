import enum

from pydantic import BaseModel


class BaseLedgerOperation(enum.Enum):
    """Base class for ledger operations."""


class SharedLedgerOperation(BaseLedgerOperation):
    """Shared ledger operations across applications."""

    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"


class LedgerEntryBase(BaseModel):
    """Base model for ledger entries."""

    operation: BaseLedgerOperation
    amount: float
    nonce: str
    owner_id: str
    created_on: str
