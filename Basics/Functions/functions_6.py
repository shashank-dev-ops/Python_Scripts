def sum_all (*args):
  
   print(args)  # This will print a tuple of all arguments passed to the function
   for i in args:
      print(i * 2)
   return sum(args)  # This will return the sum of all arguments passed to the function

print(sum_all(1, 2, 3, 4, 5))  # This will print the sum of all arguments passed to the function
print(sum_all(1, 2, 3, 4, 5, 6))  # This will print the sum of all arguments passed to the function