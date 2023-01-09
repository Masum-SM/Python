
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
