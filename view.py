"""view module
print/input model (accounting)
by Kirill"""

import decimal
import datetime
from accounting import Accounting


def enter_day():
    """enter date creation of payment"""
    date = 0
    while date <= 0 or date >= 31:
        """enter date"""
        date = input('Enter date: ')
        try:
            """try assign"""
            date = int(date)
        except ValueError:
            """exception
            incorrect date"""
            date = 0
    return date


def enter_month():
    """enter month of creation"""
    month = 0
    while month <= 0 or month > 12:
        """enter month"""
        month = input('Enter month: ')
        try:
            """try assign"""
            month = int(month)
        except ValueError:
            """exception
            incorrect month"""
            month = 0
    return month


def enter_year():
    """enter year of creation"""
    year = -1
    while year < 0:
        """enter year"""
        year = input('Enter year: ')
        try:
            """try assign"""
            year = int(year)
        except ValueError:
            """exception"""
            year = 0
    return year


def enter_desc():
    """enter description of payment"""
    return input("Enter description of accounting: ")


def enter_sum():
    """enter summa of payment"""
    import re

    sum = -1.0
    while sum < 0:
        """enter summa"""
        sum = input('Enter summa: ')
        try:
            """try assign"""
            if re.match('^\d+?\.\d\d$', sum) is None:
                # if precision more then 2
                raise ValueError
            sum = decimal.Decimal(sum)
        except ValueError:
            """exception
            incorrect summa"""
            sum = -1.0
    return sum


def is_profit():
    """enter is payment profit"""
    inp = input('Enter Y if accounting is profit: ')
    if inp is 'Y':
        """it is profit"""
        return True
    """it is consumption"""
    return False


def input_accounting():
    """input accounting"""
    account = Accounting()
    while True:
        """enter date"""
        try:
            account.set_datetime(datetime.datetime(enter_year(),
                                 enter_month(), enter_day(), 0, 0))
            break
        except ValueError:
            pass
    """set description"""
    account.set_description(enter_desc())
    """set precesion"""
    decimal.getcontext().prec = 2
    """set summa of payment"""
    account.set_sum(enter_sum())
    """set profit/consumption"""
    if is_profit():
        account.set_profit()
    else:
        account.set_consumption()
    """return result"""
    return account


def print_payments(payment_list):
    """print head of a result table"""
    print('%-25s %-20s %-8s %-15s' %
          ("Date     ", "Description   ", "Sum    ", "Profit (True/False)"))
    """print each payment from list of payments"""
    for payment in payment_list:
        info = (payment.get_datetime(), payment.get_description()[:15],
                payment.get_sum(), payment.is_profit())
        print('%-25s %-20s %-8.2f %-15s' % info)


def menu():
    """input a key to choose your next action"""
    key = input(""" Press:
                1 - to view the list of payments
                2 - to append new payment
                3 - to exit
                """)
    """return result"""
    return key
