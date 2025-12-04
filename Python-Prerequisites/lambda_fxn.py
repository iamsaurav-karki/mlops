# Lambda functions is a small anonymous function which can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments: expression
square = lambda x: x * x
print(square(5))  # Output: 25


# Example with multiple arguments
add = lambda a, b: a + b
print(add(3, 7))  # Output: 10

# Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
