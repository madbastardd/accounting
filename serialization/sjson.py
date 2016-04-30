"""module that serialize
user.User in JSON and deserialize
user.User from file"""

import json
from model.payments_list import Payments
from model.user import User
import datetime
from model.accounting import Accounting
import decimal


class UserEncoder(json.JSONEncoder):
    """
    Serializer user.User in JSON
    """
    def default(self, o):
        """
        overriding method
        """
        if isinstance(o, User):
            # user object
            return {"money": o.get_money(),
                    "payment list": tuple(o.get_payment_list())}
        if isinstance(o, Payments):
            return [item for item in o.get_payment_list()]
        if isinstance(o, Accounting):
            # accounting object
            return {"datetime": o.get_datetime(),
                    "description": o.get_description(),
                    "sum": o.get_sum()}
        if isinstance(o, decimal.Decimal):
            # decimal
            return str(o)
        if isinstance(o, datetime.datetime):
            # datetime
            return {"year": o.year,
                    "month": o.month,
                    "day": o.day}
        # another
        return json.JSONEncoder.default(self, o)


def write(obj, fname='data/info.json'):
    """
    serialize user object in JSON
    :param obj: class User to serialize
    :param fname: file name
    :return: nothing
    """
    if not isinstance(obj, User):
        # obj is not User
        raise ValueError('Incorrect type of variable obj')
    with open(fname, 'wt') as file:
        json.dump(obj, file, cls=UserEncoder, indent=4)


def encode_dict(dict):
    """
    decodes user from dictionary
    :param dict: decoded user
    :return: new user
    """
    # create new user
    ret_user = User()
    # set his money
    ret_user.set_money(decimal.Decimal(dict['money']))
    for account in dict['payment list']:
        # set new accounting
        tmp_account = Accounting()
        date = account['datetime']
        # set datetime
        tmp_account.set_datetime(datetime.datetime(date['year'],
                                                   date['month'],
                                                   date['day']))
        # set sum
        tmp_account.set_sum(decimal.Decimal(account['sum']))
        # set description
        tmp_account.set_description(account['description'])
        # add account
        ret_user.add_payment(tmp_account)
        ret_user.add_money(-tmp_account.get_sum())
    return ret_user


def read(fname='data/info.json'):
    """
    read from JSON file object
    :param fname: file name
    :return: new User object or None
    """
    try:
        with open(fname, 'rt') as file:
            # try load
            # and return user
            return encode_dict(json.load(file))
    except (OSError, ValueError):
        # file not found or incorrect value,
        # return None
        return None
