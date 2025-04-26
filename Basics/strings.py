chai_type = "Masala"
quantity = 2
list= "this is a list"
order = "I ordered {} cup of {} chai"
print(order.format(quantity, chai_type)) # to print the string in a single line we will use f-string

chai_variety = ["Masala", "Ginger", "Cardamom"] # jion the list with a comma
print("--".join(chai_variety))

print(len(chai_type))

for letter in list: #to make it in list we will use for loop
    print(letter)

    chai1= "Masala\nGinger" #to print it in single line we will use raw string
    print(chai1)

    chai2= r"Masala\nGinger" #to print it in single line we will use raw string
    print(chai2)

    testing = "This is a test string"
    print(testing[0:2]) #this is to slice the string

    chai_type2 = "Masala_Chai"
    print("Masalaaa" in chai_type2) #this is to check if the string is present in the other string

