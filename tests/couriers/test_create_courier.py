import requests
import allure
from data import Urls, generate_random_string


class TestCreateCourier:
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        payload = {
            "login": generate_random_string(),
            "password": generate_random_string(),
            "firstName": generate_random_string()
        }

        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_URL}', data=payload)
        assert response.status_code == 201
        assert "ok" in response.json()

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, create_and_delete_courier):
        login, password, first_name = create_and_delete_courier
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_URL}', data=payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Ошибки при создании курьера без обязательных полей (без пароля)")
    def test_create_courier_missing_password(self):
        payload = {
            "login": generate_random_string(),
            "firstName": generate_random_string()
        }
        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_URL}', data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"

    @allure.title("Ошибки при создании курьера без обязательных полей (без логина)")
    def test_create_courier_missing_login(self):
        payload = {
            "password": generate_random_string(),
            "firstName": generate_random_string()
        }
        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_URL}', data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"

