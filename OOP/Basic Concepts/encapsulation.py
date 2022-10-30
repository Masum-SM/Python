class Account:
    def __init__(self,holder,initial_balance) -> None:
        self.holder = holder #public attribute
        self._account_no = '136'
        self.__balance = initial_balance #private attribute

    def deposite(self,amount):
        print(f'Adding {amount} to your account')
        self.__balance += amount

    def withdraw(self,amount):
        print(f'Withdrawing {amount} from your account')
        self.__balance -= amount



class StudentAccount(Account):
    def __init__(self, holder, initial_balance,school) -> None:
        self.school = school
        super().__init__(holder, initial_balance)

    
    def get_balance(self):
        return 


masum = StudentAccount('Masum',25000,'DCC')
# print(masum.__balance)
masum.deposite(2500)
# print(masum.__balance)
masum.withdraw(3000)
# print(masum.__balance)
print(masum._account_no)