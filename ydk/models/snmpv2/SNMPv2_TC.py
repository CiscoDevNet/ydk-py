""" SNMPv2_TC 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class RowStatus_Enum(Enum):
    """
    RowStatus_Enum

    """

    ACTIVE = 1

    NOTINSERVICE = 2

    NOTREADY = 3

    CREATEANDGO = 4

    CREATEANDWAIT = 5

    DESTROY = 6


    @staticmethod
    def _meta_info():
        from ydk.models.snmpv2._meta import _SNMPv2_TC as meta
        return meta._meta_table['RowStatus_Enum']


class StorageType_Enum(Enum):
    """
    StorageType_Enum

    """

    OTHER = 1

    VOLATILE = 2

    NONVOLATILE = 3

    PERMANENT = 4

    READONLY = 5


    @staticmethod
    def _meta_info():
        from ydk.models.snmpv2._meta import _SNMPv2_TC as meta
        return meta._meta_table['StorageType_Enum']


class TruthValue_Enum(Enum):
    """
    TruthValue_Enum

    """

    TRUE = 1

    FALSE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.snmpv2._meta import _SNMPv2_TC as meta
        return meta._meta_table['TruthValue_Enum']



