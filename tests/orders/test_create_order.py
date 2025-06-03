import pytest
import requests
import allure
from data import Urls


class TestCreateOrder:
    @allure.title("Проверка создания заказа с разными вариантами цвета")
    @pytest.mark.parametrize("color", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK", "GREY"]),
        ([])
    ])
    def test_create_order_with_various_colors(self, color):
        order_data = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "ул. Пушкина, д. Колотушкина",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 5,
            "deliveryDate": "2023-12-31",
            "comment": "Тестовый заказ",
            "color": color
        }

        response = requests.post(f"{Urls.BASE_URL}orders", json=order_data)

        assert response.status_code == 201, f"Ожидали 201, получили {response.status_code}"
        assert "track" in response.json(), "В ответе нет ключа 'track'"

    @allure.title("Проверка получения списка заказов")
    def test_get_orders_list(self):
        response = requests.get(f"{Urls.BASE_URL}{Urls.ORDERS_URL}")

        # Проверка, что статус ответа 200 (успешный)
        assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"

        # Проверка, что в теле ответа есть ключ "orders" и он содержит список
        response_json = response.json()
        assert "orders" in response_json, "Ответ не содержит ключ 'orders'"
        assert isinstance(response_json["orders"], list), "'orders' не является списком"
