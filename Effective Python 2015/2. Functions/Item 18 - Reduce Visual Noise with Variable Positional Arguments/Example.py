"""
Things to Remember
Functions can accept a variable number of positional arguments by using *args in the def statement.
You can use the items from a sequence as the positional arguments for a function with the * operator.
Using the * operator with a generator may cause your program to run out of memory and crash.
Adding new positional parameters to functions that accept *args can introduce hard-to-find bugs.
"""
def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))
log('My numbers are', [1, 2])
log('Hi there', [])

def log(message, *values): # The only difference
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))
log('My numbers are', 1, 2)
log('Hi there') # Much better

favorites = [7, 33, 99]
log('Favorite colors', *favorites)


def my_generator():
    for i in range(10):
        yield i
def my_func(*args):
    print(args)
it = my_generator()
my_func(*it)


def log(sequence, message, *values):
    if not values:
        print('%s: %s' % (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s' % (sequence, message, values_str))
log(1, 'Favorites', 7, 33) # New usage is OK
log('Favorite numbers', 7, 33) # Old usage breaks