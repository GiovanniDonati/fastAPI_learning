from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.models import User, table_registry


def test_create_user():
    engine = create_engine('sqlite:///database.db')

    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(user='Giovanni', email='gr@donati.com', password='123')

        session.add(user)
        session.commit()
        session.refresh(user)

    assert user.id == 1
