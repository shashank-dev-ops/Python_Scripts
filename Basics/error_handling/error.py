file = open('test.txt', 'w') # This will raise an error if the file does not exist

try:
    file.write('Hello, World!')
finally:    
    file.close()

with open('test.txt', 'w') as file:
    file.write('Hello, World!')
# The above code will raise an error if the file does not exist