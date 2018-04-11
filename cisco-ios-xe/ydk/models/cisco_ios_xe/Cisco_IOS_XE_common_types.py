""" Cisco_IOS_XE_common_types 

This module contains type definitions common to all Cisco IOS XE native models

Copyright (c) 2016\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AddrType(Enum):
    """
    AddrType (Enum Class)

    IP address type

    .. data:: address_none = 0

    .. data:: ipv4_address = 1

    .. data:: ipv6_address = 2

    .. data:: ipv4_address_mcast = 3

    .. data:: ipv6_address_mcast = 4

    """

    address_none = Enum.YLeaf(0, "address-none")

    ipv4_address = Enum.YLeaf(1, "ipv4-address")

    ipv6_address = Enum.YLeaf(2, "ipv6-address")

    ipv4_address_mcast = Enum.YLeaf(3, "ipv4-address-mcast")

    ipv6_address_mcast = Enum.YLeaf(4, "ipv6-address-mcast")



