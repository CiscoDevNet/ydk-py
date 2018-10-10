""" Cisco_IOS_XR_Ethernet_SPAN_datatypes 

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



class SpanSessionClass(Enum):
    """
    SpanSessionClass (Enum Class)

    Span session class

    .. data:: ethernet = 0

    	Mirror Ethernet packets

    .. data:: ipv4 = 1

    	Mirror IPv4 packets

    .. data:: ipv6 = 2

    	Mirror IPv6 packets

    .. data:: mpls_ipv4 = 3

    	Mirror MPLS-encapsulated IPv4 packets

    .. data:: mpls_ipv6 = 4

    	Mirror MPLS-encapsulated IPv6 packets

    """

    ethernet = Enum.YLeaf(0, "ethernet")

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")

    mpls_ipv4 = Enum.YLeaf(3, "mpls-ipv4")

    mpls_ipv6 = Enum.YLeaf(4, "mpls-ipv6")


class SpanSessionClassOld(Enum):
    """
    SpanSessionClassOld (Enum Class)

    Span session class old

    .. data:: true = 0

    	Mirror Ethernet packets

    """

    true = Enum.YLeaf(0, "true")



