""" Cisco_IOS_XR_tty_management_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class TtyEscapeChar(Enum):
    """
    TtyEscapeChar (Enum Class)

    Tty escape char

    .. data:: break_ = 257

    	Cause escape on BREAK

    .. data:: default = 30

    	Use default escape character

    .. data:: none = 256

    	Disable escape entirely

    """

    break_ = Enum.YLeaf(257, "break")

    default = Enum.YLeaf(30, "default")

    none = Enum.YLeaf(256, "none")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyEscapeChar']


class TtyPager(Enum):
    """
    TtyPager (Enum Class)

    Tty pager

    .. data:: more = 1

    	More paging Utility

    .. data:: less = 2

    	Less paging Utility

    .. data:: none = 3

    	No Paging Utility

    """

    more = Enum.YLeaf(1, "more")

    less = Enum.YLeaf(2, "less")

    none = Enum.YLeaf(3, "none")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyPager']


class TtySessionTimeoutDirection(Enum):
    """
    TtySessionTimeoutDirection (Enum Class)

    Tty session timeout direction

    .. data:: in_ = 1

    	Input traffic

    .. data:: in_out = 3

    	In & Output traffic

    """

    in_ = Enum.YLeaf(1, "in")

    in_out = Enum.YLeaf(3, "in-out")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtySessionTimeoutDirection']


class TtyTransportProtocol(Enum):
    """
    TtyTransportProtocol (Enum Class)

    Tty transport protocol

    .. data:: none = 0

    	No protocols

    .. data:: telnet = 1

    	TCP/IP Telnet protocol

    .. data:: ssh = 3

    	Unix ssh protocol

    """

    none = Enum.YLeaf(0, "none")

    telnet = Enum.YLeaf(1, "telnet")

    ssh = Enum.YLeaf(3, "ssh")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyTransportProtocol']


class TtyTransportProtocolSelect(Enum):
    """
    TtyTransportProtocolSelect (Enum Class)

    Tty transport protocol select

    .. data:: none = 0

    	No protocols

    .. data:: all = 1

    	All protocols

    .. data:: some = 2

    	Some Protocol

    """

    none = Enum.YLeaf(0, "none")

    all = Enum.YLeaf(1, "all")

    some = Enum.YLeaf(2, "some")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_datatypes as meta
        return meta._meta_table['TtyTransportProtocolSelect']



