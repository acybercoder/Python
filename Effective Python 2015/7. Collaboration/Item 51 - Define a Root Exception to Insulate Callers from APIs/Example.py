"""
Things to Remember
Defining root exceptions for your modules allows API consumers to insulate themselves from your API.
Catching root exceptions can help you find bugs in code that consumes an API.
Catching the Python Exception base class can help you find bugs in API implementations.
Intermediate root exceptions let you add more specific types of exceptions in the future without breaking your API consumers.
"""

class Error(Exception):
    """Base-class for all exceptions raised by this module."""
    pass

class InvalidDensityError(Error):
    """There was a problem with a provided density value."""
    pass