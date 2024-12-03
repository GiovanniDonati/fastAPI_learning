from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_read_root():
    assert {'message': 'Welcome to my aplicattion!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'user': 'Giovanni',
            'email': 'teste@teste.com.br',
            'password': 'teste',
        },
    )  # Act (ação)

    assert response.status_code == HTTPStatus.CREATED  # Assert (conferencia)
    assert response.json() == {
        'id': 1,
        'user': 'Giovanni',
        'email': 'teste@teste.com.br',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'id': user.id,
            'user': 'Donati',
            'email': 'teste@teste.com.br',
            'password': '123',
        },
    )

    print(response.json())
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': user.id,
        'user': 'Donati',
        'email': 'teste@teste.com.br',
    }


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        )

    # assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}


def test_get_token(client, user):
    response = client.post(
        '/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token
