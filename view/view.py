"""view module
print/input model (accounting)
by Kirill"""

import decimal
import datetime
from model.accounting import Accounting, check_money


def enter_day():
    """
    enter date creation of payment
    :return:date
    """
    date = 0
    while not 1 <= date <= 31:
        # enter date
        date = input('Enter date: ')
        try:
            # try assign
            date = int(date)
        except ValueError:
            # exception
            # incorrect date
            date = 0
    return date


def enter_month():
    """
    enter month of creation
    :return: month
    """
    month = 0
    while not 1 <= month <= 12:
        # enter month
        month = input('Enter month: ')
        try:
            # try assign
            month = int(month)
        except ValueError:
            # exception
            # incorrect month
            month = 0
    return month


def enter_year():
    """
    enter year of creation
    :return: year
    """
    year = -1
    while year < 0:
        # enter year
        year = input('Enter year: ')
        try:
            # try assign
            year = int(year)
        except ValueError:
            # exception
            year = -1
    return year


def enter_desc():
    """
    enter description of payment
    :return: description of payment
    """
    return input("Enter description of accounting: ")


def enter_sum():
    """
    enter sum of payment
    :return:sum
    """
    sum = None
    while sum is None:
        # enter sum
        sum = input('Enter sum: ')
        try:
            # try assign
            check_money(sum)
            sum = decimal.Decimal(sum)
        except ValueError:
            # exception
            # incorrect sum
            sum = None
    return sum


def input_accounting():
    """
    input accounting
    :return: accounting.Accounting
    """
    account = Accounting()
    while True:
        # enter date
        try:
            account.set_datetime(datetime.datetime(enter_year(),
                                 enter_month(), enter_day(), 0, 0))
            break
        except ValueError:
            pass
    # set description
    account.set_description(enter_desc())
    # set summa of payment
    account.set_sum(enter_sum())
    # return result
    return account


def print_user_info(user):
    """
    :param user: instance of user.User
    :return:nothing
    """
    print('User has %.2f' % user.get_money())


def print_payments(payment_list):
    """
    print all payments in payment_list
    :param payment_list: all payments in list
    :return: nothing
    """
    print('%-25s %-20s %-8s %-15s' %
          ("Date     ", "Description   ", "Sum    ", "Profit (True/False)"))
    # print each payment from list of payments
    for payment in payment_list:
        print('{0}'.format(payment))


def menu():
    """
    draws menu
    :return: pressed key
    """
    # input a key to choose your next action
    key = input(""" Press:
                1 - to view the list of payments
                2 - to append new payment
                3 - clear all payments
                4 - to exit
                """)
    # return result
    return key
