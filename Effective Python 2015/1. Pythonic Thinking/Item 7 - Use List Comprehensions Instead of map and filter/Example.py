"""
Things to Remember
List comprehensions are clearer than the map and filter built-in functions because they don��t require extra lambda expressions.
List comprehensions allow you to easily skip items from the input list, a behavior map doesn��t support without help from filter.
Dictionaries and sets also support comprehension expressions.
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)

squares = map(lambda x: x ** 2, a)  #which is visually noisy

even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))  #it is much harder to read
assert even_squares == list(alt)


chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3} #dictonary
rank_dict = {rank: name for name, rank in chile_ranks.items()} #set
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)
