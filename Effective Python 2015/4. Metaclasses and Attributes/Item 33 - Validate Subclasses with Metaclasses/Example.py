"""
Things to Remember
Use metaclasses to ensure that subclasses are well formed at the time they are defined, before objects of their type are constructed.
Metaclasses have slightly different syntax in Python 2 vs. Python 3.
The __new__ method of metaclasses is run after the class statement's entire body has been processed.
"""

# A metaclass is defined by inheriting from type.
# In the default case, a metaclass receives the contents of associated class statements in its __new__ method.
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)


class MyClass(object, metaclass=Meta):
    stuff = 123
    def foo(self):
        pass

#
class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # Don't validate the abstract Polygon class
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)

class Polygon(object, metaclass=ValidatePolygon):
    sides = None # Specified by subclasses
    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180

class Triangle(Polygon):
    sides = 3
    
print('Before class')
class Line(Polygon):
    print('Before sides')
    sides = 1
    print('After sides')
print('After class')