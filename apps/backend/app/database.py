# ~/My_store/apps/backend/app/database.py
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load .env from project root (robust even when Alembic runs from alembic/)
project_root = Path(__file__).resolve().parents[3]  # ../..../My_store
load_dotenv(dotenv_path=project_root / ".env")

# Read DB URL (accept either name for compatibility)
DATABASE_URL = os.getenv("DATABASE_URL") or os.getenv("SQLALCHEMY_DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL (or SQLALCHEMY_DATABASE_URL) is not set in .env")

# Engine and session factory
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

