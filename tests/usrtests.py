import unittest
from model.accounting import Accounting
from model.user import User


class TestUser(unittest.TestCase):
    """
    class for User methods testing
    """

    def create_user(self):
        """
        creates instance of User class
        with two payments
        :return: user
        """
        user = User()
        user.set_money(3.00)
        payment = Accounting()
        payment.set_sum(2.00)
        another_payment = payment
        another_payment.set_description('another')
        user.add_payment(payment)
        user.add_payment(another_payment)
        return user

    def test_remove_payment(self):
        """
        tests remove_payment and add_money methods
        :return: nothing
        """
        user = self.create_user()
        payment = Accounting()
        payment.set_sum(-1.00)
        user.remove_payment(payment)
        user.add_money(2.00)
        self.assertEqual(user.get_money(), 9.00)

    def test_clear_payments(self):
        """
        tests clear_payments method
        :return: nothing
        """
        user = User(3.00)
        payment = Accounting()
        payment.set_sum(1.00)
        user.add_payment(payment)
        user.clear_payments()
        self.assertEqual(len(user.get_payment_list()), 0)

    def test_bool(self):
        """
        tests bool method
        :return: nothing
        """
        user = User(3.00)
        self.assertTrue(bool(user))

    def test_len(self):
        """
        tests len method
        :return: nothing
        """
        user = self.create_user()
        self.assertEqual(len(user), 2)

    def test_get_item(self):
        """
        tests get_item method
        :return: nothing
        """
        user = self.create_user()
        payment = user[1]
        self.assertEqual(payment.get_description(), 'another')

    def test_iter(self):
        """
        tests iter method
        :return: nothing
        """
        user = self.create_user()
        sum = 0
        for payment in user:
            sum += payment.get_sum()
        self.assertEqual(sum, 4)

if __name__ == '__main__':
    unittest.main()