
# Most object-oriented programming languages have the concept of a constructor,
# a special method that creates and initializes the object when it is created.
# Python is a little different; it has a constructor and an initializer. The constructor function is
# rarely used unless you're doing something exotic. So, we'll start our discussion
# with the initialization method.
# The Python initialization method is the same as any other method, except it has a
# special name, __init__. The leading and trailing double underscores mean this is
# a special method that the Python interpreter will treat as a special case.

class Point:
    def __init__(self, x=0, y=0):
        self.move(x,y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)


obj_1 = Point(1,2)
obj_2 = Point()    # here default value will be used by initializer (0,0)





# The constructor function is called __new__ as opposed to __init__, and accepts
# exactly one argument; the class that is being constructed (it is called before the object
# is constructed, so there is no self argument). It also has to return the newly created
# object. This has interesting possibilities when it comes to the complicated art of
# metaprogramming, but is not very useful in day-to-day programming. In practice,
# you will rarely, if ever, need to use __new__ and __init__ will be sufficient.



# It is important write API documentation that clearly summarizes what each object
# and method does. Keeping documentation up-to-date is difficult; the best way to
# do it is to write it right into our code.
# Python supports this through the use of docstrings. Each class, function, or
# method header can have a standard Python string as the first line following the
# definition (the line that ends in a colon). This line should be indented the same
# as the following code.


def add(x, y):
    '''This function adds two points together'''
    pass


class DataBase:
    def __init__(self):
        self.x = 0
        self.y = 1
        self.z = 2

