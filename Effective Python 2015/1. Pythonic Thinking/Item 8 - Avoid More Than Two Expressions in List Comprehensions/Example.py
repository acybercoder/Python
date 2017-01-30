"""
Things to Remember
List comprehensions support multiple levels of loops and multiple conditions per loop level.
List comprehensions with more than two expressions are very difficult to read and should be avoided.    
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

squared = [[x**2 for x in row] for row in matrix]
print(squared)


my_lists = matrix
#not recommended
flat =[x
       for sublist1 in my_lists
       for sublist2 in sublist1
       for x in sublist2]

#recommended
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)
        
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]   #multiple if conditions
c = [x for x in a if x > 4 and x % 2 == 0]

#short, but extremely difficult to read
filtered = [[x for x in row if x % 3 == 0]
                for row in matrix if sum(row) >= 10]
print(filtered)
