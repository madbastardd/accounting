import decimal
from model.accounting import Accounting, check_money
from model.payments_list import Payments


class User:
    """
    contains information about
    money and user accountings
    """

    def __init__(self, _money=decimal.Decimal(0.00)):
        """
        user constructor
        :param _money: user money
        :return: nothing
        """
        self._payments = Payments()
        # checks _money
        check_money(_money)
        self._money = decimal.Decimal("%.2f" % _money)

    def __format__(self, format_spec):
        """
        returns formatted string
        :param format_spec: format specifier
        :return: formatted string
        """
        res_format = 'User has %.2f\n' % self._money
        header = ("Date     ", "Description   ", "Sum    ", "Profit (True/False)")
        res_format += '%-25s %-20s %-8s %-15s\n' % header
        res_format += "{0}".format(self._payments)
        return res_format

    def __bool__(self):
        """
        :return: true if User has money
        """
        return self._money > 0

    def add_payment(self, payment):
        """
        add new payment
        :param payment: payment to add (accounting.Accounting)
        :return: nothing
        """
        self._payments.add_payment(payment)
        self._money += payment.get_sum()

    def remove_payment(self, payment):
        """
        remove payment
        :param payment: payment to remove
        :return: nothing
        """
        self._payments.remove_payment(payment)
        self.add_money(-payment.get_sum())

    def add_money(self, add_money):
        """
        add money to user
        :param add_money: money to add
        :return: nothing
        """
        # check add_money
        check_money(add_money)
        self._money += decimal.Decimal("%.2f" % add_money)

    def set_money(self, new_money):
        """
        set new money to user
        :param new_money: just new money
        :return: nothing
        """
        # check new_money
        check_money(new_money)
        self._money = decimal.Decimal("%.2f" % new_money)

    def clear_payments(self):
        """
        remove all payments
        :return: nothing
        """
        self._payments.clear_payments()

    def get_money(self):
        """
        :return: user money
        """
        return self._money

    def get_payment_list(self):
        """
        :return: user payment list
        """
        return self._payments.get_payment_list()

