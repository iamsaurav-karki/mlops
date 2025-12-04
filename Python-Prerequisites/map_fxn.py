# Map function is used to apply a specific function to all items in an iterable (like list, tuple etc.) and return a map object (which is an iterator)

def square(x):
    return x * x

print(square(4))

numbers = [1, 2, 3, 4, 5]

mapped_squares = map(square, numbers) # takes two arguments, first is function name and second is iterable

print(list(mapped_squares))  # Output: [1, 4, 9, 16, 25]


# Lambda function with map

numbers = [1, 2, 3, 4, 5,6,7,8,9,10]
print(list(map(lambda x: x ** 2, numbers)))  # Output: [1, 4, 9, 16, 25]


# Map with multiple iterables
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

summed = map(lambda x, y: x + y, nums1, nums2)
print(list(summed))  # Output: [5, 7, 9]