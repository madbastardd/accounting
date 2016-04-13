"""config file parser module"""
from serialization.sjson import read as json_read, write as json_write
from serialization.spickle import read as pickle_read, write as pickle_write
from serialization.sxml import read as xml_read, write as xml_write
from serialization.syaml import read as yaml_read, write as yaml_write
import configparser


def serialize_type(fname="data/defaults.cfg"):
    """
    parse configure file
    :param fname: configure file name
    :return: functions read/write
    """
    # get configure file
    parser = configparser.ConfigParser()
    parser.read(fname)
    # get type of serialization
    type = parser['serialization']['type']
    if type == 'json':
        # JSON
        return json_read, json_write
    elif type == 'xml':
        # XML
        return xml_read, xml_write
    elif type == 'pickle':
        # pickle
        return pickle_read, pickle_write
    elif type == 'yaml':
        # YAML
        return yaml_read, yaml_write
    else:
        # unknown type
        raise AttributeError('Incorrect serialization type')
