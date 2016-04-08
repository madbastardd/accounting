import datetime
import decimal


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


class Accounting:
    """
    class includes date and time, when accounting was created,
    sum of payment,,
    and description of payment
    """
    def __init__(self):
        """
        constructor of payment
        set all values to None
        :return: nothing
        """
        self._datetime = None
        self._sum = None
        self._desc = None

    def __format__(self, format_spec):
        """
        returns formatted string
        :param format_spec: format specifier
        :return: formatted string
        """
        info = (self.get_datetime(), self.get_description()[:15],
                self.get_sum(), self.is_profit())
        return '%-25s %-20s %-8.2f %-15s' % info

    def __bool__(self):
        """
        return True if it is profit, else - False
        :return:True if it is profit
        """
        return self._sum > 0

    def __add__(self, other):
        """
        add money of accountings
        :param other:decimal.Decimal or accounting
        :return:sum
        """
        if isinstance(other, decimal.Decimal):
            return self._sum + other
        elif isinstance(other, Accounting):
            return self._sum + other._sum
        raise TypeError('Incorrect type of variable other')

    def __radd__(self, other):
        """
        add money of accountings
        :param other:decimal.Decimal or accounting
        :return:sum of None
        """
        if isinstance(other, decimal.Decimal):
            return self._sum + other
        elif isinstance(other, Accounting):
            return self._sum + other._sum
        raise TypeError('Incorrect type of variable other')

    def __eq__(self, other):
        """
        return true if accountings are equal by money
        :param other: other Accounting
        :return: true if accountings are equal by money
        """
        if not isinstance(other, Accounting):
            raise TypeError('Incorrect type of variable other')
        return self._sum == other._sum

    def __ne__(self, other):
        """
        return true if accountings are not equal by money
        :param other: other Accounting
        :return: true if accountings are not equal by money
        """
        return not self.__eq__(other)

    def set_datetime(self, date_time):
        """
        set datetime of payment
        :param date_time: date-time creation, can be only type datetime
        :return: nothing
        """
        if not isinstance(date_time, datetime.datetime):
            raise TypeError("Incorrect type of variable date_time")
        self._datetime = date_time

    def set_sum(self, sum):
        """
        set sum of payment
        :param sum: sum of payment
        :return: nothing
        """
        check_money(sum)
        self._sum = decimal.Decimal("%.2f" % sum)

    def set_description(self, desc):
        """
        set description of payment
        :param desc: description of payment, must be string
        :return:nothing
        """
        if not isinstance(desc, str):
            raise TypeError("Incorrect type of variable _desc")
        self._desc = desc

    def get_datetime(self):
        """
        :return: datetime of creation
        """
        return self._datetime

    def get_sum(self):
        """
        :return:sum of payment
        """
        return self._sum

    def get_description(self):
        """
        :return:description of payment
        """
        return self._desc

    def is_profit(self):
        """
        :return: true, if payment is profit
        """
        return self._sum > 0

    def is_consumption(self):
        """
        :return: true, if payment is consumption
        """
        return self._sum < 0
