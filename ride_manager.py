class RideManager:
    def __init__(self) -> None:
        print('ride manager activated.\n')
        self.__income = 0
        self.__trip_history = []
        self.__available_Cars = []
        self.__available_Bikes = []
        self.__available_Cng = []
       
    def add_a_Vehicle (self, vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__available_Cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__available_Bikes.append(vehicle)
        else:
            self.__available_Cng.append(vehicle)
    
    def get_available_cars(self):
        return self.__available_Cars
    
    def total_income(self):
        return self.__income
    
    def trip_history(self):
        return self.__trip_history
    
    def find_a_vehicle(self, rider, vehicle_type, destination):
        if vehicle_type == 'car':
            vehicles = self.__available_Cars
        elif vehicle_type == 'bike':
            vehicles = self.__available_Bikes
        else:
            vehicles = self.__available_Cng
            
        if len(vehicles) == 0:
            print('sorry no cars are available now.')
            return False
        for vehicle in vehicles:
            if abs(rider.location - vehicle.driver.location) <= 20:
                print('\npotential', rider.location, vehicle.driver.location)
                distance = abs(vehicle.driver.location - destination)
                fare = distance * vehicle.rate
                
                if rider.balance < fare:
                    print(f"You do not have sufficient amount for this trip. fare : {fare}, your balance : {rider.balance}")
                    return False
                
                if vehicle.status == 'available':
                    vehicle.status = 'unavailable'
                    trip_info = f'Match {vehicle_type} For Rider : {rider.name}, Driver : {vehicle.driver.name}, From {rider.location} To {destination}, Previous Balance : {rider.balance} , Fare : {fare} , Current Balance : {rider.balance - fare} '
                    print(trip_info)
                    vehicles.remove(vehicle)
                    rider.start_a_trip(fare, trip_info)
                    vehicle.driver.start_a_trip(rider.location, destination, fare * 0.8, trip_info)
                    self.__income += fare * 0.2
                    # print('available cars : ',len(vehicles))
                    self.__trip_history.append(trip_info)
                    # print(rider.balance)
                    # print(car.driver.__dir__())
                    # print('now available cars : ',len(vehicles),'\n')
                    return True
            else:
                # print('cant find any match for this potential.\n')
                pass
        # print("looping done")
    
uber = RideManager()