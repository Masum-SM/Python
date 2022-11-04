""" 
In case of multiple inheritance , when we one to call method of parent calss, if always call the 1st class methods give in child class, here child class is Student and parent class are School & Teacher, so the say_name method print the School name,cz it is plaecd at 1!st at Student class.

But
when Child class has same method, then it call only it's method not parent method.
 """

class School:
    def __init__(self,name) -> None:
        self.schoolName = name
    def say_name(self):
        print(f'This is {self.schoolName}')
    def __repr__(self) -> str:
        return f'School({self.schoolName})'

class Teacher:
    def __init__(self,name) -> None:
        self.TeacherName = name

    def say_name(self):
        print(f'This is {self.TeacherName}')

    def __repr__(self) -> str:
        return f'Teacher({self.TeacherName})'

class Student(School,Teacher):
    def __init__(self,name,s_name,t_name) -> None:
        self.StudentName = name
        School.__init__(self,s_name)
        Teacher.__init__(self,t_name)
    def say_name(self):
        print(f'This is {self.StudentName}')
    def __repr__(self) -> str:
        return f'Student({self.StudentName})'

student = Student('masum','DCC','Jas')
print(student.schoolName,student.TeacherName)
student.say_name()