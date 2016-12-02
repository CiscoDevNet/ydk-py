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

    .. data:: ipv4 = 0

    	IPv4

    .. data:: ipv6 = 1

    	IPv6

    """

    ipv4 = 0

    ipv6 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_datatypes as meta
        return meta._meta_table['IsisAddressFamilyEnum']


class IsisInternalLevelEnum(Enum):
    """
    IsisInternalLevelEnum

    Isis internal level

    .. data:: not_set = 0

    	Level not set

    .. data:: level1 = 1

    	Level1

    .. data:: level2 = 2

    	Level2

    """

    not_set = 0

    level1 = 1

    level2 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_datatypes as meta
        return meta._meta_table['IsisInternalLevelEnum']


class IsisSubAddressFamilyEnum(Enum):
    """
    IsisSubAddressFamilyEnum

    Isis sub address family

    .. data:: unicast = 0

    	Unicast

    .. data:: multicast = 1

    	Multicast

    """

    unicast = 0

    multicast = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_datatypes as meta
        return meta._meta_table['IsisSubAddressFamilyEnum']



