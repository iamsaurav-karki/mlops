# OOPS is a programming paradigm that uses "objects" to design software.
# It is based on several key concepts including encapsulation, inheritance, polymorphism, and abstraction
# Class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

class Car: 
    pass 

# Creating an object of the Car class
audi = Car()
bmw = Car() 
print(type(audi))  # Output: <class '__main__.Car'>
print(type(bmw))   # Output: <class '__main__.Car'>
audi.door_count = 4
bmw.door_count = 2

print(audi)
print(bmw)
print(dir(audi))  # Lists all attributes and methods of the audi object


# Instance Variables and Methods

class Dog:
    # Constructor to initialize instance variables
    def __init__(self, name, age):
        # self is used to refer to the current instance of the class
        self.name = name,  
        self.age = age

# Creating an object of the Dog class
dog1 = Dog("Rocky", 3)
dog2 = Dog("Max", 5)

print(dog1.name)  # Output: Buddy
print(dog1.age)   # Output: 3
print(dog2.name)  # Output: Max
print(dog2.age)   # Output: 5


# Define a class with instance methods
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Instance method to calculate area
    def area(self):
        return 3.14 * (self.radius ** 2)

    # Instance method to calculate circumference
    def circumference(self):
        return 2 * 3.14 * self.radius
    
# Creating an object of the Circle class
circle1 = Circle(5)
print("Area:", circle1.area())  # Output: Area: 78.5
print("Circumference:", circle1.circumference())  # Output: Circumference: 31.400000000000002

# Modeling a Bank Account using OOP

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def get_balance(self):
        return self.balance


# Creating an object of the BankAccount class
account = BankAccount("Hari", 1000)
account.deposit(500)  # Deposited 500. New balance is 1500.
account.withdraw(200)  # Withdrew 200. New balance is 1300.
account.withdraw(2000)  # Insufficient funds!
print("Current Balance:", account.get_balance())  # Current Balance: 1300

