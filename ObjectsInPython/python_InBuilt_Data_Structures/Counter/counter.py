

# Counter is a class in the collections module used to count occurrences of elements in an iterable (like a list, string, etc.).
# It returns a dictionary-like object where:
# Keys are the items from the input
# Values are the counts of those items

from collections import Counter

text = "banana"
counter = Counter(text)
print(counter)
# Counter({'a': 3, 'n': 2, 'b': 1})


items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
c = Counter(items)
print(c)
# Counter({'apple': 3, 'banana': 2, 'orange': 1})


