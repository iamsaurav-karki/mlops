'''
Polymorphism in Python refers to the ability of 
different classes to be treated as instances of the same class through a common interface.
This allows methods to be used on different objects without needing to know their specific types.
Polymorphism is often achieved through method overriding and interfaces.
'''

# Method Overriding Example
# Method overriding allows a subclass to provide a specific implementation
# of a method that is already defined in its superclass.
class Bird:
    def speak(self):
        return "Chirp!"
class Parrot(Bird):
    def speak(self):
        return "Squawk!"
class Sparrow(Bird):
    def speak(self):
        return "Tweet!"

# Creating instances of the derived classes
parrot = Parrot()
sparrow = Sparrow()
print(parrot.speak())  # Output: Squawk!
print(sparrow.speak())  # Output: Tweet!

# Function that demonstrates polymorphism
def animal_sound(animal):
    print(animal.speak())
animal_sound(parrot)   # Output: Squawk!
animal_sound(sparrow)  # Output: Tweet!


# Polymorphism  with functions and methods 

# Base Class 
class Shape:
    def area(self):
        return "The area of the figure"
    
# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    
# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
# Function to calculate area using polymorphism
def calculate_area(shape):  
    print(f"The area is: {shape.area()}")

circle = Circle(5)
rectangle = Rectangle(4, 6) 
calculate_area(circle)      # Output: The area is: 78.5
calculate_area(rectangle)   # Output: The area is: 24

# Polymorphism with abstract base classes
# Abstract base classes are used to define common methods for a group of related objects.

from abc import ABC, abstractmethod
# Abstract Base Class  , Abstract class is a complete empty class.
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Derived class Car
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
# Derived class Motorcycle
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

# creating objects of derived classes
car = Car()
motorcycle = Motorcycle()
print(car.start_engine())         # Output: Car engine started
print(motorcycle.start_engine())  # Output: Motorcycle engine started