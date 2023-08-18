my_list = [1, 5, 3, 7, 2]  # sort doesn't return a list, it just sorts it
my_dict = {'car': 4, 'dog': 2, 'add': 3, 'bee': 1}

# Do not have a sorting function
my_tuple = ('d', 'c', 'e', 'a', 'b')
my_string = 'python'


print('original list', my_list)
# print(my_list.sort())  # same for my_list.reverse()
print(sorted(my_list))  # created a new list and printed it
print('new list', my_list)

print('original tuple', my_tuple)
print(sorted(my_tuple))  # returns sorted list
print('new tuple', my_tuple)

print(my_string, 'original string')
print(sorted(my_string))
print(my_string, 'new string')

print(my_dict, 'original dict')
# sorts by object KEY descending, returning in a list only keys
print(sorted(my_dict))
# sorts by object KEY descending, returning in a list only key:value
print(sorted(my_dict.items()))
# sorts by object VALUES descending, returning in a list only key:value
print(sorted(my_dict.values()))
print(my_dict, 'new dict')

print((reversed(my_list)))  # reversed object
print(list(reversed(my_list)))  # reversed object
print(my_list[::-1])

my_list = [1, 5, -3, 7, -2]
my_llist = [['car', 4, 65], ['dog', 2, 30], ['add', 3, 10], ['bee', 1, 24]]
print(sorted(my_list, key=abs))  # sorts the list and gets the absolute values
print(sorted(my_llist, key=lambda item: item[0]))
# item[0] sorts by add, bee, car, dog
# item[1] - 1,2,3,4
# item[2] - 10, 24, 30, 65
