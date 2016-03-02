""" Cisco_IOS_XR_Ethernet_SPAN_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class SpanSessionClassOld_Enum(Enum):
    """
    SpanSessionClassOld_Enum

    Span session class old

    """

    """

    Mirror Ethernet packets

    """
    TRUE = 0


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_datatypes as meta
        return meta._meta_table['SpanSessionClassOld_Enum']


class SpanSessionClass_Enum(Enum):
    """
    SpanSessionClass_Enum

    Span session class

    """

    """

    Mirror Ethernet packets

    """
    ETHERNET = 0

    """

    Mirror IPv4 packets

    """
    IPV4 = 1

    """

    Mirror IPv6 packets

    """
    IPV6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_datatypes as meta
        return meta._meta_table['SpanSessionClass_Enum']



