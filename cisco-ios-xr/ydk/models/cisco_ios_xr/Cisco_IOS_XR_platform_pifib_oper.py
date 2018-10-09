""" Cisco_IOS_XR_platform_pifib_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR platform\-pifib package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-lpts\-pre\-ifib\-oper
module with state data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class UsageAddressFamily(Enum):
    """
    UsageAddressFamily (Enum Class)

    Usage address family

    .. data:: ipv4 = 0

    	Ipv4 af

    .. data:: ipv6 = 1

    	Ipv6 af

    """

    ipv4 = Enum.YLeaf(0, "ipv4")

    ipv6 = Enum.YLeaf(1, "ipv6")



