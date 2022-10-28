# Single inheritance.
class Device:
    def __init__(self,brand,price,color) -> None:
        self.brand = brand
        self.price = price
        self.color = color
    def re_sale(self):
        print('Ready to sell again')

class Laptop(Device):
    def __init__(self,brand,price,color,disc_size) -> None:
        super().__init__(brand,price,color)
        self.disc_size = disc_size
    def run(self):
        print('The laptop is running.')
    
    def purches(self,money,discount):
        if money < (self.price - (self.price * discount)/100):
            return 'No laptop for you,add more money',
        else:
            print("This device is for you")
            return money - self.price
    def __repr__(self) -> str:
        return f'Brand Name : {self.brand},Price : {self.price},Color : {self.color} '


class Phone:
    def __init__(self,brand,price,color,camera,num_of_sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.camera = camera
        self.num_of_sim = num_of_sim

    def is_dual(self,num_of_sim):
        if self.num_of_sim == num_of_sim:
            return num_of_sim > 1

    def __repr__(self) -> str:
        return f'Brand Name : {self.brand},Price : {self.price},Color : {self.color} '


class Watch:
    def __init__(self,brand,price,color,watch_type) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.watch_type = watch_type
    def is_digital(self):
        return self.watch_type == 'Digital'

class Manager:
    def __init__(self,name,salary,experienc,designation) -> None:
        self.name = name;
        self.salary = salary
        self.experience = experienc
        self.designation = designation

    def day_total_sales(self):
        pass
    def handle_customer_compalin(self):
        pass 

    def withdraw_salary(self):
        pass

class SalesPerson:
    def __init__(self,name,salary,experience,designation,commission) -> None:
        pass

    def handle_customer(self):
        pass

    def withdraw_salary(self):
        pass

lenevo = Laptop('Lenevo',42000,'Silver','1TB')
Hp = Laptop('Hp',54000,'Silver','2TB')
print(lenevo)
lenevo.re_sale()
print(Hp)

onePlus = Phone('onePlus',40000,'sky blue','48px',2)
sumgsung = Phone('Sumgsung',34000,'sky blue','58px',2)
print(onePlus)
print(sumgsung)