import hashlib
from brta import BRTA
from veichales import Car,Bike,Cng
from ride_manager import uber
from random import random,randint,choice
from threading import Thread


class UserAlreayExists(Exception):
    def __init__(self,email, *args: object) -> None:
        print(f'User {email} already exists.')
        super().__init__(*args)

license_authority = BRTA()
class User:
    def __init__(self,name,email,password) -> None:
        self.name = name
        self.email  = email
        hased_pass = hashlib.md5(password.encode()).hexdigest()
        already_exist = False
        with open('user.txt','r') as file:
            if email in file.read():
                already_exist = True
                # raise UserAlreayExists(email)
        file.close()

        if already_exist == False:
            with open('user.txt','a') as file:
                file.write(f'{email} {hased_pass}\n')
            file.close()
        # print(self.name,'user created.')

    @staticmethod
    def login(email,password):
        with open('user.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                if  email in line:
                    stored_pass = line.split(' ')[1]
                    
        file.close()

        hashed_pas = hashlib.md5(password.encode()).hexdigest()
        if hashed_pas == stored_pass:
            print('Valid User.')
            return True
        else:
            print('Invalid User.')
            return False


class Rider(User):
    def __init__(self, name, email, password,location,balance) -> None:
        self.location = location
        self.balance = balance
        self.__trip_history = []
        super().__init__(name, email, password)
            
    def set_location(self,location):
        self.location = location

    def get_location(self):
        return self.location
    
    def request_trip(self,destination):
        pass

    def get_trip_history(self):
        return self.__trip_history

    def start_a_trip(self,fare,trip_info):
        print()
        print(f"A trip started for {self.name}\n")
        self.balance -= fare
        self.__trip_history.append(trip_info)

class Driver(User):
    def __init__(self, name, email, password,location,license_) -> None:
        self.location = location
        self.license = license_
        self.__trip_history = []
        self.valid_driver = license_authority.validate_license(email,license_)
        self.earning = 0
        self.vehicle = None
        super().__init__(name, email, password)

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            # print("Sorry you are failed!!! try again.")
            self.license = None
        else:
            self.license = result
            self.valid_driver = True
        
    def register_a_vehicle(self,vehicle_type,license_plate,rate):
        if self.valid_driver is True:
            if vehicle_type == 'car':
                self.vehicle = Car(vehicle_type,license_plate,rate,self)
                uber.add_vehicle(vehicle_type,self.vehicle)
            elif vehicle_type == 'bike':
                 self.vehicle = Bike(vehicle_type,license_plate,rate,self)
                 uber.add_vehicle(vehicle_type,self.vehicle)
            elif vehicle_type == 'cng':
                 self.vehicle = Cng(vehicle_type,license_plate,rate,self)
                 uber.add_vehicle(vehicle_type,self.vehicle)
        else:
            pass
            # print('You are not a valid driver.')


    def start_a_trip(self,start,destination,fare,trip_info):
        self.location = destination
        self.earning += fare
        # Start thread
        trip_thread = Thread(target=self.vehicle.start_trip,args=(start,destination,))
        trip_thread.start()
        # self.vehicle.start_trip(start,destination)

        self.__trip_history.append(trip_info)

rider1 = Rider('rider1','rider1@gmail.com','rider1',randint(0,30),1000)
rider2 = Rider('rider2','rider2@gmail.com','rider2',randint(0,30),5000)
rider3 = Rider('rider3','rider3@gmail.com','rider3',randint(0,30),5000)
rider4 = Rider('rider4','rider4@gmail.com','rider4',randint(0,30),5000)
rider5 = Rider('rider5','rider5@gmail.com','rider5',randint(0,30),5000)

vehicles_type = ['cng','bike','cng']

for i in range(0,100):
    driver1 = Driver(f'driver{i}', f'driver{i}@gmail.com', f'driver{i}',randint(0,100), randint(1000,9999))
    driver1.take_driving_test()
    driver1.register_a_vehicle(choice(vehicles_type), randint(10000,99999),10)

# print(uber.get_availbe_car())
uber.find_a_vehicle(rider1,choice(vehicles_type),randint(1,100))
uber.find_a_vehicle(rider2,choice(vehicles_type),randint(1,100))
uber.find_a_vehicle(rider3,choice(vehicles_type),randint(1,100))
uber.find_a_vehicle(rider4,choice(vehicles_type),randint(1,100))
uber.find_a_vehicle(rider5,choice(vehicles_type),randint(1,100))
# uber.find_a_vehicle(rider1,'car',randint(1,100))
# print()
# print(rider1.get_trip_history())
# print()
# print(uber.total_income())