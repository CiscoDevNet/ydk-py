""" Cisco_IOS_XR_ethernet_cfm_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-cfm package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-l2\-eth\-infra\-cfg,
  Cisco\-IOS\-XR\-snmp\-agent\-cfg,
  Cisco\-IOS\-XR\-infra\-sla\-cfg
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CfmLmCountersCfgEnum(Enum):
    """
    CfmLmCountersCfgEnum

    Cfm lm counters cfg

    .. data:: aggregate = 1

    	Aggregate Counters

    .. data:: list = 2

    	List of per-CoS counters

    .. data:: range = 3

    	Range of per-CoS counters

    """

    aggregate = 1

    list = 2

    range = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmLmCountersCfgEnum']


class CfmMdidFormatEnum(Enum):
    """
    CfmMdidFormatEnum

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

    null = 1

    dns_like = 2

    mac_address = 3

    string = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmMdidFormatEnum']


class CfmMipPolicyEnum(Enum):
    """
    CfmMipPolicyEnum

    Cfm mip policy

    .. data:: all = 2

    	Create MIPs on all ports in the Bridge Domain

    	or Cross-connect

    .. data:: lower_mep_only = 3

    	Create MIPs on ports which have a MEP at a

    	lower level

    """

    all = 2

    lower_mep_only = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmMipPolicyEnum']


class CfmServiceEnum(Enum):
    """
    CfmServiceEnum

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

    .. data:: down_meps = 4

    	Down MEPs - no MIPs permitted

    """

    bridge_domain = 1

    p2p_cross_connect = 2

    mp2mp_cross_connect = 3

    down_meps = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmServiceEnum']


class CfmShortMaNameFormatEnum(Enum):
    """
    CfmShortMaNameFormatEnum

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

    vlan_id = 1

    string = 2

    number = 3

    vpn_id = 4

    icc_based = 32


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmShortMaNameFormatEnum']



