""" Cisco_IOS_XR_ipv6_ma_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-ma package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ipv6DefaultPing(Enum):
    """
    Ipv6DefaultPing (Enum Class)

    Ipv6 default ping

    .. data:: disabled = 0

    	Default route is not allowed to match when

    	checking source address

    .. data:: enabled = 1

    	Allow default route to match when checking

    	source address

    """

    disabled = Enum.YLeaf(0, "disabled")

    enabled = Enum.YLeaf(1, "enabled")


class Ipv6Qppb(Enum):
    """
    Ipv6Qppb (Enum Class)

    Ipv6 qppb

    .. data:: none = 0

    	No QPPB configuration

    .. data:: ip_precedence = 1

    	Enable ip-precedence based QPPB

    .. data:: qos_group = 2

    	Enable qos-group based QPPB

    .. data:: both = 3

    	Enable both ip-precedence and qos-group based

    	QPPB

    """

    none = Enum.YLeaf(0, "none")

    ip_precedence = Enum.YLeaf(1, "ip-precedence")

    qos_group = Enum.YLeaf(2, "qos-group")

    both = Enum.YLeaf(3, "both")


class Ipv6Reachable(Enum):
    """
    Ipv6Reachable (Enum Class)

    Ipv6 reachable

    .. data:: any = 0

    	Source is reachable via any interface

    .. data:: received = 1

    	Source is reachable via interface on which

    	packet was received

    """

    any = Enum.YLeaf(0, "any")

    received = Enum.YLeaf(1, "received")


class Ipv6SelfPing(Enum):
    """
    Ipv6SelfPing (Enum Class)

    Ipv6 self ping

    .. data:: disabled = 0

    	Doesn't allow router to ping itself

    .. data:: enabled = 1

    	Allow router to ping itself

    """

    disabled = Enum.YLeaf(0, "disabled")

    enabled = Enum.YLeaf(1, "enabled")



