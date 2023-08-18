nums = [1, 2, 3, 4]
nums2 = '1234'
letters = ['a', 'b', 'c', 'd']
names = ['John', 'Eric', 'Michael', 'Graham', 'Joe']

# combo = zip(nums, letters)
# combo = zip(nums2, letters)
combo = list(zip(nums, letters, names))

# print(combo) # prints zip object
# print(combo)  # prints a list of tuples, matched by index number

# unzip, called unpacking into three different variables
num, let, nam = zip(*combo)  # vals stored as tupple
# print(num)
# print(let)
# print(nam)

# With dictionaries
keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'

keys = keys.split()
values = values.split()
print(keys, values)
en_sv_dict = dict(zip(keys, values))
print(en_sv_dict)

# comprehension
new_dict = {key: value for key, value in zip(keys, values)}
print(new_dict)

en, sv = list(en_sv_dict.keys()), list(en_sv_dict.values())
print(en)
print(sv)

en1, sv1 = zip(*en_sv_dict.items())
print(en1, sv1)  # prints in typles
