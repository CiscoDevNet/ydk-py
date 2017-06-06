""" Cisco_IOS_XE_ospf 

Cisco XE Native Open Shortest Path First (OSPF) Yang model.
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class RedistOspfExternalTypeEnum(Enum):
    """
    RedistOspfExternalTypeEnum

    .. data:: Y_1 = 0

    .. data:: Y_2 = 1

    """

    Y_1 = 0

    Y_2 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_ospf as meta
        return meta._meta_table['RedistOspfExternalTypeEnum']



