msg = 'Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'

friends_list = ['Eric', 'John', 'Michael', 'Terry', 'Graham']

print(msg.split())  # split by white-space, it does trim too
print(csv.split(','))
print('-'.join(friends_list))

# Same thing
print(''.join(msg.split()))
print(msg.replace(' ', ''))
