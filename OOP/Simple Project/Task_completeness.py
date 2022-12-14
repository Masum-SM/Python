from datetime import datetime
from uuid import uuid4

class Task:
    all_task = []
    new_task_list = []
    def __init__(self) -> None:
        self.id = str(uuid4())
        self.Task_Name = "";
        self.Created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S");
        self.Updated_time = "NA"
        self.Task_done = False
        self.Completed_time= "NA"
        
    def update_task(self):
        no = -1;
        new_dict = {}
        is_upadatabe = False

        for task in self.all_task:
            if task["Task_done"] == False:
                is_upadatabe = True

        if is_upadatabe == True:
            print("Select Which Task To Update.")
            for task in self.all_task:
                no += 1;
                print()
                new_dict = {"Task No" : no+1}
                new_dict.update(task)
                # task["Task No - "] = no+1;
                for key in new_dict:
                    if(task["Task_done"] == False):
                        print(f"{key} - {new_dict[key]}")
                print()
                self.new_task_list.append(new_dict)

            task_num = int(input("Enter Task No : "))
            task_new_name = input("Enter updated name : ")


            for task in self.all_task:
                for new_task in self.new_task_list: 
                    if(task_num == new_task["Task No"] and task["id"] == new_task["id"] and task["Task_done"] == False):
                        task["Task_Name"] = task_new_name
                        task["Updated_time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            print("Task Updated successfully.")
        else:
            print("No Task to update.")
        


    def complete_task(self):

        is_upadatabe = False

        for task in self.all_task:
            if task["Task_done"] == False:
                is_upadatabe = True   

        if is_upadatabe == True:

            print("Select Which task to complete.")
            no = -1;
            new_dict = {}
            for task in self.all_task:
                no += 1;
                print()
                new_dict = {"Task No" : no+1}
                new_dict.update(task)
                # task["Task No - "] = no+1;
                for key in new_dict:
                    if(task["Task_done"] == False):
                        print(f"{key} - {new_dict[key]}")
                print()

                self.new_task_list.append(new_dict)

            task_num = int(input("Enter Task No : "))
            for task in self.all_task:
                for new_task in self.new_task_list: 
                    if(task_num == new_task["Task No"] and task["id"] == new_task["id"] and task["Task_done"] == False):
                        task["Task_done"] = True
                        task["Completed_time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print("Task Completed successfully.")
        else:
            print("No Task To Complete.")

class AllTask(Task):

    def create_task(self):
        task_name = input("Enter New Task : ")
        self.all_task.append({"id":str(uuid4()),"Task_Name":task_name,"Created_time":datetime.now().strftime("%d/%m/%Y %H:%M:%S") ,"Updated_time":"NA","Task_done":False,"Completed_time":"NA"})
        print()
        print("Created Task Successfully.")
        
    
    def show_all_task(self):
        print()
        for task in self.all_task:
            for key in task:
                print(f"{key} - {task[key]}")

            print()

    def show_incompleted_task(self):
        print()
        is_exist = False
        for task in self.all_task:
            for key in task:
                if(task["Task_done"] == False):
                    is_exist = True
                    print(f"{key} - {task[key]}")
            print()

        if is_exist == False:
            print("No Incompleted Task.")
            print()
       
    def show_completed_task(self):
        is_exist = False
        for task in self.all_task:
            for key in task:
                if(task["Task_done"] == True):
                    is_exist = True
                    print(f"{key} - {task[key]}")
            print()
        if is_exist == False:
            print("No Completed Task.")
            print()
    


while True:
    task = AllTask()
    print()
    print('1.Add new task.\n2.Show all tasks\n3.Show incompleted tasks.\n4.Show completed tasks.\n5.Update task.\n6.Mark a task completed.')
    print()
    option = input('Enter Option:')
    if option == '1':
        task.create_task()
    elif option == '2':
        task.show_all_task()
    elif option == '3':
        task.show_incompleted_task()
    elif option == '4':
        task.show_completed_task()
    elif option == '5':
        task.update_task()
    elif option == '6':
        task.complete_task();
    else:
        break
    

