"""
Things to Remember
Class registration is a helpful pattern for building modular Python programs.
Metaclasses let you run registration code automatically each time your base class is subclassed in a program.
Using metaclasses for class registration avoids errors by ensuring that you never miss a registration call.
"""

class Serializable(object):
    def __init__(self, *args):
        self.args = args
    def serialize(self):
        return json.dumps({'args': self.args})
    
class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point2D(%d, %d)' % (self.x, self.y)
point = Point2D(5, 3)
print('Object: ', point)
print('Serialized:', point.serialize())


class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])
    
#Include the serialized object¡¯s class name in the JSON data.
class BetterSerializable(object):
    def __init__(self, *args):
        self.args = args
    def serialize(self):
        return json.dumps({
        'class': self.__class__.__name__,
        'args': self.args,
        })
    def __repr__(self):
        # ...
        pass

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls) # Be confident that the call to register_class happened and deserialize will always work as expected.
        return cls
    
class RegisteredSerializable(BetterSerializable, metaclass=Meta):
    pass