"""  
- Class attribute
- Instance attribut
- Adding attribute outside the class by instance
- adding private attribute outside the class
- Accessing private attribute outside the class
"""


class Item:
    all_item = []
    def __init__(self,item_name, item_selling_price,item_buying_price) -> None:
        self.item_name = item_name
        self.item_selling_price = item_selling_price
        self.__item_buying_price = item_buying_price
        self.all_item.append(self)

    def __repr__(self) -> str:
        return f'Item Name : {self.item_name}, Item price : {self.item_selling_price}, Item_buying_price : {self.__item_buying_price} '

item = Item('Watch', 2100,2000)
print(item.item_name) # instance attribute
print(item.all_item) # class attribute

# print(item.__item_buying_price) # giving error,bcz trying to access private class outside the class


# ------------ adding attribute outside the class -----------------
item.discount = 10
print(item.__dict__) # {'item_name': 'Watch', 'item_selling_price': 2100, '_Item__item_buying_price': 2000, 'discount': 10}
print(item.discount)
print(item._Item__item_buying_price) # accecing private class outside the class.

#------------- adding private attribute ------------------------
item._Item__profit = item.item_selling_price - item._Item__item_buying_price # accecing private class outside the class.
print(item.__dict__) # {'item_name': 'Watch', 'item_selling_price': 2100, '_Item__item_buying_price': 2000, 'discount': 10, '_Item__profit': 100}

item2 = Item("Sun glass",1600,1400)
print(Item.all_item) 

print(item.__dict__)
print(item2.__dict__)