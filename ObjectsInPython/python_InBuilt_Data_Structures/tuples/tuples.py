
# Tuples and named tuples

# Tuples are objects that can store a specific number of other objects in order. They
# are immutable, so we can't add, remove, or replace objects on the fly.

my_tuple_1 = ('swaraj', 1,2 ,3)
my_tuple_2 = 'swaraj', 1,2 ,3

# A namedtuple is a subclass of Python’s built-in tuple, from the collections module, that allows you to:
# Access elements by name (like .x, .y) instead of just by index
# Have readable, self-documenting code
# Keep the immutability and lightweight nature of a tuple

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(10, 20)
print(p.x)  # 10
print(p.y)  # 20
print(p[0]) # 10 (still acts like a tuple)











