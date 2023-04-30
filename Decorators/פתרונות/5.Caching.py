import functools


def main():
    print(fibonacci(100))


def cache(capacity=100):
    def decorator(func):
        _dict = {}

        @functools.wraps(func)
        def wrapper(n):
            if n not in _dict.keys() or n > capacity:
                _dict[n] = func(n)
            return _dict[n]

        return wrapper
    return decorator


@cache()
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    main()
