from monorepo.core.config import settings
from monorepo.core.db.ledger_repository import LedgerRepository
from monorepo.core.ledgers.schemas import SharedLedgerOperation


class BaseLedgerService:
    def __init__(self, ledger_repository: LedgerRepository):
        self.ledger_repository = ledger_repository

    def get_balance(self, owner_id: str):
        entries = self.ledger_repository.get_entries_by_owner(owner_id)
        balance = 0
        for entry in entries:
            operation_value = settings.LEDGER_OPERATION_CONFIG.get(
                entry.operation.value
            )

            if operation_value is not None:
                balance += operation_value * entry.amount

        return balance

    def check_duplicate_nonce(self, nonce: str):
        return self.ledger_repository.check_nonce_exists(nonce)

    def update_balance(
        self,
        operation: SharedLedgerOperation,
        amount: int,
        owner_id: str,
        nonce: str,
        created_on: str,
    ):
        ledger_entry = {
            "operation": operation,
            "amount": amount,
            "owner_id": owner_id,
            "nonce": nonce,
            "created_on": created_on,
        }

        self.ledger_repository.create_entry(ledger_entry)
