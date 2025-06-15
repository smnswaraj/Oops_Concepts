

# Multiple inheritance is a touchy subject. In principle, it's very simple: a subclass that
# inherits from more than one parent class is able to access functionality from both of
# them. In practice, this is less useful than it sounds and many expert programmers
# recommend against using it.

# The simplest and most useful form of multiple inheritance is called a mixin. A mixin
# is generally a superclass that is not meant to exist on its own, but is meant to be
# inherited by some other class to provide extra functionality.

class Father:
    def __init__(self, name):
        print("Father: Constructor called")
        self.name = name
        self.father_skill = "Carpentry"

    def show_father_skill(self):
        print(f"Father skill: {self.father_skill}")


class Mother:
    def __init__(self, name):
        print("Mother: Constructor called")
        self.name = name
        self.mother_skill = "Painting"

    def show_mother_skill(self):
        print(f"Mother skill: {self.mother_skill}")


class Child(Father, Mother):
    def __init__(self, f_name, m_name, name):
        print("Child: Constructor called")
        Father.__init__(self, f_name)     # Explicitly calling each parent's initializer
        Mother.__init__(self, m_name)
        self.name = name
        self.child_skill = "Coding"

    def show_child_skill(self):
        print(f"Child skill: {self.child_skill}")


# Create object
c = Child("swaraj", "LKM", "BM")

# Access all methods
c.show_father_skill()
c.show_mother_skill()
c.show_child_skill()


# Due to multiple inheritane c can access both Father and Mother attributes/methods.


# Multiple inheritance works all right when mixing methods from different classes,
# but it gets very messy when we have to call methods on the superclass. There are
# multiple superclasses. How do we know which one to call? How do we know
# what order to call them in ?
# The tricky part is that we now have two parent __init__ methods
# both of which need to be initialized. And they need to be initialized with different
# arguments. How do we do this? Well, we could start with a naive approach:

# In this example, we directly call the __init__ function on each of the superclasses
# and explicitly pass the self argument. This example technically works; we can
# access the different variables directly on the class. But there are a few problems.

# First, it is possible for a superclass to go uninitialized if we neglect to explicitly call
# the initializer.

# Second, and more sinister, is the possibility of a superclass being called multiple times
# because of the organization of the class hierarchy.

# Child -> Father -> object class
# Child -> Mother -> object class
# This means the parent class has been set up twice. With
# the object class, that's relatively harmless, but in some situations, it could spell
# disaster. Imagine trying to connect to a database twice for every request!
# The base class should only be called once.

# The order in which methods can be called can be adapted on the fly
# by modifying the __mro__ (Method Resolution Order) attribute on
# the class.









