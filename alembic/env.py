# ~/My_store/alembic/env.py
import os
import sys
from pathlib import Path
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# ----- ensure project root is importable -----
project_root = Path(__file__).resolve().parents[1]  # My_store
sys.path.insert(0, str(project_root))

# Load .env explicitly from project root
load_dotenv(dotenv_path=project_root / ".env")

# Alembic Config object
config = context.config

# Logging config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Read DATABASE_URL (allow fallback var name)
database_url = os.getenv("DATABASE_URL") or os.getenv("SQLALCHEMY_DATABASE_URL")
print("🔍 DATABASE_URL from .env:", database_url)

if not database_url:
    raise ValueError("❌ DATABASE_URL not found in project .env file (DATABASE_URL or SQLALCHEMY_DATABASE_URL).")

# Inject into alembic config
config.set_main_option("sqlalchemy.url", database_url)

# Import Base (where your declarative_base() lives) and ensure models are imported
from apps.backend.app.database import Base    # path matches your project layout
import apps.backend.app.models as models      # ensure models are imported so metadata is populated

target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

