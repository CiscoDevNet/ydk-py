""" Cisco_IOS_XR_ipv4_io_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-io package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class Ipv4DefaultPingEnum(Enum):
    """
    Ipv4DefaultPingEnum

    Ipv4 default ping

    .. data:: disabled = 0

    	Default route is not allowed to match when

    	checking source address

    .. data:: enabled = 1

    	Allow default route to match when checking

    	source address

    """

    disabled = 0

    enabled = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_cfg as meta
        return meta._meta_table['Ipv4DefaultPingEnum']


class Ipv4InterfaceQppbEnum(Enum):
    """
    Ipv4InterfaceQppbEnum

    Ipv4 interface qppb

    .. data:: ip_precedence = 1

    	Enable IP precedence based QPPB

    .. data:: qos_group = 2

    	Enable QoS-group based QPPB

    .. data:: both = 3

    	Enable both IP precedence and QoS-group based

    	QPPB

    """

    ip_precedence = 1

    qos_group = 2

    both = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_cfg as meta
        return meta._meta_table['Ipv4InterfaceQppbEnum']


class Ipv4ReachableEnum(Enum):
    """
    Ipv4ReachableEnum

    Ipv4 reachable

    .. data:: any = 0

    	Source is reachable via any interface

    .. data:: received = 1

    	Source is reachable via interface on which

    	packet was received

    """

    any = 0

    received = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_cfg as meta
        return meta._meta_table['Ipv4ReachableEnum']


class Ipv4SelfPingEnum(Enum):
    """
    Ipv4SelfPingEnum

    Ipv4 self ping

    .. data:: disabled = 0

    	Doesn't allow router to ping itself

    .. data:: enabled = 1

    	Allow router to ping itself

    """

    disabled = 0

    enabled = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_cfg as meta
        return meta._meta_table['Ipv4SelfPingEnum']



