"""Inheritance: Hiding the complex implementation details and showing only what's necessary"""
from abc import ABC, abstractmethod

# Abstract class: "Every animal MUST make a sound"
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass # just says "you must have this"

# Concrete classes: Each defines HOW they make a sound
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
# this works cause both have make_sound()
your_pets = [Dog(), Cat()]
for pet in your_pets:
    print(pet.make_sound())