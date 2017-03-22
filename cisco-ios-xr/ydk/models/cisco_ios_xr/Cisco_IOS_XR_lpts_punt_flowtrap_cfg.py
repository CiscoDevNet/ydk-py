""" Cisco_IOS_XR_lpts_punt_flowtrap_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-punt\-flowtrap package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-lpts\-lib\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class LptsPuntFlowtrapProtoIdEnum(Enum):
    """
    LptsPuntFlowtrapProtoIdEnum

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

    arp = 1

    icmp = 2

    dhcp = 3

    pppoe = 4

    ppp = 5

    igmp = 6

    ipv4 = 7

    l2tp = 8

    unclassified = 9

    ospf = 10

    bgp = 11

    default = 12


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_punt_flowtrap_cfg as meta
        return meta._meta_table['LptsPuntFlowtrapProtoIdEnum']



