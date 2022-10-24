
""" 
Question: 
Write a python program to read student_name and mark from keyboard and store the data in a text file with an unique student_id .
"""
with open("student_info",'w') as f:

    def Student():
        stu_list = []
        for i in range(1,4):
            name = input("Name : ")
            marks = input("Marks : ")
            dict = {"ID":i,"Name":name,"Marks":marks}
            stu_list.append(dict)

        all_stu = str(stu_list)
        # all_stu = "".join(map(str,stu_list))
        return all_stu
    f.write(Student())
    f.close()
