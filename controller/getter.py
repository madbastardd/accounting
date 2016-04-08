import view.view as module_view
from controller.cfgparser import cfgparse
from model.user import User

def main():
    """
    print all payments of user and user info
    :return:nothing
    """
    read = cfgparse()[0]
    main_user = read()
    if main_user is None:
        main_user = User(0.00)
    module_view.print_user_info(main_user)
    module_view.print_payments(main_user.get_payment_list())