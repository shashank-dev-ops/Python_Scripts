import time

def func_with_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time} seconds")
        return result
    return wrapper

@func_with_decorator # This is a decorator
def example_function(n):    
    time.sleep(n)
            
example_function(2)            