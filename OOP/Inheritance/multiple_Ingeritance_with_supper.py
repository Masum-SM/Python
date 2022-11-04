"""  
In case of multiple inheritance, we can inheritance on class's attribute and method using supper,we can not inherite more than one class using supper, in that case we have use calss name instant of supper.
"""


class School:
    def __init__(self,name) -> None:
        self.schoolName = name
    def __repr__(self) -> str:
        return f'School({self.schoolName})'

class Teacher:
    def __init__(self,name) -> None:
        self.TeacherName = name
    def __repr__(self) -> str:
        return f'Teacher({self.TeacherName})'

class Student(School,Teacher):
    def __init__(self,name,s_name,t_name) -> None:
        self.StudentName = name
        super().__init__(s_name)
        # super().__init__(t_name)
    def __repr__(self) -> str:
        return f'Student({self.StudentName})'

student = Student('masum','DCC','Jas')
print(student.schoolName)