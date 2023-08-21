from collections import Counter, OrderedDict, defaultdict, ChainMap, namedtuple, deque

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

# print('\nAfter re-inserting')
# for key, value in od.items():
#     print(key, value)

# While deleting and re-inserting the same key will push
# the key to the last to maintain the order of insertion of the key.

# Default dict -  It is used to provide some default values for the key
# that does not exist and never raises a KeyError.

# df_dict_arr = defaultdict(int)

# L = [1, 2, 3, 4, 2, 4, 1, 2]

# for i in L:
#     df_dict_arr[i] += 1

# print(df_dict_arr)

# df_dict_list = defaultdict(list)

# for i in L:
#     df_dict_list[i].append(i)

# print(df_dict_list)

# Chain map
# A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d4 = {'g': 7, 'h': 8}


# Defining the chainmap
c = ChainMap(d1, d2, d3)

# Accessing Values using key name
# print(c['a'])

# Accessing values using values()
# method
# print(c.values())

# Accessing keys using keys()
# method
# print(c.keys())

# new_child() adds new dictionary at the beggining of the Chain Map
c = c.new_child(d4)

# print(c)

# NamedTupple - returns a tuple object with names for each position which the ordinary tuples lack.

Student = namedtuple('Student', ['name', 'age', 'DOB'])
S = Student('Vangel', 23, '24111999')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)

# initializing iterable
li = ['Manjeet', '19', '411997']

# initializing dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# using _make() to return namedtuple()
# print("The namedtuple instance using iterable is  : ")
# print(Student._make(li))

# # using _asdict() to return an OrderedDict()
# print("The OrderedDict instance using namedtuple is  : ")
# print(S._asdict())

# Deque - Doubly ended queue O(1) for pop and append

# Declaring deque
# queue = deque([1, 2, 3])
# queue.append(4)  # at the end
# queue.appendleft(0)  # at start

# print(queue)

# queue.pop()  # at the end
# queue.popleft()  # at start

# print(queue)
