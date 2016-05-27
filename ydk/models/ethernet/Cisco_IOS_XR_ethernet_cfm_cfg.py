""" Cisco_IOS_XR_ethernet_cfm_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-cfm package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-l2\-eth\-infra\-cfg,
  Cisco\-IOS\-XR\-snmp\-agent\-cfg,
  Cisco\-IOS\-XR\-infra\-sla\-cfg,
  Cisco\-IOS\-XR\-icpe\-infra\-cfg
modules with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CfmLmCountersCfgEnum(Enum):
    """
    CfmLmCountersCfgEnum

    Cfm lm counters cfg

    .. data:: AGGREGATE = 1

    	Aggregate Counters

    .. data:: LIST = 2

    	List of per-CoS counters

    .. data:: RANGE = 3

    	Range of per-CoS counters

    """

    AGGREGATE = 1

    LIST = 2

    RANGE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmLmCountersCfgEnum']


class CfmMdidFormatEnum(Enum):
    """
    CfmMdidFormatEnum

    Cfm mdid format

    .. data:: NULL = 1

    	Null MDID

    .. data:: DNS_LIKE = 2

    	DNS-like MDID

    .. data:: MAC_ADDRESS = 3

    	MDID Comprising MAC Address and 16-bit integer

    .. data:: STRING = 4

    	String MDID

    """

    NULL = 1

    DNS_LIKE = 2

    MAC_ADDRESS = 3

    STRING = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmMdidFormatEnum']


class CfmMipPolicyEnum(Enum):
    """
    CfmMipPolicyEnum

    Cfm mip policy

    .. data:: ALL = 2

    	Create MIPs on all ports in the Bridge Domain

    	or Cross-connect

    .. data:: LOWER_MEP_ONLY = 3

    	Create MIPs on ports which have a MEP at a

    	lower level

    """

    ALL = 2

    LOWER_MEP_ONLY = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmMipPolicyEnum']


class CfmServiceEnum(Enum):
    """
    CfmServiceEnum

    Cfm service

    .. data:: BRIDGE_DOMAIN = 1

    	Use a Bridge Domain - all MEPs will be Up MEPs

    	and MIPs are permitted

    .. data:: P2P_CROSS_CONNECT = 2

    	Use a P2P Cross Connect - all MEPs will be Up

    	MEPs and MIPs are permitted

    .. data:: MP2MP_CROSS_CONNECT = 3

    	Use a MP2MP Cross Connect - all MEPs will be Up

    	MEPs and MIPs are permitted

    .. data:: DOWN_MEPS = 4

    	Down MEPs - no MIPs permitted

    """

    BRIDGE_DOMAIN = 1

    P2P_CROSS_CONNECT = 2

    MP2MP_CROSS_CONNECT = 3

    DOWN_MEPS = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmServiceEnum']


class CfmShortMaNameFormatEnum(Enum):
    """
    CfmShortMaNameFormatEnum

    Cfm short ma name format

    .. data:: VLAN_ID = 1

    	VLAN ID

    .. data:: STRING = 2

    	String Short MA Name

    .. data:: NUMBER = 3

    	Numeric Short MA Name

    .. data:: VPN_ID = 4

    	RFC 2685 VPN ID

    .. data:: ICC_BASED = 32

    	ICC-based format

    """

    VLAN_ID = 1

    STRING = 2

    NUMBER = 3

    VPN_ID = 4

    ICC_BASED = 32


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmShortMaNameFormatEnum']



