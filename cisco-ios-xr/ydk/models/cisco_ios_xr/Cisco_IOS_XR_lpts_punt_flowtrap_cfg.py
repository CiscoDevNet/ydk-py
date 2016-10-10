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

    .. data:: DEFAULT = 0

    	All protocols

    .. data:: ARP = 1

    	ARP

    .. data:: ICMP = 2

    	Internet Control Message Protocol

    .. data:: DHCP = 3

    	Dynamic Host Configuration Protocol

    .. data:: PPPOE = 4

    	PPP over Ethernet

    .. data:: PPP = 5

    	Point to point Protocol

    .. data:: IGMP = 6

    	Internet Gateway Message Protocol

    .. data:: IPV4 = 7

    	IPv4

    .. data:: L2TP = 8

    	Layer2 Tunneling Protocol

    .. data:: UNCLASSIFIED = 9

    	Unclassified Source

    """

    DEFAULT = 0

    ARP = 1

    ICMP = 2

    DHCP = 3

    PPPOE = 4

    PPP = 5

    IGMP = 6

    IPV4 = 7

    L2TP = 8

    UNCLASSIFIED = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_punt_flowtrap_cfg as meta
        return meta._meta_table['LptsPuntFlowtrapProtoIdEnum']



