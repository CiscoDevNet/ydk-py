""" ietf_nvo_tp_types 

ietf\-nvo\-tp\-types

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class PwtagmodeEnum(Enum):
    """
    PwtagmodeEnum

    PWTagMode

    .. data:: RAW = 0

    	RAW

    .. data:: TAGGED = 1

    	TAGGED

    """

    RAW = 0

    TAGGED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_tp_types as meta
        return meta._meta_table['PwtagmodeEnum']



