from data.test_data import *
import pytest
# В этих тестах описсание результатов не говорящее т.к функция __репр__ описывает только 2 первых элемента
# класса, чтобы не быть очень большой
# пустой список клиентов
@pytest.mark.parametrize("input",empty_client_list,ids=[repr(x) for x in empty_client_list])
def test_empty_client_list(req,input):
    assert req.my_request(input)=="В системе нет клиентов"
# пустой список итемов
@pytest.mark.parametrize("input",empty_items_list,ids=[repr(x) for x in empty_items_list])
def test_empty_items_list(req,input):
    assert req.my_request(input)=="В системе нет итемов"
# пустой список ордеров
@pytest.mark.parametrize("input",empty_orders_list,ids=[repr(x) for x in empty_orders_list])
def test_empty_orders_list(req,input):
    assert req.my_request(input)=="В системе нет ордеров"