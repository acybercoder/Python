"""
Things to Remember
Python's standard method resolution order (MRO) solves the problems of superclass initialization order and diamond inheritance.
Always use the super built-in function to initialize parent classes.
"""

class MyBaseClass(object):
    def __init__(self, value):
        self.value = value

class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)
        
class TimesTwo(object):
    def __init__(self):
        self.value *= 2

class PlusFive(object):
    def __init__(self):
        self.value += 5
        
class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)
        
foo = OneWay(5)
print('First ordering is (5 * 2) + 5 =', foo.value) # 15

class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)
        
bar = AnotherWay(5)
print('Second ordering still is', bar.value) # 15

class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)
class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)