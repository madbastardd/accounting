"""

>>> import datetime

>>> from decimal import Decimal

>>> from accounting import Accounting

>>> accounting = Accounting()

>>> accounting.set_datetime(datetime.datetime(2016, 3, 10, 19, 53, 42))

>>> accounting.get_datetime()
datetime.datetime(2016, 3, 10, 19, 53, 42)
>>> accounting.set_datetime('we hate rules')
Traceback (most recent call last):
        ...
TypeError: Incorrect type of variable date_time
>>> accounting.set_sum(Decimal(10))

>>> accounting.get_sum()
Decimal('10.00')
>>> accounting.set_sum("17")
Traceback (most recent call last):
        ...
TypeError: float argument required, not str
>>> accounting.set_description('description')

>>> accounting.get_description()
'description'
>>> accounting.set_description(10)
Traceback (most recent call last):
        ...
TypeError: Incorrect type of variable _desc
>>> accounting.is_profit()
True
>>> accounting.is_consumption()
False
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
