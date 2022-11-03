class RideManager:
    def __init__(self) -> None:
        print('Ride manager activated')
        self.__income = 0
        self.__trip_history = []
        self.__availabe_cars = []
        self.__availabe_bikes = []
        self.__availabe_cng = []

    def add_vehicle(self,vehicle_type,vehicle):
        if vehicle_type == 'car':
            self.__availabe_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__availabe_bikes.append(vehicle)
        else:
            self.__availabe_cng.append(vehicle)

    def get_availbe_car(self):
        return(self.__availabe_cars)

    def total_income(self):
        return self.__income

    def trip_history(self):
        return self.__trip_history

    def find_a_vehicle(self,rider,vehicle_type,destination):
        if vehicle_type == 'car':
            vehicles = self.__availabe_cars
        elif vehicle_type == 'bike':
            vehicles = self.__availabe_bikes
        else:
            vehicles = self.__availabe_cng

        if len(vehicles) == 0:
            print('No car availbe')
            return False
        for vehicle in vehicles:
            # print("Potential ",rider.location,car.driver.location)
            if abs(rider.location -vehicle.driver.location)<10:
                distance = abs(rider.location - destination)
                fare = distance * vehicle.rate
                if rider.balance < fare:
                    print(f"You do not have enough money for this trip. Fare is {fare} and your balance is {rider.balance}")
                    return False
                if vehicle.status == 'available':
                    vehicle.status = 'unavailable'
                    # print('Available cars: ',len(vehicles))
                    trip_info = f'Match {vehicle_type} for {rider.name} Fare is {fare} tk with {vehicle.driver.name} started from {vehicle.driver.location} to {destination}'
                    print()
                    print(trip_info)
                    print()
                    vehicles.remove(vehicle)
                    rider.start_a_trip(fare,trip_info)
                    vehicle.driver.start_a_trip(rider.location,destination,fare * 0.8,trip_info)
                    self.__income += fare * 0.2
                    # print('Available cars: ',len(self.__availabe_cars))
                    self.__trip_history.append(trip_info)
                    
                    return True
            # print('looping done')
        

uber = RideManager()
