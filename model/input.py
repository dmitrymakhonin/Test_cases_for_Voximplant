class input:
    def __init__(self, client_id=None, item_ids=[],order_list=[],client_list=[],item_list=[]):
        self.client_id=client_id
        self.item_ids=item_ids
        self.order_list = order_list
        self.client_list = client_list
        self.item_list = item_list

#Описание о том в каком виде предоставляется информация о элемнтах класса
    def __repr__(self):
        return "client_id=%s item_ids=%s "%(self.client_id,self.item_ids)


#Не уверен что работает для вложенных списков, почти уверен, что не работает
    def __eq__(self, other):
        return  self.client_id==other.client_id and self.item_ids==other.item_ids \
                and self.client_list==other.client_list and self.item_list==other.item_list and self.order_list==other.order_list


