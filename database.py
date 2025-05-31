from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator
import os
from dotenv import load_dotenv

# Load environment variables (only used during local dev)
load_dotenv()

# Use DATABASE_URL from environment or fallback to SQLite (for dev)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ngo.db")

# PostgreSQL needs no special connect_args
connect_args = {"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base class
Base = declarative_base()

# Dependency to get DB session
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
