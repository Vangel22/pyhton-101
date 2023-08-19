def power(n):
    return n ** n


numbers = [1, 2, 3, 4]

result = map(power, numbers)


def greet(name):
    return f'Hi {name}!'


print(list(result))

friends_list = ['Eric', 'John', 'Michael', 'Terry', 'Graham']

res = map(greet, friends_list)

print(list(res))


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

sum = map(lambda x, y: x + y, numbers1, numbers2)
print(list(sum))
