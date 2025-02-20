import enum
from src.monorepo.core.ledgers.enums import create_extended_enum
from src.monorepo.core.ledgers.schemas import BaseLedgerOperation


class HealthAILedgerOperation(enum.Enum):
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"


HealthAppLedgerOperation = create_extended_enum("AppLedgerOperation", BaseLedgerOperation, HealthAILedgerOperation)
