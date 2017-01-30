"""
Things to Remember
Closure functions can refer to variables from any of the scopes in which they were defined.
By default, closures can¡¯t affect enclosing scopes by assigning variables.
In Python 3, use the nonlocal statement to indicate when a closure can modify a variable in its enclosing scopes.
In Python 2, use a mutable value (like a single-item list) to work around the lack of the nonlocal statement.
Avoid using nonlocal statements for anything beyond simple functions.
"""

def sort_priority(numbers, group):
    found = False   # Scope: 'sort_priority2'
    def helper(x):
        if x in group:
            found = True # Seems simple, but scope: 'helper' -- Bad!
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}

found = sort_priority(numbers, group)
print('Found:', found)      # False
print(numbers)

#=>
def sort_priority2(numbers, group):
    found = False # Scope: 'sort_priority2'
    def helper(x):
        nonlocal found  # Scope: 'sort_priority2'
        if x in group:
            found = True 
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

found = sort_priority2(numbers, group)
print('Found:', found)      # True
print(numbers)
