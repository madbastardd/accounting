import unittest
from model.accounting import Accounting
from datetime import datetime


class TestAccounting(unittest.TestCase):
    """
    class for accounting methods testing
    """

    def test_get_datetime(self):
        """
        checks for setting and getting datetime correctly
        :return: nothing
        """
        account = Accounting()
        account.set_datetime(datetime(2016, 3, 10, 0, 0, 0))
        self.assertEqual(account.get_datetime(), datetime(2016, 3, 10, 0, 0, 0))

    def test_get_sum(self):
        """
        checks methods is_profit, is_consumption and bool
        :return: nothing
        """
        account = Accounting()
        account.set_sum(2.00)
        self.assertEqual(account.get_sum(), 2.00)
        self.assertTrue(account.is_profit())
        self.assertFalse(account.is_consumption())
        self.assertTrue(bool(account))

    def test_get_description(self):
        """
        checks description correctness
        :return: nothing
        """
        account = Accounting()
        account.set_description('description')
        self.assertEqual(account.get_description(), 'description')

    def test_add(self):
        """
        checks eq, neq and add methods of class Accounting
        :return: nothing
        """
        account1 = Accounting()
        account2 = Accounting()
        account1.set_sum(3.50)
        account2.set_sum(2.00)
        self.assertFalse(account1 == account2)
        self.assertTrue(account1 != account2)
        self.assertEqual(account1 + account2, 5.50)

if __name__ == '__main__':
    unittest.main()