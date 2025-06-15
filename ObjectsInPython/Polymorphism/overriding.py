
# ✅ 1. Overriding by Altering (Replacing)

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):  # override and alter
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks

print("\n-----------------------")


# ✅ 2. Overriding by Extending (Using super())

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Cat(Animal):
    def speak(self):  # override and extend
        super().speak()               # call parent method
        print("Cat meows")

c = Cat()
c.speak()


