""" Cisco_IOS_XR_clns_isis_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class IsisAddressFamily_Enum(Enum):
    """
    IsisAddressFamily_Enum

    Isis address family

    """

    """

    IPv4

    """
    IPV4 = 0

    """

    IPv6

    """
    IPV6 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_datatypes as meta
        return meta._meta_table['IsisAddressFamily_Enum']


class IsisInternalLevel_Enum(Enum):
    """
    IsisInternalLevel_Enum

    Isis internal level

    """

    """

    Level not set

    """
    NOT_SET = 0

    """

    Level1

    """
    LEVEL1 = 1

    """

    Level2

    """
    LEVEL2 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_datatypes as meta
        return meta._meta_table['IsisInternalLevel_Enum']


class IsisSubAddressFamily_Enum(Enum):
    """
    IsisSubAddressFamily_Enum

    Isis sub address family

    """

    """

    Unicast

    """
    UNICAST = 0

    """

    Multicast

    """
    MULTICAST = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_datatypes as meta
        return meta._meta_table['IsisSubAddressFamily_Enum']



