""" Cisco_IOS_XR_lpts_punt_flowtrap_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-punt\-flowtrap package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-lpts\-lib\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LptsPuntFlowtrapProtoId(Enum):
    """
    LptsPuntFlowtrapProtoId (Enum Class)

    Lpts punt flowtrap proto id

    .. data:: arp = 1

    	ARP

    .. data:: icmp = 2

    	Internet Control Message Protocol

    .. data:: dhcp = 3

    	Dynamic Host Configuration Protocol

    .. data:: pppoe = 4

    	PPP over Ethernet

    .. data:: ppp = 5

    	Point to point Protocol

    .. data:: igmp = 6

    	Internet Gateway Message Protocol

    .. data:: ipv4 = 7

    	IPv4

    .. data:: l2tp = 8

    	Layer2 Tunneling Protocol

    .. data:: unclassified = 9

    	Unclassified Source

    .. data:: ospf = 10

    	OSPF

    .. data:: bgp = 11

    	BGP

    .. data:: default = 12

    	All protocols

    """

    arp = Enum.YLeaf(1, "arp")

    icmp = Enum.YLeaf(2, "icmp")

    dhcp = Enum.YLeaf(3, "dhcp")

    pppoe = Enum.YLeaf(4, "pppoe")

    ppp = Enum.YLeaf(5, "ppp")

    igmp = Enum.YLeaf(6, "igmp")

    ipv4 = Enum.YLeaf(7, "ipv4")

    l2tp = Enum.YLeaf(8, "l2tp")

    unclassified = Enum.YLeaf(9, "unclassified")

    ospf = Enum.YLeaf(10, "ospf")

    bgp = Enum.YLeaf(11, "bgp")

    default = Enum.YLeaf(12, "default")



