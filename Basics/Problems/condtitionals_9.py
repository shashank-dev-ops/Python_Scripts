Animal_type = "Dog"
Year = 1


if Animal_type == "Dog" and Year < 2:
    Food = "Puppy Food"
elif Animal_type == "Cat" and Year > 5:
    Food = "Adult Cat Food"

else:
    Food = "Unknown Food"

print("Food for", Animal_type, "is:", Food)
# The code above checks the type of animal and its age to determine the appropriate food. If the animal is a dog and less than 2 years old, it gets puppy food. If it's a cat and 5 years or older, it gets adult cat food.