import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'main'))
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
    auth = AuthSystem(db)

    user = auth.register("johan", "johan@example.com")

    assert str(user.username) == "johan"
    assert str(user.email) == "johan@example.com"

    authenticated = auth.authenticate("johan", "johan@example.com")
    assert authenticated is not None
    assert str(authenticated.username) == "johan"
