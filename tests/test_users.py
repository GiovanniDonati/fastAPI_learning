from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
<<<<<<< HEAD
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
=======
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
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
    }


def test_read_users(client):
<<<<<<< HEAD
    response = client.get('/users')
=======
    response = client.get('/users/')

>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


<<<<<<< HEAD
def test_read_users_with_users(client, user):
=======
def test_read_users_with_user(client, user):
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
<<<<<<< HEAD
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': user.id,
    }


=======
            'id': user.id,
            'user': 'Donati',
            'email': 'teste@teste.com.br',
            'password': '123',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': user.id,
        'user': 'Donati',
        'email': 'teste@teste.com.br',
    }


def test_wrong_user_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id + 1}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'id': user.id,
            'user': 'Donati',
            'email': 'teste@teste.com.br',
            'password': '123',
        },
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permission'}


>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
<<<<<<< HEAD
    assert response.json() == {'message': 'User deleted'}


def test_update_user_with_wrong_user(client, other_user, token):
    response = client.put(
        f'/users/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}


def test_update_integrity_error(client, user, other_user, token):
    response_update = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': other_user.username,
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response_update.status_code == HTTPStatus.CONFLICT
    assert response_update.json() == {
        'detail': 'Username or Email already exists'
    }


def test_delete_user_wrong_user(client, other_user, token):
    response = client.delete(
        f'/users/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}
=======
    assert response.json() == {'message': 'User deleted!'}


def test_wrong_user_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id + 1}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permission'}
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
