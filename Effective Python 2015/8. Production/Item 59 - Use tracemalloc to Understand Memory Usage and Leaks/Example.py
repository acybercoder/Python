"""
Things to Remember
It can be difficult to understand how Python programs use and leak memory.
The gc module can help you understand which objects exist, but it has no information about how they were allocated.
The tracemalloc built-in module provides powerful tools for understanding the source of memory usage.
tracemalloc is only available in Python 3.4 and above.
"""