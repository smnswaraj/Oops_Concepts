
# 🔁 What is Polymorphism in Python?
# Polymorphism means "many forms".
# It allows objects of different classes to be treated as objects of a common super class,
# usually by sharing method names but with different implementations.

# different behaviors happen depending on
# which subclass is being used, without having to explicitly know what the subclass actually is.

# 🔷 Types of Polymorphism in Python

# | Type                         | Description                                          | Example                        |
# | ---------------------------- | ---------------------------------------------------- | ------------------------------ |
# | **1. Duck Typing**           | If it "quacks like a duck", it's treated like a duck | Object passed if it has method |
# | **2. Operator Overloading**  | Using operators like `+`, `*` on different types     | `5 + 3`, `'a' + 'b'`           |
# | **3. Method Overriding**     | Subclass redefines a method from parent class        | OOP inheritance                |
# | **4. Function Polymorphism** | Functions like `len()` work on different types       | `len("abc")`, `len([1, 2])`    |

# ✅ 1. DUCK TYPING:
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())

# Output:
# Woof!
# Meow!
# Moo!
# Here, the subclass overrides the base class method speak

# But to extend it:
class Alien(Animal):
    def speak(self):
        parent_sound = super().speak()  # Call parent method
        print(parent_sound + " + Woof!")  # Extend it

alien = Alien()
alien.speak()

#Output
# Some sound + Woof!

# ✅ 2. Operator Overloading



# ✅ 3. Method Overriding (Runtime Polymorphism)

class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):  # overridden
        print("Penguin can't fly")

b = Bird()
p = Penguin()

b.fly()  # Bird can fly
p.fly()  # Penguin can't fly

# ✅ 4. Function Polymorphism (Built-in)

print(len("hello"))     # 5 → string
print(len([1, 2, 3]))    # 3 → list
print(len({"a": 1}))     # 1 → dictionary



