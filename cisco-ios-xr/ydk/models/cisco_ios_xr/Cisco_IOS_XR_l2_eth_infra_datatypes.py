""" Cisco_IOS_XR_l2_eth_infra_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EthertypeMatchEnum(Enum):
    """
    EthertypeMatchEnum

    Ethertype match

    .. data:: ppp_over_ethernet = 34915

    	PPP over Ethernet

    """

    ppp_over_ethernet = 34915


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['EthertypeMatchEnum']


class MatchEnum(Enum):
    """
    MatchEnum

    Match

    .. data:: match_default = 1

    	All otherwise unmatched packets

    .. data:: match_untagged = 2

    	Untagged packets

    .. data:: match_dot1q = 3

    	Match Dot1Q tags

    .. data:: match_dot1ad = 4

    	Match Dot1ad tags

    .. data:: match_dot1q_priority = 5

    	Match Dot1Q priority-tagged packets

    .. data:: match_dot1ad_priority = 6

    	Match Dot1ad priority-tagged packets

    """

    match_default = 1

    match_untagged = 2

    match_dot1q = 3

    match_dot1ad = 4

    match_dot1q_priority = 5

    match_dot1ad_priority = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['MatchEnum']


class RewriteEnum(Enum):
    """
    RewriteEnum

    Rewrite

    .. data:: pop1 = 1

    	Pop 1 tag

    .. data:: pop2 = 2

    	Pop 2 tags

    .. data:: push1 = 3

    	Push 1 tag

    .. data:: push2 = 4

    	Push 2 tags

    .. data:: translate1to1 = 5

    	Translate 1-to-1

    .. data:: translate1to2 = 6

    	Translate 1-to-2

    .. data:: translate2to1 = 7

    	Translate 2-to-1

    .. data:: translate2to2 = 8

    	Translate 2-to-2

    """

    pop1 = 1

    pop2 = 2

    push1 = 3

    push2 = 4

    translate1to1 = 5

    translate1to2 = 6

    translate2to1 = 7

    translate2to2 = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['RewriteEnum']


class VlanEnum(Enum):
    """
    VlanEnum

    Vlan

    .. data:: vlan_type_dot1ad = 1

    	An 802.1ad VLAN

    .. data:: vlan_type_dot1q = 2

    	An 802.1q VLAN

    """

    vlan_type_dot1ad = 1

    vlan_type_dot1q = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['VlanEnum']


class VlanTagOrAnyEnum(Enum):
    """
    VlanTagOrAnyEnum

    Vlan tag or any

    .. data:: any = 4096

    	Match any VLAN tag value

    """

    any = 4096


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['VlanTagOrAnyEnum']


class VlanTagOrCvpEnum(Enum):
    """
    VlanTagOrCvpEnum

    Vlan tag or cvp

    .. data:: native_with_cvlan_preservation = 65534

    	This is the Native VLAN and C-VLAN

    	preservation is enabled

    """

    native_with_cvlan_preservation = 65534


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['VlanTagOrCvpEnum']


class VlanTagOrNativeEnum(Enum):
    """
    VlanTagOrNativeEnum

    Vlan tag or native

    .. data:: native = 65535

    	This is the Native VLAN

    .. data:: native_with_cvlan_preservation = 65534

    	This is the Native VLAN and C-VLAN

    	preservation is enabled

    """

    native = 65535

    native_with_cvlan_preservation = 65534


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['VlanTagOrNativeEnum']


class VlanTagOrNullEnum(Enum):
    """
    VlanTagOrNullEnum

    Vlan tag or null

    .. data:: any = 0

    	Match any inner VLAN tag value

    """

    any = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['VlanTagOrNullEnum']



