# What is encapsulation in Python?
'''
Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP) in Python.
It refers to the bundling of data (attributes) and methods (functions) 
that operate on that data into a single unit known as a class.
Encapsulation helps to restrict direct access to some of an object's components, 
which can prevent the accidental modification of data. 
This is typically achieved by using access specifiers to define the visibility of

'''
# Example of Encapsulation in Python

class Person:
    def __init__(self, name, age):
        self.name = name          # Public attribute
        self.__age = age         # Private attribute

    # Public method to access private attribute
    def get_age(self):
        return self.__age

    # Public method to modify private attribute
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")

# Creating an instance of the Person class
person = Person("Shyam", 30)
print("Name:", person.name)            # Accessing public attribute
print("Age:", person.get_age())        # Accessing private attribute via public method
person.set_age(35)                     # Modifying private attribute via public method
print("Updated Age:", person.get_age())

# Attempting to access private attribute directly will raise an AttributeError
# print(person.__age) # This will raise an error class members:
# - Public: Accessible from anywhere
# - Private: Accessible only within the class
# - Protected: Accessible within the class and its subclasses (conventionally indicated by

# Protected example 

class Employee:
    def __init__(self, name, salary):
        self.name = name              # Public attribute
        self._salary = salary         # Protected attribute

    def get_salary(self):
        return self._salary
    
# Creating an instance of the Employee class
employee = Employee("Ram", 50000)
print("Employee Name:", employee.name)          # Accessing public attribute
print("Employee Salary:", employee.get_salary()) # Accessing protected attribute via public method a single underscore)

# Accessing protected attribute directly (not recommended, but possible)
print("Accessing Protected Salary directly:", employee._salary)

# Accesssing from other class
class Manager(Employee):
    def display_info(self):
        print(f"Manager Name: {self.name}")
        print(f"Manager Salary: {self._salary}")  # Accessing protected attribute
# Creating an instance of the Manager class
manager = Manager("Hari", 80000)
manager.display_info()









