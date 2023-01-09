
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
