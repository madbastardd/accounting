from view.view import View
from controller.cfgparser import serialize_type
from model.user import User


def main():
    """
    print all payments of user and user info
    :return:nothing
    """
    read = serialize_type()[0]
    main_user = read()
    if main_user is None:
        main_user = User(0.00)
    View.print_payments(main_user)
