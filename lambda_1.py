# Single line functions that we can use in one line and then throw away
# Lambdas or anonymous functions

# Normal function

def square(x):
    return x*x

# name = lambda parameter(s): expression

# Lambda function


def square1(x): return x*x


def double_mult(x, y): return 2*x*y


# print(square(3))
# print(square1(4))
# print(double_mult(2, 3))


def name_and_alias(name, alias):
    return name.strip().title() + ':' + alias.strip().title()


def name_and_alias1(name, alias): return name.strip(
).title() + ":" + alias.strip().title()


# print(name_and_alias(' john  ClEEse  ', 'HECKLER'))
# print(name_and_alias1(' john  ClEEse  ', 'HECKLER'))

monty_python = ['John Marwood Cleese', 'Eric Idle', 'Michael Edward Palin',
                'Terrence Vance Gilliam', 'Terry Graham Perry Jones', 'Graham Arthur Chapman']


def sort_names(name):
    return name.split(' ')


monty_python.sort(key=lambda name: name.split(' ')[-1])  # sorted by last name
print(monty_python)
monty_python.sort(key=sort_names)
print(monty_python)
