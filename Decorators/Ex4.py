import time

def slowdown(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            total_time = time.perf_counter()-start_time
            if total_time < n:
                time.sleep(n - total_time)
            
            return result
        return wrapper
    return decorator

@slowdown(1)
def foo():
 return "foo!"
@slowdown(0.3)
def bar():
 time.sleep(0.5)
 return "bar!"
t = time.time()
print(foo())
assert 1<=time.time()-t<1.1
t = time.time()
print(bar())
assert 0.5<=time.time()-t<0.51