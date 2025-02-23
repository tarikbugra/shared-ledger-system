import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from monorepo.core.config import settings
from monorepo.core.db.database import Base
from monorepo.main import create_app

SQLALCHEMY_TEST_DATABASE_URL = settings.get_database_URI()

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    yield app


@pytest.fixture(scope="module")
def test_client(test_app):
    with TestClient(test_app) as client:
        yield client


@pytest.fixture(scope="function")
def test_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
