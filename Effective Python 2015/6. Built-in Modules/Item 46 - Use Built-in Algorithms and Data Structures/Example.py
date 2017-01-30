"""
Things to Remember
Use Python¡¯s built-in modules for algorithms and data structures.
Don¡¯t reimplement this functionality yourself. It¡¯s hard to get right.
"""

from collections import deque

fifo = deque()
fifo.append(1) # Producer
x = fifo.popleft() # Consumer

a = {}
a['foo'] = 1
a['bar'] = 2
# Randomly populate 'b' to cause hash conflicts

from random import randint

while True:
    z = randint(99, 1013)
    b = {}
    for i in range(z):
        b[i] = i
    b['foo'] = 1
    b['bar'] = 2
    for i in range(z):
        del b[i]
    if str(b) != str(a):
        break
print(a)
print(b)
print('Equal?', a == b)

from collections import OrderedDict
a = OrderedDict()
a['foo'] = 1
a['bar'] = 2
b = OrderedDict()
b['foo'] = 'red'
b['bar'] = 'blue'
for value1, value2 in zip(a.values(), b.values()):
    print(value1, value2)

from collections import defaultdict
stats = {}
key = 'my_counter'
if key not in stats:
    stats[key] = 0
stats[key] += 1

stats = defaultdict(int)
stats['my_counter'] += 1

from heapq import *
a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)

#Items are always removed by highest priority (lowest number) first.
print(heappop(a), heappop(a), heappop(a), heappop(a))

a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)
assert a[0] == nsmallest(1, a)[0] == 3

print('Before:', a)
a.sort()
print('After: ', a)

from bisect import bisect_left

x = list(range(10**6))
i = x.index(991234)

i = bisect_left(x, 991234)