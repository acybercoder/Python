"""
Things to Remember
Keyword arguments make the intention of a function call more clear.
Use keyword-only arguments to force callers to supply keyword arguments for potentially confusing functions, especially those that accept
multiple Boolean flags.
Python 3 supports explicit syntax for keyword-only arguments in functions.
Python 2 can emulate keyword-only arguments for functions by using **kwargs and manually raising TypeError exceptions.
"""

def safe_division(number, divisor, ignore_overflow,
    ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise
        
# The * symbol in the argument list indicates the end of positional arguments and the beginning of keyword-only arguments.
def safe_division_c(number, divisor, *,
ignore_overflow=False,
ignore_zero_division=False):
    pass

safe_division_c(1, 10**500, True, False) # TypeError: safe_division_c() takes 2 positional arguments but 4 were given
safe_division_c(1, 0, ignore_zero_division=True) # OK