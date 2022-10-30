
class Account:
    def __init__(self,holder) -> None:
        self._account_holder = holder

class StudentAcount(Account):
    def __init__(self,holder,balance,school) -> None:
        self.__balance = balance

    def withdraw(self,amount):
        if amount > self.__balance:
            return 'Out of balance'
        self.__balance -= amount

    def deposite(self,amount):
        if(amount < 0):
            return 'Go to hell'
        self.__balance += amount

    def get_balance(self):
        return self.__balance
        
masum = StudentAcount('Masum',40000,'SCC')
print(masum.get_balance())

masum.deposite(2100)
print(masum.get_balance())

# print(dir(masum.__balance))
print(masum._StudentAcount__balance) #accecing private attribute outside the class.
