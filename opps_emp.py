# Class definition
class Animal:
    def __init__(self, name):
        self.name = name  # Encapsulation: attribute is part of the class
    
    def speak(self):
        pass  # This will be defined in subclasses

class Dog(Animal):  # Inheritance: Dog inherits from Animal
    def speak(self):  # Polymorphism: same method name, different behavior
        return f"{self.name} says Woof!"

class Cat(Animal):  # Inheritance: Cat inherits from Animal
    def speak(self):
        return f"{self.name} says Meow!"

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling methods
print(dog.speak())  # Outputs: Buddy says Woof!
print(cat.speak())  # Outputs: Whiskers says Meow!
