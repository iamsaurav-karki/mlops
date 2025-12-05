"""
Iterators in Python allow for efficient looping and memory management.
They provide a way to access elements of a collection sequentially 
without exposing the underlying structure.
"""

My_List = [10, 20, 30, 40, 50]

# Creating an iterator
iterator = iter(My_List)
print(type(iterator))

# Iterating using next()
try:
    while True:
        value = next(iterator)
        print(value)
except StopIteration:
    print("Iteration finished.")

# Another example with try-except
iterator = iter(My_List)
try:
    while True:
        print(next(iterator))
except StopIteration:
    print("There are no more elements to iterate.")

# String Iterator
my_string = "Hello"
string_iterator = iter(my_string)
# Iterating using next()
try:
    while True:
        value = next(string_iterator)
        print(value)
except StopIteration:
    print("Iteration finished.")

# Another example with try-except
string_iterator = iter(my_string)
try:
    while True:
        print(next(string_iterator))
except StopIteration:
    print("There are no more elements to iterate.")