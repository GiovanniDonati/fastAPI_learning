from http import HTTPStatus

from sqlalchemy import create_engine,select
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException

from fast_zero.models import User
from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema
from fast_zero.settings import Settings

app = FastAPI()

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message' : 'Welcome to my aplicattion!'}

@app.get('/users/', response_model=UserList)
def read_users():
    pass

@app.get('/users/{id}', response_model=UserPublic)
def read_user(id: int):
    pass

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    engine = create_engine(Settings().DATABASE_URL)

    with Session(engine) as session:
        db_user = session.scalar(
            select(User).where(
                (User.user == user.user) | (User.email == user.email)
            )
        )

        if db_user:
            if db_user.username == user.user:
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST,
                    detail='User already exists'
                )

            elif db_user.email == user.email:
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST,
                    detail='Email already exists'
                )
        
        db_user = User(
            user=user.user, email=user.email, password=user.password
            )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)

    return db_user

@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    pass

@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    pass