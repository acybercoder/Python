"""
Things to Remember
Python threads can't run bytecode in parallel on multiple CPU cores because of the global interpreter lock (GIL).
Python threads are still useful despite the GIL because they provide an easy way to do multiple things at seemingly the same time.
Use Python threads to make multiple system calls in parallel. This allows you to do blocking I/O at the same time as computation.
"""
from time import time

def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i
            
numbers = [2139079, 1214759, 1516637, 1852285]
start = time()
for number in numbers:
    list(factorize(number))
end = time()
print('Took %.3f seconds' % (end - start))


from threading import Thread
class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number
    def run(self):
        self.factors = list(factorize(self.number))
        
start = time()
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()
end = time()
print('Took %.3f seconds' % (end - start))  # This takes even longer than running factorize in serial.

import socket, sys
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_list = []

def slow_systemcall():
    try:
        select.select(socket_list, [], [], 0.1)
    except Exception as e:
        print(e)

start = time()
for _ in range(5):
    slow_systemcall()
end = time()
print('Took %.3f seconds' % (end - start))