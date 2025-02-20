import enum
from datetime import datetime
from pydantic import BaseModel


class BaseLedgerOperation(enum.Enum):
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"


class LedgerEntrySchema(BaseModel):
    id: int
    operation: BaseLedgerOperation
    amount: int
    nonce: str
    owner_id: str
    created_on: datetime