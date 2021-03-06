"""
Use these exceptions to `try` against specific Rpw Exceptions.

>>> from rpw.exceptions import RpwWrongStorageType
>>> try:
...     element.parameters['Height'].value = 'String'
... except RpwWrongStorageType:
...     print('Height Parameter cannot be a string')
...     raise

This module also provides easy access to the ``Autodesk.Revit.Exceptions``
namespaces:

>>> from rpw.exceptions.RevitExceptions import InvalidObjectException
>>> try:
...     doc.Delete(ElementId)
... except InvalidObjectException:
...     print('This element is no longer valid ')

"""  #

from rpw.utils.logger import logger
from Autodesk.Revit import Exceptions as RevitExceptions

class RpwException(Exception):
    """ Revit Python Wrapper Base Exception """


class RpwTypeError(TypeError):
    """ Revit Python Wrapper Type Exception """
    def __init__(self, type_expected, type_received='not reported'):
        msg = 'expected [{}], got [{}]'.format(type_expected, type_received)
        super(RpwTypeError, self).__init__(msg)


class RpwValueError(ValueError):
    """ Revit Python Wrapper Value Error Exception """
    def __init__(self, value_expected, value_received='not reported'):
        msg = 'expected [{}], got [{}]'.format(value_expected, value_received)
        super(RpwValueError, self).__init__(msg)


class RpwParameterNotFound(RpwException, KeyError):
    """ Revit Python Wrapper Parameter Error """
    def __init__(self, element, param_name):
        msg = 'parameter not found [element:{}]:[param_name:{}]'.format(element.Id, param_name)
        super(RpwParameterNotFound, self).__init__(msg)


class RpwWrongStorageType(RpwException, TypeError):
    """ Wrong Storage Type """
    def __init__(self, storage_type, value):
        msg = 'Wrong Storage Type: [{}]:[{}:{}]'.format(storage_type,
                                                        type(value), value)
        super(RpwWrongStorageType, self).__init__(msg)


class RpwCoerceError(RpwException, ValueError):
    """ Coerce Error """
    def __init__(self, value, target_type):
        msg = 'Could not cast value:{} to target_type:{}'.format(value, target_type)
        super(RpwCoerceError, self).__init__(msg)


