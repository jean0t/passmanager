from sqlcipher3 import dbapi2 as sqlite
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from src.database.model import Base, User
from src.config import Config
from src.message import Message


class Database:
    def __init__(self, password):
        self.db_url = f"sqlite+pysqlcipher://:{str(password)}@/{Config.database_path}?cipher=aes-256-cfb&kdf_iter=400000"
        self.engine = create_engine(self.db_url, module=sqlite)
        self.query = None
        Base.metadata.create_all(self.engine)

    def Add(self, username: str, password: str, comments: str) -> None:
        with Session(self.engine) as session:
            if username and password:
                user = User(
                    name=username,
                    password=password,
                    comments=comments,
                )
                session.add(user)
                session.commit()

    def Update(
        self, id: int, username: str = "", password: str = "", comments: str = ""
    ) -> None:
        with Session(self.engine) as session:
            user = session.get(User, id)
            if username and user:
                user.name = username

            if password and user:
                user.password = password

            if comments and user:
                user.comments = comments

            session.commit()

    def Query_one(self, id: int):
        with Session(self.engine) as session:
            self.query = session.get(User, id)

        return self.query

    def Query_all(self):
        with Session(self.engine) as session:
            self.query = session.query(User).all()

        return self.query

    def Remove(self, id):
        with Session(self.engine) as session:
            user = session.get(User, id)
            session.delete(user)
            session.commit()

    def Close(self):
        self.engine.dispose()
