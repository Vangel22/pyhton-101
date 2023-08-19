import itertools as it


def grouper(inputs, n, fill_value=None):
    # gets the current input and the next n places after and combines it into one tuple
    iters = [iter(inputs)] * n
    return it.zip_longest(*iters, fillvalue=fill_value)


alpha = ['g', 'e', 'e', 'k', 's', 'f', 'o',
         'r', 'g', 'e', 'e', 'k', 's']
print(list(grouper(alpha, 3)))
