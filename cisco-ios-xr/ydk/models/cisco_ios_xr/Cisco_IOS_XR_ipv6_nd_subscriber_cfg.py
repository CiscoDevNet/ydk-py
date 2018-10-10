""" Cisco_IOS_XR_ipv6_nd_subscriber_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-nd\-subscriber package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ipv6NdRouterPrefTemplate(Enum):
    """
    Ipv6NdRouterPrefTemplate (Enum Class)

    Ipv6 nd router pref template

    .. data:: high = 1

    	High preference

    .. data:: medium = 2

    	Medium preference

    .. data:: low = 3

    	Low preference

    """

    high = Enum.YLeaf(1, "high")

    medium = Enum.YLeaf(2, "medium")

    low = Enum.YLeaf(3, "low")



