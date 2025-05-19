class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @staticmethod
    def static_method():
        return "Static method called" 
    
    @property # This is a property decorator
    def model(self):
        return self.model

# Define ElectricCar as a subclass of Car
class ElectricCar(Car):
    pass

my_tesla = ElectricCar('Tesla', 'Model S')

print(isinstance(my_tesla, ElectricCar))  # Output: True


my__car = Car("Toyota", "Corolla")
# print(Car.static_method())  # Output: Static method called

print(my__car.model)  # Output: <property object at 0x...>
