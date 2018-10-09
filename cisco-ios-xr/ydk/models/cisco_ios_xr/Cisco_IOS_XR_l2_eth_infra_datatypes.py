""" Cisco_IOS_XR_l2_eth_infra_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EthertypeMatch(Enum):
    """
    EthertypeMatch (Enum Class)

    Ethertype match

    .. data:: ppp_over_ethernet = 34915

    	PPP over Ethernet

    """

    ppp_over_ethernet = Enum.YLeaf(34915, "ppp-over-ethernet")


class Match(Enum):
    """
    Match (Enum Class)

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

    match_default = Enum.YLeaf(1, "match-default")

    match_untagged = Enum.YLeaf(2, "match-untagged")

    match_dot1q = Enum.YLeaf(3, "match-dot1q")

    match_dot1ad = Enum.YLeaf(4, "match-dot1ad")

    match_dot1q_priority = Enum.YLeaf(5, "match-dot1q-priority")

    match_dot1ad_priority = Enum.YLeaf(6, "match-dot1ad-priority")


class Rewrite(Enum):
    """
    Rewrite (Enum Class)

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

    pop1 = Enum.YLeaf(1, "pop1")

    pop2 = Enum.YLeaf(2, "pop2")

    push1 = Enum.YLeaf(3, "push1")

    push2 = Enum.YLeaf(4, "push2")

    translate1to1 = Enum.YLeaf(5, "translate1to1")

    translate1to2 = Enum.YLeaf(6, "translate1to2")

    translate2to1 = Enum.YLeaf(7, "translate2to1")

    translate2to2 = Enum.YLeaf(8, "translate2to2")


class Vlan(Enum):
    """
    Vlan (Enum Class)

    Vlan

    .. data:: vlan_type_dot1ad = 1

    	An 802.1ad VLAN

    .. data:: vlan_type_dot1q = 2

    	An 802.1q VLAN

    """

    vlan_type_dot1ad = Enum.YLeaf(1, "vlan-type-dot1ad")

    vlan_type_dot1q = Enum.YLeaf(2, "vlan-type-dot1q")


class VlanTagOrAny(Enum):
    """
    VlanTagOrAny (Enum Class)

    Vlan tag or any

    .. data:: any = 4096

    	Match any VLAN tag value

    """

    any = Enum.YLeaf(4096, "any")


class VlanTagOrCvp(Enum):
    """
    VlanTagOrCvp (Enum Class)

    Vlan tag or cvp

    .. data:: native_with_cvlan_preservation = 65534

    	This is the Native VLAN and C-VLAN

    	preservation is enabled

    """

    native_with_cvlan_preservation = Enum.YLeaf(65534, "native-with-cvlan-preservation")


class VlanTagOrNative(Enum):
    """
    VlanTagOrNative (Enum Class)

    Vlan tag or native

    .. data:: native = 65535

    	This is the Native VLAN

    .. data:: native_with_cvlan_preservation = 65534

    	This is the Native VLAN and C-VLAN

    	preservation is enabled

    """

    native = Enum.YLeaf(65535, "native")

    native_with_cvlan_preservation = Enum.YLeaf(65534, "native-with-cvlan-preservation")


class VlanTagOrNull(Enum):
    """
    VlanTagOrNull (Enum Class)

    Vlan tag or null

    .. data:: any = 0

    	Match any inner VLAN tag value

    """

    any = Enum.YLeaf(0, "any")


class VsMode(Enum):
    """
    VsMode (Enum Class)

    Vs mode

    .. data:: trunk = 1

    	VLAN-Switched trunk mode

    .. data:: access = 2

    	VLAN-Switched access mode

    """

    trunk = Enum.YLeaf(1, "trunk")

    access = Enum.YLeaf(2, "access")



