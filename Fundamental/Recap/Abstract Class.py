
#------------------------------------------------->ABSTRACT CLASS <------------------------------------------

"""  
To create blue-print of object we use class

ABSTRACT-CLASS : To create a blue-print of a class, we use abstract class. It is not possible to create object of an abstract class.

ABSTRACT-MEHTOD : if we declare a function/method but do not perform any task the it is called abstract method
"""

#-------------- Normal class ----------------
class Vehicle:
    def run(self):
        print('Vehicle is running......')
car = Vehicle()
car.run() #output : Vehicle is running
