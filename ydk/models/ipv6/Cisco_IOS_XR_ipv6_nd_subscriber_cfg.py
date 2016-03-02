""" Cisco_IOS_XR_ipv6_nd_subscriber_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-nd\-subscriber package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class Ipv6NdHopLimit_Enum(Enum):
    """
    Ipv6NdHopLimit_Enum

    Ipv6 nd hop limit

    """

    """

    Zero hoplimit value

    """
    UNSPECIFIED = 0


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_nd_subscriber_cfg as meta
        return meta._meta_table['Ipv6NdHopLimit_Enum']


class Ipv6NdRouterPrefTemplate_Enum(Enum):
    """
    Ipv6NdRouterPrefTemplate_Enum

    Ipv6 nd router pref template

    """

    """

    High preference

    """
    HIGH = 1

    """

    Medium preference

    """
    MEDIUM = 2

    """

    Low preference

    """
    LOW = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_nd_subscriber_cfg as meta
        return meta._meta_table['Ipv6NdRouterPrefTemplate_Enum']



