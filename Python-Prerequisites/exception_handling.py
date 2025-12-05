# Working with exception Handling in Python
'''
Exception handling in Python is done using the try, except, else, and finally blocks.
It allows you to gracefully handle errors and exceptions that may occur during the execution of your code.
Exception are events that can disrupt the normal flow of a program's execution.
They occur when an error is encountered during program execution, such as division by zero, file not found, or invalid input.
'''

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    else:
        return f"The result is: {result}"
    finally:
        print("Execution of divide_numbers function is complete.")
# Finally block is executed no matter what, whether an exception occurred or not.

# Testing the function
print(divide_numbers(10, 2))  # Valid division
print(divide_numbers(10, 0))  # Division by zero
print(divide_numbers(10, 'a'))  # Invalid input type


# Another example of exception 
try:
    a = b # 'b' is not defined, this will raise a NameError
except:
    print("An exception occurred: Variable 'b' is not defined.")


try:
    d = e 
except NameError as ne:
    print(ne)  # prints the specific error message

# File not found exception handling
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file was not found.")

# Handling multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Result: {result}")

# Handing memory error exception
# try:
#     large_list = [0] * (10**10)  # Attempting to create a very large list
# except MemoryError:
#     print("Error: Memory limit exceeded while trying to create a large list.")


try:
    result = 1/2 
    f=g 
except ZeroDivisionError as ex:
    print(ex)
except Exception as e:   # All the exceptions is derived from Exception class, so it will catch any exception
    # Write the Exception class in last to catch all the exceptions , not before specific exceptions
    print("An error occurred:", e)
    print("Main exception caught here.")

# File handling and Exception handling 
try:
    file = open('sample.txt', 'r')
    content = file.read()
    a=b
except FileNotFoundError as fnf_error:
    print("FileNotFoundError:", fnf_error)
except Exception as e:
    print("Exception:", e)
finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print("File closed.")