""" Cisco_IOS_XR_ipv4_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-ma package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-ipv4\-io\-oper
module with state data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class Ipv4MaOperLineState_Enum(Enum):
    """
    Ipv4MaOperLineState_Enum

    Interface line states

    """

    """

    Interface state is unknown

    """
    UNKNOWN = 0

    """

    Interface has been shutdown

    """
    SHUTDOWN = 1

    """

    Interface state is down

    """
    DOWN = 2

    """

    Interface state is up

    """
    UP = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_ma_oper as meta
        return meta._meta_table['Ipv4MaOperLineState_Enum']


class RpfMode_Enum(Enum):
    """
    RpfMode_Enum

    Interface line states

    """

    """

    Strict RPF

    """
    STRICT = 0

    """

    Loose RPF

    """
    LOOSE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_ma_oper as meta
        return meta._meta_table['RpfMode_Enum']



