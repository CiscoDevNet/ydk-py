""" Cisco_IOS_XR_ipv6_ma_subscriber_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-ma\-subscriber package configuration.

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



class Ipv6ReachableViaEnum(Enum):
    """
    Ipv6ReachableViaEnum

    Ipv6 reachable via

    .. data:: received = 1

    	Source is reachable via interface on which

    	packet was received

    """

    received = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_subscriber_cfg as meta
        return meta._meta_table['Ipv6ReachableViaEnum']



