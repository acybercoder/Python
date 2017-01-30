"""
Things to Remember
Using generators can be clearer than the alternative of returning lists of accumulated results.
The iterator returned by a generator produces the set of values passed to yield expressions within the generator function¡¯s body.
Generators can produce a sequence of outputs for arbitrarily large inputs because their working memory doesn¡¯t include all inputs and outputs.
"""

def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:3])

#=>
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1
            

# Another example
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

from itertools import islice
with open('item16.txt', 'r') as f:
    it = index_file(f)
    print(list(it))
    
with open('item16.txt', 'r') as f:
    it = index_file(f)
    results = islice(it, 0, 3)
    print(list(results))