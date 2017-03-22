""" Cisco_IOS_XR_ipv6_nd_subscriber_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-nd\-subscriber package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class Ipv6NdRouterPrefTemplateEnum(Enum):
    """
    Ipv6NdRouterPrefTemplateEnum

    Ipv6 nd router pref template

    .. data:: high = 1

    	High preference

    .. data:: medium = 2

    	Medium preference

    .. data:: low = 3

    	Low preference

    """

    high = 1

    medium = 2

    low = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_subscriber_cfg as meta
        return meta._meta_table['Ipv6NdRouterPrefTemplateEnum']



