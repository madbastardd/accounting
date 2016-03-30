"""module that serialize
user.User in XML and deserialize
user.User from file"""

import user
import datetime
import accounting
import decimal
from xml.etree.ElementTree import Element, SubElement
from xml.etree import ElementTree
from xml.dom import minidom


def prettify(elem):
    """
    Return a pretty-printed XML string for the Element.
    :param elem: XML top
    :return: pretty-printed XML
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")


def create_xml(obj):
    """
    serialize obj to XML
    :param obj: user object
    :return: XML top
    """
    # create top
    top = Element('user')
    # set attribute
    top.set('money', str(obj.get_money()))
    # create subellement - list of payments
    accountings_list = SubElement(top, 'accountings')
    for account in obj.get_payment_list():
        # create one payment element
        one_account = SubElement(accountings_list, 'account')
        # set his attribute
        one_account.set('price', str(account.get_sum()))
        one_account.set('description', account.get_description())
        # set datetime of creation
        date_element = SubElement(one_account, 'datetime')
        dtime = account.get_datetime()
        date_element.set('year', str(dtime.year))
        date_element.set('month', str(dtime.month))
        date_element.set('day', str(dtime.day))

    return top


def parse_xml(tree):
    """
    try to parse XML from tree
    :param tree: XML
    :return: user
    """
    # get root
    root = tree.getroot()
    # creates new user
    ret_user = user.User()
    # set his money
    ret_user.set_money(decimal.Decimal(root.attrib['money']))

    for account in root[0]:
        # create new account
        new_account = accounting.Accounting()
        # set its description
        new_account.set_description(account.attrib['description'])
        # set new sum
        new_account.set_sum(decimal.Decimal(account.attrib['price']))
        # get datetime
        dtime = account[0]
        # set datetime
        new_account.set_datetime(datetime.datetime(int(dtime.attrib['year']),
                                                   int(dtime.attrib['month']),
                                                   int(dtime.attrib['day'])))
        # set this payment to user
        ret_user.add_payment(new_account)
        # add money
        ret_user.add_money(-new_account.get_sum())

    return ret_user


def write(obj, fname='info.xml'):
    """
    serialize user object in XML
    :param obj: class User to serialize
    :param fname: file name
    :return: nothing
    """
    if not isinstance(obj, user.User):
        # obj is not User
        raise ValueError('Incorrect type of variable obj')
    with open(fname, "wt") as file:
        file.write(prettify(create_xml(obj)))


def read(fname='info.xml'):
    """
    deserialize user object in XML
    :param fname: file name
    :return: class User
    """
    try:
        # try parse
        return parse_xml(ElementTree.parse(fname))
    except (OSError, ValueError):
        # file not found, return None
        return None
