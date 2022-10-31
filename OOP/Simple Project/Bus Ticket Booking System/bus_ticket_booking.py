class User:
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password

class Bus:
    def __init__(self,coach,driver,arrival,departure,from_des,to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ['Empty' for i in range(20)]

class PhitrinCompany: #bus install for admin
    total_bus = 5
    total_bus_list = [] # dummy Database
    def installed(self):
        bus_no = int(input("Enter The BUS No : "))
        flag = 1
        for bus in self.total_bus_list: #checing existing bus on the road.
            if bus_no == bus['coach']: #bus['coach']= 12,13,....
                print("Bus is already installed")
                flag = 0
        if flag:
            bus_driver = input("Enter Bus driver name : ")
            bus_arrival = input("Enter Bus Arrival Time : ")
            bus_departure = input("Enter Bus Departure Time : ")
            bus_from = input("Enter Bus Start From : ")
            bus_to = input("Enter Bus Destinatin To : ")
            self.newBus = Bus(bus_no,bus_driver,bus_arrival,bus_departure,bus_from,bus_to)
            self.total_bus_list.append(vars(self.newBus)) #vars for creating dictonary.
            print("\nBus inastalled succesfully.\n")

class BusCounter(PhitrinCompany):
    user_list = []
    bus_seat = 20
    def reservation(self):
        bus_no = int(input("Enter the bus no : "))
        flag = 1
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                passenger = input("Enter your name : ")
                seat_no = int(input("Enter your desired seat no : "))
                if seat_no -1 > self.bus_seat:
                    print("Invalid seat number.")
                elif bus['seat'][seat_no - 1] != 'Empty':
                    print('Seat already booked.')
                else:
                    bus['seat'][seat_no-1] = passenger
            else:
                flag = 1
                break
        if flag == 0:
            print("No bus available.")

    def showBusInfo(self): #info for one bus
        bus_no = int(input("Enter the bus no : "))
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                print("*"*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {'#'*10}")
                print(f"Bus number : {bus_no} \t\t Driver : {bus['driver']} ")
                print(f"Arrival : {bus['arrival']} \t\t Departure : {bus['departure']} ")
                print(f"From : {bus['from_des']}\t\t To : {bus['to']} ")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a} : {bus['seat'][a-1]}",end ="\t" )
                        a += 1
                    print("\t",end="")

                    for j in range(2):
                        print(f"{a} : {bus['seat'][a-1]}",end ="\t" )
                        a += 1
                    print()
    def get_user(self):
        return self.user_list

    def create_account(self):
        name = input("Enter your name : ")
        flag = 0
        for user in self.user_list:
            if user['username'] == name:
                print("User name already exists.")
                flag = 1
                break
        if flag == 0:
            password = input("Enter your password : ")
            self.new_user = User(name,password)
            self.user_list.append(vars(self.new_user))
            print("Account created Succesfully")


    def availabe_buses(self): #all bus info
        if len(self.total_bus_list) == 0:
            print("No bus availabe.")
        else:
            for bus in self.total_bus_list:
                print("*"*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {bus['coach']} {'#'*10}")
                print(f"Bus number : {bus['coach']} \t\t Driver : {bus['driver']} ")
                print(f"Arrival : {bus['arrival']} \t\t Departure : {bus['departure']} ")
                print(f"From : {bus['from_des']}\t\t To : {bus['to']} ")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a} : {bus['seat'][a-1]}",end ="\t" )
                        a += 1
                    print("\t",end="")

                    for j in range(2):
                        print(f"{a} : {bus['seat'][a-1]}",end ="\t" )
                        a += 1
                    print()

              
while True:
    counter = BusCounter()
    print("1. Create account.\n2. Login to your account.\n3. Exit")
    user_input = int(input("Enter your choice : "))
    if user_input == 3:
        break
    elif user_input == 1:
        counter.create_account()
    elif user_input == 2:
        name = input("Enter your name : ")
        password = input("Enter your password : ")
        isAdmin = False
        flag = 0
        if name == 'admin' and password == '123':
            isAdmin = True
        if isAdmin == False : 
            for user in counter.get_user():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f'1. Available buses,\n2. Show Bus information.\n3. Reservation.\n4. Exit')
                    a = int(input("Enter your choice : "))
                    if a == 4:
                        break
                    elif a == 1:
                        counter.availabe_buses()
                    elif a == 2:
                        counter.showBusInfo()
                    elif a == 3:
                        counter.reservation()
            else:
                print("Please register first.")
        else:
            while True:
                print("Hello Admin , welcome back.")
                print(f'1. Install bus.\n2. Available Buses.\n3.Show Buse.\n4.Show user list.\n5.Exit')
                a = int(input("Enter your choice : "))
                if a == 5:
                    break
                elif a == 1:
                    counter.installed()
                elif a == 2:
                    counter.availabe_buses()
                elif a == 3:
                    counter.showBusInfo()
                elif a == 4:
                    counter.user_list()




sm_company = PhitrinCompany()
