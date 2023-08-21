# A Geneartor is a function that returns an iterator with the yield keyword

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
# for value in simpleGeneratorFun():
#     print(value)

x = simpleGeneratorFun()

# print(next(x))
# print(next(x))
# print(next(x))

# generator expression
generator_exp = (i * 5 for i in range(5) if i % 2 == 0)

for i in generator_exp:
    print(i)
