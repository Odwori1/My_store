# ~/My_store/apps/backend/app/deps.py
from .database import SessionLocal
from typing import Generator

# Dependency to get DB session
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

