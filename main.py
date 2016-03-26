import view
import user
import decimal


def main():
    # user declaration
    main_user = user.User(200.00)
    # menu1
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
            exit()
        else:
            print("You've entered incorrect value")


main()
