# Dunder i.e double under (underscores)
# Used for operator overloading

# Magic methods (some):
# __init__ -> created when an instance of a class is created, without any call
# __add__
# __len__
# __repr__ -> represents our object

# declare our own string class
class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string

    def __repr__(self) -> str:
        return 'Object: {}'.format(self.string)

    def __add__(self, other):
        return self.string + other


# Driver Code
if __name__ == '__main__':

    # object creation
    string1 = String('Hello')
    # print object location
    print(string1)
    print(string1 + ' world')
