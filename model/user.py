import decimal
from model.accounting import Accounting, check_money


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
        self._payment_list = []
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
        for payment in self._payment_list:
            res_format += format(payment) + '\n'
        return res_format

    def __bool__(self):
        """
        :return: true if User has money
        """
        return self._money > 0

    def __len__(self):
        """
        :return: amount of User's payments
        """
        return len(self._payment_list)

    def __getitem__(self, item):
        """
        returns payment with index of item
        :param item: payment index
        :return: payment
        """
        if not isinstance(item, int):
            raise TypeError("Incorrect type of variable item")
        if 0 <= item < len(self):
            return self._payment_list[item]
        raise IndexError("item index out of range")

    def __iter__(self):
        """
        :return: payment
        """
        for payment in self._payment_list:
            yield payment

    def add_payment(self, payment):
        """
        add new payment
        :param payment: payment to add (accounting.Accounting)
        :return: nothing
        """
        if not isinstance(payment, Accounting):
            # incorrect type
            raise TypeError("Incorrect type of variable payment")
        self._payment_list.append(payment)
        self._money += payment.get_sum()

    def remove_payment(self, payment):
        """
        remove payment
        :param payment: payment to remove
        :return: nothing
        """
        try:
            self._payment_list.remove(payment)
            self.add_money(-payment.get_sum())
        except ValueError:
            # payment not in list
            pass

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
        while self._payment_list:
            self._payment_list.pop()

    def get_money(self):
        """
        :return: user money
        """
        return self._money

    def get_payment_list(self):
        """
        :return: user payment list
        """
        return self._payment_list
