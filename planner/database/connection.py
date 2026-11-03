from sqlmodel import SQLModel, Session, create_engine
from models.events import Event  # noqa: F401  (регистрирует таблицу event)
from models.users import User  # noqa: F401  (регистрирует таблицу user)

database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}
engine = create_engine(
    database_connection_string, echo=True, connect_args=connect_args
)


def conn():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
