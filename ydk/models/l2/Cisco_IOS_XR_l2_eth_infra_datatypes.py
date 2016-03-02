""" Cisco_IOS_XR_l2_eth_infra_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class EthertypeMatch_Enum(Enum):
    """
    EthertypeMatch_Enum

    Ethertype match

    """

    """

    PPP over Ethernet

    """
    PPP_OVER_ETHERNET = 34915


    @staticmethod
    def _meta_info():
        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['EthertypeMatch_Enum']


class Match_Enum(Enum):
    """
    Match_Enum

    Match

    """

    """

    All otherwise unmatched packets

    """
    MATCH_DEFAULT = 1

    """

    Untagged packets

    """
    MATCH_UNTAGGED = 2

    """

    Match Dot1Q tags

    """
    MATCH_DOT1Q = 3

    """

    Match Dot1ad tags

    """
    MATCH_DOT1AD = 4

    """

    Match Dot1Q priority\-tagged packets

    """
    MATCH_DOT1Q_PRIORITY = 5

    """

    Match Dot1ad priority\-tagged packets

    """
    MATCH_DOT1AD_PRIORITY = 6


    @staticmethod
    def _meta_info():
        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['Match_Enum']


class Rewrite_Enum(Enum):
    """
    Rewrite_Enum

    Rewrite

    """

    """

    Pop 1 tag

    """
    POP1 = 1

    """

    Pop 2 tags

    """
    POP2 = 2

    """

    Push 1 tag

    """
    PUSH1 = 3

    """

    Push 2 tags

    """
    PUSH2 = 4

    """

    Translate 1\-to\-1

    """
    TRANSLATE1TO1 = 5

    """

    Translate 1\-to\-2

    """
    TRANSLATE1TO2 = 6

    """

    Translate 2\-to\-1

    """
    TRANSLATE2TO1 = 7

    """

    Translate 2\-to\-2

    """
    TRANSLATE2TO2 = 8


    @staticmethod
    def _meta_info():
        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['Rewrite_Enum']


class VlanTagOrAny_Enum(Enum):
    """
    VlanTagOrAny_Enum

    Vlan tag or any

    """

    """

    Match any VLAN tag value

    """
    ANY = 4096


    @staticmethod
    def _meta_info():
        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['VlanTagOrAny_Enum']


class VlanTagOrCvp_Enum(Enum):
    """
    VlanTagOrCvp_Enum

    Vlan tag or cvp

    """

    """

    This is the Native VLAN and C\-VLAN
    preservation is enabled

    """
    NATIVE_WITH_CVLAN_PRESERVATION = 65534


    @staticmethod
    def _meta_info():
        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['VlanTagOrCvp_Enum']


class VlanTagOrNative_Enum(Enum):
    """
    VlanTagOrNative_Enum

    Vlan tag or native

    """

    """

    This is the Native VLAN

    """
    NATIVE = 65535

    """

    This is the Native VLAN and C\-VLAN
    preservation is enabled

    """
    NATIVE_WITH_CVLAN_PRESERVATION = 65534


    @staticmethod
    def _meta_info():
        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['VlanTagOrNative_Enum']


class VlanTagOrNull_Enum(Enum):
    """
    VlanTagOrNull_Enum

    Vlan tag or null

    """

    """

    Match any inner VLAN tag value

    """
    ANY = 0


    @staticmethod
    def _meta_info():
        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['VlanTagOrNull_Enum']


class Vlan_Enum(Enum):
    """
    Vlan_Enum

    Vlan

    """

    """

    An 802.1ad VLAN

    """
    VLAN_TYPE_DOT1AD = 1

    """

    An 802.1q VLAN

    """
    VLAN_TYPE_DOT1Q = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2._meta import _Cisco_IOS_XR_l2_eth_infra_datatypes as meta
        return meta._meta_table['Vlan_Enum']



