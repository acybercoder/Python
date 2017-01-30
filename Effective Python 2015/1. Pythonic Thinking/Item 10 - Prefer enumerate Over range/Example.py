"""
Things to Remember
enumerate provides concise syntax for looping over an iterator and getting the index of each item from the iterator as you go.
Prefer enumerate instead of looping over a range and indexing into a sequence.
You can supply a second parameter to enumerate to specify the number from which to begin counting (zero is the default).
"""

from random import randint

random_bits = 0
for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i
print(random_bits)


flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print('%s is delicious' % flavor)

#harder to read    
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i + 1, flavor))

#use enumerate    
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))

#much shorter    
for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s' % (i, flavor))