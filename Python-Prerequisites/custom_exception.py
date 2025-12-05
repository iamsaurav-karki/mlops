# Raise and Throw Custom Exception in Python

class Error(Exception):
    pass

class dobException(Error):
    """Raised when the date of birth is invalid."""
    pass

age = int(input("Enter your Age: "))
current_age = 2025 - age

try:
    if age <= 30 and age >= 20:
        print("Your age is valid, so you can apply for the job.")
    else:
        raise dobException
except dobException:
    print("Error: Your age is not valid to apply for the job. Age must be between 20 and 30.")
