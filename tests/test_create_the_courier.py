import allure
import requests
from endpoint import Endpoint
from url import Url
from gen import registrations_new_courier as gener
from gen import registrations_new_courier_without_login as gener_without_login
from gen import registrations_new_courier_without_password as gener_without_password


class TestCreateCourier:
    data = gener()

    @allure.title('Создание курьера')
    def test_create_courier(self):
        response_body = '{"ok":true}'
        response = requests.post(
            f'{Url.URL}{Endpoint.CREATE_COURIER}',
            TestCreateCourier.data)
        assert response.status_code == 201 and response.text == response_body

    @allure.title('Нельзя создать двух одинаковых курьеров с одинаковыми логинами')
    def test_courier_was_created(self):
        response = requests.post(
            f'{Url.URL}{Endpoint.CREATE_COURIER}',
            TestCreateCourier.data)
        assert response.status_code == 409 and 'Этот логин уже используется' in response.text

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login(self):
        response = requests.post(
            f'{Url.URL}{Endpoint.CREATE_COURIER}',
            gener_without_login())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password(self):
        response = requests.post(
            f'{Url.URL}{Endpoint.CREATE_COURIER}',
            gener_without_password())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text