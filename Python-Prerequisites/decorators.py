'''
Decorators are a powerful and flexible feature in Python that allow you to modify the 
behavior of functions or methods. They are often used for logging, access control, 
instrumentation, and caching.
'''

# Function Copy 
def welcome():
    return "Welcome to the Decorators Example!"

welcome_copy = welcome
print(welcome_copy())  # Output: Welcome to the Decorators Example!

del welcome
print(welcome_copy())  # Output: Welcome to the Decorators Example!

# Closures - Function inside another function
def outer_function(msg):
    def inner_function():
        return f"Message: {msg}"
    return inner_function
closure_func = outer_function("Hello, World!")
print(closure_func())  # Output: Message: Hello, World!

# Basic Decorator
def simple_decorator(func):
    """
    A simple decorator that prints messages before and after
    the decorated function is called.
    """
    def wrapper():
        print(">>> Starting function execution...")
        func()  # Call the original function
        print(">>> Function execution finished.")
    return wrapper

@simple_decorator
def greet():
    """
    A simple function to be decorated.
    """
    print("Hello, World!")

# Calling the decorated function
greet()

# Real World Decorator Example - Timing a function
import time
def timer_decorator(func):
    """
    A decorator that measures the execution time of the decorated function.
    """
    def wrapper(*args, **kwargs): # args and kwargs means any number of arguments
        start_time = time.time()
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds.") 
        # func.__name__ gives the name of the function 
        # .__name__ is a special attribute in Python that holds the name of the object
        return result
    return wrapper
@timer_decorator # This means compute_squares = timer_decorator(compute_squares)
def compute_squares(n):
    """
    A function that computes the squares of numbers from 0 to n-1.
    """
    return [i ** 2 for i in range(n)]   
# Calling the decorated function
squares = compute_squares(100000)
print(f"Computed {len(squares)} squares.")
    