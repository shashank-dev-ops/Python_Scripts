# for game in "hogwart":
#     print(game)

gamer = ["Hogwart", "Harry Potter", "Dumbledore"]
# print(gamer)
# gamer.append("Gears of War") # Add to the end of the list
# print(gamer)
    
if "Gears of War" in gamer: # Check if the item is in the list

  print("Gears of War is in the list")

  gamer.pop() # Remove the last item in the list
  gamer.remove("Harry Potter") # Remove the item from the list

  gamer.insert(1, "Death Stranding") # Add to the beginning of the list

  gamer_copy = gamer.copy() # Copy the list
  print(gamer_copy)
# for game in gamer: # to iterate through the list
#     print(game, end="-")

 
 