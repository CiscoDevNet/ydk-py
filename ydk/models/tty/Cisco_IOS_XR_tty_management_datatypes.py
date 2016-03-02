""" Cisco_IOS_XR_tty_management_datatypes 

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



class TtyEscapeChar_Enum(Enum):
    """
    TtyEscapeChar_Enum

    Tty escape char

    """

    """

    Cause escape on BREAK

    """
    BREAK = 257

    """

    Use default escape character

    """
    DEFAULT = 30

    """

    Disable escape entirely

    """
    NONE = 256


    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyEscapeChar_Enum']


class TtyPager_Enum(Enum):
    """
    TtyPager_Enum

    Tty pager

    """

    """

    More paging Utility

    """
    MORE = 1

    """

    Less paging Utility

    """
    LESS = 2

    """

    No Paging Utility

    """
    NONE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyPager_Enum']


class TtySessionTimeoutDirection_Enum(Enum):
    """
    TtySessionTimeoutDirection_Enum

    Tty session timeout direction

    """

    """

    Input traffic

    """
    IN = 1

    """

    In & Output traffic

    """
    IN_OUT = 3


    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtySessionTimeoutDirection_Enum']


class TtyTransportProtocolSelect_Enum(Enum):
    """
    TtyTransportProtocolSelect_Enum

    Tty transport protocol select

    """

    """

    No protocols

    """
    NONE = 0

    """

    All protocols

    """
    ALL = 1

    """

    Some Protocol

    """
    SOME = 2


    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyTransportProtocolSelect_Enum']


class TtyTransportProtocol_Enum(Enum):
    """
    TtyTransportProtocol_Enum

    Tty transport protocol

    """

    """

    No protocols

    """
    NONE = 0

    """

    TCP/IP Telnet protocol

    """
    TELNET = 1

    """

    Unix ssh protocol

    """
    SSH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyTransportProtocol_Enum']



