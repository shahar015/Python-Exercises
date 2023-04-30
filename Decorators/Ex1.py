import time

def trace(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"'{func.__name__}' got {args}\nThe result is {result}\n{func.__name__} took {total_time}")
        return func(*args, **kwargs)

    return wrapper

@trace
def my_function(x, y):
    return x + y

result = my_function(3, 4)
print(result)
