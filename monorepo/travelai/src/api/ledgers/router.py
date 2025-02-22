from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from monorepo.core.db.database import get_db
from monorepo.core.db.ledger_repository import LedgerRepository
from monorepo.core.ledgers.services.base_ledger_service import BaseLedgerService
from monorepo.travelai.src.api.ledgers.models import TravelAILedgerEntryModel
from monorepo.travelai.src.api.ledgers.schemas import TravelAILedgerOperation

travelai_router = APIRouter()


def get_ledger_service(db: Session = Depends(get_db)) -> BaseLedgerService:
    return BaseLedgerService(LedgerRepository(db=db, model=TravelAILedgerEntryModel))


@travelai_router.get("/ledger/{owner_id}")
def get_balance(
    owner_id: str, ledger_service: BaseLedgerService = Depends(get_ledger_service)
):
    balance = ledger_service.get_balance(owner_id)
    if balance is None:
        raise HTTPException(status_code=404, detail="Owner not found")
    return {"owner_id": owner_id, "balance": balance}


@travelai_router.post("/ledger")
def add_ledger_entry(
    operation: TravelAILedgerOperation,
    amount: int,
    owner_id: str,
    nonce: str,
    ledger_service: BaseLedgerService = Depends(get_ledger_service),
):
    balance = ledger_service.get_balance(owner_id)

    if balance is None:
        raise HTTPException(status_code=404, detail="Owner not found")

    if balance < amount and operation != TravelAILedgerOperation.CREDIT_ADD:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    if ledger_service.check_duplicate_nonce(nonce):
        raise HTTPException(status_code=400, detail="Duplicate transaction")

    ledger_service.update_balance(
        operation=operation,
        amount=amount,
        owner_id=owner_id,
        nonce=nonce,
        created_on=datetime.now(),
    )

    return {"message": "Ledger entry added successfully"}
