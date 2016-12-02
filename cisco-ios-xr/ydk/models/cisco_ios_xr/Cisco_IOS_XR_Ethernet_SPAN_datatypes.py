""" Cisco_IOS_XR_Ethernet_SPAN_datatypes 

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



class SpanSessionClassEnum(Enum):
    """
    SpanSessionClassEnum

    Span session class

    .. data:: ethernet = 0

    	Mirror Ethernet packets

    .. data:: ipv4 = 1

    	Mirror IPv4 packets

    .. data:: ipv6 = 2

    	Mirror IPv6 packets

    """

    ethernet = 0

    ipv4 = 1

    ipv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_datatypes as meta
        return meta._meta_table['SpanSessionClassEnum']


class SpanSessionClassOldEnum(Enum):
    """
    SpanSessionClassOldEnum

    Span session class old

    .. data:: true = 0

    	Mirror Ethernet packets

    """

    true = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_datatypes as meta
        return meta._meta_table['SpanSessionClassOldEnum']



