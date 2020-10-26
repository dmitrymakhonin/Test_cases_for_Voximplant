from data.test_data import *
import pytest

#  Негатив по полю Client ID
#Указаного клиента не существует, указанное значение clientID=int
@pytest.mark.parametrize("input",clientID_out_of_ClientList,ids=[repr(x) for x in clientID_out_of_ClientList])
def test_clientID_out_of_ClientList(req,input):
    b= req.my_request(input)
    a="Клиент с ID%s не существует" % input.client_id
    assert req.my_request(input)==a
#Указаного клиента не существует, указанное значение clientID=0
@pytest.mark.parametrize("input",clientID_is_0,ids=[repr(x) for x in clientID_is_0])
def test_clientID_is_0(req,input):
    b= req.my_request(input)
    a="Клиент с ID%s не существует" % input.client_id
    assert req.my_request(input)==a
#Указаного клиента не существует, указанное значение clientID отрицательное
@pytest.mark.parametrize("input",clientID_is_negative,ids=[repr(x) for x in clientID_is_negative])
def test_clientID_is_negative(req,input):
    b= req.my_request(input)
    a="Клиент с ID%s не существует" % input.client_id
    assert req.my_request(input)==a
#Указаного клиента не существует, указанное значение clientID дробное
@pytest.mark.parametrize("input",clientID_is_float,ids=[repr(x) for x in clientID_is_float])
def test_clientID_is_float(req,input):
    b= req.my_request(input)
    a="Клиент с ID%s не существует" % input.client_id
    assert req.my_request(input)==a
#Указаного клиента не существует, указанное значение clientID str
@pytest.mark.parametrize("input",clientID_is_str,ids=[repr(x) for x in clientID_is_str])
def test_clientID_is_str(req,input):
    b= req.my_request(input)
    a="Клиент с ID%s не существует" % input.client_id
    assert req.my_request(input)==a
#Указаного клиента не существует, указанное значение clientID empty
@pytest.mark.parametrize("input",clientID_is_empty,ids=[repr(x) for x in clientID_is_empty])
def test_clientID_is_empty(req,input):
    b= req.my_request(input)
    a="Клиент с ID%s не существует" % input.client_id
    assert req.my_request(input)==a
#Указаного клиента не существует, указанное значение clientID None
@pytest.mark.parametrize("input",clientID_is_None,ids=[repr(x) for x in clientID_is_None])
def test_clientID_is_None(req,input):
    b= req.my_request(input)
    a="Клиент с ID%s не существует" % input.client_id
    assert req.my_request(input)==a
#указанное значение clientID - пустой список
@pytest.mark.parametrize("input",clientID_is_empty_list,ids=[repr(x) for x in clientID_is_empty_list])
def test_clientID_is_empty_list(req,input):
    b= req.my_request(input)
    a="Клиент с ID%s не существует" % input.client_id
    assert req.my_request(input)==a
#указанное значение clientID - список
@pytest.mark.parametrize("input",clientID_is_list,ids=[repr(x) for x in clientID_is_list])
def test_clientID_is_list(req,input):
    b= req.my_request(input)
    a="Клиент с ID%s не существует" % input.client_id
    assert req.my_request(input)==a
#Все тесты выше можно было параметризировать и вместо 50 строчек получилось бы 10,
# ноооооо я подумал об этом после того как сделал, однако в случае реальной системы сильно сомневаюсь,
# что все экпектед резалты будут одинаковыми
#---------------------------------------------------------------------------------------------------------
#  Негатив по полю Item ID
#Указаного item не существует, указанное значение item=int
@pytest.mark.parametrize("input",itemID_out_of_ClientList,ids=[repr(x) for x in itemID_out_of_ClientList])
def test_itemID_out_of_ClientList(req,input):
    b= req.my_request(input)
    a=['Продукта с ID6 не существует']
    assert req.my_request(input)==a
#Указаного item не существует, указанное значение item_ids=0
@pytest.mark.parametrize("input",itemID_is_0,ids=[repr(x) for x in itemID_is_0])
def test_itemID_is_0(req,input):
    b= req.my_request(input)
    a=['Продукта с ID0 не существует']
    assert req.my_request(input)==a
