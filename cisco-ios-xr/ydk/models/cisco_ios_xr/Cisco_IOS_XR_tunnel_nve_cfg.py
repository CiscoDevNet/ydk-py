""" Cisco_IOS_XR_tunnel_nve_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-nve package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class HostReachProtocolEnum(Enum):
    """
    HostReachProtocolEnum

    Host reach protocol

    .. data:: bgp = 1

    	Use BGP EVPN for VxLAN tunnel endpoint

    	reachability

    """

    bgp = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_nve_cfg as meta
        return meta._meta_table['HostReachProtocolEnum']


class OverlayEncapEnumEnum(Enum):
    """
    OverlayEncapEnumEnum

    Overlay encap enum

    .. data:: vx_lan_encapsulation = 0

    	VxLAN Encapsulation

    .. data:: soft_gre_encapsulation = 1

    	Soft GRE Encapsulation

    """

    vx_lan_encapsulation = 0

    soft_gre_encapsulation = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_nve_cfg as meta
        return meta._meta_table['OverlayEncapEnumEnum']


class VxlanUdpPortEnumEnum(Enum):
    """
    VxlanUdpPortEnumEnum

    Vxlan udp port enum

    .. data:: ietf_udp_port = 4789

    	IETF defined UDP port for VxLAN

    .. data:: ivx_lan_udp_port = 48879

    	UDP port for iVxLAN

    """

    ietf_udp_port = 4789

    ivx_lan_udp_port = 48879


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_nve_cfg as meta
        return meta._meta_table['VxlanUdpPortEnumEnum']



