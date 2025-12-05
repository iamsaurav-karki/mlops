
'''
Filter function is a built-in function in Python that
allows you to filter elements from an iterable (like a list, tuple, etc.) based on
a specified condition. It takes two arguments: a function that defines the condition and
an iterable to be filtered. The filter function returns an iterator that contains only the 
elements that satisfy the condition defined by the function.
'''

def is_even(num):
    return num % 2 == 0     

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10] 


# Using lambda function with filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

