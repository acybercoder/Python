"""
Things to Remember
Moving CPU bottlenecks to C-extension modules can be an effective way to improve performance while maximizing your investment in Python
code. However, the cost of doing so is high and may introduce bugs.
The multiprocessing module provides powerful tools that can parallelize certain types of Python computation with minimal effort.
The power of multiprocessing is best accessed through the concurrent.futures built-in module and its simple ProcessPoolExecutor class.
The advanced parts of the multiprocessing module should be avoided because they are so complex.
"""

from time import time

def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

numbers = [(1963309, 2265973), (2030677, 3814172),
(1551645, 2229620), (2039045, 2020802)]
start = time()
results = list(map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))

#
print('====ThreadPoolExecutor=====')
from concurrent.futures import ThreadPoolExecutor
start = time()
pool = ThreadPoolExecutor(max_workers=2)
results = list(pool.map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))

#
from concurrent.futures import ProcessPoolExecutor
if __name__ == '__main__':
    print('====ProcessPoolExecutor=====')
    start = time()
    with ProcessPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(gcd, numbers))
    end = time()
    print('Took %.3f seconds' % (end - start))
