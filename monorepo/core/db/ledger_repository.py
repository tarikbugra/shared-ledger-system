from sqlalchemy.orm import Session


class LedgerRepository:
    def __init__(self, db: Session, model):
        self.db = db
        self.model = model

    def get_entries_by_owner(self, owner_id: str):
        return self.db.query(self.model).filter(self.model.owner_id == owner_id).all()

    def check_nonce_exists(self, nonce: str):
        return (
            self.db.query(self.model).filter(self.model.nonce == nonce).first()
            is not None
        )

    def create_entry(self, entry_data: dict):
        ledger_entry = self.model(**entry_data)
        self.db.add(ledger_entry)
        self.db.commit()
        self.db.refresh(ledger_entry)
        return ledger_entry
