"""
Things to Remember
Pipelines are a great way to organize sequences of work that run concurrently using multiple Python threads.
Be aware of the many problems in building concurrent pipelines: busy waiting, stopping workers, and memory explosion.
The Queue class has all of the facilities you need to build robust pipelines: blocking operations, buffer sizes, and joining.
"""

from collections import deque
from threading import Thread, Lock
from time import sleep
import time

class MyQueue(object):
    def __init__(self):
        self.items = deque()
        self.lock = Lock()
    def put(self, item):
        with self.lock:
            self.items.append(item)
    def get(self):
        with self.lock:
            return self.items.popleft()
        
class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0
        
    def run(self):
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                sleep(0.01) # No work to do
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1    

download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()
done_queue = MyQueue()

def download(object):
    pass
def resize(object):
    pass
def upload(object):
    pass

threads = [
Worker(download, download_queue, resize_queue),
Worker(resize, resize_queue, upload_queue),
Worker(upload, upload_queue, done_queue),
]

for thread in threads:
    thread.start()
for _ in range(1000):
    download_queue.put(object())    
    #resize_queue.put(object())
    #upload.put(object())

processed = len(done_queue.items)
polled = sum(t.polled_count for t in threads)
print('Processed', processed, 'items after polling', polled, 'times')

# Queue to the Rescue
from queue import Queue

queue = Queue()

def consumer():
    print('Consumer waiting')
    queue.get() # Runs after put() below
    print('Consumer done')
thread = Thread(target=consumer)
thread.start()

print('Producer putting')
queue.put(object()) # Runs before get() above
thread.join()
print('Producer done')

print('==========')
queue = Queue(1) # Buffer size of 1
def consumer():
    time.sleep(0.1) # Wait
    queue.get() # Runs second
    print('Consumer got 1')
    queue.get() # Runs fourth
    print('Consumer got 2')
thread = Thread(target=consumer)
thread.start()

queue.put(object()) # Runs first
print('Producer put 1')
queue.put(object()) # Runs third
print('Producer put 2')
thread.join()
print('Producer done')

print('==========')
in_queue = Queue()
def consumer():
    print('Consumer waiting')
    work = in_queue.get() # Done second
    print('Consumer working')
    # Doing work
    # ...
    print('Consumer done')
    in_queue.task_done() # Done third
Thread(target=consumer).start()

in_queue.put(object()) # Done first
print('Producer waiting')
in_queue.join() # Done fourth
print('Producer done')

print('==========')
class ClosableQueue(Queue):
    SENTINEL = object()
    def close(self):
        self.put(self.SENTINEL)
    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                        return # Cause the thread to exit
                yield item
            finally:
                self.task_done()
        
class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        #self.polled_count = 0
        self.work_done = 0
    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)