from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String)

class AuthSystem:
    def __init__(self, session):
        self.session = session

    def register(self, username, email):
        user = User(username=username, email=email)
        self.session.add(user)
        self.session.commit()
        return user

    def authenticate(self, username, email):
        return (
            self.session.query(User)
            .filter_by(username=username, email=email)
            .first()
        )

