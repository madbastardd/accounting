"""module that serialize
user.User in Pickle and deserialize
user.User from file"""

import pickle
import user


def write(obj, fname='info.pickle'):
    """
    serialize user object in Pickle
    :param obj: class User to serialize
    :param fname: file name
    :return: nothing
    """
    if not isinstance(obj, user.User):
        # obj is not User
        raise ValueError('Incorrect type of variable obj')
    with open(fname, 'wb') as file:
        pickle.dump(obj, file)


def read(fname='info.pickle'):
    """
    read from Pickle file object
    :param fname: file name
    :return: new User object or None
    """
    try:
        with open(fname, 'rb') as file:
            # try load
            # and return user
            return pickle.load(file)
    except (OSError, ValueError):
        # file not found or incorrect value,
        # return None
        return None
