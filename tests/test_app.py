from http import HTTPStatus


<<<<<<< HEAD
def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
=======
def test_read_root(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert {'message': 'Welcome to my aplicattion!'}
>>>>>>> e86f40ec1b724c3ac842dfe055c887bf307915c6
