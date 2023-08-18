# Sets - blazingly fast unordered Lists
# We can't get an element from set by index, because it is unordered

friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
friends_tuple = ('John', 'Michael', 'Terry', 'Eric', 'Graham')

friends_set = {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Eric'}
my_friends_set = {'Reg', 'Loretta', 'Colin', 'Eric', 'Graham'}

# In sets the duplicates are removed, in this case the last element Eric is removed

# print(friends)
# print(friends_tuple)
# print(friends_set)

print(friends_set.intersection(my_friends_set))
print(friends_set.union(my_friends_set))  # Removed duplicates
print(friends_set.difference(my_friends_set))  # Union - intersection


# empty Lists
empty_list = []
empyt_list = list()

# empty Tuple
empty_tuple = ()
empty_tuple = tuple()

# empty Set
empty_set = {}  # this is wrong, this is a dictionary
empty_set = set()
