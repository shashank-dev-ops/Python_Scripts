Password_strenghth = "hbh"

if len(Password_strenghth) < 6:
    Password = "Weak"
elif len(Password_strenghth)  <= 10:
    Password = "Medium"
elif len(Password_strenghth) <= 15:
    Password = "Strong"

print("Password strength is:", Password)