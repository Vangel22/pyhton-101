# my_file = open('greeting.txt', 'r')

# # print(my_file.read())
# # print(my_file.read(10))  # how many chars we want to read
# # print(my_file.readline())  # reads line by line - only the first in this case

# # these are the same
# line_by_line = my_file.readlines()
# line_by_line1 = my_file.read().splitlines()
# print('readlines: ', line_by_line)
# print('splitlines: ', line_by_line1)


# my_file = open('greeting.txt', 'r')  # w, a
# print(my_file.read(10))
# print(my_file.readline())
# print(my_file.readline())

# If we previously read the file, error occurs
# Solution: You read the file already, and the file pointer is not at the end of the file.
# Calling readlines() then will not return data. Read the file just once:
# line_by_line = my_file.readlines()
# line_by_line1 = my_file.read().splitlines()  # same for splitlines()
# print('readlines: ', line_by_line)
# this will be empty - comment 22 and 24 to see it populated
# print('splitlines: ', line_by_line1)

# my_file.close()

# Context management will close the file for us
with open('friends.csv', 'r') as f:
    # print(f.read()) # this line make the next one not return result as mentioned above
    friends = f.read().splitlines()
    for friend in friends:
        friend = friend.split(',')
        name = friend[0]
        year = int(friend[1].strip())  # removes the whitespace after the comma
        # print(f'In 2030 {name} will be {2030 -year} years old')


with open('movies.txt', 'r') as f:
    for line in f:
        print(line)


# The with keyword note
# In Python, the with statement replaces a try-catch block with a concise shorthand.
# More importantly, it ensures closing resources right after processing them.
