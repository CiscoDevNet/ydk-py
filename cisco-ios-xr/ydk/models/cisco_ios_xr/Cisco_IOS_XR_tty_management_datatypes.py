""" Cisco_IOS_XR_tty_management_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class TtyEscapeCharEnum(Enum):
    """
    TtyEscapeCharEnum

    Tty escape char

    .. data:: break_ = 257

    	Cause escape on BREAK

    .. data:: default = 30

    	Use default escape character

    .. data:: none = 256

    	Disable escape entirely

    """

    break_ = 257

    default = 30

    none = 256


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyEscapeCharEnum']


class TtyPagerEnum(Enum):
    """
    TtyPagerEnum

    Tty pager

    .. data:: more = 1

    	More paging Utility

    .. data:: less = 2

    	Less paging Utility

    .. data:: none = 3

    	No Paging Utility

    """

    more = 1

    less = 2

    none = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyPagerEnum']


class TtySessionTimeoutDirectionEnum(Enum):
    """
    TtySessionTimeoutDirectionEnum

    Tty session timeout direction

    .. data:: in_ = 1

    	Input traffic

    .. data:: in_out = 3

    	In & Output traffic

    """

    in_ = 1

    in_out = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtySessionTimeoutDirectionEnum']


class TtyTransportProtocolEnum(Enum):
    """
    TtyTransportProtocolEnum

    Tty transport protocol

    .. data:: none = 0

    	No protocols

    .. data:: telnet = 1

    	TCP/IP Telnet protocol

    .. data:: ssh = 3

    	Unix ssh protocol

    """

    none = 0

    telnet = 1

    ssh = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyTransportProtocolEnum']


class TtyTransportProtocolSelectEnum(Enum):
    """
    TtyTransportProtocolSelectEnum

    Tty transport protocol select

    .. data:: none = 0

    	No protocols

    .. data:: all = 1

    	All protocols

    .. data:: some = 2

    	Some Protocol

    """

    none = 0

    all = 1

    some = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyTransportProtocolSelectEnum']



