""" Cisco_IOS_XE_rip 

Cisco XE Native Routing Information Protocol (RIP) Yang model.
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class OffsetListInOutTypeEnum(Enum):
    """
    OffsetListInOutTypeEnum

    .. data:: in_ = 0

    .. data:: out = 1

    """

    in_ = 0

    out = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rip as meta
        return meta._meta_table['OffsetListInOutTypeEnum']



