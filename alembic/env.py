import os
from dotenv import load_dotenv
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# -----------------------
# Load environment variables
# -----------------------
load_dotenv()
db_url = os.getenv("DATABASE_URL")

# -----------------------
# Alembic Config object
# -----------------------
config = context.config

# Escape % for ConfigParser (handles passwords like p@sw0rd -> p%%40sw0rd)
if db_url:
    config.set_main_option("sqlalchemy.url", db_url.replace("%", "%%"))

# -----------------------
# Logging
# -----------------------
fileConfig(config.config_file_name)

# -----------------------
# Import your models' metadata
# -----------------------
from app.database import Base
from app import models  # Make sure all models are imported so Alembic sees them

target_metadata = Base.metadata

# -----------------------
# Offline migrations
# -----------------------
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

# -----------------------
# Online migrations
# -----------------------
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

# -----------------------
# Run the right mode
# -----------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
