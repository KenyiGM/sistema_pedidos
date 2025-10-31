from sqlmodel import create_engine
from core.config import settings

sqlite_url = settings.DATABASE_URL

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)
