from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from monorepo.core.config import settings

Base = declarative_base()


engine = create_engine(
    settings.get_database_URI(),
)

SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
