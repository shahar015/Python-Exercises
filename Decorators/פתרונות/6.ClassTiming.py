import functools
import time


def main():
    foo = Foo()

    foo.change("aaa")
    print(foo.string)

    print(foo.length())

    foo.display()


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        class_name = args[0].__class__.__name__

        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        print(f"Function name :{func_name}, Class name : {class_name}")

        run_time = end_time - start_time

        print(f"The function took : {float(run_time)}`s")
        return result

    return wrapper


class Foo:
    def __init__(self, string="foo!"):
        self.__string = string

    @property
    def string(self):
        return self.__string

    @trace
    def display(self):
        print(self.__string)

    @trace
    def length(self):
        return len(self.__string)

    @trace
    def change(self, temp_str):
        future_an_even = ""
        future_even = ""

        final_string = ""

        for i in range(len(self.__string)):
            if i % 2 == 0:
                future_an_even += self.__string[i]

        for i in range(len(temp_str)):
            if i % 2 == 1:
                future_even += temp_str[i]

        for i in range(max(len(future_even), len(future_an_even))):
            if i < len(future_even):
                final_string += future_even[i]

            if i < len(future_an_even):
                final_string += future_an_even[i]
        self.__string = final_string


if __name__ == '__main__':
    main()
