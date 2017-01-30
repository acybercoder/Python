"""
Things to Remember
Functions that return None to indicate special meaning are error prone because None and other values (e.g., zero, the empty string) all evaluate
to False in conditional expressions.
Raise exceptions to indicate special situations instead of returning None. Expect the calling code to handle exceptions properly when they¡¯re
documented.
"""

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

x, y = 5, 0
result = divide(x, y)
if result is None:
    print('Invalid inputs')
    
#=>
    
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e

x, y = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)