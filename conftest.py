import pytest
import requests
from data import register_new_courier_and_return_login_password, Urls


@pytest.fixture
def create_and_delete_courier():
    credentials = register_new_courier_and_return_login_password()
    yield credentials
    if credentials:
        login, password, _ = credentials
        login_response = requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_URL}{Urls.LOGIN}', data={'login': login, 'password': password})
        courier_id = login_response.json().get('id')
        if courier_id:
            requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier{courier_id}')


@pytest.fixture
def create_and_login_courier():
    credentials = register_new_courier_and_return_login_password()
    if not credentials:
        pytest.fail("Не удалось зарегистрировать курьера")
    login, password, _ = credentials

    login_response = requests.post(
        f'{Urls.BASE_URL}courier/login',
        data={'login': login, 'password': password}
    )

    if login_response.status_code != 200 or 'id' not in login_response.json():
        pytest.fail("Не удалось авторизовать курьера")

    courier_id = login_response.json()['id']

    yield {
        "login": login,
        "password": password,
        "id": courier_id
    }

    requests.delete(f'{Urls.BASE_URL}courier/{courier_id}')
