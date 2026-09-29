from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    pool_pre_ping=True,       # Crucial for serverless: tests connection liveness
    pool_size=5,              # Keeps per-Lambda container connection count conservative
    max_overflow=10,
    pool_recycle=300,         # Recycles stale connections every 5 minutes
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()