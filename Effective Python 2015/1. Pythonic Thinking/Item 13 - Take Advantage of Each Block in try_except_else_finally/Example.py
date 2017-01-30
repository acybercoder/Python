"""
Things to Remember
The try/finally compound statement lets you run cleanup code regardless of whether exceptions were raised in the try block.
The else block helps you minimize the amount of code in try blocks and visually distinguish the success case from the try/except blocks.
An else block can be used to perform additional actions after a successful try block but before common cleanup in a finally block.
"""

handle = open('random_data.txt') # May raise IOError
try:
    data = handle.read() # May raise UnicodeDecodeError
finally:
    handle.close() # Always runs after try:
    

import json
    
def load_json_key(data, key):
    try:
        result_dict = json.loads(data) # May raise ValueError
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key] # May raise KeyError
    
UNDEFINED = object()
def divide_json(path):
    handle = open(path, 'r+') # May raise IOError
    try:
        data = handle.read() # May raise UnicodeDecodeError
        op = json.loads(data) # May raise ValueError
        value = (
        op['numerator'] /
        op['denominator']) # May raise ZeroDivisionError
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result) # May raise IOError
        return value
    finally:
        handle.close() # Always runs