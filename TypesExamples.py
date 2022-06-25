import os
import sys
from decimal import Decimal
from fractions import Fraction
from datetime import datetime as dt

os.system("clear")

#Floating point Numbers
print(sys.float_info)

#Decimals
print(2 * Decimal(6.001))
print(Decimal(0.8) - Decimal(0.7))
print(Decimal('0.8') - Decimal('0.7'))

#Fractions
print(Fraction(8,10) - Fraction(7,10))

#Complex Numbers
print(type(2j))
print('Compare float and int = ', (2 == 2.0))
print('Compare decimal and int = ', (2 == Decimal('2.0')))
print('Compare decimal and float = ', (2.0 == Decimal('2.0')))
print('Compare fraction and int = ', (2 == Fraction(20,10)))
print('Compare fraction and float = ', (2.0 == Fraction(20,10)))
print('Compare fraction and decimal = ', (Fraction(20,10) == Decimal('2.0')))

print(type(dt.today()))
print(dt.today())
print(dt.now())
print(dt.utcnow())
print(dt.strptime("13 March 2022 Monday, 12:53:30", "%d %B %Y %A, %H:%M:%S"))
print(dt.strptime("13 March 2022 Monday, 12:53:30", "%d %B %Y %A, %H:%M:%S") - dt.strptime("12 March 2022 Monday, 10:53:30", "%d %B %Y %A, %H:%M:%S"))