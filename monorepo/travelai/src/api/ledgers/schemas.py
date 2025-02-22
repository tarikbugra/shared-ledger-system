from enum import Enum

from monorepo.core.ledgers.schemas import LedgerEntryBase, SharedLedgerOperation

TravelAILedgerOperation = Enum(
    "TravelAILedgerOperation",
    {
        **{item.name: item.value for item in SharedLedgerOperation},
        "CONTENT_CREATION": "CONTENT_CREATION",
        "CONTENT_ACCESS": "CONTENT_ACCESS",
    },
)


class TravelAILedgerEntry(LedgerEntryBase):
    """Ledger entry model specific to TravelhAI."""

    operation: TravelAILedgerOperation
    owner_id: str
    nonce: str
    created_on: str
