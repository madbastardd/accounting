"""
module for reading files
to StringIO objects
"""
from io import StringIO


def readToStringIO(fname='info.yaml'):
    """
    :param fname: file name to read from
    :return: StringIO object
    """
    obj = StringIO()
    with open(fname, "rt") as f:
        for line in f:
            obj.write(line)
    return obj
