"""
Things to Remember
List comprehensions can cause problems for large inputs by using too much memory.
Generator expressions avoid memory issues by producing outputs one at a time as an iterator.
Generator expressions can be composed by passing the iterator from one generator expression into the for subexpression of another.
Generator expressions execute very quickly when chained together.
"""

from _collections_abc import Iterator
value = [len(x) for x in open('item9.txt')]
print(value)

#generator
it = (len(x) for x in open('item9.txt'))
print(it)

while True:
    try:
        print(next(it), end=' ')
    except StopIteration:
        break
print()    

assert isinstance(it, Iterator)
assert isinstance(iter([]), Iterator)

it = iter([1, 2, 3, 4, 5])
roots = ((x, x**0.5) for x in it)
print(next(roots))



