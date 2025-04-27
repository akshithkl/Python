x = 5  # variable (global)

class Dog:
    def __init__(self, name):
        self.name = name  # attribute

d = Dog("Tommy")
print(x)        # variable
print(d.name)   # attribute
