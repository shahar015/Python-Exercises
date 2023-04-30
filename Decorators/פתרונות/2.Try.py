import functools
import time
from decimal import Decimal


def main():
    foo(3, 0)
    print(foo(3, 1))


def save(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"You got  {e}")

    return wrapper


@save
def foo(x, y):
    return x / y


if __name__ == '__main__':
    main()

