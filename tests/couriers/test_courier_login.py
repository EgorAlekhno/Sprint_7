import requests
import allure
from data import Urls


class TestCourierLogin:
    @allure.title("Успешная авторизация курьера")
    def test_successful_courier_login(self, create_and_login_courier):
        login = create_and_login_courier['login']
        password = create_and_login_courier['password']

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIERS_URL}{Urls.LOGIN}", data=payload)

        assert response.status_code == 200
        assert "id" in response.json(), "В ответе нет ID курьера"

    @allure.title("Попытка авторизация курьера с неверным логином")
    def test_authorization_with_invalid_login(self, create_and_login_courier):
        login = 'invalid_login'
        password = create_and_login_courier['password']

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIERS_URL}{Urls.LOGIN}", data=payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Попытка авторизации с неверным паролем")
    def test_authorization_with_invalid_password(self, create_and_login_courier):
        login = create_and_login_courier['login']
        password = "wrong_password"

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIERS_URL}{Urls.LOGIN}", data=payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Попытка авторизации без логина")
    def test_authorization_without_login(self, create_and_login_courier):
        login = ''
        password = create_and_login_courier['password']

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIERS_URL}{Urls.LOGIN}", data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Попытка авторизации без пароля")
    def test_authorization_without_password(self, create_and_login_courier):
        login = create_and_login_courier['login']
        password = ''

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIERS_URL}{Urls.LOGIN}", data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Попытка авторизации без логина и пароля")
    def test_authorization_without_login_and_password(self):
        login = ''
        password = ''

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIERS_URL}{Urls.LOGIN}", data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"


