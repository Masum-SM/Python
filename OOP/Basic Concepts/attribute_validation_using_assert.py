"""  
Assert :
Definition and Usage. The assert keyword is used when debugging code. The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError. You can write a message to be written if the code returns False, check the example below.

"""

class Item:
    def __init__(self,item_name, item_price, item_quantity) -> None:
        self.item_name = item_name
        assert item_price > 0, f'Price should be more than zero'
        self.item_price = item_price
        assert item_quantity > 0, f'Quantity should be more than zero'
        self.item_quantity = item_quantity

    
    """ 
    In Python, __repr__ is a special method used to represent a class’s objects as a string. __repr__ is called by the repr() built-in function. You can define your own string representation of your class objects using the __repr__ method.
    """
    def __repr__(self) -> str:
        return(f'Item Name : {self.item_name}, Item Price : {self.item_price}, Item Quantity : {self.item_quantity}')


items = Item('Mouse',700,0)
print(items)