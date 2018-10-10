""" Cisco_IOS_XR_ethernet_cfm_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-cfm package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-l2\-eth\-infra\-cfg,
  Cisco\-IOS\-XR\-snmp\-agent\-cfg,
  Cisco\-IOS\-XR\-infra\-sla\-cfg
modules with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CfmLmCountersCfg(Enum):
    """
    CfmLmCountersCfg (Enum Class)

    Cfm lm counters cfg

    .. data:: aggregate = 1

    	Aggregate Counters

    .. data:: list = 2

    	List of per-CoS counters

    .. data:: range = 3

    	Range of per-CoS counters

    """

    aggregate = Enum.YLeaf(1, "aggregate")

    list = Enum.YLeaf(2, "list")

    range = Enum.YLeaf(3, "range")


class CfmMdidFormat(Enum):
    """
    CfmMdidFormat (Enum Class)

    Cfm mdid format

    .. data:: null = 1

    	Null MDID

    .. data:: dns_like = 2

    	DNS-like MDID

    .. data:: mac_address = 3

    	MDID Comprising MAC Address and 16-bit integer

    .. data:: string = 4

    	String MDID

    """

    null = Enum.YLeaf(1, "null")

    dns_like = Enum.YLeaf(2, "dns-like")

    mac_address = Enum.YLeaf(3, "mac-address")

    string = Enum.YLeaf(4, "string")


class CfmMipPolicy(Enum):
    """
    CfmMipPolicy (Enum Class)

    Cfm mip policy

    .. data:: all = 2

    	Create MIPs on all ports in the Bridge Domain

    	or Cross-connect

    .. data:: lower_mep_only = 3

    	Create MIPs on ports which have a MEP at a

    	lower level

    """

    all = Enum.YLeaf(2, "all")

    lower_mep_only = Enum.YLeaf(3, "lower-mep-only")


class CfmService(Enum):
    """
    CfmService (Enum Class)

    Cfm service

    .. data:: bridge_domain = 1

    	Use a Bridge Domain - all MEPs will be Up MEPs

    	and MIPs are permitted

    .. data:: p2p_cross_connect = 2

    	Use a P2P Cross Connect - all MEPs will be Up

    	MEPs and MIPs are permitted

    .. data:: mp2mp_cross_connect = 3

    	Use a MP2MP Cross Connect - all MEPs will be Up

    	MEPs and MIPs are permitted

    .. data:: vlan_aware_flexible_cross_connect = 4

    	Use a VLAN-aware Flexible Cross Connect - all

    	MEPs will be Up MEPs and MIPs are permitted

    .. data:: vlan_unaware_flexible_cross_connect = 5

    	Use a VLAN-unaware Flexible Cross Connect - all

    	MEPs will be Up MEPs and MIPs are permitted

    .. data:: down_meps = 6

    	Down MEPs - no MIPs permitted

    """

    bridge_domain = Enum.YLeaf(1, "bridge-domain")

    p2p_cross_connect = Enum.YLeaf(2, "p2p-cross-connect")

    mp2mp_cross_connect = Enum.YLeaf(3, "mp2mp-cross-connect")

    vlan_aware_flexible_cross_connect = Enum.YLeaf(4, "vlan-aware-flexible-cross-connect")

    vlan_unaware_flexible_cross_connect = Enum.YLeaf(5, "vlan-unaware-flexible-cross-connect")

    down_meps = Enum.YLeaf(6, "down-meps")


class CfmShortMaNameFormat(Enum):
    """
    CfmShortMaNameFormat (Enum Class)

    Cfm short ma name format

    .. data:: vlan_id = 1

    	VLAN ID

    .. data:: string = 2

    	String Short MA Name

    .. data:: number = 3

    	Numeric Short MA Name

    .. data:: vpn_id = 4

    	RFC 2685 VPN ID

    .. data:: icc_based = 32

    	ICC-based format

    """

    vlan_id = Enum.YLeaf(1, "vlan-id")

    string = Enum.YLeaf(2, "string")

    number = Enum.YLeaf(3, "number")

    vpn_id = Enum.YLeaf(4, "vpn-id")

    icc_based = Enum.YLeaf(32, "icc-based")



