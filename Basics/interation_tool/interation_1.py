range(5) 
print(range)

R = range(5)
print(R)

I = iter(R)
next(I)
print(next(I))  # 0
print(next(I))  # 1 
print(next(I))  # 2
print(next(I))  # 3        
print(next(I))  # 4         # StopIterationError