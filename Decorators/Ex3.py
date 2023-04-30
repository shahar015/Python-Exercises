import random

def random_failure(func):
    def wrapper(*args, **kwargs):
        if random.randint(1, 4) == 1: 
            raise RandomError("Random failure occurred.")
        else:
            return func(*args, **kwargs)
    return wrapper

class RandomError(Exception):
    pass

@random_failure
def my_function():
    print("Function executed successfully.")

# ניסוי להריץ את הפונקציה מספר פעמים
for _ in range(5):
    try:
        my_function()
    except RandomError as e:
        print(e)
