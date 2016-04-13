import configparser
from controller.getter import main as main_get
from controller.setter import main as main_set


def get_type_controller(fname="data/defaults.cfg"):
    """
    choose controller type
    :param fname: configure file name
    :return: main function
    """
    # get configure file
    parser = configparser.ConfigParser()
    parser.read(fname)
    # get type of controller
    type = parser['controller']['type']
    if type == 'set':
        # setter controller
        return main_set
    if type == 'get':
        # getter controller
        return main_get
    else:
        # unknown controller
        raise AttributeError('Incorrect controller type')


get_type_controller()()
