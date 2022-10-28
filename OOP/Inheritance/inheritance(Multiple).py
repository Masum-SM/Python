class School:
    def __init__(self,name) -> None:
        self.school_name = name
        print('School class init called')


class Grade:
    def __init__(self,grade_name):
        self.grade_name = grade_name
        print('Grade class init called')

class SportsTeam:
    def __init__(self,sports_name) -> None:
        self.sports_name = sports_name
        self.team = []
    def add_player(self,player_name):
        self.team.append(player_name)

class Student(School,Grade,SportsTeam):
    def __init__(self, name,grade_name,school_name,sports_name) -> None:
        self.name = name
        print('Student init called')
        Grade.__init__(self,grade_name) #when we call init function with class name we have to provide self perameter.
        School.__init__(self,school_name)
        SportsTeam.__init__(self,sports_name)

masum = Student('Masum','BSC','DCC','Cricket')
print(masum.name,masum.school_name,masum.grade_name)
masum.add_player('Unus')
masum.add_player('Masum')
print(masum.team)