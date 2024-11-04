import json
import allure
import pytest
import requests
from data import Orders
from endpoint import Endpoint
from url import Url


class TestCreateOrder:

    @pytest.mark.parametrize('order_data', [{"color": ["BLACK"]}, {"color": ["GREY"]}, {"color": [""]}, {"color": ["BLACK", "GREY"]}])
    @allure.title('Создание заказа')
    def test_create_order(self, order_data):
        Orders.data_order.update(order_data)
        order_data = json.dumps(Orders.data_order)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{Url.URL}{Endpoint.CREATE_ORDER}', data=order_data, headers=headers)
        assert response.status_code == 201 and 'track' in response.text