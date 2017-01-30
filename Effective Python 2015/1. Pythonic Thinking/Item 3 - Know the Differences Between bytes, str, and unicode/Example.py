"""
Things to Remember
In Python 3, bytes contains sequences of 8-bit values, str contains sequences of Unicode characters. bytes and str instances can¡¯t be used
together with operators (like > or +).
In Python 2, str contains sequences of 8-bit values, unicode contains sequences of Unicode characters. str and unicode can be used
together with operators if the str only contains 7-bit ASCII characters.
Use helper functions to ensure that the inputs you operate on are the type of character sequence you expect (8-bit values, UTF-8 encoded
characters, Unicode characters, etc.).
If you want to read or write binary data to/from a file, always open the file using a binary mode (like 'rb' or 'wb').
"""

import sys

print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())

import locale
print(locale.getdefaultlocale())
print(locale.getpreferredencoding())


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # Instance of str

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # Instance of str


with open('/tmp/random.bin', 'wb') as f:
    f.write(os.urandom(10))