from http import HTTPStatus
from jwt import decode

from fast_zero.security import ALGORITHM, SECRET_KEY, create_access_token


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    assert decoded['test'] == data['test']
    assert decoded['exp']


def test_invalid_token(client):
    response = client.delete(
        '/user/1', headers={'Authorization' : 'Bearer token-invalid'}
    )
    
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail' : 'Could not validate credentials'}