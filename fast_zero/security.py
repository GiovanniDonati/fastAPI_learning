from datetime import datetime, timedelta
from http import HTTPStatus
from zoneinfo import ZoneInfo

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
<<<<<<< HEAD
from jwt import DecodeError, ExpiredSignatureError, decode, encode
=======
from jwt import decode, encode
from jwt.exceptions import PyJWKError
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import User
<<<<<<< HEAD
from fast_zero.schemas import TokenData
from fast_zero.settings import Settings

settings = Settings()
pwd_context = PasswordHash.recommended()


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({'exp': expire})
    encoded_jwt = encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt
=======
from fast_zero.settings import Settings

pwd_context = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/token')

settings = Settings()
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


<<<<<<< HEAD
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/token')
=======
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({'exp': expire})

    encoded_jwt = encode(
        to_encode, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6


def get_current_user(
    session: Session = Depends(get_session),
    token: str = Depends(oauth2_scheme),
):
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
<<<<<<< HEAD

    try:
        payload = decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get('sub')
        if not username:
            raise credentials_exception
        token_data = TokenData(username=username)
    except DecodeError:
        raise credentials_exception
    except ExpiredSignatureError:
        raise credentials_exception

    user = session.scalar(
        select(User).where(User.email == token_data.username)
    )

    if not user:
        raise credentials_exception

    return user
=======
    try:
        payload = decode(
            token, key=settings.SECRET_KEY, algorithms=settings.ALGORITHM
        )
        username: str = payload.get('sub')

        if not username:
            raise credentials_exception
    except PyJWKError:
        raise credentials_exception

    user_db = session.scalar(select(User).where(User.email == username))
    if user_db is None:
        raise credentials_exception

    return user_db
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
