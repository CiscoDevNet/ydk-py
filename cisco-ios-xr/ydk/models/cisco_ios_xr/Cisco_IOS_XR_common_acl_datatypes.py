""" Cisco_IOS_XR_common_acl_datatypes 

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



class AclUsageAppIdEnumEnum(Enum):
    """
    AclUsageAppIdEnumEnum

    Acl usage app id enum

    .. data:: pfilter = 1

    	General Usage Statistics

    .. data:: bgp = 2

    	Usage staistics related to BGP Traffic

    .. data:: ospf = 3

    	Usage staistics related to OSPF Traffic

    """

    pfilter = 1

    bgp = 2

    ospf = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_common_acl_datatypes as meta
        return meta._meta_table['AclUsageAppIdEnumEnum']



