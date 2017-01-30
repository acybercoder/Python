"""
Things to Remember
Even though Python has a global interpreter lock, you¡¯re still responsible for protecting against data races between the threads in your
programs.
Your programs will corrupt their data structures if you allow multiple threads to modify the same objects without locks.
The Lock class in the threading built-in module is Python¡¯s standard mutual exclusion lock implementation.
"""

from threading import Thread, Lock

class Counter(object):
    def __init__(self):
        self.count = 0
    def increment(self, offset):
        self.count += offset
        
def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        # Read from the sensor
        # ...
        counter.increment(1)
        
def run_threads(func, how_many, counter):
    threads = []
    for i in range(5):
        args = (i, how_many, counter)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
        
how_many = 10**5
counter = Counter()
run_threads(worker, how_many, counter)
print('Counter should be %d, found %d' %(5 * how_many, counter.count))


#=>
class LockingCounter(object):
    def __init__(self):
        self.lock = Lock()
        self.count = 0
    def increment(self, offset):
        with self.lock:
            self.count += offset
            
counter = LockingCounter()
run_threads(worker, how_many, counter)
print('Counter should be %d, found %d' %(5 * how_many, counter.count))
