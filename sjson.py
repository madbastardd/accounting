"""module that serialize
user.User in JSON and deserialize
user.User from file"""

import json
import user
import datetime
import accounting
import decimal


class UserEncoder(json.JSONEncoder):
    """
    Serializer user.User in JSON
    """
    def default(self, o):
        """
        overriding method
        """
        if isinstance(o, user.User):
            # user object
            return {"money": o.get_money(),
                    "payment list": tuple(o.get_payment_list())}
        if isinstance(o, accounting.Accounting):
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


def write(obj):
    """
    serialize user object
    :param obj: class User to serialize
    :return: nothing
    """
    if not isinstance(obj, user.User):
        # obj is not User
        raise ValueError('Incorrect type of variable obj')
    with open('info.json', 'wt') as file:
        json.dump(obj, file, cls=UserEncoder)


def encode_dict(dict):
    """
    decodes user
    :param dict: decoded user
    :return: new user
    """
    # create new user
    ret_user = user.User()
    # set his money
    ret_user.set_money(decimal.Decimal(dict['money']))
    for account in dict['payment list']:
        # set new accounting
        tmp_account = accounting.Accounting()
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


def read():
    """
    read from file object
    :return: new User object or None
    """
    dict = None
    try:
        with open('info.json', 'rt') as file:
            # try load
            dict = json.load(file)
    except (OSError, ValueError):
        # file not found, return None
        return None

    # return user
    return encode_dict(dict)
