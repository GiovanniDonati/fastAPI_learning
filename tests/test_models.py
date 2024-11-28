from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(user='Giovanni', email='gr@donati.com', password='123')

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'gr@donati.com'))

    assert result.user == 'Giovanni'
