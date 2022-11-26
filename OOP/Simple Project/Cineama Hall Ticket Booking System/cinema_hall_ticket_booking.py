
class Star_cinema:
    hall_list = []
    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.__booked_list = []
        super().entry_hall(self)

    def enty_show(self,id,movie_name,time):
        self.__show_list.append((id, movie_name,time))
        sit_num = ['A', 'B', 'C', 'D', 'E']
        temp_sit = []
        for i in range(self.rows):
            temp = []
            for j in range(self.cols):
                temp.append(sit_num[i]+str(j))
            temp_sit.append(temp)
        self.__seats[id] = temp_sit



    def book_seats(self,name,phone,id,seat_number=[]):
        
        if id not in self.__seats.keys():
            print()
            print('-'*30)
            print()
            print("ID DON'T MATCH WITH ANY SHOW!!!!")
            print()
            print('-'*30)
            return
        show_id = self.__seats[id]
        for i in range(len(seat_number)):
            seat = seat_number[i]

            is_booked = False
            try:
                if 'A'<=seat[0] and seat[0] > 'C' or 1<= int(seat[1]) and int(seat[1])>3:
                    print()
                    print('_'*30)
                    print()
                    print("Invalid seat number !!!")
                    print()
                    print('-'*30)
                    
                    return
            except:
                print()
                print('-'*30)
                print()
                print("Invalid seat number !!!")
                print()
                print('-'*30)
                
                return
            
            
            for j in self.__booked_list:
                if j == seat:
                    is_booked = True
                    print()
                    print('-'*30)
                    print(f'SEAT {j} IS ALREADY BOOKED')
                    print()
                    print('-'*30) 
                    
                    return
                

            if is_booked == False:
                for j in range(self.rows):
                    for k in range(self.cols):
                        if seat == show_id[j][k]:
                            show_id[j][k] = "x"
                            self.__booked_list.append(seat)
    
        print("\n******* TICKET BOOKED SUCCESSFULLY!! *******")
        print('-'*50)
        print(f"NAME :{name}")
        print(f"PHONE NUMBER :{phone}")
        print()
        for show in self.__show_list:
            if id == show[0]:
                print(f'MOVIE NAME:{show[1]}\t\t\tTIME: {show[2]}\n')
        print('TICKETS: ',end='')
        for t in self.__booked_list:
            print(f'{t} ',end='')
        print("\nHALL : ",self.hall_no)
        print()
        print('-'*50)
        return
            
                
    def view_show_list(self):
        print('-'*83)
        for show in self.__show_list:
            print(f'MOVIE NAME: {show[1]}\t\t SHOW ID : {show[0]}\t\t TIME: {show[2]}')
        print('-'*83)

    def view_available_seats(self,id):
        if id not in self.__seats.keys():
            print()
            print('-'*30)
            print()
            print("ID DON'T MATCH WITH ANY SHOW!!!!")
            print()
            print('-'*30)
            return
        print()
        for show in self.__show_list:
            if id == show[0]:
                print(f'MOVIE NAME:{show[1]}\t\tTIME: {show[2]}')
                print('x for already booked seats.\n')
                print('-'*50)
                show_id = self.__seats[id]
                for i in range(3):
                    for j in range(4):
                        print(show_id[i][j],end = '\t\t')
                    print()
                print('-'*50)



bolaka = Hall(3,4,1)
bolaka.enty_show("101","Damal","Oct 26 2022 10:00 PM")
bolaka.enty_show("102","Poran","Oct 26 2022 8:00 PM")

while True:
    print('1.VIEW ALL SHOWS TODAY.\n2.VIEW AVAILABE SEATS\n3.BOOK TICKET')
    option = input('ENTER OPTION: ')
    if option == '1':
        bolaka.view_show_list()
        print()
    elif option == '2':
        id = input("Enter show ID : ")
        bolaka.view_available_seats(id)
        print()
    elif option == '3':
        name = input('Enter your name : ')
        phone = input('Enter your number : ')
        id = input('Enter show id : ')
        seats = []
        num_of_ticket = int(input('Enter number of ticket : '))
        for i in range(num_of_ticket):
            s = input('Seat no : ')
            seats.append(s)

        bolaka.book_seats(name,phone,id,seats)
        print()
    
    else:
        break
