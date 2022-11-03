from abc import ABC,abstractmethod
from time import sleep

class Vehicle(ABC):
    speed = {
        'car' : 30,
        'bike':50,
        'cng':20
    }
    def __init__(self,vehicle_type,license_plate,rate,driver) -> None:
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.driver = driver
        self.status = 'available'
        self.license_plate = license_plate
        self.speed = self.speed[vehicle_type]
        
    @abstractmethod
    def start_trip(self):
        pass

    @abstractmethod
    def trip_finished(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_trip(self,start,destination):
        self.status = 'unavailable'
        print()
        print(self.vehicle_type,self.license_plate,'started trip')
        distance = abs(start - destination)
        for i in range(0,distance):
            sleep(0.3)
            print(f'Driving: {self.license_plate} current postion :{i} of {distance}')
        self.trip_finished()
        
    def trip_finished(self):
        self.status = 'avilable'
        print(self.vehicle_type,self.license_plate,'Complited trip')





class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_trip(self,start,destination):
        self.status = 'unavailable'
        print()
        print(self.vehicle_type,self.license_plate,'started trip')
        distance = abs(start - destination)
        for i in range(0,distance):
            sleep(0.3)
            print(f'Driving: {self.license_plate} current postion :{i} of {distance}')
        self.trip_finished()

    def trip_finished(self):
        self.status = 'avilable'
        print(self.vehicle_type,self.license_plate,'Complited trip')




class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_trip(self,start,destination):
        self.status = 'unavailable'
        print()
        print(self.vehicle_type,self.license_plate,'started trip')
        distance = abs(start - destination)
        for i in range(0,distance):
            sleep(0.3)
            print(f'Driving: {self.license_plate} current postion :{i} of {distance}')
        self.trip_finished()

    def trip_finished(self):
        self.status = 'avilable'
        print(self.vehicle_type,self.license_plate,'Complited trip')