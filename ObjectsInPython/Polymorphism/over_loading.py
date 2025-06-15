
# 🔁 What is Function Overloading in Python?
# In many languages (like C++ or Java), function overloading means defining multiple functions with the same name but different parameters (type or count).
#
# 🔹 Python does NOT support function overloading in the traditional way, because functions are overwritten if you define them multiple times.
#
# ❌ This does NOT work in Python:

def greet(name):
    print("Hello", name)

def greet(name, age):  # ❌ This replaces the above function
    print("Hello", name, "you are", age)

greet("Suman")  # ❌ TypeError: missing 1 required positional argument

