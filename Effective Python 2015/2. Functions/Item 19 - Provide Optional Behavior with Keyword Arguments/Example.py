"""
Things to Remember
Function arguments can be specified by position or by keyword.
Keywords make it clear what the purpose of each argument is when it would be confusing with only positional arguments.
Keyword arguments with default values make it easy to add new behaviors to a function, especially when the function has existing callers.
Optional keyword arguments should always be passed by keyword instead of by position.
"""

def remainder(number, divisor):
    return number % divisor
assert remainder(20, 7) == 6

remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

remainder(number=20, 7) # SyntaxError: non-keyword arg after keyword arg
remainder(20, number=7) # TypeError: remainder() got multiple values for argument 'number'


def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print('%.3f kg per second' % flow)

def flow_rate(weight_diff, time_diff, period=1):    # The period argument is now optional.
    return (weight_diff / time_diff) * period

