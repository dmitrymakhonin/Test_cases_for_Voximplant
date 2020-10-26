from data.test_data import *
import pytest
# Кроме тестов, которые расположены в текущем проекте возможно добавление доп. тестов к примеру,
# раз это абстрактная функция, ограничение по ClientID >=1 и <=999, кол-во допустимых Items в одном запросе
# т.е тесты на все возможные условия, которые можно придумать

@pytest.mark.parametrize("input",test_data_set1,ids=[repr(x) for x in test_data_set1])
#Тест, который использует параметры, содержит позитивный сценарий и негативный для примера
def test_for_check(req,input):
    a=[[1, True, 3, 'today', 1], [2, True, 2, 'today', 2], 'Продукта с ID5 не существует', 'Продукта с ID6 не существует']
    assert req.my_request(input)==a
# Проверка форматов полученных данных (Неудачная попытка) Проверка всех типов переменных,
# кроме даты возможно провести при сравнении с экспектед резалтс
#@pytest.mark.parametrize("input",test_data_set1,ids=[repr(x) for x in test_data_set1])
#def test_format_of_values(req,input):
#   b = req.my_request(input)
#   assert b[0] == str


