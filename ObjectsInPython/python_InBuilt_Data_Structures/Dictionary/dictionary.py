
# defaultdict is a subclass of Python('s built-in dict (dictionary) — from the collections module'
# — that automatically assigns a default value to a key that doesn')t exist instead of raising a KeyError.


from collections import defaultdict

# Creates a dict where default value is 0
counts = defaultdict(int)

counts['apple'] += 1
counts['banana'] += 1
print(counts)  # {'apple': 1, 'banana': 1}

# WITHOUT DEFAULTDICT

d = {}
d['apple'] += 1  # ❌ KeyError: 'apple'

# COMMON DEFAULTFACTORY -> counts = defaultdict(defaultfactory)

# | Factory       | Meaning                |
# | ------------- | ---------------------- |
# | `int`         | Default value: `0`     |
# | `list`        | Default value: `[]`    |
# | `set`         | Default value: `set()` |
# | `str`         | Default value: `''`    |
# | `lambda: 100` | Default value: `100`   |



























