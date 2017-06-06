""" Cisco_IOS_XE_eem 

Cisco XE Native Embedded Event Manager (EEM) Yang model.
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class OperatorTypeEnum(Enum):
    """
    OperatorTypeEnum

    .. data:: eq = 0

    .. data:: ge = 1

    .. data:: gt = 2

    .. data:: le = 3

    .. data:: lt = 4

    .. data:: ne = 5

    """

    eq = 0

    ge = 1

    gt = 2

    le = 3

    lt = 4

    ne = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_eem as meta
        return meta._meta_table['OperatorTypeEnum']



