class Car:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"{self.brand} {self.model}"
    

    my_car = Car("Toyota", "Corolla") 
    print(my_car.brand)  # Output: Toyota
    print(my_car.model)  # Output: Corolla
    print(my_car.fullname())  # Output: Toyota Corolla
    
    my_new_car = Car("Honda", "Civic") 
    print(my_new_car.brand)  # Output: Honda