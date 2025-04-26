distance = 5

if distance < 3:
    transportation = "walk"
elif distance < 10:
    transportation = "bike"
elif distance < 20: 
    transportation = "bus"

print("You should take the", transportation, "for a distance of", distance, "km.")

