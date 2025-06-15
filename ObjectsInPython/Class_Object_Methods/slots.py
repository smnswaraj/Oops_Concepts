

# __slots__ is a special class attribute that tells Python to only allow a fixed set of attributes on instances of a class.
#
# It helps:
# Save memory
# Speed up attribute access
# Prevent adding new attributes dynamically


class Point:
    __slots__ = ('x', 'y')  # Only these two attributes are allowed

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
p.x = 5           # ✅ OK
p.z = 10          # ❌ AttributeError: 'Point' object has no attribute 'z'
