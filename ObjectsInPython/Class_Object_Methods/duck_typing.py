

# Duck typing in Python is a concept of dynamic typing where the type of an object is
# determined by its behavior (methods and properties) rather than its class or inheritance.


class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm imitating a duck!")

def make_it_quack(entity):
    entity.quack()  # No type check, just call

duck = Duck()
person = Person()

make_it_quack(duck)    # Output: Quack!
make_it_quack(person)  # Output: I'm imitating a duck!


# Errors might happen at runtime if the object doesn't have the expected methods

# make_it_quack(42)  # Will raise AttributeError

# To handle such cases gracefully, Python often uses EAFP
# (Easier to Ask Forgiveness than Permission) style with try/except.
