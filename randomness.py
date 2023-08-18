import random
import string

# generates numbers between 0 and 1 but not 1
# print(random.random())

# 5 randoms
for i in range(5):
    # to generate numbers by 6
    # print(random.random() * 6)
    # generate random number in range 1 to 6
    # print(random.uniform(1, 6))
    # random integers
    # print(random.randint(1, 6))
    # from to and steps
    # print(random.randrange(1, 100, 2))  # odd numbers
    print(random.randrange(2, 100, 2))  # even numbers


friends_list = ['John', 'Eric', 'Michael', 'Terry', 'Graham']
# print(random.choice(friends_list))
# print(random.sample(friends_list, 3))  # does not hold duplicates
# can have duplicates when random choosing
# print(random.choices(friends_list, k=5))

# changes order of the list
# random.shuffle(friends_list)
# print(friends_list)

smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
letters_numbers = string.ascii_letters + string.digits
word = ''

for i in range(7):
    word += random.choice(letters_numbers)

word1 = ''.join(random.sample(letters_numbers, 7))
# word = random.choices(letters_numbers, k=7) # same as the for loop

print(word)
print(word1)  # this will never have duplicates
