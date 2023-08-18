# Comprehensions are a tool that enables us to create list, tuples, sets, dictionaries

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# give me a list with num squared for each num in numbers
new_list = []
for num in numbers:
    new_list.append(num * num)
print(new_list)

# same as above
new_list = [num * num for num in numbers]
# print(new_list)

# give me a list with num for each num in numbers if num is even
new_list = [num for num in numbers if num % 2 == 0]
print(new_list)


# filter returns a filter object
new_list = filter(lambda num: num % 2 == 0, numbers)
print(list(new_list))

# I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
new_list = []
for letter in 'spam':
    for num in range(4):
        new_list.append((letter, num))
print(new_list)

# with comprehension
new_list = [(letter, num) for letter in 'spam' for num in range(4)]
print(new_list)

# 1. variable naming
# 2. storage variable must be the same as the variable name in the loop
# 3. looping
# 4. close []
my_var_name = [data for data in ['a', 'b', 'c']]
# 2.1 data is the name that should be used
