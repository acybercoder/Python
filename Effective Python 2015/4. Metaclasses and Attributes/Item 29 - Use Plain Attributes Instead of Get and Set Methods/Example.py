"""
Things to Remember
Define new class interfaces using simple public attributes, and avoid set and get methods.
Use @property to define special behavior when attributes are accessed on your objects, if necessary.
Follow the rule of least surprise and avoid weird side effects in your @property methods.
Ensure that @property methods are fast; do slow or complex work using normal methods.
"""

r0 = OldResistor(50e3)
print('Before: %5r' % r0.get_ohms())
r0.set_ohms(10e3)
print('After: %5r' % r0.get_ohms())


r0.set_ohms(r0.get_ohms() + 5e3)    # especially clumsy

class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0
r1 = Resistor(50e3)
r1.ohms = 10e3
r1.ohms += 5e3


class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
    
    @property
    def ohms(self):
        return self._ohms
    
    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms
        
class FixedResistance(Resistor):
    # ...
    @property
    def ohms(self):
        return self._ohms
    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms