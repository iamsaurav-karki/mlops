'''
Generators are a simpler way to create iterators. They use the yield keyword to produce a series 
of values lazily, which means they generate values on the fly and do not store them in memory.
This makes generators more memory efficient for large datasets compared to traditional iterators.
'''
# def square(n):
#     for i in range(3):
#         return i**2
# print(square(5))  # Output: 0

def square(n):
    for i in range(5):
        yield i**2
print(square(5))  # Output: <generator object square at ...>

for i in square(5):
    print(i)

# Another way 

a = square(5)
print(next(a))  # Output: 0
print(next(a))  # Output: 1
print(next(a))  # Output: 4
print(next(a))  # Output: 9
print(next(a))  # Output: 16
# print(next(a))  # Raises StopIteration error


# Another Example 
def my_generator():
    yield 1 
    yield 2
    yield 3

gen = my_generator()                                
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))  # Output: 3
# print(next(gen))  # Raises StopIteration error

# using for loop 

for val in gen:
    print(val) 


# Practical Example : Reading Large Files 

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # Yield one line at a time, stripping whitespace

file_path = 'large_file.txt'  
for line in read_large_file(file_path):
    print(line)  # Process each line as needed
# This approach is memory efficient as it reads one line at a time instead of loading the entire file into memory.