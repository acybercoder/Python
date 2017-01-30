"""
Things to Remember
Python¡¯s syntax makes it all too easy to write single-line expressions that are overly complicated and difficult to read.
Move complex expressions into helper functions, especially if you need to use the same logic repeatedly.
The if/else expression provides a more readable alternative to using Boolean operators like or and and in expressions.
"""


from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(my_values)
print(repr(my_values))

def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

#red = int(my_values.get('red', [''])[0] or 0)
green = get_first_int(my_values, 'green')