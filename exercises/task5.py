# Sets - Exercise

# 1. Check if ‘Eric’ and ‘John’ exist in friends
# 2. combine or add the two sets
# 3. Find names that are in both sets
# 4. find names that are only in friends
# 5. Show only the names who only appear in one of the lists
# 6. Create a new cars-list without duplicates

friends = {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
my_friends = {'Reg', 'Loretta', 'Colin', 'John', 'Graham'}
cars = ['900', '420', 'V70', '911', '996',
        'V90', '911', '911', 'S', '328', '900']

new_cars = set(cars)

print('Eric' in friends and 'John' in friends)

# First
# set_one = friends.difference(my_friends)
# set_two = my_friends.difference(friends)
# unique_friends = set_one.union(set_two)
# print(unique_friends)

# Second
unique_friends = friends.symmetric_difference(my_friends)
# unique_friends = friends ^ my_friends


all_friends = friends.union(my_friends)
# all_friends = friends | my_friends
foaf = friends.intersection(my_friends)
# foaf = friends & my_friends
not_foaf = friends.difference(my_friends)
# not_foaf = friends - my_friends

print(all_friends)
print(foaf)
print(not_foaf)
print(unique_friends)
print(new_cars)
