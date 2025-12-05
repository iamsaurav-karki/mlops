# Inheritance is a fundamental concept in object-oriented programming (OOP) that 
# allows a class (called the child or subclass) to inherit attributes and methods from 
# another class (called the parent or superclass). This promotes code reusability 
# and establishes a hierarchical relationship between classes.

# Single Inheritance Example
# Base class (Parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"
    
# Derived class (Child class) inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Another derived class (Child class) inheriting from Animal
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")  
print(f"{dog.name} says: {dog.speak()}")  # Output: Buddy says: Woof!
print(f"{cat.name} says: {cat.speak()}")  # Output: Whiskers says: Meow!


# Another example of inheritance Base class
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"
    
    def start_engine(self):
        return "Engine started"

# Derived class inheriting from Car
class Tesla(Car):
    def __init__(self, model, battery_range):
        super().__init__("Tesla", model)  # Call the constructor of the base class
        self.battery_range = battery_range

    def info(self):
        base_info = super().info()  # Call the info method of the base class
        return f"{base_info}, Battery Range: {self.battery_range} miles"

# Creating an instance of the derived class
my_tesla = Tesla("Model S", 370)
print(my_tesla.info())  # Output: Tesla Model S, Battery Range: 370 miles
print(my_tesla.start_engine())  # Output: Engine started




# Multiple Inheritance Example
# Base class 1
class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print("subclasses must implement this method")

# Base class 2
class Pet:
    def __init__(self,owner):
        self.owner = owner
    def play(self):
        return f"{self.owner}'s pet is playing."
    
# Derived class inheriting from both Animal and Pet
class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)  # Initialize Animal part
        Pet.__init__(self, owner)    # Initialize Pet part

    def speak(self):
        return "Woof!"
    
# Creating an instance of the derived class
dog = Dog("Buddy", "Alice")
print(f"{dog.name} says: {dog.speak()}")  # Output: Buddy says: Woof!
print(dog.play())  # Output: Alice's pet is playing.


# Multilevel Inheritance Example
# Base class
class Vehicle:
    def start(self):
        return "Vehicle started"
# Derived class inheriting from Vehicle
class Car(Vehicle):
    def drive(self):
        return "Car is driving"
# Further derived class inheriting from Car
class ElectricCar(Car):
    def charge(self):
        return "Electric car is charging"

# Creating an instance of the most derived class
my_electric_car = ElectricCar()
print(my_electric_car.start())  # Output: Vehicle started
print(my_electric_car.drive())  # Output: Car is driving
print(my_electric_car.charge())  # Output: Electric car is charging


































































































































































