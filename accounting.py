import datetime
import decimal


class Accounting:
    """class includes date and time, when accounting was created,
    sum of payment,
    type of payment (profit/consumption),
    and description of payment"""
    def __init__(self):
        """constructor of payment
        set all values to None"""
        self.__datetime = None
        self.__sum = None
        self.__desc = None
        self.__isprofit = None

    def set_datetime(self, _datetime):
        """set datetime of payment
        _datetime can be only type datetime
        return nothing"""
        if type(_datetime) is not datetime.datetime:
            raise TypeError("Incorrect type of variable _datetime")
        self.__datetime = _datetime

    def set_sum(self, _sum):
        """set sum of payment
        _sum must be decimal
        return nothing"""
        if type(_sum) is not decimal.Decimal:
            raise TypeError("Incorrect type of variable _sum")
        self.__sum = _sum

    def set_description(self, _desc):
        """set description of payment
        _desc must be string
        return nothing"""
        if type(_desc) is not str:
            raise TypeError("Incorrect type of variable _desc")
        self.__desc = _desc

    def set_profit(self):
        """set profit payment type"""
        self.__isprofit = True

    def set_consumption(self):
        """set consumption payment type"""
        self.__isprofit = False

    def get_datetime(self):
        """returns datetime"""
        return self.__datetime

    def get_sum(self):
        """return sum"""
        return self.__sum

    def get_description(self):
        """return description of profit"""
        return self.__desc

    def is_profit(self):
        """return true, if payment is profit"""
        return self.__isprofit

    def is_consumption(self):
        """return true, if payment is consumption"""
        return not self.__isprofit
