""" Cisco_IOS_XR_ipv4_io_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-io package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class Ipv4DefaultPingEnum(Enum):
    """
    Ipv4DefaultPingEnum

    Ipv4 default ping

    .. data:: DISABLED = 0

    	Default route is not allowed to match when

    	checking source address

    .. data:: ENABLED = 1

    	Allow default route to match when checking

    	source address

    """

    DISABLED = 0

    ENABLED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_io_cfg as meta
        return meta._meta_table['Ipv4DefaultPingEnum']


class Ipv4InterfaceQppbEnum(Enum):
    """
    Ipv4InterfaceQppbEnum

    Ipv4 interface qppb

    .. data:: IP_PRECEDENCE = 1

    	Enable IP precedence based QPPB

    .. data:: QOS_GROUP = 2

    	Enable QoS-group based QPPB

    .. data:: BOTH = 3

    	Enable both IP precedence and QoS-group based

    	QPPB

    """

    IP_PRECEDENCE = 1

    QOS_GROUP = 2

    BOTH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_io_cfg as meta
        return meta._meta_table['Ipv4InterfaceQppbEnum']


class Ipv4ReachableEnum(Enum):
    """
    Ipv4ReachableEnum

    Ipv4 reachable

    .. data:: ANY = 0

    	Source is reachable via any interface

    .. data:: RECEIVED = 1

    	Source is reachable via interface on which

    	packet was received

    """

    ANY = 0

    RECEIVED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_io_cfg as meta
        return meta._meta_table['Ipv4ReachableEnum']


class Ipv4SelfPingEnum(Enum):
    """
    Ipv4SelfPingEnum

    Ipv4 self ping

    .. data:: DISABLED = 0

    	Doesn't allow router to ping itself

    .. data:: ENABLED = 1

    	Allow router to ping itself

    """

    DISABLED = 0

    ENABLED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_io_cfg as meta
        return meta._meta_table['Ipv4SelfPingEnum']



