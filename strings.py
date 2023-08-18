# Strings

msg = 'Welcome to Python 101: Strings'
print(msg.find('h'))
print(msg.find('Python'))  # starts from P
print(msg.replace('Python', 'JavaScript'))

print("Python" in msg)  # searches for keyword in string
print("Python" not in msg)


name = 'TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg)
print(msg1)
