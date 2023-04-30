from time import time



class Foo:
    def __init__(self, string="foo"):
        self.string = string


    def print_execution_time(func):
        def wrapper(*args, **kwargs):
            print(f"Class: {func.__qualname__} - Function: {func.__name__}")
            start_time = time()
            result = func(*args, **kwargs)
            elapsed_time = time() - start_time
            print(f"Execution Time: {elapsed_time} seconds\n")
            return result
        return wrapper
    
    @print_execution_time
    def display(self):
        print(self.string)
    
    @print_execution_time
    def Length(self):
        return len(self.string)
    
    @print_execution_time
    def change(self, new_string):
        even_chars = self.string[::2]  # תווים במקומות זוגיים
        odd_chars = new_string[1::2] 
        self.string = ''.join([odd_chars[i] + even_chars[i] for i in range(min(len(odd_chars), len(even_chars)))])
        if len(self.string) < len(new_string):
            extra_chars = new_string[len(self.string):]  # תווים נוספים מהמחרוזת החדשה
            self.string += extra_chars
        
    
# יצירת אובייקט מהמחלקה Foo
foo = Foo()

# קריאה לפונקציה display
foo.display()

# קריאה לפונקציה Length
length = foo.Length()
print(f"Length: {length}")

# קריאה לפונקציה change עם מחרוזת חדשה
foo.change("hello world")

# קריאה מחדש לפונקציה display
foo.display()
