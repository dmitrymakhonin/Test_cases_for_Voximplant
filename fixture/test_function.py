import os.path
import jsonpickle
# "items": ["item_id" "purchased" "last_order_number"
# "last_purchase_date": "2020-01-16T13:33:00.000Z","purchase_count"]
# [client_id,[item_id,price,quantity],order_id,order_number]
# Ордер намбер - сквозная последовательность номеров для ордеров для всех клиентов

class Test_function:
    def my_request(input):
        if Test_function.clients(input.client_list)==True:
            return "В системе нет клиентов"
        if Test_function.items(input.item_list)==True:
            return "В системе нет итемов"
        if Test_function.orders(input.order_list)==True:
            return "В системе нет ордеров"
        Response = []
        list_of_ids_clients=[]
        new_order_list = []
        #проверка, что запрашиваемый клиент существует
        if input.client_id in input.client_list:
        #Создание списка включаещего только айтемс для указаного клиента
            Test_function.create_list_of_current_client(list_of_ids_clients, input.client_id, new_order_list,input.order_list)
        # Проверка что у данного клиента были заказы
            if input.client_id in list_of_ids_clients:
        #Создание ответа для клиента у когорого были заказы
                Test_function.create_response(input.item_ids, new_order_list,Response,input.item_list)
            else:
                Response="Клиент с ID%s не делал заказов" % input.client_id
        else:
            Response = "Клиент с ID%s не существует" % input.client_id
        return Response


    def create_response(item_ids,  new_order_list, Response, item_list):
        purchased = None
        last_purchase_date = "today"
        last_order_number = None
    # Цикл, который проходит по кажому ItemID из запроса и определяет значения,
        # которые мы должны получить в результате
        for element in range(len(item_ids)):
            purchase_count = 0
            for i in new_order_list:
                # для каждого ID из запроса определяется номер заказа и кол-во покупок
                if item_ids[element] == i[1][0]:
                    last_order_number = i[3] # отработает неверно если в new_order_list не верный порядок
                    purchase_count += 1
                # для каждого ID из запроса определяется были ли совершены покупки или нет
                if purchase_count > 0:
                    purchased = True
                else:
                    purchased = False
            # проверка на существование вещи указанной в запросе
            if item_ids[element] in item_list:
                Response.append([item_ids[element], purchased, last_order_number,
                                 last_purchase_date, purchase_count ])
            else:
                Response.append("Продукта с ID%s не существует" % item_ids[element])


    def create_list_of_current_client(list_of_ids_clients, client_id, new_order_list,order_list):
        # создание списка, по клиентам из заспроса
        for i in order_list:
            if i[0] == client_id:
                list_of_ids_clients.append(i[0])
                new_order_list.append(i)

    def load_form_json():
        with open("C:\Test_cases_Voximplant\data\client_list.json") as f:
            return jsonpickle.decode(f.read())

    def clients(client_list):
        if client_list==[]:
            return True
    def items(item_list):
        if item_list==[]:
            return True
    def orders(order_list):
        if order_list==[]:
            return True