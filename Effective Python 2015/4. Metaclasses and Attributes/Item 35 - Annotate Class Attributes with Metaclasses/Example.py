"""
Things to Remember
Metaclasses enable you to modify a class¡¯s attributes before the class is fully defined.
Descriptors and metaclasses make a powerful combination for declarative behavior and runtime introspection.
You can avoid both memory leaks and the weakref module by using metaclasses along with descriptors.
"""

class Field(object):
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name
    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')
    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)
        
class Customer(object):
    public_a = 0;
    _protected_a = 0;
    __private_a = 0;
    # Class attributes
    first_name = Field('first_name')    # It seems redundant
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')
    def __init__(self):
        self.public_b = 0;
        self._protected_b = 0;
        self.__private_b = 0;
    
foo = Customer()
print('Before: ', repr(foo.first_name), foo.__dict__)
foo.first_name = 'Euclid'
foo.public_a = 1
print('After: ', repr(foo.first_name), foo.__dict__)

# Eliminate the redundancy
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls
    
class DatabaseRow(object, metaclass=Meta):
    pass

class BetterCustomer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()