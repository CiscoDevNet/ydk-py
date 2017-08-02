""" Cisco_IOS_XR_tunnel_nve_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-nve package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class HostReachProtocol(Enum):
    """
    HostReachProtocol

    Host reach protocol

    .. data:: bgp = 1

    	Use BGP EVPN for VxLAN tunnel endpoint

    	reachability

    """

    bgp = Enum.YLeaf(1, "bgp")


class LoadBalanceEnum(Enum):
    """
    LoadBalanceEnum

    Load balance enum

    .. data:: per_evi = 1

    	Per evi load balance mode

    """

    per_evi = Enum.YLeaf(1, "per-evi")


class OverlayEncapEnum(Enum):
    """
    OverlayEncapEnum

    Overlay encap enum

    .. data:: vx_lan_encapsulation = 0

    	VxLAN Encapsulation

    .. data:: soft_gre_encapsulation = 1

    	Soft GRE Encapsulation

    """

    vx_lan_encapsulation = Enum.YLeaf(0, "vx-lan-encapsulation")

    soft_gre_encapsulation = Enum.YLeaf(1, "soft-gre-encapsulation")


class UnknownUnicastFloodingEnum(Enum):
    """
    UnknownUnicastFloodingEnum

    Unknown unicast flooding enum

    .. data:: suppress_uuf = 1

    	Suppress unknown unicast flooding

    """

    suppress_uuf = Enum.YLeaf(1, "suppress-uuf")


class VxlanUdpPortEnum(Enum):
    """
    VxlanUdpPortEnum

    Vxlan udp port enum

    .. data:: ietf_udp_port = 4789

    	IETF defined UDP port for VxLAN

    .. data:: ivx_lan_udp_port = 48879

    	UDP port for iVxLAN

    """

    ietf_udp_port = Enum.YLeaf(4789, "ietf-udp-port")

    ivx_lan_udp_port = Enum.YLeaf(48879, "ivx-lan-udp-port")



