n = 125
sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += i
print("Sum of even numbers from 1 to", n, "is:", sum_even)  