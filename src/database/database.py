from sqlcipher3 import dbapi2 as sqlite
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from model import Base, User
from src.config import Config
from src.message import Message

class Database:
    def __init__(self, password):
        self.db_url = f"sqlite+pysqlcipher://:{password}/{Config.database_path}?cipher=aes-256-cfb&kdf_iter=400000"
        self.engine = create_engine(self.db_url, module=sqlite)
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

    def Update(self, id: int, username: str = "", password: str = "", comments: str = "") -> None:
        with Session(self.engine) as session:
            user = session.get(User, id)
            if username and user:
                user.name = username

            if password and user:
                user.password = password

            if comments and user:
                user.comments = comments


    def Query_one(self, id: int):
        with Session(self.engine) as session:
            user = session.get(User, id)

            if user:
                Message.Query_result(id= user.id, name= user.name, password= user.password, comments= user.comments)
            else:
                Message.Failure("User not found!")


    def Query_all(self):
        with Session(self.engine) as session:
            users = session.query(User).order_by(User.id).all()
            for user in users:
                Message.Query_result(id= user.id, name= user.name, password= user.password, comments= user.comments)
                print("\n" + "-"*20 + "\n")


    def Remove(self, id):
        with Session(self.engine) as session:
            user = session.get(User, id)
            session.remove(user)


    def Close(self):
        self.engine.dispose()

