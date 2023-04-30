import functools
import random


class RandomError(Exception):
    pass


def main():
    foo()


def save(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        n = random.randint(0, 4)
        if not n:
            raise RandomError
        func

    return wrapper


@save
def foo():
    return


if __name__ == '__main__':
    main()

