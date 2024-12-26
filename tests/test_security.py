from http import HTTPStatus

from jwt import decode

<<<<<<< HEAD
from fast_zero.security import create_access_token, settings
=======
from fast_zero.security import create_access_token
from fast_zero.settings import Settings

settings = Settings()
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(
        token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )

    assert decoded['test'] == data['test']
    assert decoded['exp']


def test_jwt_invalid_token(client):
    response = client.delete(
<<<<<<< HEAD
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
=======
        '/users/1', headers={'Authorization': 'Bearer.token.invalid'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Not authenticated'}
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
