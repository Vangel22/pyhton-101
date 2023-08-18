# Note - you can't name the file enum.py
print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']
# efriends = [(51,'Brian'), (52,'Judith'), (53,'Reg'), (54,'Loretta'), (55,'Colin')]
#  - this is what enumerate does - it turns the elements into an tuples


# i = 1
# for friend in friends:
#     print(i, friend)
#     i = i + 1  # += 1

for num, friend in enumerate(friends, 51):
    print(num, friend)

print(type(enumerate(friends)))
print(list(enumerate(friends)))
