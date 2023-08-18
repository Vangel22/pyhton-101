friends = ['John', 'Marty', 'Doe', 'Future']

# print(friends)
# print(friends[1])
# print(friends[1:3])  # [from, to)
# print(len(friends))
# print(friends.index('Doe'))
# print(friends.count('Future'))

cars = [911, 540, 922, 525, 320, 335]

cars.sort()
cars.sort(reverse=True)  # reverses in decending order

cars.reverse()  # the original string reversed

# print(cars)

# print(min(cars))  # lowest from the list
# print(max(cars))  # highest from the list
# print(sum(cars))  # sum of cars

# Adding entry
cars.append(650)
cars.insert(1, 750)

# print(cars)

cars_tmp = [100, 200, 300]

cars.extend(cars_tmp)
# print(cars)

cars.remove(300)
cars.pop()  # returns the popped value, at the end of the list
cars.pop(-1)

print(cars)

print(friends)
friends.clear()  # list is now empty
print(friends)

del friends  # deletes friends from memory
del friends[1]  # deletes entry at entry 2 - deletes an object?

new_friends = friends[:]  # or
# new_friends = friends.copy() # or
# new_friends = list(friends)
print(friends)
print(new_friends)
