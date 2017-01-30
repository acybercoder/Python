"""
Things to Remember
It¡¯s important to profile Python programs before optimizing because the source of slowdowns is often obscure.
Use the cProfile module instead of the profile module because it provides more accurate profiling information.
The Profile object¡¯s runcall method provides everything you need to profile a tree of function calls in isolation.
The Stats object lets you select and print the subset of profiling information you need to see to understand your program¡¯s performance.
"""

def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result

def insert_value(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)
    
from random import randint
max_size = 10**4
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)

from cProfile import Profile
profiler = Profile()
profiler.runcall(test)

from pstats import Stats
stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()