import requests
import random
import string


class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    ORDERS_URL = '/orders'
    COURIERS_URL = '/courier'
    LOGIN = '/login'


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def register_new_courier_and_return_login_password():
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_URL}', data=payload)

    if response.status_code == 201:
        return [login, password, first_name]
    return []
