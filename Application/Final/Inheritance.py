""" 
Single Inheritence: Single inheritance enables a derived class to inherit properties from a single parent class, enabling code reusability and the addition of new features to existing code.
"""

class Mouse: # Base class
    def __init__(self,brand,wire_type,color) -> None:
        self.brand = brand
        self.wire_type = wire_type
        self.color = color

class Logitech(Mouse): #Derived class
    def __init__(self, brand, wire_type, color,price) -> None:
        self.price = price
        super().__init__(brand, wire_type, color) # This is supper function that allow the derived class to access attribute and method of base class.
        
    def __repr__(self) -> str: 
        return f"Brand Name : {self.brand}\nWire Type : {self.wire_type}\nColor : {self.color}\nPrice : {self.price} " 
mouse_M820 = Logitech('Logitech','Wireless','gray_balck',980)
print(mouse_M820)


""" 
Multiple Inheritance: When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class.  
"""

class Father: #Base class
    def __init__(self,father_name) -> None:
        self.fatherName = father_name
        print("Father name is ",self.fatherName)

        
class Mother: #Base class
    def __init__(self,mother_name) -> None:
        self.motherName = mother_name
        print("Mother name is ",self.motherName)
