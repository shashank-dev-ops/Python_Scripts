def print_names(*kwargs):
     for key , value in kwargs.items():
         print(f"{key} : {value}")


         print_names(name = "John", age = 30, city = "New York")  # This will print the name, age, and city of the person   
         print_names(name = "Alice", age = 25, city = "Los Angeles")  # This will print the name, age, and city of the person
         print_names(name = "Bob", age = 35, city = "Chicago")