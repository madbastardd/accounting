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
