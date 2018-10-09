""" Cisco_IOS_XR_ipv4_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-ma package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-ipv4\-io\-oper
module with state data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ipv4MaOperConfig(Enum):
    """
    Ipv4MaOperConfig (Enum Class)

    ipv4 client type

    .. data:: ipv4_ma_oper_client_none = 0

    	ipv4 ma oper client none

    .. data:: ipv4_ma_oper_non_oc_client = 1

    	ipv4 ma oper non oc client

    .. data:: ipv4_ma_oper_oc_client = 2

    	ipv4 ma oper oc client

    """

    ipv4_ma_oper_client_none = Enum.YLeaf(0, "ipv4-ma-oper-client-none")

    ipv4_ma_oper_non_oc_client = Enum.YLeaf(1, "ipv4-ma-oper-non-oc-client")

    ipv4_ma_oper_oc_client = Enum.YLeaf(2, "ipv4-ma-oper-oc-client")


class Ipv4MaOperLineState(Enum):
    """
    Ipv4MaOperLineState (Enum Class)

    Interface line states

    .. data:: unknown = 0

    	Interface state is unknown

    .. data:: shutdown = 1

    	Interface has been shutdown

    .. data:: down = 2

    	Interface state is down

    .. data:: up = 3

    	Interface state is up

    """

    unknown = Enum.YLeaf(0, "unknown")

    shutdown = Enum.YLeaf(1, "shutdown")

    down = Enum.YLeaf(2, "down")

    up = Enum.YLeaf(3, "up")


class RpfMode(Enum):
    """
    RpfMode (Enum Class)

    Interface line states

    .. data:: strict = 0

    	Strict RPF

    .. data:: loose = 1

    	Loose RPF

    """

    strict = Enum.YLeaf(0, "strict")

    loose = Enum.YLeaf(1, "loose")



