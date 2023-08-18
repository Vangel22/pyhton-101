def num_days(month):
    days = 31
    # sets are faster than list or tuples when checking - 5x slower
    if month in {'apr', 'jun', 'sep', 'nov'}:
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in', month, 'is', days)


num_days('feb')
# optimize/shorten the code in the function
# try to reduce the number of conditionals
