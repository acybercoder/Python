"""
Things to Remember
Private attributes aren¡¯t rigorously enforced by the Python compiler.
Plan from the beginning to allow subclasses to do more with your internal APIs and attributes instead of locking them out by default.
Use documentation of protected fields to guide subclasses instead of trying to force access control with private attributes.
Only consider using private attributes to avoid naming conflicts with subclasses that are out of your control.
"""

class MyObject(object):
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10
        
    def get_private_field(self):
        return self.__private_field
    
class MyOtherObject(object):
    def __init__(self):
        self.__private_field = 71
    
    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field

bar = MyOtherObject()
assert MyOtherObject.get_private_field_of_instance(bar) == 71


class MyParentObject(object):
    def __init__(self):
        self.__private_field = 71

class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field 

baz = MyChildObject()
#baz.get_private_field() # AttributeError: 'MyChildObject' object has no attribute '_MyChildObject__private_field'

assert baz._MyParentObject__private_field == 71 # It works


class ApiClass(object):
    def __init__(self):
        self._value = 5
    def get(self):
        return self._value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello' # Conflicts

a = Child()
print(a.get(), 'and', a._value, 'should be different')