import view.view as module_view
from model.user import User
from serialization.sjson import read as json_read, write as json_write
from serialization.spickle import read as pickle_read, write as pickle_write
from serialization.sxml import read as xml_read, write as xml_write
from serialization.syaml import read as yaml_read, write as yaml_write
import configparser

main_user = None


def choose_type_ser(fname="data/defaults.cfg"):
    """
    choose type of serialization
    :param fname: configure file name
    :return: functions read/write
    """
    # get configure file
    parser = configparser.ConfigParser()
    parser.read(fname)
    # get type of serialization
    type = parser['serialization']['type']
    if type == 'json':
        # JSON
        return json_read, json_write
    elif type == 'xml':
        # XML
        return xml_read, xml_write
    elif type == 'pickle':
        # pickle
        return pickle_read, pickle_write
    elif type == 'yaml':
        # YAML
        return yaml_read, yaml_write
    else:
        # unknown type
        raise AttributeError('Incorrect serialization type')


def main():
    # user declaration
    # menu
    while True:
        key = module_view.menu()
        # if statement to check what menu item was chosen
        if key == '1':
            module_view.print_user_info(main_user)
            module_view.print_payments(main_user.get_payment_list())
        elif key == '2':
            account = module_view.input_accounting()
            main_user.add_payment(account)
        elif key == '3':
            main_user.clear_payments()
            main_user.set_money(0.00)
        elif key == '4':
            return None
        else:
            print("You've entered incorrect value")


read, write = choose_type_ser()
main_user = read()
if main_user is None:
    main_user = User(0.00)
main()
write(main_user)
