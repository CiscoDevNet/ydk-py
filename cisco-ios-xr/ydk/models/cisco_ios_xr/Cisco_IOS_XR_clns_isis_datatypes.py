""" Cisco_IOS_XR_clns_isis_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IsisAddressFamily(Enum):
    """
    IsisAddressFamily (Enum Class)

    Isis address family

    .. data:: ipv4 = 0

    	IPv4

    .. data:: ipv6 = 1

    	IPv6

    """

    ipv4 = Enum.YLeaf(0, "ipv4")

    ipv6 = Enum.YLeaf(1, "ipv6")


class IsisInternalLevel(Enum):
    """
    IsisInternalLevel (Enum Class)

    Isis internal level

    .. data:: not_set = 0

    	Level not set

    .. data:: level1 = 1

    	Level1

    .. data:: level2 = 2

    	Level2

    """

    not_set = Enum.YLeaf(0, "not-set")

    level1 = Enum.YLeaf(1, "level1")

    level2 = Enum.YLeaf(2, "level2")


class IsisSubAddressFamily(Enum):
    """
    IsisSubAddressFamily (Enum Class)

    Isis sub address family

    .. data:: unicast = 0

    	Unicast

    .. data:: multicast = 1

    	Multicast

    """

    unicast = Enum.YLeaf(0, "unicast")

    multicast = Enum.YLeaf(1, "multicast")



