""" Cisco_IOS_XR_ipv4_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-ma package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-ipv4\-io\-oper
module with state data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class Ipv4MaOperLineStateEnum(Enum):
    """
    Ipv4MaOperLineStateEnum

    Interface line states

    .. data:: UNKNOWN = 0

    	Interface state is unknown

    .. data:: SHUTDOWN = 1

    	Interface has been shutdown

    .. data:: DOWN = 2

    	Interface state is down

    .. data:: UP = 3

    	Interface state is up

    """

    UNKNOWN = 0

    SHUTDOWN = 1

    DOWN = 2

    UP = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_ma_oper as meta
        return meta._meta_table['Ipv4MaOperLineStateEnum']


class RpfModeEnum(Enum):
    """
    RpfModeEnum

    Interface line states

    .. data:: STRICT = 0

    	Strict RPF

    .. data:: LOOSE = 1

    	Loose RPF

    """

    STRICT = 0

    LOOSE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_ma_oper as meta
        return meta._meta_table['RpfModeEnum']



