"""
Things to Remember
Coroutines provide an efficient way to run tens of thousands of functions seemingly at the same time.
Within a generator, the value of the yield expression will be whatever value was passed to the generator¡¯s send method from the exterior code.
Coroutines give you a powerful tool for separating the core logic of your program from its interaction with the surrounding environment.
Python 2 doesn¡¯t support yield from or returning values from generators.
"""

# There are three big problems with threads:
# (1) They require special tools to coordinate with each other safely (see Item 38).
# (2) Threads require a lot of memory, about 8 MB per executing thread.
# (3) Threads are costly to start.

def my_coroutine():
    while True:
        received = yield
        print('Received:', received)
it = my_coroutine()
next(it) # Prime the coroutine
it.send('First')
it.send('Second')

def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)
        
it = minimize()
next(it) # Prime the generator
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))