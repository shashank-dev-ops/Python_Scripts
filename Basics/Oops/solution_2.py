class ElectricCar:
    total_electric_cars = 0

    def __init__(self, brand, model, batery_size):
        self.brand = brand
        self.model = model
        self.batery_size = batery_size
        ElectricCar.total_electric_cars += 1 # Incrementing the class variable

class NewElectricCar(ElectricCar):
    def __init__(self, brand, model, batery_size):
        super().__init__(brand, model, batery_size) # calling the parent class constructor

    def fullname(self):
        return f"{self.brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + " ! " # This will raise an error because __brand is private in the parent class

myy_tesla = NewElectricCar('Tesla', 'Model x', 120)
# print(myy_tesla.brand)
# print(myy_tesla.model)
# print(myy_tesla.batery_size)
# print(myy_tesla.fullname())
# print(myy_tesla.__brand)
# print(myy_tesla.get_brand()) # This will raise an error because __brand is private in the parent class

print(ElectricCar.total_electric_cars) # This will print the total number of electric cars created 
# my_tesla = ElectricCar('Tesla', 'Model S', 100)
# print(my_tesla.brand)

        