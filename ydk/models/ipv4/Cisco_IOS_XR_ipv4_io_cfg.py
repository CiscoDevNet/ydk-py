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



class Ipv4DefaultPing_Enum(Enum):
    """
    Ipv4DefaultPing_Enum

    Ipv4 default ping

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
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_io_cfg as meta
        return meta._meta_table['Ipv4DefaultPing_Enum']


class Ipv4InterfaceQppb_Enum(Enum):
    """
    Ipv4InterfaceQppb_Enum

    Ipv4 interface qppb

    """

    """

    Enable IP precedence based QPPB

    """
    IP_PRECEDENCE = 1

    """

    Enable QoS\-group based QPPB

    """
    QOS_GROUP = 2

    """

    Enable both IP precedence and QoS\-group based
    QPPB

    """
    BOTH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_io_cfg as meta
        return meta._meta_table['Ipv4InterfaceQppb_Enum']


class Ipv4Reachable_Enum(Enum):
    """
    Ipv4Reachable_Enum

    Ipv4 reachable

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
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_io_cfg as meta
        return meta._meta_table['Ipv4Reachable_Enum']


class Ipv4SelfPing_Enum(Enum):
    """
    Ipv4SelfPing_Enum

    Ipv4 self ping

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
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_io_cfg as meta
        return meta._meta_table['Ipv4SelfPing_Enum']



