import time
class School:
    #constuctor
    def __init__(self,name,address,principal = '') -> None:
        self.name = name
        self.address = address
        self.prinpal = principal
        self.grades = []
    def add_grade(self,name,teacher):
        new_grade = Grade(name,teacher)
        self.grades.append(new_grade)
    
    def remove(self,name):
        idx = 0
        for i,grade in enumerate(self.grades):
            if grade.name == name:
                idx = i
        del self.grades[idx]

class Grade:
    # constuctor
    def __init__(self,name,teacher) -> None:
        self.student = []
        self.name = name
        self.teacher = teacher

    def __repr__(self) -> str:
        return f'class of {self.name} with teacher {self.teacher}'

    #distuctor
    def __del__(self):
        print(f'Deleting {self.name} with teacher {self.teacher}')



oxford = School('Oxford Kid Academy','Mirpur','Obayed Alam')
oxford.add_grade('calss 5','Shirin Akter')
oxford.add_grade('calss 3','Mostofa Kamal')
oxford.add_grade('calss 8','sumon alom')
oxford.remove('class 5')
print(oxford.grades)
print('My code is done')
time.sleep(10)