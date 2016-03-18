"""

>>> import datetime

>>> from decimal import *

>>> from accounting import Accounting

>>> accounting = Accounting()

>>> accounting.set_datetime(datetime.datetime(2016, 3, 10, 19, 53, 42))

>>> accounting.get_datetime()
datetime.datetime(2016, 3, 10, 19, 53, 42)
>>> accounting.set_datetime('we hate rules')
Traceback (most recent call last):
        ...
TypeError: Incorrect type of variable _datetime
>>> accounting.set_sum(Decimal(10))

>>> accounting.get_sum()
Decimal('10')
>>> accounting.set_sum("17")
Traceback (most recent call last):
        ...
TypeError: Incorrect type of variable _sum
>>> accounting.set_description('description')

>>> accounting.get_description()
'description'
>>> accounting.set_description(10)
Traceback (most recent call last):
        ...
TypeError: Incorrect type of variable _desc
>>> accounting.set_profit()

>>> accounting.is_profit()
True
>>> accounting.set_consumption()

>>> accounting.is_consumption()
True
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
