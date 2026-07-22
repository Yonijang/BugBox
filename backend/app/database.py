from pathlib import Path
from sqlmodel import SQLModel, Session, create_engine

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATABASE_PATH = (
    PROJECT_ROOT
    / "data"
    / "database"
    / "bugbox.db"
)

DATABASE_PATH.parent.mkdir(
    parents=True,
    exist_ok=True,
)

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    },
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session