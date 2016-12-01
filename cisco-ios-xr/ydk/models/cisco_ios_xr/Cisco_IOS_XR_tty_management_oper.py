""" Cisco_IOS_XR_tty_management_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-management package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-tty\-server\-oper
module with state data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class TransportServiceEnum(Enum):
    """
    TransportServiceEnum

    Transport service protocol

    .. data:: unknown = 0

    	Unknown service

    .. data:: telnet = 1

    	Telnet

    .. data:: rlogin = 2

    	Remote login

    .. data:: ssh = 3

    	SSH

    """

    unknown = 0

    telnet = 1

    rlogin = 2

    ssh = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_oper as meta
        return meta._meta_table['TransportServiceEnum']



class HostAfIdBaseIdentity(object):
    """
    Base identity for Host\-af\-id
    
    

    """

    _prefix = 'Cisco-IOS-XR-tty-management-oper'
    _revision = '2015-01-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_oper as meta
        return meta._meta_table['HostAfIdBaseIdentity']['meta_info']


class Ipv4Identity(HostAfIdBaseIdentity):
    """
    IPv4 family
    
    

    """

    _prefix = 'Cisco-IOS-XR-tty-management-oper'
    _revision = '2015-01-07'

    def __init__(self):
        HostAfIdBaseIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_oper as meta
        return meta._meta_table['Ipv4Identity']['meta_info']


class Ipv6Identity(HostAfIdBaseIdentity):
    """
    IPv6 family
    
    

    """

    _prefix = 'Cisco-IOS-XR-tty-management-oper'
    _revision = '2015-01-07'

    def __init__(self):
        HostAfIdBaseIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_oper as meta
        return meta._meta_table['Ipv6Identity']['meta_info']


