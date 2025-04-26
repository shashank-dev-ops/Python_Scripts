input_str = "teether"

for char in input_str:
    if input_str.count(char) == 1:
        print("char is not repeat: ", char)
        break # This will stop the loop when the first non-repeating character is found. 
