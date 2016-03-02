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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class Ipv6DefaultPing_Enum(Enum):
    """
    Ipv6DefaultPing_Enum

    Ipv6 default ping

    """

    """

    Default route is not allowed to match when
    checking source address

    """
    DISABLED = 0

    """

    Allow default route to match when checking
    source address

    """
    ENABLED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_ma_cfg as meta
        return meta._meta_table['Ipv6DefaultPing_Enum']


class Ipv6Qppb_Enum(Enum):
    """
    Ipv6Qppb_Enum

    Ipv6 qppb

    """

    """

    No QPPB configuration

    """
    NONE = 0

    """

    Enable ip\-precedence based QPPB

    """
    IP_PRECEDENCE = 1

    """

    Enable qos\-group based QPPB

    """
    QOS_GROUP = 2

    """

    Enable both ip\-precedence and qos\-group based
    QPPB

    """
    BOTH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_ma_cfg as meta
        return meta._meta_table['Ipv6Qppb_Enum']


class Ipv6Reachable_Enum(Enum):
    """
    Ipv6Reachable_Enum

    Ipv6 reachable

    """

    """

    Source is reachable via any interface

    """
    ANY = 0

    """

    Source is reachable via interface on which
    packet was received

    """
    RECEIVED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_ma_cfg as meta
        return meta._meta_table['Ipv6Reachable_Enum']


class Ipv6SelfPing_Enum(Enum):
    """
    Ipv6SelfPing_Enum

    Ipv6 self ping

    """

    """

    Doesn't allow router to ping itself

    """
    DISABLED = 0

    """

    Allow router to ping itself

    """
    ENABLED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_ma_cfg as meta
        return meta._meta_table['Ipv6SelfPing_Enum']



