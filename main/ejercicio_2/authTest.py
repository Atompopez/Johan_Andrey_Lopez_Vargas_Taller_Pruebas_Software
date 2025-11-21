import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from auth import Base, AuthSystem, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_registration_and_authentication(db):
    name = "johan"
    email = "johan@example.com"
    auth = AuthSystem(db)

    user = auth.register(name, email)

    assert str(user.username) == name
    assert str(user.email) == email

    authenticated = auth.authenticate(name, email)
    assert authenticated is not None
    assert str(authenticated.username) == name