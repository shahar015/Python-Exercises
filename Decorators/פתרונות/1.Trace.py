import functools
import time
from decimal import Decimal


def main():
    foo(3, 2)


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        print(f"@ @ @ '{func_name}' got {args}")

        print(f"@ @ @ The result is {result}")

        run_time = end_time - start_time
        print(f"@ @ @ '{func_name}' took {float(run_time)}`s")

    return wrapper


@trace
def foo(x, y):
    print("foo!")
    return x ** y


if __name__ == '__main__':
    main()

