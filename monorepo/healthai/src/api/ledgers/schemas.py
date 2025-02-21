from enum import Enum

from monorepo.core.ledgers.schemas import LedgerEntryBase, SharedLedgerOperation

HealthAILedgerOperation = Enum(
    "HealthAILedgerOperation",
    {
        **{item.name: item.value for item in SharedLedgerOperation},
        "CONTENT_CREATION": "CONTENT_CREATION",
        "CONTENT_ACCESS": "CONTENT_ACCESS",
    },
)


class HealthAILedgerEntry(LedgerEntryBase):
    """Ledger entry model specific to HealthAI."""

    operation: HealthAILedgerOperation
    owner_id: str
    nonce: str
    created_on: str
