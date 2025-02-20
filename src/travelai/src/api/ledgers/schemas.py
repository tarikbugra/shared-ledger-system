import enum
from src.monorepo.core.ledgers.enums import create_extended_enum
from src.monorepo.core.ledgers.schemas import BaseLedgerOperation


class TravelAILedgerOperation(enum.Enum):
    TRAVEL_BOOKING = "TRAVEL_BOOKING"
    HOTEL_RESERVATION = "HOTEL_RESERVATION"


TravelAppLedgerOperation = create_extended_enum("AppLedgerOperation", BaseLedgerOperation, TravelAILedgerOperation)
