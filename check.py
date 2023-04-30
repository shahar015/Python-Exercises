def improve(original_function):
    def new_function():
        print("*** > Before", original_function.__name__)
        original_function()
        print("*** < After", original_function.__name__)    
    return new_function 
@improve
def bluh():
    print("Foo!")

bluh()
