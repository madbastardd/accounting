import decimal
import accounting


def check_money(money):
    """
    :param money: check money
    if money has more then two number after decimal point -
    raise ValueError
    :return:nothing
    """
    # check type
    decimal.Decimal(money)
    try:
        fractional = str(money).split('.')[1]
        if len(fractional) > 2:
            # fractional part has more then two numbers after decimal point
            raise ValueError("Two numbers are required " +
                             "after decimal point in variable _money")
    except IndexError:
        # no fractional part
        pass


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

    def add_payment(self, payment):
        """
        add new payment
        :param payment: payment to add (accounting.Accounting)
        :return: nothing
        """
        if not isinstance(payment, accounting.Accounting):
            # incorrect type
            raise ValueError("Incorrect type of variable payment")
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
