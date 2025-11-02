import pytest
from sqlmodel import create_engine, Session, SQLModel

@pytest.fixture(scope="module")
def engine():
    sqlite_url = "sqlite:///:memory:"
    connect_args = {"check_same_thread": False}

    engine = create_engine(sqlite_url, connect_args=connect_args)

    SQLModel.metadata.create_all(engine)

    return engine

@pytest.fixture
def session(engine):
    with Session(engine) as session:
        yield session   