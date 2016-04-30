import configparser
from controller.cui import main as main_set
from controller.cons_main import main as cons_main


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
    if type == 'std':
        # setter controller
        return main_set
    if type == 'console':
        # console controller
        return cons_main
    else:
        # unknown controller
        raise AttributeError('Incorrect controller type')


get_type_controller()()
