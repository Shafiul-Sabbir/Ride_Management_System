import hashlib
from brta import BRTA
from vehicles import Car, Cng, Bike
from ride_manager import uber
from random import random, randint, choice



license_authority = BRTA()

class User:
    def __init__(self,name,email,password) -> None:
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
            
        already_exists = False
        with open('user.txt','r') as file:
            if email in file.read():
                already_exists = True
                # print(f"{email} is already exists.")
        file.close()
                    
        if already_exists == False:
            with open('user.txt','a') as file:
                file.write(f"{email} {pwd_encrypted}\n")
            file.close()
        
        # print(self.name," user created.")
        
    @staticmethod
    def log_in(email,password):
        stored_password = ''
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        with open("user.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(' ')[1]
                    
        file.close()
        if hashed_password == stored_password:
            print("valid user.")
        else:
            print("invalid user.")
        # print("password found ",stored_password)

class Rider(User):
    def __init__(self, name, email, password, location, balance) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.balance = balance
        self.__trip_history = []
        
    def set_location(self,location):
        self.location = location
        
    def get_location(self):
        return self.location
    
    def request_trip(self, destination):
        pass
    
    def start_a_trip(self,fare, trip_info):
        print(f'A trip started for {self.name}')
        self.balance -= fare
        self.__trip_history.append(trip_info)
        
    def trip_history(self):
        return self.__trip_history
        
class Driver(User):
    def __init__(self, name, email, password,location,license) -> None:
        super().__init__( name, email, password) 
        self.location = location
        self.license = license
        self.__trip_history = []
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0
        self.vehicle = None
    
    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            # print("not a valid driver, try again")
            self.license = None       
        else:
            self.license = result 
            self.valid_driver = True
    
    def register_a_Vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            if vehicle_type == 'car':
                self.vehicle = Car(vehicle_type, license_plate, rate, self)
                uber.add_a_Vehicle(vehicle_type, self.vehicle)
                
            elif vehicle_type == 'bike':
                self.vehicle = Bike(vehicle_type, license_plate, rate, self)
                uber.add_a_Vehicle(vehicle_type, self.vehicle)
            else:
                self.vehicle = Cng(vehicle_type, license_plate, rate, self)
                uber.add_a_Vehicle(vehicle_type, self.vehicle)
        else:
            # print("You are not a valid driver.")
            pass
    
    def start_a_trip(self, start, destination, fare, trip_histoy):
        import threading
        self.earning += fare
        self.location = destination
        trip_thread = threading.Thread(target = self.vehicle.start_driving, args = (start, destination,))
        trip_thread.start()
        # self.vehicle.start_driving(start, destination)
        self.__trip_history.append(trip_histoy)
        
    def trip_history(self):
        return self.__trip_history
        
# creating Rider user.
rider1 = Rider('rider1','rider1@gmail.com','rider1',randint(0,30),5000)
rider2 = Rider('rider2','rider2@gmail.com','rider2',randint(0,30),5000)
rider3 = Rider('rider3','rider3@gmail.com','rider3',randint(0,30),5000)
print("\n")

# creating Driver user
vehicle_types = ['car','bike','cng']
for i in range(1,100):
    driver = Driver(f'driver{i}', f'driver{i}@gmail.com', f'driver{i}', randint(0,100), randint(5000,9999))
    driver.take_driving_test()
    driver.register_a_Vehicle(choice(vehicle_types), randint(50000,99999), 10)
    # print("\n")

# print(uber.get_available_cars())

uber.find_a_vehicle(rider1, choice(vehicle_types), randint(1,100))
uber.find_a_vehicle(rider2, choice(vehicle_types), randint(1,100))
uber.find_a_vehicle(rider3, choice(vehicle_types), randint(1,100))
uber.find_a_vehicle(rider1, choice(vehicle_types), randint(1,100))
uber.find_a_vehicle(rider2, choice(vehicle_types), randint(1,100))



print(rider1.trip_history())
print(uber.total_income())
