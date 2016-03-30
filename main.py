import view
import user
import decimal
import sjson
import spickle
import sxml
import syaml
import configparser

main_user = None


def choose_type_ser(fname="defaults.cfg"):
    """
    choose type of serialization
    :param fname: configure file name
    :return: functions read/write
    """
    parser = configparser.ConfigParser()
    parser.read('defaults.cfg')
    type = parser['serialization']['type']
    if (type == 'json'):
        return sjson.read, sjson.write
    elif (type == 'xml'):
        return sxml.read, sxml.write
    elif (type == 'pickle'):
        return spickle.read, spickle.write
    elif (type == 'yaml'):
        return syaml.read, syaml.write
    else:
        raise AttributeError('Incorrect serialization type')


def main():
    # user declaration
    # menu
    while True:
        key = view.menu()
        # if statement to check what menu item was chosen
        if key == '1':
            view.print_user_info(main_user)
            view.print_payments(main_user.get_payment_list())
        elif key == '2':
            account = view.input_accounting()
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
if (main_user == None):
    main_user = user.User(0.00)
main()
write(main_user)
