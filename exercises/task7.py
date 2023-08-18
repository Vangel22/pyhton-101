print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

operation = input(
    "Enter operation symbol (+,-,*,/) or f for Celsius-Fahrenheit conversion: ")
number_one = float(input("Enter digit one: "))
if operation == "f".lower():
    fhr = (number_one * 9 / 5) + 32
    print(f'{number_one} Celsius is equivalent to {fhr} fahrenheit')
else:
    number_two = float(input("Enter digit two: "))
    if operation == "+":
        sum = number_one + number_two
        print(sum)
    elif operation == "-":
        difference = number_one - number_two
        print(difference)
    elif operation == "*":
        product = number_one * number_two
        print(product)
    elif operation == "/":
        division = number_one / number_two
        print(division)
    else:
        print("Input error!")
