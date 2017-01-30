"""
Things to Remember
Instead of defining and instantiating classes, functions are often all you need for simple interfaces between components in Python.
References to functions and methods in Python are first class, meaning they can be used in expressions like any other type.
The __call__ special method enables instances of a class to be called like plain Python functions.
When you need a function to maintain state, consider defining a class that provides the __call__ method instead of defining a stateful closure
(see Item 15: ¡°Know How Closures Interact with Variable Scope¡±).
"""

names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)

def log_missing():
    print('Key added')
    return 0

current = {'green': 12, 'blue': 3}
increments = [
('red', 5),
('blue', 17),
('orange', 9),
]

from collections  import defaultdict
result = defaultdict(log_missing, current)
print('Before:', dict(result))
for key, amount in increments:
    result[key] += amount
print('After: ', dict(result))


def increment_with_report(current, increments):
    added_count = 0
    def missing():
        nonlocal added_count # Stateful closure
        added_count += 1
        return 0
    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2


class BetterCountMissing(object):
    def __init__(self):
        self.added = 0
    def __call__(self):
        self.added += 1
        return 0
counter = BetterCountMissing()
assert callable(counter)

result = defaultdict(counter, current) # Relies on __call__
for key, amount in increments:
    result[key] += amount
assert counter.added == 2