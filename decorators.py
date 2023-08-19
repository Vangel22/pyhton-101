# Used to modify the behaviour of a function or a class
# Functions are first class objects meaning they can be used or passed as argument

# Python program to illustrate functions
# can be passed as arguments to other functions
import math
import time


def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func(
        """Hi, I am created by a function passed as an argument.""")
    print(greeting)


# greet(shout)
# greet(whisper)


# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

# print(add_15(10))

# Decorators are objects, functions used to modify the behaviour of a function or a class

# Example 1 - demo

# def decorator_fun(func):
#     def inner_fun():
#         print("Hello, this is before function execution")
#         func()
#         print('After func argument execution')
#     return inner_fun


# def func_used():
#     print('This is inside the inner function')


# func_used = decorator_fun(func_used)
# func_used()

# Example two - syntax change

# def calculate_time(func):
#     def inner(*args):
#         begin = time.time()
#         func(*args)
#         end = time.time()
#         print("Total time taken in : ", func.__name__, end - begin)
#     return inner


# @calculate_time
# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))


# factorial(10)

# Example 3 - return value

# def hello_decorator(func):
#     def inner(*args):
#         print('Before execution')
#         returned_val = func(*args)
#         print('After execution')
#         return returned_val
#     return inner


# @hello_decorator
# def sum_two_num(a, b):
#     print('Inside sum func')
#     return a + b


# a, b = 1, 2

# print("Sum =", sum_two_num(a, b))

# Example 4 - chaining decorators
def decorator_one(func):
    def inner():
        x = func()
        return x * x
    return inner


def decorator(func):
    def inner():
        x = func()
        return 2 * x
    return inner


@decorator_one
@decorator
def num():
    return 10


@decorator
@decorator_one
def num_two():
    return 10


print(num())
print(num_two())

# Same as calling
# decorator_one(decorator(num))
# decorator(decorator_one(num_two))
