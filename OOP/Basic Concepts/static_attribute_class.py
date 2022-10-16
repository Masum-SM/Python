class shop:
    cart = []
    def __init__(self,buyer):
        self.buyer = buyer
    
    def add_to_card(self,item):
        self.cart.append(item)

shopper_1 = shop("Nawrin")
shopper_1.add_to_card("lipstric")
print(shopper_1.cart)
shopper_2 = shop("Masum")
shopper_2.add_to_card("Laptop")
print(shopper_2.cart) #problem is, item of shopper_1 shown in shopper_2's item because of static card.