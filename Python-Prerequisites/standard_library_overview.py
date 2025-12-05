'''
Standard library overview in Python includes a wide range of modules and packages
that provide various functionalities such as file I/O, system calls, data serialization,
mathematical operations, and more. Some commonly used standard library modules are: 
- os: for interacting with the operating system
- sys: for accessing system-specific parameters and functions
- math: for mathematical functions
- datetime: for manipulating dates and times
- json: for working with JSON data
- re: for regular expressions
- collections: for specialized container datatypes
- itertools: for creating iterators for efficient looping
These modules can be imported and used in your Python programs to perform various tasks
'''

import os
import sys
import math
import datetime
import json
import re
import collections
import itertools
import array
import random 
import shutil
import timedelta

# Example usage of some standard library modules
# Using os module to get current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Using sys module to get Python version
python_version = sys.version
print("Python Version:", python_version)

# Using math module to calculate square root
sqrt_16 = math.sqrt(16)
print("Square root of 16:", sqrt_16)

# Using datetime module to get current date and time
now = datetime.datetime.now()
print("Current Date and Time:", now)

yesterday = now - datetime.timedelta(days=1)
print("Yesterday's Date and Time:", yesterday)

# Using json module to serialize a Python dictionary
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
json_data = json.dumps(data)
print("JSON Data:", json_data)

# Using re module to find all words starting with 'a' or 'A'
text = "Alice and Bob are attending an art exhibition."
words_starting_with_a = re.findall(r'\b[aA]\w*', text)
print("Words starting with 'a' or 'A':", words_starting_with_a)

# Using collections module to create a counter
counter = collections.Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print("Fruit Counter:", counter)    

# Using array module to create an array of integers
int_array = array.array('i', [1, 2, 3, 4, 5])
print("Integer Array:", int_array.tolist())


# Using random module to generate a random number
random_number = random.randint(1, 100)
print("Random Number between 1 and 100:", random_number)
print("Random Choice from list:", random.choice(['apple', 'banana', 'cherry']))


# Using os to make a new directory
new_dir = "test_directory"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created.")
else:
    print(f"Directory '{new_dir}' already exists.")

# Cleaning up by removing the created directory
os.rmdir(new_dir)
print(f"Directory '{new_dir}' removed.")    


# High level operations on files 
source_file = "source.txt"  
with open(source_file, 'w') as f:
    f.write("This is a test file.")
destination_file = "destination.txt"
shutil.copy(source_file, destination_file)
print(f"File copied from '{source_file}' to '{destination_file}'.")

# Clean up created files
os.remove(source_file)
os.remove(destination_file)
print(f"Files '{source_file}' and '{destination_file}' removed.")

# Data serialization using json
data = {'name': 'Bob', 'age': 25, 'city': 'San Francisco'}
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)
print("Data serialized to 'data.json'.")
print(type(data))

# Data deserialization using json
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)
print("Data loaded from 'data.json':", loaded_data)
print(type(loaded_data))

# What is the difference between json.dumps and json.dump?
# json.dump() writes JSON data to a file-like object
# json.dumps() returns the JSON data as a string



data2 = {'name': 'saurav', 'age': 23, 'city': 'kathmandu'}
json_str = json.dumps(data2)
print("Serialized JSON string:", json_str)
print(type(json_str))

loaded_data2 = json.loads(json_str)
print("Deserialized data:", loaded_data2)
print(type(loaded_data2))



# More reqular expression examples

pattern = r'\d+'  # pattern to match one or more digits
text = "There are 3 apples and 5 bananas."
matches = re.findall(pattern, text)
print("Digits found in text:", matches)  # Output: ['3', '5']

