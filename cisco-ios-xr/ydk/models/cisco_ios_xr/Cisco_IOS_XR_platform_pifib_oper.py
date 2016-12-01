""" Cisco_IOS_XR_platform_pifib_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR platform\-pifib package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-lpts\-pre\-ifib\-oper
module with state data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class UsageAddressFamilyEnum(Enum):
    """
    UsageAddressFamilyEnum

    Usage address family

    .. data:: ipv4 = 0

    	Ipv4 af

    .. data:: ipv6 = 1

    	Ipv6 af

    """

    ipv4 = 0

    ipv6 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_platform_pifib_oper as meta
        return meta._meta_table['UsageAddressFamilyEnum']



