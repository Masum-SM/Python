class School:
    def __init__(self,name) -> None:
        self.s_name = name
    def say_name(self):
        print(f"hello from {self.s_name}")

class Teacher:
    def __init__(self,name) -> None:
        self.t_name = name
    def say_name(self):
        print(f"hello from {self.t_name}")


class Students():
    def __init__(self, name , obj) -> None:
        self.s_name =name
        obj.say_name()


schl = School("DCC")
tchr  = Teacher('sumon')
stu1 =Students('Masum',tchr)




