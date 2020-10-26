from data.test_data import *
import pytest

#Рандомный тест с несколькими значениями в Item
@pytest.mark.parametrize("input",random_data_with_several_items,ids=[repr(x) for x in random_data_with_several_items])
def test_random_data_with_several_items(req,input):
    assert req.my_request(input)=="Клиент с ID%s не существует" % input.client_id
#Рандомный тест с 1 значением в Item
@pytest.mark.parametrize("input",random_data_with_one_item,ids=[repr(x) for x in random_data_with_one_item])
def test_random_data_with_one_item(req,input):
    assert req.my_request(input)=="Клиент с ID%s не существует" % input.client_id
#-----------------------------------------------------------------------------------------------------
# Тесты под текущее поведение и они псевдо рандомные, вероятность того, что длина поля клайент=1
# и это будет цифра крайне мала, поэтому и тесты пасятся, т.к резалт везде однотипный и не зависит от позиции всписке

