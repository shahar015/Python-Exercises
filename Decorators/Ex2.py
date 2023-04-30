def save(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except Exception as ex:
            print(f"You Got {ex}")

    return wrapper

@save
def foo(x,y):
    return x/y

foo(3,0)
print(foo(3,1))
