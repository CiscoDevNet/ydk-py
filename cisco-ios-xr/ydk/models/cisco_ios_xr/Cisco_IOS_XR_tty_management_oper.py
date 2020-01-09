""" Cisco_IOS_XR_tty_management_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-management package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-tty\-server\-oper
module with state data.

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



class TransportService(Enum):
    """
    TransportService (Enum Class)

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

    unknown = Enum.YLeaf(0, "unknown")

    telnet = Enum.YLeaf(1, "telnet")

    rlogin = Enum.YLeaf(2, "rlogin")

    ssh = Enum.YLeaf(3, "ssh")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_oper as meta
        return meta._meta_table['TransportService']



class HostAfIdBase(Identity):
    """
    Base identity for Host\-af\-id
    
    

    """

    _prefix = 'Cisco-IOS-XR-tty-management-oper'
    _revision = '2017-05-01'

    def __init__(self, ns="http://cisco.com/ns/yang/Cisco-IOS-XR-tty-management-oper", pref="Cisco-IOS-XR-tty-management-oper", tag="Cisco-IOS-XR-tty-management-oper:Host-af-id-base"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(HostAfIdBase, self).__init__(ns, pref, tag)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_oper as meta
        return meta._meta_table['HostAfIdBase']['meta_info']


class Ipv4(HostAfIdBase):
    """
    IPv4 family
    
    

    """

    _prefix = 'Cisco-IOS-XR-tty-management-oper'
    _revision = '2017-05-01'

    def __init__(self, ns="http://cisco.com/ns/yang/Cisco-IOS-XR-tty-management-oper", pref="Cisco-IOS-XR-tty-management-oper", tag="Cisco-IOS-XR-tty-management-oper:ipv4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ipv4, self).__init__(ns, pref, tag)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_oper as meta
        return meta._meta_table['Ipv4']['meta_info']


class Ipv6(HostAfIdBase):
    """
    IPv6 family
    
    

    """

    _prefix = 'Cisco-IOS-XR-tty-management-oper'
    _revision = '2017-05-01'

    def __init__(self, ns="http://cisco.com/ns/yang/Cisco-IOS-XR-tty-management-oper", pref="Cisco-IOS-XR-tty-management-oper", tag="Cisco-IOS-XR-tty-management-oper:ipv6"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ipv6, self).__init__(ns, pref, tag)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_oper as meta
        return meta._meta_table['Ipv6']['meta_info']


