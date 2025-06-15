# 🔐 What is Encapsulation in Python?

# It means bundling data (variables) and the methods (functions) that operate on that data into
# a single unit — usually a class — and restricting direct access to some of the object’s internal components.

# ✅ Why Use Encapsulation?
# Protect internal state of an object.
# Prevent external modification of sensitive data.
# Control access via getter/setter methods or property decorators.

# 🧱 Example of Encapsulation in Python

class Student:
    def __init__(self, name, marks):
        self.name = name              # public
        self.__marks = marks          # private (with name mangling)

    def get_marks(self):
        return self.__marks           # Getter

    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value      # Setter with validation
        else:
            print("Invalid marks")

student = Student("Rahul", 85)

print(student.name)           # ✅ Accessible
print(student.get_marks())   # ✅ Controlled access

student.set_marks(110)       # ❌ Invalid
student.set_marks(90)        # ✅ Updated
print(student.get_marks())   # 90

# Trying direct access:
# print(student.__marks)     # ❌ AttributeError

# 🧠 Access Levels in Python
# Prefix	Type	         Meaning
# name	    Public	      Accessible everywhere
# _name	    Protected     (convention)	Meant for internal use
# __name	Private       (name mangled)	Restricted access
#
# 🔸 Python doesn’t enforce strict access control like Java/C++, but uses naming conventions
# and name mangling (_ClassName__var) to simulate privacy.
#
# ✅ Real-Life Example of Encapsulation
# Bank Account class — you wouldn’t want balance to be changed directly without rules:


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")

    def get_balance(self):
        return self.__balance


# 📌 Summary
# Concept	Purpose
# Encapsulation	Hides internal state
# Private variable	Prefix with __ to restrict access
# Getter/Setter	Controlled access to attributes
# @property	Pythonic way to get/set values

