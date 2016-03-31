"""
module with unittests
for testing serialization methods
"""
import unittest
import user
import accounting
import stringio
import syaml
import sjson
import datetime


class TestSerialization(unittest.TestCase):

    def create_user(self):
        """
        :return: User object
        """
        acc = accounting.Accounting()
        acc.set_datetime(datetime.datetime(2016, 3, 27, 0, 0))
        acc.set_description('desc')
        acc.set_sum(17.00)
        usr = user.User()
        usr.add_payment(acc)
        return usr

    def test_yaml(self):
        syaml.write(self.create_user())
        serial_usr = stringio.readToStringIO()
        serial_usr.seek(0)
        self.assertEqual(serial_usr.readline(), '!!python/object:user.User\n')

    def test_json(self):
        sjson.write(self.create_user())
        serial_usr = stringio.readToStringIO('info.json')
        serial_usr.seek(0)
        self.assertEqual(serial_usr.readline(), '{\n')


if __name__ == '__main__':
    unittest.main()
