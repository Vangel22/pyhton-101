greet = 'welcome to Python 101: Strings'
greetMod = greet[18] + " " + greet[:8] + \
    greet[25:29]+greet[7:11] + greet[13] + \
    greet[12]+greet[2]+greet[1]+greet[-5]
print(greetMod.title())
print(greetMod[::-1].title())  # reversed string
