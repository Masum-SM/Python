
class bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def deposite(self,amount):
        self.balance = self.balance + amount
    
    def get_balance(self):
        return self.balance

    def withdraw(self,amount):
        if amount <100:
            return f'No money for you, Minimu withdraw : {self.min_withdraw}'
        elif amount > 10000:
            return f'You crossed max limit: {self.max_withdraw}'
        elif amount > self.balance:
            return 'You are broke!!! No money for you.'
        else:
            self.balance = self.balance - amount
            return f'Here is your money: {amount}'

my_bank = bank(8000)
reply1 = my_bank.withdraw(50)
print(reply1)

reply2 = my_bank.withdraw(10010)
print(reply2)

reply3 = my_bank.withdraw(9000)
print(reply3)

reply4 = my_bank.withdraw(5000)
print(reply4)

balance = my_bank.get_balance()
print("Your remaining balance is : ",balance)

depo = my_bank.deposite(8000)
balance = my_bank.get_balance()
print("After deposite balance is : ",balance)