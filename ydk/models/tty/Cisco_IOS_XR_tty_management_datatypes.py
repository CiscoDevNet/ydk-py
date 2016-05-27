""" Cisco_IOS_XR_tty_management_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class TtyEscapeCharEnum(Enum):
    """
    TtyEscapeCharEnum

    Tty escape char

    .. data:: BREAK = 257

    	Cause escape on BREAK

    .. data:: DEFAULT = 30

    	Use default escape character

    .. data:: NONE = 256

    	Disable escape entirely

    """

    BREAK = 257

    DEFAULT = 30

    NONE = 256


    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyEscapeCharEnum']


class TtyPagerEnum(Enum):
    """
    TtyPagerEnum

    Tty pager

    .. data:: MORE = 1

    	More paging Utility

    .. data:: LESS = 2

    	Less paging Utility

    .. data:: NONE = 3

    	No Paging Utility

    """

    MORE = 1

    LESS = 2

    NONE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyPagerEnum']


class TtySessionTimeoutDirectionEnum(Enum):
    """
    TtySessionTimeoutDirectionEnum

    Tty session timeout direction

    .. data:: IN = 1

    	Input traffic

    .. data:: IN_OUT = 3

    	In & Output traffic

    """

    IN = 1

    IN_OUT = 3


    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtySessionTimeoutDirectionEnum']


class TtyTransportProtocolEnum(Enum):
    """
    TtyTransportProtocolEnum

    Tty transport protocol

    .. data:: NONE = 0

    	No protocols

    .. data:: TELNET = 1

    	TCP/IP Telnet protocol

    .. data:: SSH = 3

    	Unix ssh protocol

    """

    NONE = 0

    TELNET = 1

    SSH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyTransportProtocolEnum']


class TtyTransportProtocolSelectEnum(Enum):
    """
    TtyTransportProtocolSelectEnum

    Tty transport protocol select

    .. data:: NONE = 0

    	No protocols

    .. data:: ALL = 1

    	All protocols

    .. data:: SOME = 2

    	Some Protocol

    """

    NONE = 0

    ALL = 1

    SOME = 2


    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyTransportProtocolSelectEnum']



