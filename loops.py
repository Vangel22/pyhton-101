i = 0
while i < 5:
    i += 1
    print(f"{i}." + "*"*i + "Loops are awesome" + "*"*i)
# Three Loop Questions:
# 1. What do I want to repeat?
#  -> message
# 2. What do I want to change each time?
#  -> stars
# 3. How long should we repeat?
#  -> 5 times

for letter in 'Norwegian blue':
    print(letter)

print("For Loop done!")

for furgle in range(8):
    print(furgle)

print("For Loop done!")

for furgle in range(1, 15, 3):
    print(furgle)

print("For Loop done!")

friends = ['John', 'Terry', 'Eric', 'Michael', 'George']
for friend in friends:
    print(friend)

print("For Loop done!")

friends = ['John', 'Terry', 'Eric']
for friend in friends:
    for number in [1, 2, 3]:
        print(friend, number)

print("For Loop done!")
