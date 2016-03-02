""" Cisco_IOS_XR_tty_management_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-management package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-tty\-server\-oper
module with state data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class TransportService_Enum(Enum):
    """
    TransportService_Enum

    Transport service protocol

    """

    """

    Unknown service

    """
    UNKNOWN = 0

    """

    Telnet

    """
    TELNET = 1

    """

    Remote login

    """
    RLOGIN = 2

    """

    SSH

    """
    SSH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_management_oper as meta
        return meta._meta_table['TransportService_Enum']



class HostAfIdBase_Identity(object):
    """
    Base identity for Host\-af\-id
    
    

    """

    _prefix = 'Cisco-IOS-XR-tty-management-oper'
    _revision = '2015-01-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_management_oper as meta
        return meta._meta_table['HostAfIdBase_Identity']['meta_info']


class Ipv4_Identity(HostAfIdBase_Identity):
    """
    IPv4 family
    
    

    """

    _prefix = 'Cisco-IOS-XR-tty-management-oper'
    _revision = '2015-01-07'

    def __init__(self):
        HostAfIdBase_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_management_oper as meta
        return meta._meta_table['Ipv4_Identity']['meta_info']


class Ipv6_Identity(HostAfIdBase_Identity):
    """
    IPv6 family
    
    

    """

    _prefix = 'Cisco-IOS-XR-tty-management-oper'
    _revision = '2015-01-07'

    def __init__(self):
        HostAfIdBase_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_management_oper as meta
        return meta._meta_table['Ipv6_Identity']['meta_info']


