""" Cisco_IOS_XR_common_acl_datatypes 

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



class AclUsageAppIdEnumEnum(Enum):
    """
    AclUsageAppIdEnumEnum

    Acl usage app id enum

    .. data:: PFILTER = 1

    	General Usage Statistics

    .. data:: BGP = 2

    	Usage staistics related to BGP Traffic

    .. data:: OSPF = 3

    	Usage staistics related to OSPF Traffic

    """

    PFILTER = 1

    BGP = 2

    OSPF = 3


    @staticmethod
    def _meta_info():
        from ydk.models.common._meta import _Cisco_IOS_XR_common_acl_datatypes as meta
        return meta._meta_table['AclUsageAppIdEnumEnum']



