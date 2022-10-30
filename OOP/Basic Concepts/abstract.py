from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def name(self,name):
        print(f"animal name is {name}")

    def eat(self):
        print('Animal need to eat.')

    @property
    @abstractmethod
    def move(self):
        print("Animal can move.")

class cat(Animal):
    def __init__(self) -> None:
        self._name = 'Cat'
       
    def say(self):
        print('this is cat class')

    @property
    def name(self): # we have to create a name class beacuse it is abstrated from base class, without defining name class it will show error.
        print("abstructed")
        super().name(self._name)
    
    @name.setter #setting property value.
    def name(self,value):
        self._name = value

    @property
    def move(self):
        super().move # it is property,we can not call a property of class.
        return 'cat can move'


tom = cat()
tom.name = 'Meeew' #give property name.
tom.eat()
tom.name
print(tom.move) # it is property,we can not call a property of class.