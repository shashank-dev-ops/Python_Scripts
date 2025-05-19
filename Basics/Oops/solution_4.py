class Battery:
    def battery_info(self):
        return "Battery: 4000mAh"

class Engine:    
    def engine_info(self):
        return "Engine: 2.0L"

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class ElectricCar(Battery, Engine, Car):
    pass

my_new_Car = ElectricCar("Tesla", "Model S")
print(my_new_Car.battery_info())  # Output: Battery: 4000mAh
print(my_new_Car.engine_info())  # Output: Engine: 2.0L