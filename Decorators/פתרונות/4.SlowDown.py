import functools
import time


def main():
    print(foo())
    print(bar())


def slowdown(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()

            result = func(*args, **kwargs)

            end_time = time.perf_counter()
            run_time = end_time - start_time

            if run_time < seconds:
                time.sleep(seconds - run_time)
            return result
        return wrapper
    return decorator


@slowdown(1)
def foo():
    return "foo!"


@slowdown(1)
def bar():
    time.sleep(0.5)
    return "bar!"


if __name__ == '__main__':
    main()

