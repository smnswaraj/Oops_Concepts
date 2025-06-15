

# The DIAMOND PROBLEM LINK: https://www.geeksforgeeks.org/python/diamond-problem-in-python/
# BaseClass -> LeftSubclass
# BaseClass -> RightSubclass
# LeftSubclass & RightSubclass -> Subclass

print("\n-----------Diamond Problem------------")

class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Left Subclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self):
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print("Calling method on Subclass")
        self.num_sub_calls += 1

s = Subclass()
s.call_me()
# Output:
# Calling method on Base Class
# Calling method on Left Subclass
# Calling method on Base Class
# Calling method on Right Subclass
# Calling method on Subclass

# Thus we can clearly see the base class's call_me method being called twice. This
# could lead to some insidious bugs if that method is doing actual work—like
# depositing into a bank account—twice.

# Thus we can clearly see the base class's call_me method being called twice. This
# could lead to some insidious bugs if that method is doing actual work—like
# depositing into a bank account—twice.
# The thing to keep in mind with multiple inheritance is that we only want to call
# the "next" method in the class hierarchy, not the "parent" method. In fact, that next
# method may not be on a parent or ancestor of the current class. The super keyword
# comes to our rescue once again. Indeed, super was originally developed to make
# complicated forms of multiple inheritance possible. Here is the same code written
# using super:

print("\n--------Fixed Diamond Problem--------------")


class Subclass2(BaseClass):
    num_sub_calls = 0

class BaseClass_1:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubclass_1(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Left Subclass")
        self.num_left_calls += 1

class RightSubclass_1(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class Subclass_1(LeftSubclass_1, RightSubclass_1):
    num_sub_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        self.num_sub_calls += 1

s = Subclass_1()
s.call_me()

# Output:
# Calling method on Base Class
# Calling method on Right Subclass
# Calling method on Left Subclass
# Calling method on Subclass

print("\n--------Fixed Diamond Problem with KWARGS**--------------")

# First, call_me of Subclass calls super().call_me(), which happens to refer
# to LeftSubclass.call_me(). The LeftSubclass.call_me() method then calls
# super().call_me(), but in this case, super() is referring to RightSubclass.call_
# me().
# Pay particular attention to this: the super call is not calling the method on the
# superclass of LeftSubclass (which is BaseClass). Rather, it is calling RightSubclass,
# even though it is not a direct parent of LeftSubclass! This is the next method, not
# the parent method. RightSubclass then calls BaseClass and the super calls have
# ensured each method in the class hierarchy is executed once.

# Solution :

class Contact:
    all_contacts = []

    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street='', city='', state='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

# ✅ Create instance using keyword arguments
friend_obj = Friend(
    name="Swaraj",
    email="smnswaraj@gmail.com",
    street="2nd",
    city="BLR",
    state="KA",
    code="560048",
    phone="6202594196"
)

# You can check values
print(friend_obj.name)    # Swaraj
print(friend_obj.email)   # smnswaraj@gmail.com
print(friend_obj.street)  # 2nd
print(friend_obj.phone)   # 6202594196


# We've changed all arguments to keyword arguments by giving them an empty
# string as a default value. We've also ensured that a **kwargs parameter is included
# to capture any additional parameters that our particular method doesn't know what
# to do with. It passes these parameters up to the next class with the super call.

# If you aren't familiar with the **kwargs syntax, it basically collects
# any keyword arguments passed into the method that were not
# explicitly listed in the parameter list. These arguments are stored in a
# dictionary named kwargs.


# ANOTHER EXAMPLE FOR DIAMOND PROBLEM'S SOLUTION:

# When dealing with the diamond problem in Python and using super().__init__() with parameters,
# the key idea is to ensure all classes accept *args and **kwargs to allow flexible and
# clean passing of parameters through the MRO chain.

print("\n--------------------------------")

class A:
    def __init__(self, a_param, **kwargs):
        print(f"A initialized with a_param = {a_param}")
        super().__init__(**kwargs)

class B(A):
    def __init__(self, b_param, **kwargs):
        print(f"B initialized with b_param = {b_param}")
        super().__init__(**kwargs)

class C(A):
    def __init__(self, c_param, **kwargs):
        print(f"C initialized with c_param = {c_param}")
        super().__init__(**kwargs)

class D(B, C):
    def __init__(self, a_param, b_param, c_param):
        print("D initialized")
        super().__init__(a_param=a_param, b_param=b_param, c_param=c_param)

# Create an instance of D
obj = D(a_param=1, b_param=2, c_param=3)

# D initialized
# B initialized with b_param = 2
# C initialized with c_param = 3
# A initialized with a_param = 1

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)







