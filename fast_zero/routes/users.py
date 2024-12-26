from http import HTTPStatus
from typing import Annotated

<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
=======
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import User
<<<<<<< HEAD
from fast_zero.schemas import (
    FilterPage,
    Message,
    UserList,
    UserPublic,
    UserSchema,
)
=======
from fast_zero.schemas import Message, UserList, UserPublic, UserSchema
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
from fast_zero.security import (
    get_current_user,
    get_password_hash,
)

router = APIRouter(prefix='/users', tags=['users'])
<<<<<<< HEAD
Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: Session):
    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
=======
T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[User, Depends(get_current_user)]


@router.get('/', response_model=UserList)
def read_users(session: T_Session, limit: int = 10, skip: int = 0):
    user = session.scalars(select(User).limit(limit).offset(skip))
    return {'users': user}


@router.get('/{id}', response_model=UserPublic)
def read_user(id: int, session: T_Session):
    user = session.scalar(select(User).where(User.id == id))
    return user


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: T_Session):
    db_user = session.scalar(
        select(User).where(
            (User.user == user.user) | (User.email == user.email)
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
        )
    )

    if db_user:
<<<<<<< HEAD
        if db_user.username == user.username:
=======
        if db_user.user == user.user:
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Username already exists',
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email already exists',
            )

    hashed_password = get_password_hash(user.password)

    db_user = User(
        email=user.email,
<<<<<<< HEAD
        username=user.username,
=======
        user=user.user,
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
        password=hashed_password,
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


<<<<<<< HEAD
@router.get('/', response_model=UserList)
def read_users(session: Session, filter_users: Annotated[FilterPage, Query()]):
    users = session.scalars(
        select(User).offset(filter_users.offset).limit(filter_users.limit)
    ).all()

    return {'users': users}


=======
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
@router.put('/{user_id}', response_model=UserPublic)
def update_user(
    user_id: int,
    user: UserSchema,
<<<<<<< HEAD
    session: Session,
    current_user: CurrentUser,
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permissions'
        )

    try:
        current_user.username = user.username
        current_user.password = get_password_hash(user.password)
        current_user.email = user.email
        session.commit()
        session.refresh(current_user)

        return current_user

    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Username or Email already exists',
        )
=======
    session: T_Session,
    current_user: T_CurrentUser,
):
    current_user.user = user.user
    current_user.email = user.email
    current_user.password = get_password_hash(user.password)

    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permission'
        )

    session.commit()
    session.refresh(current_user)

    return current_user
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6


@router.delete('/{user_id}', response_model=Message)
def delete_user(
    user_id: int,
<<<<<<< HEAD
    session: Session,
    current_user: CurrentUser,
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permissions'
=======
    session: T_Session,
    current_user: T_CurrentUser,
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permission'
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
        )

    session.delete(current_user)
    session.commit()

<<<<<<< HEAD
    return {'message': 'User deleted'}
=======
    return {'message': 'User deleted!'}
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
