Leap_year = 2023

if (Leap_year %4 == 0 and Leap_year%100 != 0) or (Leap_year % 400 == 0):
    print(Leap_year, "is a leap year")
else:
    print(Leap_year, "is not a leap year")
# The code above checks if the year 2024 is a leap year or not. A year is a leap year if it is divisible by 4, but not divisible by 100, unless it is also divisible by 400.