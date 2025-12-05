import math  # importing math module to use its functions 

'''
Math have lots of inbuilt functions like sqrt, pow, factorial, etc.
'''

print(math.sqrt(16))  # returns square root of 16
print(math.pow(2, 3))  # returns 2 raised to the power 3
print(math.factorial(5))  # returns factorial of 5


## Importing specific function from module
from math import sqrt, pow, pi
print(sqrt(25))  # returns square root of 25
print(pow(3, 4))  # returns 3 raised to the power 4
print(pi)  # returns value of pi


# Using Numpy package for numerical operations
import numpy as np    
'''
Numpy is a powerful package for numerical computations in Python. It provides support for arrays, matrices, and a 
wide range of mathematical functions to operate on these data
'''
array = np.array([1, 2, 3, 4, 5])
print("Numpy Array:", array)
print("Mean:", np.mean(array))
print("Standard Deviation:", np.std(array))

# Importing Everything from math module
from math import *
print(log(100, 10))  # returns logarithm of 100 to base 10
print(cos(pi))  # returns cosine of pi
print(sin(pi / 2))  # returns sine of pi/2


# Using Custom Package
from package.maths import addition 
# OR 
# from package import maths

result = addition(10, 5)  # Using addition function from custom package
print(result)

# Using subtraction function from custom package
from package.maths import subtraction
result = subtraction(10, 5)
print(result)

# using all functions from the custom package
from package.maths import *
print(multiplication(4, 5))
print(division(20, 4))
print(division(10, 0))  # Testing division by zero case


# Using factorial function from subpackage
from package.subpackages.factorial import fact
print(fact(5))  # Output: 120