tea_shop = {
    "chai": {
        "green tea": "green",
        "black tea": "black",
    },
    "coffee": {
        "espresso": "dark",
        "latte": "light",
    },
}
print(tea_shop)  # Printing the dictionary
print(tea_shop["chai"])  # Accessing the nested dictionary for "chai"
print(tea_shop["chai"]["green tea"])  # Accessing the value for "green tea" under "chai"

key1 = ["chai","coffee","tea","milk"] # Creating a set of keys
key2 = "latte" # Creating a key

combined_key = dict.fromkeys(key1, key2) # Creating a dictionary with the keys from key1 and the value from key2
print(combined_key)  # Printing the combined dictionary