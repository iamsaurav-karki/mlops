# What is operator overloading in Python?
'''
Operator overloading in Python allows you to define custom behavior for standard operators
(like +, -, *, etc.) when they are used with instances of user-defined classes.
By implementing special methods (also known as magic methods or dunder methods) in your classes,
you can specify how operators should behave for objects of those classes.
'''
# Mathematical operations for Vector
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overloading the - operator
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Overloading the * operator
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # String representation of the object
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
# Creating instances of Vector
v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1+v2)  # Output: Vector(6, 8)
print(v1-v2)  # Output: Vector(-2, -2)
print(v1*3)   # Output: Vector(6, 9)
