"""
Things to Remember
Beware of functions that iterate over input arguments multiple times. If these arguments are iterators, you may see strange behavior and
missing values.
Python¡¯s iterator protocol defines how containers and iterators interact with the iter and next built-in functions, for loops, and related
expressions.
You can easily define your own iterable container type by implementing the __iter__ method as a generator.
You can detect that a value is an iterator (instead of a container) if calling iter on it twice produces the same result, which can then be
progressed with the next built-in function.
"""

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)

#=>
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


def normalize_func(get_iter):   #Same as normalize
    total = sum(get_iter()) # New iterator
    result = []
    for value in get_iter(): # New iterator
        percent = 100 * value / total
        result.append(percent)
    return result

path = 'Item17.txt'
it = read_visits(path)
percentages = normalize_func(lambda: read_visits(path))
print(percentages)

#=>
class ReadVisits(object):       # A container
    def __init__(self, data_path):
        self.data_path = data_path
    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)
                
visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)

# defensive
def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers): # An iterator -- bad!
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
normalize_defensive(visits) # No error
visits = ReadVisits(path)
normalize_defensive(visits) # No error

it = iter(visits)
normalize_defensive(it)     # TypeError