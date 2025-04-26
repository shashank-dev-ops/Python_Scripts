tea_types = ("green", "black", "oolong", "white")  # Tuple of tea types
more_tea_types = ("herbal", "rooibos")  # Another tuple of tea types

combined_tea_types = tea_types + more_tea_types  # Concatenating the two tuples

print(combined_tea_types)  # Printing the combined tuple

if "green" in combined_tea_types:  # Checking if "green" is in the combined tuple
    print("Green tea is available!")  # Printing a message if "green" is found

more_tea_types.count("herbal")  # Counting the occurrences of "herbal" in the tuple
print(more_tea_types.count("herbal"))  # Printing the count of "herbal" in the tuple

type(tea_types)  # Getting the type of the variable tea_types
print(type(tea_types))  # Printing the type of the variable tea_types