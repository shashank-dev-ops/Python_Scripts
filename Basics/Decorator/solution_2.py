import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def slow_function(a, b):
    time.sleep(2)
    return a + b    

print("Starting slow_function(1, 2)")
print(slow_function(1, 2))  # This will take 2 seconds
print("Starting slow_function(1, 2) again")