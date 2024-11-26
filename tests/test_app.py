from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'user': 'Giovanni',
            'email': 'teste@teste.com.br',
            'password': '123',
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
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'user': 'Giovanni',
                'email': 'teste@teste.com.br',
            }
        ]
    }


def test_update_users(client):
    response = client.put(
        '/users/1',
        json={
            'id': 1,
            'user': 'Donati',
            'email': 'teste@teste.com.br',
            'password': '123',
        },
    )

    # assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'user': 'Donati',
        'email': 'teste@teste.com.br',
    }


def test_update_users_error(client):
    response = client.put(
        '/users/2',
        json={
            'id': 2,
            'user': 'Donati',
            'email': 'teste@teste.com.br',
            'password': '123',
        },
    )

    # assert response.status_code == HTTPStatus.OK
    assert response.json() == {'detail': 'User not found'}


def test_delete_users(client):
    response = client.delete('/users/1')

    # assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'user deleted!'}


def test_delete_users_eroor(client):
    response = client.delete('/users/1')

    # assert response.status_code == HTTPStatus.OK
    assert response.json() == {'detail': 'User not found'}
