import view


def main():
    # declaration of a payments list
    payments_list = []
    # menu1
    while True:
        key = view.menu()
        # if statement to check what menu item was chosen
        if key == '1':
            view.print_payments(payments_list)
        elif key == '2':
            account = view.input_accounting()
            payments_list.append(account)
        elif key == '3':
            exit()
        else:
            print("You've entered incorrect value")

main()
