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

    .. data:: PPP_OVER_ETHERNET = 34915

    	PPP over Ethernet

    """

    PPP_OVER_ETHERNET = 34915


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['EthertypeMatchEnum']


class MatchEnum(Enum):
    """
    MatchEnum

    Match

    .. data:: MATCH_DEFAULT = 1

    	All otherwise unmatched packets

    .. data:: MATCH_UNTAGGED = 2

    	Untagged packets

    .. data:: MATCH_DOT1Q = 3

    	Match Dot1Q tags

    .. data:: MATCH_DOT1AD = 4

    	Match Dot1ad tags

    .. data:: MATCH_DOT1Q_PRIORITY = 5

    	Match Dot1Q priority-tagged packets

    .. data:: MATCH_DOT1AD_PRIORITY = 6

    	Match Dot1ad priority-tagged packets

    """

    MATCH_DEFAULT = 1

    MATCH_UNTAGGED = 2

    MATCH_DOT1Q = 3

    MATCH_DOT1AD = 4

    MATCH_DOT1Q_PRIORITY = 5

    MATCH_DOT1AD_PRIORITY = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['MatchEnum']


class RewriteEnum(Enum):
    """
    RewriteEnum

    Rewrite

    .. data:: POP1 = 1

    	Pop 1 tag

    .. data:: POP2 = 2

    	Pop 2 tags

    .. data:: PUSH1 = 3

    	Push 1 tag

    .. data:: PUSH2 = 4

    	Push 2 tags

    .. data:: TRANSLATE1TO1 = 5

    	Translate 1-to-1

    .. data:: TRANSLATE1TO2 = 6

    	Translate 1-to-2

    .. data:: TRANSLATE2TO1 = 7

    	Translate 2-to-1

    .. data:: TRANSLATE2TO2 = 8

    	Translate 2-to-2

    """

    POP1 = 1

    POP2 = 2

    PUSH1 = 3

    PUSH2 = 4

    TRANSLATE1TO1 = 5

    TRANSLATE1TO2 = 6

    TRANSLATE2TO1 = 7

    TRANSLATE2TO2 = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['RewriteEnum']


class VlanEnum(Enum):
    """
    VlanEnum

    Vlan

    .. data:: VLAN_TYPE_DOT1AD = 1

    	An 802.1ad VLAN

    .. data:: VLAN_TYPE_DOT1Q = 2

    	An 802.1q VLAN

    """

    VLAN_TYPE_DOT1AD = 1

    VLAN_TYPE_DOT1Q = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['VlanEnum']


class VlanTagOrAnyEnum(Enum):
    """
    VlanTagOrAnyEnum

    Vlan tag or any

    .. data:: ANY = 4096

    	Match any VLAN tag value

    """

    ANY = 4096


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['VlanTagOrAnyEnum']


class VlanTagOrCvpEnum(Enum):
    """
    VlanTagOrCvpEnum

    Vlan tag or cvp

    .. data:: NATIVE_WITH_CVLAN_PRESERVATION = 65534

    	This is the Native VLAN and C-VLAN

    	preservation is enabled

    """

    NATIVE_WITH_CVLAN_PRESERVATION = 65534


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['VlanTagOrCvpEnum']


class VlanTagOrNativeEnum(Enum):
    """
    VlanTagOrNativeEnum

    Vlan tag or native

    .. data:: NATIVE = 65535

    	This is the Native VLAN

    .. data:: NATIVE_WITH_CVLAN_PRESERVATION = 65534

    	This is the Native VLAN and C-VLAN

    	preservation is enabled

    """

    NATIVE = 65535

    NATIVE_WITH_CVLAN_PRESERVATION = 65534


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['VlanTagOrNativeEnum']


class VlanTagOrNullEnum(Enum):
    """
    VlanTagOrNullEnum

    Vlan tag or null

    .. data:: ANY = 0

    	Match any inner VLAN tag value

    """

    ANY = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['VlanTagOrNullEnum']



