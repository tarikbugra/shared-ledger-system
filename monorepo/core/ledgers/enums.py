from monorepo.core.ledgers.schemas import SharedLedgerOperation


def ensure_shared_operations_included(cls):
    """Check if all shared operations exist in the new class."""
    shared_ops = SharedLedgerOperation.get_operations()
    current_ops = cls.get_operations()

    missing_ops = shared_ops - current_ops
    if missing_ops:
        raise ValueError(f"Missing shared operations: {missing_ops}")

    return cls
