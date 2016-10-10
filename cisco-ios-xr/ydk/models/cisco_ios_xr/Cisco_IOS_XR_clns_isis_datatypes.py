""" Cisco_IOS_XR_clns_isis_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class IsisAddressFamilyEnum(Enum):
    """
    IsisAddressFamilyEnum

    Isis address family

    .. data:: IPV4 = 0

    	IPv4

    .. data:: IPV6 = 1

    	IPv6

    """

    IPV4 = 0

    IPV6 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_datatypes as meta
        return meta._meta_table['IsisAddressFamilyEnum']


class IsisInternalLevelEnum(Enum):
    """
    IsisInternalLevelEnum

    Isis internal level

    .. data:: NOT_SET = 0

    	Level not set

    .. data:: LEVEL1 = 1

    	Level1

    .. data:: LEVEL2 = 2

    	Level2

    """

    NOT_SET = 0

    LEVEL1 = 1

    LEVEL2 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_datatypes as meta
        return meta._meta_table['IsisInternalLevelEnum']


class IsisSubAddressFamilyEnum(Enum):
    """
    IsisSubAddressFamilyEnum

    Isis sub address family

    .. data:: UNICAST = 0

    	Unicast

    .. data:: MULTICAST = 1

    	Multicast

    """

    UNICAST = 0

    MULTICAST = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_datatypes as meta
        return meta._meta_table['IsisSubAddressFamilyEnum']



