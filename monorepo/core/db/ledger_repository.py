from typing import Any, Dict, List, Type

from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import Session


class LedgerRepository:
    """
    A repository class for managing ledger entries in the database.

    This class provides methods to interact with the ledger entries table,
    including querying entries by owner, checking for the existence of a nonce,
    and creating new ledger entries.

    Attributes:
        db (Session): The SQLAlchemy database session.
        model (Type[DeclarativeMeta]): The SQLAlchemy model representing the ledger entries.
    """

    def __init__(self, db: Session, model: Type[DeclarativeMeta]) -> None:
        """
        Initializes the LedgerRepository with a database session and a model.

        Args:
            db (Session): The SQLAlchemy database session.
            model (Type[DeclarativeMeta]): The SQLAlchemy model representing the ledger entries.
        """
        self.db = db
        self.model = model

    def get_entries_by_owner(self, owner_id: str) -> List[Any]:
        """
        Retrieves all ledger entries associated with a specific owner.

        Args:
            owner_id (str): The unique identifier of the owner.

        Returns:
            List[Any]: A list of ledger entries owned by the specified owner.
        """
        return self.db.query(self.model).filter(self.model.owner_id == owner_id).all()

    def check_nonce_exists(self, nonce: str) -> bool:
        """
        Checks if a ledger entry with the specified nonce exists.

        Args:
            nonce (str): The nonce to check for existence.

        Returns:
            bool: True if a ledger entry with the nonce exists, False otherwise.
        """
        return (
            self.db.query(self.model).filter(self.model.nonce == nonce).first()
            is not None
        )

    def create_entry(self, entry_data: Dict[str, Any]) -> Any:
        """
        Creates a new ledger entry in the database.

        Args:
            entry_data (Dict[str, Any]): A dictionary containing the data for the new ledger entry.

        Returns:
            Any: Newly created ledger entry.
        """
        ledger_entry = self.model(**entry_data)
        self.db.add(ledger_entry)
        self.db.commit()
        self.db.refresh(ledger_entry)
        return ledger_entry
