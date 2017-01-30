"""
Things to Remember
Specifying start, end, and stride in a slice can be extremely confusing.
Prefer using positive stride values in slices without start or end indexes. Avoid negative stride values if possible.
Avoid using start, end, and stride together in a single slice. If you need all three parameters, consider doing two assignments (one to slice,
another to stride) or using islice from the itertools built-in module.
"""
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[::2] # ['a', 'c', 'e', 'g']
a[::-2] # ['h', 'f', 'd', 'b']

a[2::2] # ['c', 'e', 'g']
a[-2::-2] # ['g', 'e', 'c', 'a']
a[-2:2:-2] # ['g', 'e']
a[2:2:-2] # []

b = a[::2] # ['a', 'c', 'e', 'g']
c = b[1:-1] # ['c', 'e']