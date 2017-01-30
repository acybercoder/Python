"""
Things to Remember
Calling print on built-in Python types will produce the human-readable string version of a value, which hides type information.
Calling repr on built-in Python types will produce the printable string version of a value. These repr strings could be passed to the eval built-in
function to get back the original value.
%s in format strings will produce human-readable strings like str. %r will produce printable strings like repr.
You can define the __repr__ method to customize the printable representation of a class and provide more detailed debugging information.
You can reach into any object's __dict__ attribute to view its internals.
"""

print('foo bar')

print('%s' % 'foo bar')

a = '\x07'
print(repr(a))

b = eval(repr(a))
assert a == b

print('%r' % 5)
print('%r' % '5')


class OpaqueClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
obj = OpaqueClass(1, 2)
print(obj)

class BetterClass(object):
    def __init__(self, x, y):
        # ...
        self.x = x
        self.y = y
    def __repr__(self):
        return 'BetterClass(%d, %d)' % (self.x, self.y)
    
obj = BetterClass(1, 2)
print(obj)