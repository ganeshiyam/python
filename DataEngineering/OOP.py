# OOP (Object Oriented Programming)
# OOP is a programming paradigm that revolves around the concept of objects.
# An object is a self contained unit that encapsulates data and behavior related to the data.
# In Python everything is a object, including Int, Str and even functions.
# Four Pillars - Encapsulation, Abstraction, Inheritance & Polymorphism

# Encapsulation
# Bundling data & methods that operate on that data within a single unit
# It provides data hiding and protects the internal implementation from outside interference.
# In python we achieve encapsulation using classes.
# Ex: Think of a Bank operations, everything gets protected within the Bank account

# Abstraction
# Allows us to hide the complex implementation details of an object and only expose the relevant features.
# Helps us focus on what an object does rather than how it does it.
# Abstract classes or interfaces in Python help achieve abstraction.

# Inheritance
# Creating hierarchies and allowing classes to inherit properties and methods from other classes.
# It promotes code reuse and enables us to build a hierarchy of classes.
# Python supports inheritance through base and derived classes.

# Polymorphism
# Enabling objects to take multiple forms.
# Objects can be treated as instances of their parent class or as instances of their child classes.
# This promotes flexibility and extensibility in code.

# Simple Class in Python
class Car:  # Car that represents basic car properties in Python
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f'{self.year} {self.make} {self.model}'


def oops_car():  # create objects (instances) of the Car class and use them:
    car1 = Car('Toyota', 'Tesla', 2022)
    car2 = Car('Tesla', 'Acura MDX', 2023)
    print(car1.display_info())
    print(car2.display_info())


class ElectricCar(Car):  # Create a new class ElectricCar that inherits from the Car class
    def __init__(self, make, model, year, battery_cap):
        super().__init__(make, model, year)
        self.battery_cap = battery_cap

    def display_info(self):
        return f'{self.year} {self.make} {self.model} with {self.battery_cap} kWh battery'


def oops_ev_car():  # Create an ElectricCar object and use its methods just like a regular Car object
    ev_car1 = ElectricCar('Nissan', 'Leaf', 2023, 40)
    ev_car2 = ElectricCar('Tesla', 'S', 2023, 400)
    ev_car3 = ElectricCar('Tesla', '3', 2023, 220)
    ev_car4 = ElectricCar('Tesla', 'X', 2023, 430)
    ev_car5 = ElectricCar('Tesla', 'Y', 2023, 280)
    ev_car6 = ElectricCar('Tesla', 'CyberTruck', 2023, 600)
    print(ev_car1.display_info())
    print(ev_car2.display_info())
    print(ev_car3.display_info())
    print(ev_car4.display_info())
    print(ev_car5.display_info())
    print(ev_car6.display_info())


if __name__ == "__main__":
    oops_car()
    oops_ev_car()
