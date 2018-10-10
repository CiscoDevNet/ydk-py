""" Cisco_IOS_XR_ipv4_io_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-io package configuration.

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



class Ipv4DefaultPing(Enum):
    """
    Ipv4DefaultPing (Enum Class)

    Ipv4 default ping

    .. data:: disabled = 0

    	Default route is not allowed to match when

    	checking source address

    .. data:: enabled = 1

    	Allow default route to match when checking

    	source address

    """

    disabled = Enum.YLeaf(0, "disabled")

    enabled = Enum.YLeaf(1, "enabled")


class Ipv4InterfaceQppb(Enum):
    """
    Ipv4InterfaceQppb (Enum Class)

    Ipv4 interface qppb

    .. data:: ip_precedence = 1

    	Enable IP precedence based QPPB

    .. data:: qos_group = 2

    	Enable QoS-group based QPPB

    .. data:: both = 3

    	Enable both IP precedence and QoS-group based

    	QPPB

    """

    ip_precedence = Enum.YLeaf(1, "ip-precedence")

    qos_group = Enum.YLeaf(2, "qos-group")

    both = Enum.YLeaf(3, "both")


class Ipv4Reachable(Enum):
    """
    Ipv4Reachable (Enum Class)

    Ipv4 reachable

    .. data:: any = 0

    	Source is reachable via any interface

    .. data:: received = 1

    	Source is reachable via interface on which

    	packet was received

    """

    any = Enum.YLeaf(0, "any")

    received = Enum.YLeaf(1, "received")


class Ipv4SelfPing(Enum):
    """
    Ipv4SelfPing (Enum Class)

    Ipv4 self ping

    .. data:: disabled = 0

    	Doesn't allow router to ping itself

    .. data:: enabled = 1

    	Allow router to ping itself

    """

    disabled = Enum.YLeaf(0, "disabled")

    enabled = Enum.YLeaf(1, "enabled")



