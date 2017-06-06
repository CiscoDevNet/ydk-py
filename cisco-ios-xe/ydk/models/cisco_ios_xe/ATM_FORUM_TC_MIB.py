""" ATM_FORUM_TC_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AtmservicecategoryEnum(Enum):
    """
    AtmservicecategoryEnum

    ATM Service Categories use this data type

    .. data:: other = 1

    .. data:: cbr = 2

    .. data:: rtVbr = 3

    .. data:: nrtVbr = 4

    .. data:: abr = 5

    .. data:: ubr = 6

    """

    other = 1

    cbr = 2

    rtVbr = 3

    nrtVbr = 4

    abr = 5

    ubr = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_FORUM_TC_MIB as meta
        return meta._meta_table['AtmservicecategoryEnum']


class TruthvalueEnum(Enum):
    """
    TruthvalueEnum

    Boolean values use this data type from RFC\-1903

    .. data:: true = 1

    .. data:: false = 2

    """

    true = 1

    false = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ATM_FORUM_TC_MIB as meta
        return meta._meta_table['TruthvalueEnum']



