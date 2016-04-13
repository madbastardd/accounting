from view.view import View
from controller.cfgparser import serialize_type
from model.user import User


def get_key():
    """
    draws menu
    :return: pressed key
    """
    # input a key to choose your next action
    key = input(""" Press:
                1 - to append new payment
                2 - clear all payments
                3 - to exit
                """)
    # return result
    return key


def main():
    """
    allows to append User's payments and clear them
    :return: nothing
    """
    read = serialize_type()[0]
    write = serialize_type()[1]
    main_user = read()
    if main_user is None:
        main_user = User(0.00)
    while True:
        key = get_key()
        if key == '1':
            account = View.input_accounting()
            main_user.add_payment(account)
        elif key == '2':
            main_user.clear_payments()
            main_user.set_money(0.00)
        elif key == '3':
            write(main_user)
            return None
        else:
            print("You've entered incorrect value")