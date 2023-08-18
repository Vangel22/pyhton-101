# Always declare functions before you are going to use it

def greeting(name, age=18):
    print("Hello " + name + ", you are " + str(age) + " old.")
    print(f"Hello {name}, you are {age}.")

# with indentation the function sees line 4 as its body


# name = input("Enter your name: ")

# greeting(name, 23)
# greeting("John")


# Functions - Named notations

def greeting(name, age=28, color="red"):
 # Greets user with “name” from “input box” and “age”, if unavailable, default age is used

    print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
    print(f"We hear you like the color {color.lower()}!")


greeting(age=27, name="brian", color="Blue")

# Profile(1995,83.5,192,"blue") - not likely to know the inputs
# Profile(yob=1995,weight=83.5,height=192,eye_color="blue") - more easier

# Return statements


def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    # return amount, tax, total_amount - returns a tupple
    # return [amount, tax, total_amount] - returns a list
    # return {amount, tax, total_amount} - returns a set
    # return f'{amount}, {tax}, {total_amount}' - returns a string
    return amount, tax, total_amount


price = value_added_tax(100)
print(price, type(price))

# a = [3,7,42]
# b = [3,7,42]
# print(a == b) - comparison
# print(a is b) - this checks in memory
# print(id(a), id(b)) - memory
