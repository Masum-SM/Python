class Student:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
    


class Course:
    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher

class Teacher:
    def __init__(self,name,course):
        self.name = name
        self.course = course

class School:
    def __init__(self,name,teachers,courses,students):
        self.name = name
        self.teachers = teachers
        self.courses = courses
        self.students =students
    def get_student(self):
        for student in studens:
            print(student.name)

school_name = 'sm_academy'
ds_course = Course('Data Structure','Nawrin')
techer_1 =Teacher('Nawrin',ds_course)

algo_course = Course('Algorithm','Liza')
techer_2 =Teacher('Liza',algo_course)

stu_1 = Student('abir',13,1001)
stu_2 = Student('afra',12,1002)
stu_3 = Student('efat',13,1003)

teachers = [techer_1,techer_2]
courses = [ds_course,algo_course]
studens = [stu_1,stu_2,stu_3]

my_school = School(school_name,teachers,courses,studens)
print(my_school.students)
my_school.get_student()