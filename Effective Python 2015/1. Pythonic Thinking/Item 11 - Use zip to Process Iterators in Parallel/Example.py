"""
Things to Remember
The zip built-in function can be used to iterate over multiple iterators in parallel.
In Python 3, zip is a lazy generator that produces tuples. In Python 2, zip returns the full result as a list of tuples.
zip truncates its output silently if you supply it with iterators of different lengths.
The zip_longest function from the itertools built-in module lets you iterate over multiple iterators in parallel regardless of their lengths (see
Item 46: ¡°Use Built-in Algorithms and Data Structures¡±).
"""
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

longest_name = None
max_letters = 0

#this whole loop statement is visually noisy
for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i] 
        max_letters = count
        print(longest_name)
        
#=>
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count
#=>        
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

names.append('Rosalind')    
for name, count in zip(names, letters):
    print(name)     #The new item for 'Rosalind' isn¡¯t here
    