
# While duck typing is useful, it is not always easy to tell in advance if a class is going
# to fulfill the protocol you require. Therefore, Python introduced the idea of abstract
# base classes. Abstract base classes, or ABCs, define a set of methods and properties
# that a class must implement in order to be considered a duck-type instance of that
# class. The class can extend the abstract base class itself in order to be used as an
# instance of that class, but it must supply all the appropriate methods.

from collections.abc import Container

print(Container.__abstractmethods__)
# frozenset({'__contains__'})   -> one abstract method in Container class to implement

# One example for abstract class implementation.

from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def speak(self):
        pass  # Abstract method, must be implemented in subclass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Book(Animal):
    def read(self):
        return "Read!"

# animal = Animal()  # ❌ This will raise an error (can't instantiate abstract class)

dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!


book = Book() # TypeError: Can't instantiate abstract class Book with abstract method speak






