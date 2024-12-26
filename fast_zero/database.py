from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.settings import Settings

engine = create_engine(Settings().DATABASE_URL)


<<<<<<< HEAD
def get_session():
=======
def get_session():  # pragma: no cover
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
    with Session(engine) as session:
        yield session
