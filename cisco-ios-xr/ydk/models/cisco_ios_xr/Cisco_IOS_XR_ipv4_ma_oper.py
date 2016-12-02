""" Cisco_IOS_XR_ipv4_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-ma package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-ipv4\-io\-oper
module with state data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class Ipv4MaOperLineStateEnum(Enum):
    """
    Ipv4MaOperLineStateEnum

    Interface line states

    .. data:: unknown = 0

    	Interface state is unknown

    .. data:: shutdown = 1

    	Interface has been shutdown

    .. data:: down = 2

    	Interface state is down

    .. data:: up = 3

    	Interface state is up

    """

    unknown = 0

    shutdown = 1

    down = 2

    up = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ma_oper as meta
        return meta._meta_table['Ipv4MaOperLineStateEnum']


class RpfModeEnum(Enum):
    """
    RpfModeEnum

    Interface line states

    .. data:: strict = 0

    	Strict RPF

    .. data:: loose = 1

    	Loose RPF

    """

    strict = 0

    loose = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ma_oper as meta
        return meta._meta_table['RpfModeEnum']



