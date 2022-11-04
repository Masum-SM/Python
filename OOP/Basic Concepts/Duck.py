class Teacher:
    def __init__(self,name) -> None:
        self.t_name = name
        self.students = []
    def entry_student(self,stu_obj):
        self.students.append(stu_obj)


class Students():
    def __init__(self, name) -> None:
        self.s_name =name
        Teacher.__init__(self,'Sumon')
        Teacher.entry_student(self,self)

    """ 
    Teacher class ar akta object pathaice,then oi object diye teacher class studens k access kore tar moddhe append korce.
    """
    def enter_in_teacher(self,teacherObj):
        teacherObj.students.append(self)

    def __repr__(self) -> str:
        return f'Student({self.s_name})'

sumon = Teacher('sumon sir')
shirin = Teacher('shirin mam')
lina = Teacher('lina mam')

stu1 = Students('masum')
stu1.enter_in_teacher(sumon) # student class a teacher class ar object pass korce.
stu1.enter_in_teacher(shirin)

print(sumon.students)
print(shirin.students)