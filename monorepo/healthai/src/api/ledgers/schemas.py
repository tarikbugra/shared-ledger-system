from datetime import datetime

from monorepo.core.ledgers.enums import ensure_shared_operations_included
from monorepo.core.ledgers.schemas import BaseLedgerOperation, LedgerEntryBase


@ensure_shared_operations_included
class HealthAILedgerOperation(BaseLedgerOperation):
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"

    CONTENT_ACCESS = "CONTENT_ACCESS"
    CONTENT_CREATION = "CONTENT_CREATION"


class HealthAILedgerEntry(LedgerEntryBase):
    """Ledger entry model specific to HealthAI."""

    operation: HealthAILedgerOperation
    owner_id: str
    nonce: str
    created_on: datetime
