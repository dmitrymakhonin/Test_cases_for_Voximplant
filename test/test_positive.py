from data.test_data import *
import pytest


#Позитивный сценарий с повторяющимися ItemsID
@pytest.mark.parametrize("input",test1_duplicate_meanings,ids=[repr(x) for x in test1_duplicate_meanings])
def test_for_duplicate(req,input):
    b= req.my_request(input)
    a=[[1, True, 3, 'today', 1], [1, True, 3, 'today', 1], [1, True, 3, 'today', 1], [1, True, 3, 'today', 1]]
    assert req.my_request(input)==a
#все тесты будут заданы отдельной функцией, чтобы в отчете они были разделены, это поможет в их анализе
# в случае фейла
#Указано только 1 Item
@pytest.mark.parametrize("input",only_one_item,ids=[repr(x) for x in only_one_item])
def test_only_one_item(req,input):
    b= req.my_request(input)
    a=[[1, True, 3, 'today', 1]]
    assert req.my_request(input)==a
#Указано несколько Items все валидные
@pytest.mark.parametrize("input",several_valid_items,ids=[repr(x) for x in several_valid_items])
def test_several_valid_items(req,input):
    b= req.my_request(input)
    a=[[1, True, 3, 'today', 1],[2, True, 2, 'today', 2]]
    assert req.my_request(input)==a
