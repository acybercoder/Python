"""
Things to Remember
Write documentation for every module, class, and function using docstrings. Keep them up to date as your code changes.
For modules: Introduce the contents of the module and any important classes or functions all users should know about.
For classes: Document behavior, important attributes, and subclass behavior in the docstring following the class statement.
For functions and methods: Document every argument, returned value, raised exception, and other behaviors in the docstring following the def
statement.
"""

def palindrome(word):
    """Return True if the given word is a palindrome."""
    return word == word[::-1]

print(repr(palindrome.__doc__))


def find_anagrams(word, dictionary):
    """Find all anagrams for a word.
    This function only runs as fast as the test for
    membership in the 'dictionary' container. It will
    be slow if the dictionary is a list and fast if
    it's a set.
    Args:
    word: String of the target word.
    dictionary: Container with all strings that
    are known to be actual words.
    Returns:
    List of anagrams that were found. Empty if
    none were found.
    """
    # ...
    pass

print(repr(find_anagrams.__doc__))