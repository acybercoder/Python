"""
Things to Remember
Use __getattr__ and __setattr__ to lazily load and save attributes for an object.
Understand that __getattr__ only gets called once when accessing a missing attribute, whereas __getattribute__ gets called every time an
attribute is accessed.
Avoid infinite recursion in __getattribute__ and __setattr__ by using methods from super() (i.e., the object class) to access instance
attributes directly.
"""
#__getattr__, that method is called every time an attribute can't be found in an object's instance dictionary.
class LazyDB(object):
    def __init__(self):
        self.exists = 5
    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value
    
data = LazyDB()
print('Before:', data.__dict__)
print('foo: ', data.foo)
print('After: ', data.__dict__) #After: {'exists': 5, 'foo': 'Value for foo'}

class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        return super().__getattr__(name)    # use super().__getattr__() to get the real property value in order to avoid infinite recursion.

data = LoggingLazyDB()
print('exists:', data.exists)   #The exists attribute is present in the instance dictionary
print('foo: ', data.foo)    # The foo attribute is not in the instance dictionary initially
print('foo: ', data.foo)

#The __getattribute__ method is called every time an attribute is accessed on an object
class ValidatingDB(object):
    def __init__(self):
        self.exists = 5
    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value
data = ValidatingDB()
print('exists:', data.exists)
print('foo: ', data.foo)
print('foo: ', data.foo)

#The hasattr, getattr built-in functions also look in the instance dictionary for an attribute name before calling __getattr__.
data = LoggingLazyDB()
print('Before: ', data.__dict__)
print('foo exists: ', hasattr(data, 'foo'))
print('After: ', data.__dict__)
print('foo exists: ', hasattr(data, 'foo'))

#The __setattr__ method is always called every time an attribute is assigned on an instance (either directly or through the setattr built-in function).
class SavingDB(object):
    def __setattr__(self, name, value):
        # Save some data to the DB log
        # ...
        super().__setattr__(name, value)

class LoggingSavingDB(SavingDB):
    def __setattr__(self, name, value):
        print('Called __setattr__(%s, %r)' % (name, value))
        super().__setattr__(name, value)
        
data = LoggingSavingDB()
print('Before: ', data.__dict__)
data.foo = 5
print('After: ', data.__dict__)
data.foo = 7
print('Finally:', data.__dict__)


class DictionaryDB(object):
    def __init__(self, data):
        self._data = data
    def __getattribute__(self, name):
        data_dict = super().__getattribute__('_data')       # Use the super().__getattribute__ method to avoid the recursion.
        print('data_dict', data_dict)
        return data_dict[name]

data = DictionaryDB({'key':1})
print('Try once: ', data.key)
