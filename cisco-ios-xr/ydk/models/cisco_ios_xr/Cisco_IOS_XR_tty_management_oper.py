""" Cisco_IOS_XR_tty_management_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-management package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-tty\-server\-oper
module with state data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class TransportService(Enum):
    """
    TransportService

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



class HostAfIdBase(Identity):
    """
    Base identity for Host\-af\-id
    
    

    """

    _prefix = 'Cisco-IOS-XR-tty-management-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(HostAfIdBase, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XR-tty-management-oper", "Cisco-IOS-XR-tty-management-oper", "Cisco-IOS-XR-tty-management-oper:Host-af-id-base")


class Ipv4(Identity):
    """
    IPv4 family
    
    

    """

    _prefix = 'Cisco-IOS-XR-tty-management-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(Ipv4, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XR-tty-management-oper", "Cisco-IOS-XR-tty-management-oper", "Cisco-IOS-XR-tty-management-oper:ipv4")


class Ipv6(Identity):
    """
    IPv6 family
    
    

    """

    _prefix = 'Cisco-IOS-XR-tty-management-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(Ipv6, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XR-tty-management-oper", "Cisco-IOS-XR-tty-management-oper", "Cisco-IOS-XR-tty-management-oper:ipv6")


