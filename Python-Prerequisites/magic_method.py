'''
Magic methods in Python are special methods that start and end with double underscores (__). 
They allow you to define the behavior of your objects for built-in operations, such as addition, subtraction, 
string representation, and more. By implementing these methods in your classes, you can customize how your objects 
interact with Python's built-in functions and operators. 
Also known as dunder methods (double underscore methods).
'''
# Example of Magic Methods in Python
'''
__init__ : Constructor method to initialize object attributes.
__str__ : String representation of the object.
__add__ : Defines behavior for the addition operator (+).
__len__ : Defines behavior for the len() function.
__getitem__ : Defines behavior for indexing and slicing.

'''
# Basic Magic Methods Example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Nabin", 30)
print(person)  # Output: <__main__.Person object at 0x...>

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
    
person = Person("Nabin", 30)
print(person)  # Output: <__main__.Person object at 0x...>
print(str(person))  # Output: Person(Name: Nabin, Age: 30)
print(repr(person)) # Output: Person('Nabin', 30)

