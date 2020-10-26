# В этом файле произведены действия над тестовой датой перевод в json и обратно.
# Честно говоря пока не знаю, как проводить аналогичные действия с файлами из вне т.к при генерации
# с помощью jsonpickle добавляется указание на использующийся класс
from model.input import input
import os.path
import jsonpickle
from fixture.test_function import Test_function
import random
import string

#Добавляю выборку и провожу изменения формата в json и обратно
before_json_test_data_set1=[input(client_id=1,item_ids=[1,2,5,6],
                                  order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
                                  client_list=[1,2,3,4,5,6], item_list=[1,2,3,4]),
input(client_id=1,item_ids=[1,5,6,7],
      order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
      client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Путь до генерируемого файла
file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"client_list.json")
#Запись файла в json
with open(file,"w") as out:
    jsonpickle.set_encoder_options("json",indent=2)
    out.write(jsonpickle.encode(before_json_test_data_set1))
#вывод данных из json
test_data_set1=Test_function.load_form_json()

#Дальше идет дата для различных тестов Positive
test1_duplicate_meanings=[
input(client_id=1,item_ids=[1,1,1,1],
      order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
      client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])

]
#Указано только 1 Item
only_one_item=[
input(client_id=1,item_ids=[1],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указано несколько Itemс все валидные
several_valid_items=[
input(client_id=1,item_ids=[1,2],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
# Тест с частью итемов, которых не существует был первым
#------------------------------------------------------------------------------------------------------
#                                      Negative
#  Негатив по полю Client ID
#Указаного клиента не существует, указанное значение clientID=int
clientID_out_of_ClientList=[
input(client_id=7,item_ids=[1,2,5,6],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного клиента не существует, указанное значение clientID=0
clientID_is_0=[
input(client_id=0,item_ids=[1,2,5,6],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного клиента не существует, указанное значение clientID отрицательное
clientID_is_negative=[
input(client_id=-7,item_ids=[1,2,5,6],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного клиента не существует, указанное значение clientID дробное
clientID_is_float=[
input(client_id=7.8,item_ids=[1,2,5,6],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного клиента не существует, указанное значение clientID str
clientID_is_str=[
input(client_id="asdqwe",item_ids=[1,2,5,6],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного клиента не существует, указанное значение clientID empty
clientID_is_empty=[
input(client_id="",item_ids=[1,2,5,6],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного клиента не существует, указанное значение clientID None
clientID_is_None=[
input(client_id=None,item_ids=[1,2,5,6],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]

#указанное значение clientID - пустой список
clientID_is_empty_list=[
input(client_id=[],item_ids=[1,2,5,6],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#указанное значение clientID - список
clientID_is_list=[
input(client_id=[1,2],item_ids=[1,2,5,6],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Пробовать переберать различные значения внутри списка не вижу смысла
#====================================================================================================
#  Негатив по полю item_ids
#Указаного item не существует, указанное значение item=int
itemID_out_of_ClientList=[
input(client_id=1,item_ids=[6],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного item не существует, указанное значение item_ids=0
itemID_is_0=[
input(client_id=1,item_ids=[0],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного item не существует, указанное значение item отрицательное
itemID_is_negative=[
input(client_id=1,item_ids=[-1],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного item не существует, указанное значение item дробное
itemID_is_float=[
input(client_id=1,item_ids=[1.6],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного item не существует, указанное значение item str
itemID_is_str=[
input(client_id=1,item_ids=["qwesda"],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного item не существует, указанное значение item empty
itemID_is_empty=[
input(client_id=1,item_ids=[],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного item не существует, указанное значение item None
itemID_is_None=[
input(client_id=1,item_ids=None,
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#====================================================================================================
#Негатив для Item_ids, но остальная часть списка валидная
#Указаного item не существует, указанное значение item=int
first_ID_out_of_range=[
input(client_id=1,item_ids=[6,1],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного item не существует, указанное значение clientID=0
first_ID_is_0=[
input(client_id=1,item_ids=[0,1],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного item не существует, указанное значение item отрицательное
first_ID_is_negative=[
input(client_id=1,item_ids=[-1,1],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного item не существует, указанное значение item дробное
first_ID_is_float=[
input(client_id=1,item_ids=[1.6,1],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного item не существует, указанное значение item str
first_ID_is_str=[
input(client_id=1,item_ids=["qwesda",1],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#====================================================================================================
#  Негатив по всем полям, добавлю пару сценариев,
#  т.к это не очень актуально и на мой взгляд имеет смысл если создать какой-нибудь генератор
#Указаного item не существует, указанное значение item дробное, а клаентайди =0
itemID_float_ClientID_0=[
input(client_id=0,item_ids=[1.6,1],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
]
#Указаного item не существует, указанное значение item str, а клайент айди -1
itemID_str_ClientID_negative=[
input(client_id=-1,item_ids=["qwesda",1],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4])
    ]

#====================================================================================================
#Совсем чуть чуть рандома т.к комбинации я не перебирал и часть символов также без учета
def random_value(maxlen):
        symbols=string.ascii_letters+string.punctuation+" "+string.digits
        return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
random_data_with_several_items=[
input(client_id=random_value(10),item_ids=[random_value(2),random_value(5),random_value(3)],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4]) for i in range(5)
]
random_data_with_one_item=[
input(client_id=random_value(10),item_ids=[random_value(2)],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4]) for i in range(5)
]

#====================================================================================================
# тесты с пустыми данными
# пустой список клиентов
empty_client_list=[
input(client_id=1,item_ids=[2,1],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[], item_list=[1,2,3,4]),
input(client_id=2,item_ids=[6,1],
        order_list=[],
        client_list=[], item_list=[1,2,3,4]),
input(client_id=2,item_ids=[6,1],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[], item_list=[]),
input(client_id=2,item_ids=[6,1],
        order_list=[],
        client_list=[], item_list=[])
]
# пустой список итемов
empty_items_list=[
input(client_id=1,item_ids=[2,1],
        order_list=[[1,[2,12,12],1,1],[1,[2,12,12],2,2],[1,[1,12,12],3,3]],
        client_list=[1,2,3,4,5,6], item_list=[]),
input(client_id=2,item_ids=[6,1],
        order_list=[],
        client_list=[1,2,3,4,5,6], item_list=[]),
]

# пустой список ордеров
empty_orders_list=[
input(client_id=1,item_ids=[2,1],
        order_list=[],
        client_list=[1,2,3,4,5,6], item_list=[1,2,3,4]),
]