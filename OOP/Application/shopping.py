class shopper:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_card(self,item,quantity,price):
        self.cart.append({'Item':item, 'Quantity':quantity,'Price':price})

    def checkout(self,amount):
        print(self.cart)
        price = 0;
        for item in self.cart:
            price =price + item['Price']*item['Quantity']
        if amount < price:
            return f'Please give me more money : {price-amount}'
        elif price < amount:
            return f"Here is youre product and extra money {amount-price}"
        else:
            return "Here is your product."


shopper1 = shopper("Nawrin")
shopper1.add_to_card("Hijab",2,300)
shopper1.add_to_card("tupi",3,50)
shopper1.add_to_card("groun",1,3000)

reply = shopper1.checkout(750)
print(reply)

# reply1 = shopper1.checkout(5000)
# print(reply1)

# reply2 = shopper1.checkout(3750)
# print(reply2)