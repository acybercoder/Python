"""
Things to Remember
Python has built-in types and classes in modules that can represent practically every type of numerical value.
The Decimal class is ideal for situations that require high precision and exact rounding behavior, such as computations of monetary values.
"""

rate = 1.45
seconds = 3*60 + 42
cost = rate * seconds / 60
print(cost)

print(round(cost, 2))


rate = 0.05
seconds = 5
cost = rate * seconds / 60
print(cost)
print(round(cost, 2))

import decimal
from decimal import Decimal
rate = Decimal('1.45')
seconds = Decimal('222') # 3*60 + 42
cost = rate * seconds / Decimal('60')
print(cost)

rounded = cost.quantize(Decimal('0.01'), rounding=decimal.ROUND_UP)
print(rounded)

rate = Decimal('0.05')
seconds = Decimal('5')
cost = rate * seconds / Decimal('60')
print(cost)

rounded = cost.quantize(Decimal('0.01'), rounding=decimal.ROUND_UP)
print(rounded)