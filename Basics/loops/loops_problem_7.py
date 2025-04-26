number = 10

is_Prime = True

if number > 1:
    for i in range(2, number):
        if number %1 == 0:
            is_Prime = False
            break
print(is_Prime)