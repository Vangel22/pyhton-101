from collections import Counter, OrderedDict

# collections module provides different types of containers
# container is an object that is used to store different objects and provide
# a way to access the contained objects and iterate over them
# Some of the build-in containers are Tuple, List, Dictionary

# Containers from the collections module:
# Counters
# OrderedDict
# DefaultDict
# ChainMap
# NamedTuple
# DeQue
# UserDict
# UserList
# UserString


# --- Counters ---

# With sequence of items
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B',
               'B', 'A', 'C']))

# with dictionary
print(Counter({'A': 3, 'B': 5, 'C': 2}))

# with keyword arguments
print(Counter(A=3, B=5, C=2))

# --- Ordered Dictionary ---
print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, value in d.items():
    print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)

# remove
od.pop('a')

# re-insert
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items():
    print(key, value)

# While deleting and re-inserting the same key will push
# the key to the last to maintain the order of insertion of the key.
