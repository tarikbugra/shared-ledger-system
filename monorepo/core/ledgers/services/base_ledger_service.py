from monorepo.core.config import settings
from monorepo.core.db.ledger_repository import LedgerRepository
from monorepo.core.ledgers.schemas import SharedLedgerOperation


class BaseLedgerService:
    """
    Service class for managing ledger operations and balances.

    This class provides methods to get the balance of an owner, check for duplicate nonces,
    and update the balance by creating new ledger entries.

    Attributes:
        ledger_repository (LedgerRepository): Repository for interacting with ledger entries in the database.
    """

    def __init__(self, ledger_repository: LedgerRepository) -> None:
        """
        Initialize the BaseLedgerService with a ledger repository.

        Args:
            ledger_repository (LedgerRepository): Instance of the LedgerRepository class.
        """
        self.ledger_repository = ledger_repository

    def get_balance(self, owner_id: str):
        """
        Calculate the balance of a specific owner based on their ledger entries.

        Args:
            owner_id (str): Unique identifier of the owner.

        Returns:
            int: Calculated balance of the owner.
        """
        entries = self.ledger_repository.get_entries_by_owner(owner_id)
        balance = 0
        for entry in entries:
            operation_value = settings.LEDGER_OPERATION_CONFIG.get(
                entry.operation.value
            )

            if operation_value is not None:
                balance += operation_value * entry.amount

        return balance

    def check_duplicate_nonce(self, nonce: str) -> bool:
        """
        Check if a ledger entry with the specified nonce already exists.

        Args:
            nonce (str): Nonce to check for duplication.

        Returns:
            bool: True if a ledger entry with the same nonce exists, False otherwise.
        """
        return self.ledger_repository.check_nonce_exists(nonce)

    def update_balance(
        self,
        operation: SharedLedgerOperation,
        amount: int,
        owner_id: str,
        nonce: str,
        created_on: str,
    ) -> None:
        """
        Update the balance by creating a new ledger entry.

        Args:
            operation (SharedLedgerOperation): Type of ledger operation being performed.
            amount (int): Amount associated with the operation.
            owner_id (str): Unique identifier of the owner.
            nonce (str): Unique nonce for preventing duplicate transactions.
            created_on (str): Timestamp when the operation was created.
        """
        ledger_entry = {
            "operation": operation,
            "amount": amount,
            "owner_id": owner_id,
            "nonce": nonce,
            "created_on": created_on,
        }

        self.ledger_repository.create_entry(ledger_entry)
