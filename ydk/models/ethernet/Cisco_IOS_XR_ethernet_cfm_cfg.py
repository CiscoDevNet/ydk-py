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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CfmLmCountersCfg_Enum(Enum):
    """
    CfmLmCountersCfg_Enum

    Cfm lm counters cfg

    """

    """

    Aggregate Counters

    """
    AGGREGATE = 1

    """

    List of per\-CoS counters

    """
    LIST = 2

    """

    Range of per\-CoS counters

    """
    RANGE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmLmCountersCfg_Enum']


class CfmMdidFormat_Enum(Enum):
    """
    CfmMdidFormat_Enum

    Cfm mdid format

    """

    """

    Null MDID

    """
    NULL = 1

    """

    DNS\-like MDID

    """
    DNS_LIKE = 2

    """

    MDID Comprising MAC Address and 16\-bit integer

    """
    MAC_ADDRESS = 3

    """

    String MDID

    """
    STRING = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmMdidFormat_Enum']


class CfmMipPolicy_Enum(Enum):
    """
    CfmMipPolicy_Enum

    Cfm mip policy

    """

    """

    Create MIPs on all ports in the Bridge Domain
    or Cross\-connect

    """
    ALL = 2

    """

    Create MIPs on ports which have a MEP at a
    lower level

    """
    LOWER_MEP_ONLY = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmMipPolicy_Enum']


class CfmService_Enum(Enum):
    """
    CfmService_Enum

    Cfm service

    """

    """

    Use a Bridge Domain \- all MEPs will be Up MEPs
    and MIPs are permitted

    """
    BRIDGE_DOMAIN = 1

    """

    Use a P2P Cross Connect \- all MEPs will be Up
    MEPs and MIPs are permitted

    """
    P2P_CROSS_CONNECT = 2

    """

    Use a MP2MP Cross Connect \- all MEPs will be Up
    MEPs and MIPs are permitted

    """
    MP2MP_CROSS_CONNECT = 3

    """

    Down MEPs \- no MIPs permitted

    """
    DOWN_MEPS = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmService_Enum']


class CfmShortMaNameFormat_Enum(Enum):
    """
    CfmShortMaNameFormat_Enum

    Cfm short ma name format

    """

    """

    VLAN ID

    """
    VLAN_ID = 1

    """

    String Short MA Name

    """
    STRING = 2

    """

    Numeric Short MA Name

    """
    NUMBER = 3

    """

    RFC 2685 VPN ID

    """
    VPN_ID = 4

    """

    ICC\-based format

    """
    ICC_BASED = 32


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_cfg as meta
        return meta._meta_table['CfmShortMaNameFormat_Enum']