#Указаного item не существует, указанное значение item отрицательное
@pytest.mark.parametrize("input",itemID_is_negative,ids=[repr(x) for x in itemID_is_negative])
def test_itemID_is_negative(req,input):
    b= req.my_request(input)
    a=['Продукта с ID-1 не существует']
    assert req.my_request(input)==a
#Указаного item не существует, указанное значение item дробное
@pytest.mark.parametrize("input",itemID_is_float,ids=[repr(x) for x in itemID_is_float])
def test_itemID_is_float(req,input):
    b= req.my_request(input)
    a=['Продукта с ID1.6 не существует']
    assert req.my_request(input)==a
#Указаного item не существует, указанное значение item str
@pytest.mark.parametrize("input",itemID_is_str,ids=[repr(x) for x in itemID_is_str])
def test_itemID_is_str(req,input):
    b= req.my_request(input)
    a=['Продукта с IDqwesda не существует']
    assert req.my_request(input)==a
#Указаного item не существует, указанное значение item str
@pytest.mark.parametrize("input",itemID_is_empty,ids=[repr(x) for x in itemID_is_empty])
def test_itemID_is_empty(req,input):
    b= req.my_request(input)
    a=[]
    assert req.my_request(input)==a
#Указаного item не существует, указанное значение item None
@pytest.mark.parametrize("input",itemID_is_None,ids=[repr(x) for x in itemID_is_None])
def test_itemID_is_None(req,input):
    try:
        b=req.my_request(input)
    except TypeError: #Ловлю тайп ерор т.к в функции идео топределение длины из itemID, который = None
        a=[]
    assert a==[]
#-----------------------------------------------------------------------------------------------------
#Негатив для Item_ids, но остальная часть списка валидная
#Указаного item не существует, указанное значение item=int
@pytest.mark.parametrize("input",first_ID_out_of_range,ids=[repr(x) for x in first_ID_out_of_range])
def test_first_ID_out_of_range(req,input):
    b= req.my_request(input)
    a=['Продукта с ID6 не существует', [1, True, 3, 'today', 1]]
    assert req.my_request(input)==a
#Указаного item не существует, указанное значение clientID=0
@pytest.mark.parametrize("input",first_ID_is_0,ids=[repr(x) for x in first_ID_is_0])
def test_first_ID_is_0(req,input):
    b= req.my_request(input)
    a=['Продукта с ID0 не существует', [1, True, 3, 'today', 1]]
    assert req.my_request(input)==a
#Указаного item не существует, указанное значение item отрицательное
@pytest.mark.parametrize("input",first_ID_is_negative,ids=[repr(x) for x in first_ID_is_negative])
def test_first_ID_is_negative(req,input):
    b= req.my_request(input)
    a=['Продукта с ID-1 не существует', [1, True, 3, 'today', 1]]
    assert req.my_request(input)==a
#Указаного item не существует, указанное значение item дробное
@pytest.mark.parametrize("input",first_ID_is_float,ids=[repr(x) for x in first_ID_is_float])
def test_first_ID_is_float(req,input):
    b= req.my_request(input)
    a=['Продукта с ID1.6 не существует', [1, True, 3, 'today', 1]]
    assert req.my_request(input)==a
#Указаного item не существует, указанное значение item str
@pytest.mark.parametrize("input",first_ID_is_str,ids=[repr(x) for x in first_ID_is_str])
def test_first_ID_is_str(req,input):
    b= req.my_request(input)
    a=['Продукта с IDqwesda не существует', [1, True, 3, 'today', 1]]
    assert req.my_request(input)==a
#====================================================================================================
#  Негатив по всем полям, добавлю пару сценариев,
#  т.к это не очень актуально и на мой взгляд имеет смысл если создать какой-нибудь генератор
#Указаного item не существует, указанное значение item дробное, а клаентайди =0
@pytest.mark.parametrize("input",itemID_float_ClientID_0,ids=[repr(x) for x in itemID_float_ClientID_0])
def test_itemID_float_ClientID_0(req,input):
    b= req.my_request(input)
    a='Клиент с ID0 не существует'
    assert req.my_request(input)==a
#Указаного item не существует, указанное значение item дробное, а клаентайди =0
@pytest.mark.parametrize("input",itemID_str_ClientID_negative,ids=[repr(x) for x in itemID_str_ClientID_negative])
def test_itemID_str_ClientID_negative(req,input):
    b= req.my_request(input)
    a='Клиент с ID-1 не существует'
    assert req.my_request(input)==a