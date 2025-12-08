'''
Numpy is a fundamental library for scientific computing in Python. It provides support for 
arrays, matrices, and a wide range of mathematical functions to operate on these data
structures efficiently.

'''
import numpy as np 

# Creating arrays using numpy
arr_1 = np.array([1, 2, 3, 4,5])
print("Array 1:", arr_1)
print(type(arr_1))
print("Shape of Array 1:", arr_1.shape)

arr_2 = np.array([1, 2, 3, 4,5])
# arr_2.reshape(1,5)
print("Array 2:", arr_2)
print("Shape of Array 2:", arr_2.reshape(1,5))

# 2D Array
arr_3 = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 3:\n", arr_3)
print("Shape of Array 3:", arr_3.shape)

arr_4 = np.arange(0, 10, 2).reshape(5,1)
print("Array 4:\n", arr_4)
print("Shape of Array 4:", arr_4.shape)


arr_5 = np.ones((3, 4)) # Creates three dimensional array of ones with four columns
print("Array 5 (Ones):\n", arr_5)

# Identity Matrix
arr_6 = np.eye(4)  # Creates a 4x4 identity matrix
print("Array 6 (Identity Matrix):\n", arr_6)

# Numpy vectorized operations 

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

# Element-wise addition
add = a1 + a2
print("Element-wise Addition:", add)

# Element-wise subtraction
sub = a2 - a1
print("Element-wise Subtraction:", sub)

# Element-wise multiplication
mul = a1 * a2
print("Element-wise Multiplication:", mul)

# Universal Functions (ufuncs)
arr = np.array([1, 4, 9, 16, 25])
sqrt_arr = np.sqrt(arr)
print("Square Roots:", sqrt_arr)

# Exponential
exp_arr = np.exp(arr)
print("Exponential:", exp_arr)

# Sine 
sin_arr = np.sin(arr)
print("Sine Values:", sin_arr)

# natural log 
log_arr = np.log(arr)
print("Natural Logarithm:", log_arr)

# Array slicing and indexing 
arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)
print("Element at index 2:", arr[2])  # Output: 30
print("Elements from index 1 to 3:", arr[1:4])  # Output: [20 30 40]
# Modifying elements
arr[0] = 99
print("Modified Array:", arr)  # Output: [99 20 30 40 50]

# 2D Array Slicing
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D Array:\n", arr_2d)
print("Element at row 1, column 2:", arr_2d[1, 2])  # Output: 6 
print("First two rows and first two columns:\n", arr_2d[0:2, 0:2])
# Modifying a sub-array
arr_2d[0:2, 0:2] = 0
print("Modified 2D Array:\n", arr_2d)   

data  = np.array([1,2,3,4,5,6,7,8,9,10])
value = data[(data  >5) & (data < 8)]  # Output: [6 7]
print("Filtered Values:", value)

# Statistical operations
data = np.array([1, 2, 3, 4, 5])
print("Mean:", np.mean(data))  # Output: 3.0
print("Median:", np.median(data))  # Output: 3.0
print("Standard Deviation:", np.std(data))  # Output: 1.4142135623730951
print("Variance:", np.var(data))  # Output: 2.0