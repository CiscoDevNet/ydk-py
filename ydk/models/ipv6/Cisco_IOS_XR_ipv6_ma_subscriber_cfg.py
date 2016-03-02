""" Cisco_IOS_XR_ipv6_ma_subscriber_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-ma\-subscriber package configuration.

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



class Ipv6ReachableVia_Enum(Enum):
    """
    Ipv6ReachableVia_Enum

    Ipv6 reachable via

    """

    """

    Source is reachable via interface on which
    packet was received

    """
    RECEIVED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_ma_subscriber_cfg as meta
        return meta._meta_table['Ipv6ReachableVia_Enum']



