"""
Things to Remember
Avoid being verbose: Don¡¯t supply 0 for the start index or the length of the sequence for the end index.
Slicing is forgiving of start or end indexes that are out of bounds, making it easy to express slices on the front or back boundaries of a
sequence (like a[:20] or a[-20:]).
Assigning to a list slice will replace that range in the original sequence with what¡¯s referenced even if their lengths are different.
"""

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])
print('Last four: ', a[-4:])
print('Middle two:', a[3:-3])

assert a[:5] == a[0:5]
assert a[5:] == a[5:len(a)]

a[:] # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[:5] # ['a', 'b', 'c', 'd', 'e']
a[:-1] # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
a[4:] # ['e', 'f', 'g', 'h']
a[-3:] # ['f', 'g', 'h']
a[2:5] # ['c', 'd', 'e']
a[2:-1] # ['c', 'd', 'e', 'f', 'g']
a[-3:-1] # ['f', 'g']

first_twenty_items = a[:20]
last_twenty_items = a[-20:]

b = a[:]
assert b == a and b is not a

a[:] = [101, 102, 103]

assert a==[101, 102, 103]