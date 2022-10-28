# Hierarchical inheritance

from turtle import position


class Empolyee:
    def __init__(self,name,id,salary,position,experience) -> None:
        self.name = name
        self.id = id 
        self.salary = salary
        self.position = position
        self.experience = experience
    
class Developer(Empolyee):
    def __init__(self, name, id, salary, position, experience,tech,focus) -> None:
        self.tech = tech
        self.area_of_work = focus
        super().__init__(name, id, salary, position, experience)

class Tester(Empolyee):
    pass

class Sales(Empolyee):
    pass

class techLead(Empolyee):
    def __init__(self, name, id, salary, position, experience,team) -> None:
        self.team = team
        super().__init__(name, id, salary, position, experience)
