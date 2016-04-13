"""view module
print/input model (accounting)
by Kirill"""

import decimal
import datetime
from model.accounting import Accounting, check_money


class View:
    """
    class includes methods for
    manipulating of data about User's payments
    and printing this data
    """

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def enter_desc():
        """
        enter description of payment
        :return: description of payment
        """
        return input("Enter description of accounting: ")

    @staticmethod
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

    @staticmethod
    def input_accounting():
        """
        input accounting
        :return: accounting.Accounting
        """
        account = Accounting()
        while True:
            # enter date
            try:
                account.set_datetime(datetime.datetime(View.enter_year(),
                                                       View.enter_month(),
                                                       View.enter_day(), 0, 0))
                break
            except ValueError:
                pass
        # set description
        account.set_description(View.enter_desc())
        # set summa of payment
        account.set_sum(View.enter_sum())
        # return result
        return account

    @staticmethod
    def print_payments(user):
        """
        print information about User's payments and money
        :param user: instance of user.User
        :return: nothing
        """
        print('{0}'.format(user))
