""" Cisco_IOS_XR_ipv6_ma_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-ma package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class Ipv6DefaultPingEnum(Enum):
    """
    Ipv6DefaultPingEnum

    Ipv6 default ping

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
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_ma_cfg as meta
        return meta._meta_table['Ipv6DefaultPingEnum']


class Ipv6QppbEnum(Enum):
    """
    Ipv6QppbEnum

    Ipv6 qppb

    .. data:: NONE = 0

    	No QPPB configuration

    .. data:: IP_PRECEDENCE = 1

    	Enable ip-precedence based QPPB

    .. data:: QOS_GROUP = 2

    	Enable qos-group based QPPB

    .. data:: BOTH = 3

    	Enable both ip-precedence and qos-group based

    	QPPB

    """

    NONE = 0

    IP_PRECEDENCE = 1

    QOS_GROUP = 2

    BOTH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_ma_cfg as meta
        return meta._meta_table['Ipv6QppbEnum']


class Ipv6ReachableEnum(Enum):
    """
    Ipv6ReachableEnum

    Ipv6 reachable

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
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_ma_cfg as meta
        return meta._meta_table['Ipv6ReachableEnum']


class Ipv6SelfPingEnum(Enum):
    """
    Ipv6SelfPingEnum

    Ipv6 self ping

    .. data:: DISABLED = 0

    	Doesn't allow router to ping itself

    .. data:: ENABLED = 1

    	Allow router to ping itself

    """

    DISABLED = 0

    ENABLED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_ma_cfg as meta
        return meta._meta_table['Ipv6SelfPingEnum']



