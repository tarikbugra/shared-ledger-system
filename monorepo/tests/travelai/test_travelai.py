import pytest
from fastapi.testclient import TestClient


class TestTravelAILedger:
    @pytest.fixture
    def ledger_prefix(self):
        return "travelai"

    @pytest.fixture
    def operation(self):
        return "CREDIT_ADD"

    @pytest.fixture
    def owner_id(self):
        return "test_owner"

    @pytest.fixture
    def expected_balance(self):
        return 0

    def test_get_balance(
        self, test_client: TestClient, ledger_prefix, owner_id, expected_balance
    ):
        response = test_client.get(f"/{ledger_prefix}/ledger/{owner_id}")
        assert response.status_code == 200
        assert response.json() == {"owner_id": owner_id, "balance": expected_balance}

    def test_add_ledger_entry(
        self, test_client: TestClient, ledger_prefix, operation, owner_id
    ):
        response = test_client.post(
            f"/{ledger_prefix}/ledger?operation={operation}&amount=1&owner_id={owner_id}&nonce=test_nonce"
        )
        assert response.status_code == 200
        assert response.json() == {"message": "Ledger entry added successfully"}
