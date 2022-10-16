class laptop:
    def __init__(self,brand,price):
        self.brand =brand
        self.price = price


    def increase_price(self,price=1):
        self.last_p = self.price
        self.price = self.price+price


    def dec_price(self,dec_p=-5000):
        self.increase_price(dec_p)


my_lap = laptop("lenevo",52000)
#======= showing last price==============
my_lap.increase_price()
print(my_lap.last_p)

#============= increasing price using parameter =============
my_lap.increase_price(5000)
print(my_lap.price)

#==============increasing price using default parameter===========
my_lap.increase_price(5000)
print(my_lap.price)

#================== setting price= ================
my_lap.price = 580000
print(my_lap.price)


#============= decreasing price using default parameter =========
my_lap.dec_price()
print(my_lap.price)

#============= decreasing price using  parameter =========

my_lap.dec_price(-100000)
print(my_lap.price)

# ============== showing class attribute =================
print(my_lap.__dict__)