# Multi Level inheritance.

class Vehicals:
    def __init__(self,name,licnese,price) -> None:
        self.name = name
        self.license = license
        self.price = price
        print('Vehicle class init called')

    def start(self):
        print(f'{self.name} started.')

class Bus(Vehicals):
    def __init__(self, name, licnese, price,seat,ticket_price) -> None:
        self.seat = seat
        self.available_seats = seat
        self.sell_ticket = ticket_price
        print('Bus init Called')
        super().__init__(name,licnese,price)

    def sell_ticket(self,customer_name,quantity,amount):
        self.available_seats -= quantity
        remainder = amount - self.sell_ticket *quantity
        if remainder >= 0:
            return Ticket(customer_name)
        else:
            return ' NO ticket for you.'
class ACBus(Bus):
    def __init__(self):
        print("AC bus created.")

class MiniBus(Bus):
    def __init__(self):
        print('This is mini bus.')
        super().__init__('Mirput Metro', 'DHA1200', 1200000, 40, 50)
 
class Ticket:
    def __init__(self,owner) -> None:
        self.owner = owner

mini = MiniBus()
print(mini.seat)
print(mini.name)