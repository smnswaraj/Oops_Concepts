
# DECORATORS
# Decorator is a function that wraps another function to modify or extend its behavior.
#Example

def my_decorator(func):
    def wrapper():
        print("Something before the function runs.")
        func()
        print("Something after the function runs.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Something before the function runs.
# Hello!
# Something after the function runs.

# say_hello() is passed into my_decorator
# my_decorator returns the wrapper() function
# When you call say_hello(), it actually runs wrapper()



# ------------------------------------------------------------

# @classmethod is a decorator used to define a class method.
# A class method takes cls (not self) as its first argument.
# It can access or modify class-level data, but not instance-level data directly.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        from datetime import datetime
        age = datetime.now().year - birth_year
        return cls(name, age)

p1 = Person("John", 30)
p2 = Person.from_birth_year("Alice", 2000)

print(p1.name, p1.age)  # Output: John 30
print(p2.name, p2.age)  # Output: Alice 25 (or current age)


# Another Example:

class Counter:
    count = 0  # class variable

    @classmethod
    def increment(cls):
        cls.count += 1
        return cls.count

print(Counter.increment())  # Output: 1
print(Counter.increment())  # Output: 2



#______________________________________________

# @property is used to define a method that you can access like an attribute.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.area)  # ✅ Access like an attribute (not c.area())

# -----------------------------------------------

# The @dataclass decorator (from the dataclasses module) automatically generates boilerplate code for classes that are mainly used to store data.
# It adds:
# __init__()
# __repr__()
# __eq__()
# Optionally: __lt__(), __le__(), etc.
# You don't need to write these yourself!

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

# This is equivalent to writing:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

# -----------------------------------------------





















