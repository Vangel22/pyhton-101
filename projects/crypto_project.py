import random

print('Project -  Crypto')


def enigma():
    # create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
# autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
    print(keys)
    print(values)
# create two dictionaries
    dict_enc = dict(zip(keys, values))
    dict_dec = dict(zip(values, keys))
    # dict_dec = {values: key for key, value in dict_enc.items()}
# or create 1 and flip the dictionary
# user input 'the message' and mode
    msg = input('Enter your secret message quietly: ').lower()
    mode = input('Crypto mode: encode (e) OR decrypt as default: ').lower()
# run encode or decode
    if mode == 'e':
        new_msg = ''.join([dict_enc[letter] for letter in msg])
    else:
        new_msg = ''.join([dict_dec[letter] for letter in msg])

    return new_msg.capitalize()

# clean and beautify the code


print(enigma())
