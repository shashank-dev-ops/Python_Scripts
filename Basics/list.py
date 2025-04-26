tea_variety=["Masala", "Ginger", "Cardamom"] 
print(tea_variety[0]) #to print the first element of the list we will use indexing
print(tea_variety[1:2]) #to print the second element of the list we will use indexing

tea_variety[2] = "Cardamom2" #to add the element in the list we will use indexing
print(tea_variety) #to print the list we will use print function


tea_variety[1:2] = ["Cardamom3" , "name"] #to add the element in the list we will use indexing
print(tea_variety) #to print the list we will use print function

tea_variety[1:1] = [] # to remove the element in the list we will use indexing
print(tea_variety) #to print the list we will use print function

for tea in tea_variety: #to print the list we will use for loop
    print(tea) #to print the list we will use print function