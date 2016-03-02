""" ATM_FORUM_TC_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class AtmServiceCategory_Enum(Enum):
    """
    AtmServiceCategory_Enum

    ATM Service Categories use this data type

    """

    OTHER = 1

    CBR = 2

    RTVBR = 3

    NRTVBR = 4

    ABR = 5

    UBR = 6


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_FORUM_TC_MIB as meta
        return meta._meta_table['AtmServiceCategory_Enum']


class TruthValue_Enum(Enum):
    """
    TruthValue_Enum

    Boolean values use this data type from RFC\-1903

    """

    TRUE = 1

    FALSE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _ATM_FORUM_TC_MIB as meta
        return meta._meta_table['TruthValue_Enum']



