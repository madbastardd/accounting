from model.accounting import Accounting


class Payments:
    def __init__(self):
        """
        default constructor
        :return:nothing
        """
        self._payment_list = []

    def __format__(self, format_spec):
        """
        returns formatted string
        :param format_spec: format specifier
        :return: formatted string
        """
        res_format = ''
        for payment in self._payment_list:
            res_format += format(payment) + '\n'
        return res_format

    def __len__(self):
        """
        return length of collection
        :return: amount of User's payments
        """
        return len(self._payment_list)

    def __getitem__(self, item):
        """
        returns payment with index of item
        :param item: payment index
        :return: payment
        """
        return self._payment_list[item]

    def __iter__(self):
        """
        iterator
        :return: payment
        """
        for payment in self._payment_list:
            yield payment

    def add_payment(self, payment):
        """
        add new payment
        :param payment: payment to add (accounting.Accounting)
        :return: nothing
        """
        if not isinstance(payment, Accounting):
            # incorrect type
            raise TypeError("Incorrect type of variable payment")
        self._payment_list.append(payment)

    def remove_payment(self, payment):
        """
        remove payment
        :param payment: payment to remove
        :return: nothing
        """
        try:
            self._payment_list.remove(payment)
        except ValueError:
            # payment not in list
            pass

    def clear_payments(self):
        """
        remove all payments
        :return: nothing
        """
        while self._payment_list:
            self._payment_list.pop()

    def get_payment_list(self):
        """
        :return: user payment list
        """
        return self._payment_list